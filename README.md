# Carisurg_Week_0_Portfolio

## CariSurg MedTech Pathways Portfolio – Data Cleaning, Data Visualization, Clinical Context, Digital Triage Design, and Research Proposal Development

This repository contains my portfolio submissions for the CariSurg MedTech Pathways Programme 2026.

The work in this repository focuses on developing foundational skills in healthcare data cleaning, data visualization, clinical interpretation, healthcare AI system design, research proposal writing, reference management, and professional documentation. The assignments use tools such as Python, Pandas, NumPy, Matplotlib, Google Colab, GitHub, and Zotero to support healthcare data analysis and emergency department triage decision-making.

---

## Repository Structure

```text
Carisurg_Week_0_Portfolio/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── data/
│   ├── README.md
│   ├── Gender_Cleaned_Dataset.csv
│   └── Pulse_Cleaned_Dataset.csv
│
├── docs/
│   ├── README.md
│   ├── Assignment4_Pulse_Clinical_Context.md
│   ├── Assignment5_FiO2_Clinical_Context.md
│   ├── Assignment5_Updated_SpO2_Clinical_Context.md
│   ├── Assignment6_Digital_Triage_System.md
│   ├── Week 1 Final Submission Vishal Baboolal.pdf
│   └── Week_2_Updated_Proposal_Vishal_Baboolal.pdf
│
├── notebooks/
│   ├── README.md
│   ├── Assignment1_GenderCleaning.ipynb
│   ├── Assignment2_PulseCleaning.ipynb
│   └── Assignment3_Data_Visualization.ipynb
│
└── screenshots/
```

---

## Contents

1. Assignment 1 – Gender Column Cleaning
2. Assignment 2 – Pulse Column Cleaning
3. Assignment 3 – Data Visualization
4. Assignment 4 – Pulse Rate Clinical Context
5. Assignment 5 – Fraction of Inspired Oxygen (FiO₂) Clinical Context
6. Assignment 5 (Updated) – Oxygen Saturation (SpO₂) Clinical Context
7. Assignment 6 – Digital Emergency Triage System
8. Week 1 Preliminary Research Proposal
9. Week 2 Updated Proposal and Zotero Bibliography
10. Screenshots and Visualizations

---

# Assignment 1 – Gender Column Cleaning

## Objective

The objective of this assignment was to clean and standardize the Gender column in the Emergency Triage Dataset.

## Tasks Completed

* Loaded the dataset into Google Colab
* Inspected the Gender column
* Identified inconsistent gender values
* Standardized gender entries into a consistent format
* Exported the cleaned dataset

## Files

* `notebooks/Assignment1_GenderCleaning.ipynb`
* `data/Gender_Cleaned_Dataset.csv`

---

# Assignment 2 – Pulse Column Cleaning

## Objective

The objective of this assignment was to clean the Pulse column by identifying missing values, detecting unrealistic pulse readings, and preparing the data for further analysis.

## Cleaning Process

### 1. Initial Inspection

The Pulse column was inspected using frequency counts to understand the distribution of values and identify unusual entries.

### 2. Numeric Conversion

The Pulse column was converted to numeric format using Pandas. Invalid or non-numeric values were converted to missing values (NaN).

### 3. Missing Value Detection

Missing values were identified using data validation checks.

**Results:**

* Missing values after numeric conversion: 44

### 4. Out-of-Range Detection

A valid physiological pulse range of 40–170 beats per minute (bpm) was established.

Values outside this range were considered unrealistic and replaced with NaN.

**Results:**

* Out-of-range pulse values detected: 43

### 5. Median Imputation

Missing values were replaced using the median pulse value.

The median was selected because it is less sensitive to extreme values and outliers than the mean.

**Results:**

* Median pulse value used: 90 bpm

### 6. Validation

After cleaning, the dataset was validated using descriptive statistics and visual inspection.

**Results:**

* Missing values remaining: 0
* Minimum pulse value: 40 bpm
* Maximum pulse value: 170 bpm

## Files

* `notebooks/Assignment2_PulseCleaning.ipynb`
* `data/Pulse_Cleaned_Dataset.csv`

---

# Assignment 3 – Data Visualization

## Objective

The objective of this assignment was to create meaningful clinical visualizations using the Emergency Triage Dataset.

The Pulse column was selected because heart rate is an important vital sign used in emergency medicine to assess circulation, cardiovascular function, and patient stability.

The Pulse column was cleaned and validated during Assignment 2 before being used for visualization and analysis.

## Visualizations Created

### 1. Pulse Distribution Histogram

**Clinical Question:**

How are pulse rates distributed among Emergency Department patients?

A histogram was used to visualize the distribution of pulse values throughout the dataset.

A clinical reference line was added at:

* 100 bpm (Tachycardia Threshold)

This threshold helps identify patients whose pulse rates may indicate elevated cardiovascular stress or other clinical concerns.

### 2. Age vs Pulse Scatter Plot

**Clinical Question:**

Does age affect resting heart rate in Emergency Department patients?

A scatter plot was used to explore the relationship between Age and Pulse.

Clinical reference lines were added at:

* 60 bpm (Lower Normal Pulse)
* 100 bpm (Upper Normal Pulse)

These lines provide clinical context when interpreting heart rate measurements.

## Results

* Most pulse values were concentrated between approximately 80 and 100 bpm.
* Some patients exhibited pulse values above the tachycardia threshold.
* No strong visible relationship between age and pulse was observed.
* The visualizations demonstrated how cleaned healthcare data can be used to generate meaningful clinical insights.

## Files

* `notebooks/Assignment3_Data_Visualization.ipynb`

---

# Assignment 4 – Pulse Rate Clinical Context

## Objective

The objective of this assignment was to explain the clinical significance of Pulse Rate and its role in emergency triage.

## Key Topics Covered

* Definition of Pulse Rate
* Normal Clinical Range
* Bradycardia and Tachycardia
* Importance in Emergency Triage
* Patient Prioritization
* Clinical Decision Making

## Files

* `docs/Assignment4_Pulse_Clinical_Context.md`

---

# Assignment 5 – Fraction of Inspired Oxygen (FiO₂) Clinical Context

## Objective

The objective of this assignment was to explain the clinical significance of Fraction of Inspired Oxygen (FiO₂) and its importance in emergency triage.

## Key Topics Covered

* Definition of FiO₂
* Normal Clinical Range
* Oxygen Therapy
* Respiratory Support
* Importance in Emergency Triage
* Patient Prioritization
* Clinical Decision Making

## Files

* `docs/Assignment5_FiO2_Clinical_Context.md`

---

# Assignment 5 (Updated) – Oxygen Saturation (SpO₂) Clinical Context

## Objective

Following clarification that the selected metric should not be included in the original dataset, an updated clinical context assignment was completed using Oxygen Saturation (SpO₂).

## Key Topics Covered

* Definition of SpO₂
* Normal Clinical Range
* Respiratory Assessment
* Importance in Emergency Triage
* Patient Prioritization
* Clinical Decision Making
* Respiratory Failure Indicators
* Oxygen Monitoring

## Files

* `docs/Assignment5_Updated_SpO2_Clinical_Context.md`

---

# Assignment 6 – Digital Emergency Triage System

## Objective

The objective of this assignment was to design and justify a digital emergency triage algorithm capable of processing patient information and categorizing patients into risk levels.

## Key Topics Covered

* Patient Data Collection
* Missing Data Handling
* Risk Scoring
* Vital Sign Assessment
* Clinical Warning Signs
* Threshold Justification
* Algorithm Design Rationale
* Human-AI Collaboration
* Clinical Decision Support

## Files

* `docs/Assignment6_Digital_Triage_System.md`

---

# Week 1 Preliminary Research Proposal

The Week 1 preliminary proposal focused on AI-assisted emergency department triage decision support in a resource-constrained setting.

## Key Topics Covered

* AI-assisted emergency department triage
* Risk-flagging support for triage nurses
* Vital signs and presenting complaint data
* Research gaps in AI triage implementation
* Clinical usefulness and workflow integration

## Files

* `docs/Week 1 Final Submission Vishal Baboolal.pdf`

---

# Week 2 Updated Proposal and Zotero Bibliography

For Week 2, the preliminary research proposal was updated using Zotero for citation management and an automatically generated APA 7th edition bibliography.

The updated proposal includes seven peer-reviewed sources related to AI-assisted emergency department triage, external validation, workflow integration, clinical usefulness, and Caribbean emergency department patient flow.

## Key Updates

* Expanded the proposal from five papers to seven peer-reviewed papers
* Added Zotero-managed in-text citations
* Generated an automatic APA 7th edition bibliography using Zotero
* Strengthened the problem statement
* Improved the gap analysis
* Clarified the proposed data source and 12-week evaluation plan
* Added focus on local validation, workflow fit, missing-data handling, and nurse-facing risk flags

## Files

* `docs/Week_2_Updated_Proposal_Vishal_Baboolal.pdf`

---

# Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Google Colab
* GitHub
* Zotero
* Microsoft Word

---

# How to Reproduce the Results

1. Open the relevant notebook from the `notebooks/` folder in Google Colab.
2. Upload the required dataset when prompted.
3. Run all notebook cells from top to bottom.
4. Cleaned datasets and visualizations will be generated automatically.

---

# Screenshots and Visualizations

The repository includes screenshots showing:

### Assignment 2 – Pulse Cleaning

* Pulse Before Cleaning
* Pulse Cleaning Process
* Pulse Summary Statistics
* Final Validation Check

### Assignment 3 – Data Visualization

* Pulse Distribution Histogram
* Age vs Pulse Scatter Plot

All screenshots are available in the `screenshots/` folder.

---

# GitHub Repository

Repository URL:

https://github.com/VishalB210/Carisurg_Week_0_Portfolio

---

# Author

**Vishal Baboolal**

Electrical & Computer Engineering Student
University of the West Indies, St. Augustine

CariSurg MedTech Pathways Programme 2026
