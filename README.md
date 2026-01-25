# SumData — Offline-First Clinical Documentation Assistant

SumData is a privacy-first, AI-assisted clinical documentation prototype designed to reduce administrative burden on healthcare providers while improving patient understanding. The system captures doctor–patient conversations (with explicit consent), generates structured medical documentation for clinicians, and produces clear, patient-friendly summaries — all with a strict doctor-in-the-loop workflow.

SumData is designed as an **offline-first system**: AI processing is intended to run locally or on-premise, using preloaded medical resources rather than live internet access.

---

## Problem
Healthcare providers spend significant time on manual documentation after patient visits. This reduces time spent with patients, increases burnout, and often results in patients leaving appointments confused or overwhelmed by medical information.

---

## Solution
SumData assists clinicians by:
- Capturing patient visits only after explicit consent
- Transcribing conversations locally
- Generating draft medical documentation using an offline AI engine
- Requiring physician review and approval before any report is saved or shared
- Producing both a clinician report and a patient-friendly summary from the same visit

---

## Core Features

### 1. Secure Sign-In
Doctors access the system through a secure sign-in interface.

**File:** `signIn.html`

---

### 2. Consent-First Workflow
Before recording begins, both doctor and patient consent must be explicitly confirmed. The interface clearly explains how data is used and emphasizes privacy.

**File:** `consentform.html`

---

### 3. Live Visit Recording
The system records the visit locally and generates a live transcript in real time. Audio is intended to be processed locally and deleted after documentation is generated.

**File:** `recording.html`

---

### 4. Transcript Review & Editing
Clinicians can review and edit the transcript before generating summaries, ensuring accuracy and correcting transcription errors.

**File:** `transcript.html`

---

### 5. AI-Generated Summaries (Drafts)
Using the reviewed transcript, the system generates:
- A **doctor summary** using medical terminology and structured formatting
- A **patient summary** written in plain, understandable language

All outputs are drafts until approved by the physician.

**File:** `download.html`

---

### 6. Doctor-in-the-Loop Approval
Physicians must review, edit, and approve all AI-generated content before it is finalized or shared. This ensures clinical accuracy and accountability.

---

### 7. Dashboard & Visit Management
Doctors can view recent visits, track documentation status (draft vs completed), and start new patient sessions from a centralized dashboard.

**File:** `dashboard.html`

---

## Technical Architecture (Conceptual)
Doctor & patient consent → Local audio capture → On-device speech-to-text → ClariNote Engine (offline AI) → Preloaded medical knowledge base → Draft clinician report + patient-friendly summary → Physician review & approval → Local encrypted storage → Optional export (PDF / print)

---

## Privacy & Ethics
- No internet access required for AI processing
- No third-party data sharing
- Explicit consent required before recording
- Doctor approval required before documentation is finalized
- System acts as a documentation assistant, not a diagnostic tool

---

## Project Status
This project is a **hackathon prototype** focused on user flow, privacy-by-design architecture, and human-centered healthcare AI. Some AI components are conceptual or simulated for demonstration purposes.

---

## Future Work
- Expand AI assistance to insurance and administrative healthcare paperwork
- Offline update packages for medical knowledge resources
- EHR integration using structured export formats
- Multilingual patient summaries

---

## Disclaimer
SumData is not a medical decision-making system. It is intended to assist with documentation only and does not replace professional clinical judgment.
