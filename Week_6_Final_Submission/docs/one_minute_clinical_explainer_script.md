# Week 6 One-Minute Clinical Explainer Script

**Recording target:** approximately 55-65 seconds  
**Audience:** Dr. Reyes, Consultant Emergency Physician

## Spoken script

Hi, I’m Vishal Baboolal, and this project compares two baseline models for predicting Emergency Severity Index levels during triage.

The logistic regression model performed better overall. However, the most important result is in the first row, which represents the most critically ill patients.

Out of 16 true ESI Level 1 patients, the model correctly identified only 4.

The other 12 critical patients were assigned to lower-priority categories, which could delay resuscitation or other life-saving treatment.

The decision tree performed even worse, correctly identifying only 1 of the 16 critical cases.

Therefore, although both models detected useful patterns, neither is safe for clinical use. The next step is to improve detection of rare critical cases and validate the model on local emergency department data.

## Recording checklist

- Show the logistic-regression confusion matrix while speaking.
- Keep the recording under one minute.
- Post the video to Discord.
- Add the Loom or video link to `loom_video_link.md`.
