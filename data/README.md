# Governed Data Location

Patient-level emergency-department data is intentionally excluded from this public repository.

The final reproducible pipeline expects the cleaned modelling dataset at:

```text
data/data_cleaned_week5.csv
```

Some historical exploratory notebooks may refer to the original programme file:

```text
data/EmergencyTriageDataset_Reduced_Dirty.csv
```

Both files must remain local or in an approved governed storage location. Do not commit, redistribute, or expose them through the public repository. The root `.gitignore` blocks common data formats in this directory.
