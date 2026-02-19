import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

TELUS_BASE_URL = os.getenv("TELUS_BASE_URL", "").strip()
TELUS_API_KEY = os.getenv("TELUS_API_KEY", "").strip()
TELUS_MODEL = os.getenv("TELUS_MODEL", "google/gemma-3-27b-it").strip()

if not TELUS_BASE_URL or not TELUS_API_KEY:
    raise RuntimeError("Missing TELUS_BASE_URL or TELUS_API_KEY in .env")

client = OpenAI(base_url=TELUS_BASE_URL, api_key=TELUS_API_KEY)

app = FastAPI(title="SumData Minimal Backend")

# Allow your local HTML pages to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hackathon mode
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# "Foundational Resources Pack"
# (tiny, local, injected into prompt)
# -----------------------------
OFFLINE_RESOURCES = {
    "soap_template": {
        "Subjective": ["Chief complaint", "Symptoms", "Duration", "Relevant history", "Medications/allergies (if mentioned)"],
        "Objective": ["Vitals/exam (ONLY if mentioned) otherwise 'Not provided'"],
        "Assessment": ["Brief, non-diagnostic summary"],
        "Plan": ["Tests ordered", "Treatment discussed", "Follow-up", "Safety advice"]
    },
    "terminology_rules": [
        "Use standard clinical wording (SOAP).",
        "Do not invent facts. If missing, write 'Not specified in transcript'.",
        "Do not diagnose. Do not prescribe. Draft documentation only."
    ],
    "patient_summary_rules": [
        "Plain language, grade 6–8 readability.",
        "Use bullets.",
        "Include next steps and follow-up.",
        "If chest pain/shortness of breath appears, include a general 'seek urgent care' warning."
    ],
    "red_flags": [
        "severe or worsening chest pain",
        "trouble breathing",
        "fainting or feeling like you will pass out"
    ]
}


class GenerateReq(BaseModel):
    transcript: str


def build_prompt(transcript: str) -> str:
    return f"""
You are ClariNote Engine inside SumData.
You do NOT browse the internet.
You do NOT diagnose or prescribe.
You ONLY draft documentation from the transcript and the OFFLINE_RESOURCES provided.
If info is missing, write: "Not specified in transcript".

OFFLINE_RESOURCES:
- SOAP_TEMPLATE: {OFFLINE_RESOURCES["soap_template"]}
- TERMINOLOGY_RULES: {OFFLINE_RESOURCES["terminology_rules"]}
- PATIENT_SUMMARY_RULES: {OFFLINE_RESOURCES["patient_summary_rules"]}
- RED_FLAGS: {OFFLINE_RESOURCES["red_flags"]}

TASK:
From the transcript, output EXACTLY TWO sections:

=== CLINICIAN_NOTE ===
(SOAP format: Subjective / Objective / Assessment / Plan)

=== PATIENT_SUMMARY ===
(Plain language bullets; include red-flag warning if relevant)

TRANSCRIPT:
\"\"\"{transcript}\"\"\"
"""


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/generate")
def generate(req: GenerateReq):
    transcript = (req.transcript or "").strip()
    if len(transcript) < 20:
        return {"error": "Transcript too short. Paste the full visit conversation."}

    prompt = build_prompt(transcript)

    # TELUS kickoff shows OpenAI-compatible /v1 usage with completions :contentReference[oaicite:4]{index=4}
    resp = client.completions.create(
        model=TELUS_MODEL,
        prompt=prompt,
        max_tokens=900
    )

    text = (resp.choices[0].text or "").strip()

    # naive parsing: split by markers
    clinician_note = ""
    patient_summary = ""
    if "=== CLINICIAN_NOTE ===" in text and "=== PATIENT_SUMMARY ===" in text:
        a, b = text.split("=== PATIENT_SUMMARY ===", 1)
        clinician_note = a.replace("=== CLINICIAN_NOTE ===", "").strip()
        patient_summary = b.strip()
    else:
        # fallback
        clinician_note = text
        patient_summary = ""

    return {
        "clinician_note": clinician_note,
        "patient_summary": patient_summary
    }
