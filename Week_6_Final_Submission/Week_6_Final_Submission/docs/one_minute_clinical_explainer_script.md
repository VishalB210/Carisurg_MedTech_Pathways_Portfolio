# Week 6 One-Minute Clinical Explainer Script

**Recording target:** approximately 55-65 seconds  
**Audience:** Dr. Reyes, Consultant Emergency Physician

## Spoken script

Dr. Reyes, this model is intended to support the first triage decision by flagging patients who may need immediate attention.

The number I care about most is how many genuinely Level 1 patients the system successfully catches. That matters more than the overall percentage correct because Level 1 cases are extremely rare, and a model can look good while still missing the sickest patients.

In the test set, logistic regression correctly identified 4 of 16 Level 1 patients. That means it missed 12. For a patient, that could mean delayed resuscitation or treatment during a life-threatening emergency.

The model performs better than random guessing overall, but it is not safe for deployment. My next step would be to address the class imbalance, study the missed critical cases, and validate any improved model locally before it is shown to triage staff.

## Recording checklist

- Show the logistic-regression confusion matrix while speaking.
- Keep the recording under one minute.
- Post the video to Discord.
- Add the Loom or video link to `loom_video_link.md`.
