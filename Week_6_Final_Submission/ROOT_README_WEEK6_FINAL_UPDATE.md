## Week 6 Final Submission - Baseline Triage Modelling

Week 6 completed the first supervised-learning phase of the AI-assisted emergency department triage project. Using the cleaned Week 5 dataset, I trained and compared a stratified random baseline, logistic regression, and a bounded decision tree using the same 80/20 stratified split with `random_state=42`.

Logistic regression was the strongest overall baseline, achieving **66.7% accuracy**, **0.492 macro F1**, and **0.661 weighted F1**. However, it correctly identified only **4 of 16 ESI Level 1 patients**, giving **25.0% ESI Level 1 recall**. The decision tree achieved **58.5% accuracy** and identified only **1 of 16 ESI Level 1 patients**.

These results show that the dataset contains useful predictive signal, but neither model is clinically safe for deployment. ESI Level 1 recall was selected as the primary safety metric because missing a critically ill patient could delay immediate life-saving treatment.

Folder:

`Week_6_Final_Submission/`
