# Screenshots

This folder contains screenshots documenting the data cleaning, validation, and visualisation work completed during Week 0 of the CariSurg MedTech Pathways Programme.

The screenshots support the notebooks in the `notebooks/` folder and provide visual evidence of the cleaning, validation, summary statistics, and clinical visualisation steps.

---

## Assignment 2 – Pulse Column Cleaning

### `A2_Pulse_Before_Cleaning.png`

Shows the initial inspection of the `Pulse` column before cleaning. Frequency counts were reviewed to understand the distribution of values and identify unusual or invalid entries.

### `A2_Pulse_Cleaning_Process.png`

Shows the pulse-cleaning workflow, including:

- Numeric conversion
- Missing value detection
- Out-of-range value identification
- Median imputation

### `A2_Pulse_Summary_Statistics.png`

Displays descriptive statistics after cleaning, including:

- Count
- Mean
- Standard deviation
- Minimum value
- Maximum value
- Quartiles

### `A2_Final_Validation_Check.png`

Shows the final validation stage confirming that:

- No missing values remain
- Pulse values fall within the accepted physiological range of 40–170 bpm
- The cleaned dataset is ready for analysis

---

## Assignment 3 – Data Visualisation

### `A3_Pulse_Histogram.png`

Histogram showing the distribution of pulse values within the emergency triage dataset.

**Clinical question:**  
How are pulse rates distributed among emergency department patients?

**Clinical reference line:**  
Tachycardia threshold = 100 bpm

**Purpose:**  
To identify the overall distribution of pulse values and highlight patients whose heart rate exceeds the tachycardia threshold.

### `A3_Age_vs_Pulse_Scatter.png`

Scatter plot showing the relationship between age and pulse.

**Clinical question:**  
Does age affect resting heart rate in emergency department patients?

**Clinical reference lines:**  

- Lower normal pulse = 60 bpm
- Upper normal pulse = 100 bpm

**Purpose:**  
To explore whether any relationship exists between patient age and pulse rate while providing clinical context for normal heart-rate ranges.

---

## Summary

These screenshots provide evidence of the Week 0 workflow, including:

- Data cleaning
- Missing value handling
- Validation checks
- Summary statistics
- Clinical data visualisation
- Interpretation of healthcare data

Together, these files support the Week 0 notebooks and demonstrate the process used to prepare and visualise healthcare-style triage data.
