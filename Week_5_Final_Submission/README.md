# Week 5 Final Submission – AI-Assisted Triage Data Exploration

## Project Overview

This submission investigates the suitability of a real-world emergency department (ED) triage dataset for machine learning. The project focuses on exploratory data analysis (EDA), data quality assessment, clinical feature exploration, and feasibility evaluation prior to model development.

The objective is to determine whether the dataset is appropriate for building an AI-assisted emergency triage prediction model while identifying any important limitations or risks.

---

## Repository Contents

```
Week_5_Final_Submission/
│
├── README.md
├── docs/
│   ├── feasibility_memo.pdf
│   ├── feasibility_memo.docx
│   ├── feasibility_memo.md
│   ├── missingness_table.csv
│   ├── outlier_table.csv
│   ├── top_chief_complaints.csv
│   ├── top_10_feature_shortlist.csv
│   └── figures/
│       ├── dashboard_4_plots.png
│       ├── figure_1_missingness.png
│       ├── figure_2_esi_distribution.png
│       ├── figure_3_age_distribution.png
│       ├── figure_4_race_ethnicity.png
│       ├── figure_5_top_complaints.png
│       ├── figure_6_complaints_per_patient.png
│       ├── figure_7_vitals_by_esi.png
│       └── figure_8_correlation_heatmap.png
│
└── notebooks/
    └── week5_final_exploration.ipynb
```

---

## Deliverables

### Notebook

- `notebooks/week5_final_exploration.ipynb`
  - Complete exploratory data analysis
  - Data quality assessment
  - Feature exploration
  - Visualizations
  - Clinical interpretation
  - Correlation analysis

### Feasibility Memo

Located in `docs/`

- PDF version
- Microsoft Word version
- Markdown version

The memo provides:

- Executive summary
- Dataset overview
- Data quality assessment
- Reasons to proceed
- Key limitations
- Clinical recommendations
- Top 10 predictive feature shortlist

### Supporting Tables

Located in `docs/`

- Missingness summary
- Outlier assessment
- Top chief complaints
- Top 10 predictive features

### Figures

Located in `docs/figures/`

Includes:

- Missingness overview
- ESI distribution
- Age distribution
- Race and ethnicity distribution
- Chief complaint distribution
- Complaints per patient
- Vital signs by ESI level
- Correlation heatmap
- Combined dashboard

---

## Overall Verdict

**Proceed with caveats.**

The dataset is appropriate for exploratory analysis and baseline machine learning development. However, leakage variables should be excluded, clinically implausible values reviewed, and subgroup fairness assessed before considering deployment in a clinical environment.

---

## Dataset Note

The dataset contains de-identified healthcare information.

The raw dataset has **not** been uploaded to this public repository.

Expected local dataset location:

```
data/yaleemmlc_admissionprediction_triage.csv
```

Alternatively, update the notebook `DATA_PATH` variable to match the local dataset location.

---

## Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Clinical data profiling
- Healthcare data cleaning
- Missing data assessment
- Outlier detection
- Feature engineering
- Correlation analysis
- Clinical data visualization
- Data quality reporting
- Technical documentation
- GitHub project organisation

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- GitHub

---

**Author**

**Vishal Baboolal**

Electrical & Computer Engineering Student

University of the West Indies, St. Augustine

CariSurg MedTech Pathways Programme – Week 5
