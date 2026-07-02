# Week 4 Risk Register

**Project:** AI-Assisted Risk Flagging for Emergency Department Triage in Resource-Constrained Settings  
**Student:** Vishal Baboolal  
**Programme:** CariSurg MedTech Pathways Programme 2026  

**Note:** H = High, M = Medium.

## 9.1 Draft Risk Register

| Risk Name | Category | Likelihood | Impact | Mitigation | Signal of Success |
|---|---|---|---|---|---|
| Distribution Shift Across Hospitals | AI-Technical | M — performance may change at another hospital or during outbreaks. | H — high-risk patients may be missed. | Silent validation at each new site before go-live; pause rollout if Level 1/2 recall drops by more than 3 percentage points. | Site recall and calibration stay within ±3 percentage points of baseline. |
| Data Leakage from Post-Triage Variables | AI-Technical | M — dataset may contain variables only known after triage. | H — model may look accurate in testing but fail in real use. | Audit all features before deployment; remove any input not available at the time of triage. | 100% of approved features are timestamped before triage decision. |
| Alert Fatigue | Operational | H — frequent alerts may train nurses to ignore the system. | H — true urgent alerts may be missed. | Review alert rate weekly; adjust threshold if fewer than 10% of alerts lead to clinical action. | Weekly alert-action rate remains above 10%. |
| EHR Integration or Downtime Failure | Operational | M — EHR delays or downtime may occur. | H — triage may be delayed or incomplete. | Keep paper fallback workflow; run quarterly downtime drills. | 100% of triage staff pass downtime drill; fallback starts within 5 minutes. |
| Automation Bias | Ethical | M — clinicians may trust the AI too much. | H — staff may follow unsafe AI advice over clinical judgement. | Interface states AI is support only; nurses document agreement or override for high-risk alerts. | Staff override unsafe AI recommendations in ≥90% of simulations. |
| Accountability and Consent Gap | Ethical | M — patients may not know AI supported triage. | H — unclear responsibility may delay investigation after harm. | Name a clinical owner; create incident review protocol; provide patient-facing disclosure. | 100% of AI incidents have named reviewer within 48 hours. |
| Under-Representation of Patient Groups | Equity | H — some groups may be under-represented in training data. | H — model may under-triage elderly, rural, paediatric, or atypical cases. | Check performance by age, gender, arrival method, and site before rollout. | Subgroup recall gap remains ≤5 percentage points. |
| Language, Literacy, and Infrastructure Disparity | Equity | M — some users may struggle with English-only alerts or weak infrastructure. | M — system may work better at resourced sites than rural sites. | Use plain-language interface; review local language needs; complete site readiness checklist. | 100% of sites pass readiness checks; ≥90% of staff pass comprehension check. |

## 9.2 Top 3 Risks in Plain Language

### 1. Alert Fatigue

The system may send too many warnings, causing nurses to ignore them even when they are correct. This is dangerous because the tool is meant to highlight patients who need urgent review, not create extra noise. The mitigation is to track how many alerts lead to real clinical action each week and adjust the alert threshold if the action rate becomes too low.

### 2. Distribution Shift Across Hospitals

A model trained on Mercer data may not work the same way at another public hospital. Different hospitals may have different patient populations, documentation habits, staffing patterns, or outbreak patterns. The mitigation is to test the model silently at each new hospital before it is used in live triage decisions.

### 3. Under-Representation of Patient Groups

If some patient groups are missing or under-represented in the training data, the model may be less safe for them. This is especially important for elderly patients, paediatric patients, rural patients, and patients with atypical symptoms. The mitigation is to check model performance separately for different patient groups and stop rollout if one group is being missed more often.

## 9.3 Residual Risk

Even with these mitigations, the system may still miss unusual presentations or perform poorly in hospitals with weak data quality. This cannot be fully resolved at the proposal stage. For that reason, the first deployment should be a silent pilot before any AI output is used for live patient-facing triage decisions.
