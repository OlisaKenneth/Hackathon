# Privacy (SumData / ClariNote Engine)

## Privacy Goal
SumData is designed to reduce documentation workload while keeping patient information private. The system is **offline-first**: AI processing is intended to run locally (on-device or on-premise) and does not require internet access.

## What Data is Collected (EPI)
Depending on configuration, SumData may process:
- Audio of the doctor–patient conversation (temporary)
- Transcript text
- Draft clinical documentation (doctor summary)
- Plain-language patient summary
- Minimal session metadata (timestamp, clinician ID, visit ID)

## Data Minimization
SumData follows “collect the least necessary”:
- Audio can be set to **not persist** (only live processing)
- Transcripts can be **deleted automatically** after approval
- Only the **doctor-approved final note** must be retained

## Local-First Processing
- Speech-to-text and summarization are intended to run locally.
- The ClariNote Engine has **no internet browsing** and does not query external sources.
- The only references allowed are the **preloaded resource pack** shipped with the system.

## Storage & Encryption
Recommended controls:
- Encrypt data at rest on the device (disk encryption or app-level encryption)
- Encrypt exports (PDF) when saved or transferred
- Use role-based access (clinician only)

## Consent & Transparency
- Recording requires explicit consent from doctor and patient.
- The UI should clearly indicate when recording is active.
- Patients should receive a simple explanation of how data is used.

## Auditability
- Maintain an audit trail: draft created → edits → final approval → export
- Record who approved the note and when.

## Retention Policy (Suggested Defaults)
- Audio: delete immediately after transcript generation
- Transcript: delete after physician approval (configurable)
- Final approved report: retained according to clinic policy

## Security Disclaimer
This is a hackathon prototype. For production, compliance requirements vary by province and organization and should be validated with legal/privacy officers.
