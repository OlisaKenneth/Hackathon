# Ethics & Safety (SumData / ClariNote Engine)

## What SumData Is
SumData is a **documentation assistant**, not a clinician. It drafts notes from a consented visit conversation and requires a doctor to review and approve all outputs.

## What SumData Is NOT
SumData does NOT:
- Diagnose conditions
- Prescribe medication
- Replace clinical judgment
- Provide emergency decision-making

## Doctor-in-the-Loop Safety
- All summaries are labeled as **Draft**
- A clinician must review, edit, and approve before saving or sharing
- Low-confidence fields (e.g., dosage unclear) are flagged

## Bias & Fairness
Risks:
- Language and accent differences may reduce transcription accuracy
- Under-documentation may occur for patients with different communication styles

Mitigations:
- Transcript editing step before summaries
- Clear uncertainty flags
- Encouraging clinicians to confirm key facts (meds, allergies)

## Hallucination Prevention
To reduce “made up” details:
- Generate notes primarily from structured extraction (entities and facts)
- Avoid inserting new medical facts not present in the transcript
- Mark missing information as “Not discussed / Unknown”

## Patient Safety Language
Patient summary should:
- Use simple language
- Include “when to seek help” safety guidance for red flags
- Avoid providing specific medical advice beyond the clinician’s plan

## Responsible Deployment
For real-world use, SumData should be tested with clinicians, validated for accuracy, and configured for local privacy requirements.
