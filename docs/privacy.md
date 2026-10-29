# Privacy Policy & Ethical Data Safeguards

This document defines the privacy guarantees, data retention boundaries, and safety protocols implemented in the platform per Section 8.E.

---

### 1. In-Memory Processing by Default
- All user responses entered into the Relationship Reflection questionnaire are handled entirely in volatile browser session memory (`st.session_state`).
- Responses are **never written to disk, databases, server logs, or local storage**.
- Closing or refreshing the browser tab completely destroys all submitted questionnaire inputs.

---

### 2. Zero Personally Identifiable Information (PII)
- The reflection questionnaire strictly prohibits collecting:
  - Litigant or spouse names
  - Phone numbers or email addresses
  - Physical street addresses or residential locations
  - Court case numbers, CNR numbers, or FIR identifiers
  - Intimate personal narratives
- Any question can be freely skipped without penalizing the guidance output.

---

### 3. Absolute Prohibition of Third-Party AI Transmission
- The application executes 100% locally on the user's host machine.
- User responses are **never transmitted to external commercial AI APIs, cloud LLM providers, or remote telemetry servers**.
- No questionnaire data is utilized for machine learning model training or fine-tuning.

---

### 4. Safety Escalation & Domestic Violence Protocol
- If a user selects options indicating physical danger, threats, intimidation, or coercive control, the system immediately:
  - Halts standard reflection guidance.
  - Prominently displays emergency contact numbers for immediate protective support:
    - **181:** Women Helpline (Tamil Nadu, 24/7 Toll-Free).
    - **112:** National Emergency Response Support System (ERSS).
    - **044-25342441 / 15100:** Tamil Nadu State Legal Services Authority (TNSLSA) Free Legal Aid.
    - **044-28592750:** Tamil Nadu State Commission for Women (Chepauk, Chennai).
  - Explicitly advises against joint confrontation or joint marriage counselling when personal safety is at risk.

---

### 5. Local Chat History Protection (User Rule 1)
- Project developer conversation logs and chat history are confined to `chat_history/` and `.chat_history/`.
- These directories are permanently ignored in `.gitignore` to guarantee they remain solely on the laptop's local storage and can never be committed or uploaded to remote repositories.
