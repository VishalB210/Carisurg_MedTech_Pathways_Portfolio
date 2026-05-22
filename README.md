# Carisurg_Week_0_Portfolio

## CariSurg Week 0 Portfolio – Data Cleaning Assignments

This repository contains my Week 0 submissions for the CariSurg MedTech Pathways Program.

The assignments focused on developing fundamental data cleaning skills using Python and Pandas. The goal was to identify inconsistencies, handle missing values, validate data quality, and prepare datasets for future analysis and machine learning applications.



# Assignment 1 – Gender Column Cleaning

## Objective

The objective of this assignment was to clean and standardize the Gender column in the Emergency Triage Dataset.

## Tasks Completed

- Loaded the dataset into Google Colab
- Inspected the Gender column
- Identified inconsistent gender values
- Standardized gender entries into a consistent format
- Exported the cleaned dataset

## Files

- Carisurg_Task1_Week0.ipynb
- EmergencyTriageDataset_Cleaned.csv



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

Result:
- Missing values after numeric conversion: 44

### 4. Out-of-Range Detection

A valid physiological pulse range of 40–170 beats per minute (bpm) was established.

Values outside this range were considered unrealistic and replaced with NaN.

Result:
- Out-of-range pulse values detected: 43

### 5. Median Imputation

Missing values were replaced using the median pulse value.

The median was selected because it is less sensitive to extreme values and outliers than the mean.

Result:
- Median pulse value used: 90 bpm

### 6. Validation

After cleaning, the dataset was validated using descriptive statistics and visual inspection.

Results:
- Missing values remaining: 0
- Minimum pulse value: 40 bpm
- Maximum pulse value: 170 bpm


## Files Included

### Assignment 1

- Carisurg_Task1_Week0.ipynb
- EmergencyTriageDataset_Cleaned.csv

### Assignment 2

- Assignment2_PulseCleaning.ipynb
- EmergencyTriageDataset_Cleaned_Pulse.csv


## Tools Used

- Python
- Pandas
- NumPy (for handling missing values)
- Matplotlib (for data visualization)
- Google Colab
- GitHub


## How to Reproduce the Results

1. Open the notebook in Google Colab.
2. Upload the provided dataset.
3. Run all notebook cells from top to bottom.
4. The cleaned dataset will be generated automatically and exported as a CSV file.


## Author

**Vishal Baboolal**

CariSurg MedTech Pathways Program 2026
