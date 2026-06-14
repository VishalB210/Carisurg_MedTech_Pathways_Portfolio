**Final Week 0 Deliverable – Pseudocode for a Digital Emergency Triage System**

**Name: Vishal Baboolal**

**Objective**

The objective of this pseudocode is to describe how a digital triage system can use patient information to place patients into different risk categories. The system looks at important emergency department measurements such as vital signs, Glasgow Coma Scale (GCS), oxygen requirements, and warning symptoms to help identify patients who may need urgent care.

The purpose of this system is not to replace nurses or doctors. Instead, it is designed to support healthcare workers by quickly highlighting abnormal findings and helping them make faster, safer triage decisions.

**Pseudocode**

START

Collect patient information:

Age
Gender
Glasgow Coma Scale (GCS)
Systolic Blood Pressure (SBP)
Diastolic Blood Pressure (DBP)
Mean Arterial Pressure (MAP)
Pulse Rate
Temperature
Respiratory Rate
Fraction of Inspired Oxygen (FiO₂)
Oxygen Saturation (SpO₂), if available
Main symptoms or complaint

Check for missing or invalid values.

IF any important value is missing:

Flag patient record for nurse review
Continue using available data
Mark confidence level as reduced

Set risk_score = 0

Check consciousness level:

IF GCS ≤ 8:

Add 4 points

ELSE IF GCS is between 9 and 14:

Add 2 points

Check blood pressure:

IF SBP < 90:

Add 4 points

ELSE IF SBP is very high:

Add 2 points

Check pulse rate:

IF Pulse < 60:

Add 2 points

ELSE IF Pulse > 100:

Add 2 points

ELSE IF Pulse is extremely high or extremely low:

Add 4 points

Check respiratory rate:

IF Respiratory Rate is very low or very high:

Add 3 points

Check temperature:

IF Temperature is very high:

Add 2 points

ELSE IF Temperature is very low:

Add 3 points

Check oxygen support:

IF FiO₂ > 21%:

Add 2 points

IF FiO₂ is very high:

Add 4 points

Check critical warning signs:

IF patient has:

Chest pain
Severe shortness of breath
Major bleeding
Signs of stroke
Unconsciousness
Severe trauma

THEN:

Add 5 points

Categorize patient:

IF risk_score ≥ 8:

High Risk / Immediate Attention

ELSE IF risk_score is between 4 and 7:

Moderate Risk / Urgent Review

ELSE:

Low Risk / Routine Assessment

Display output:

Risk Level
Abnormal Findings
Suggested Urgency
Confidence Level
Recommendation for Clinical Review

END

**Threshold Justification**

The thresholds used in this model were selected based on common emergency department practices and the clinical significance of abnormal findings.

A Glasgow Coma Scale (GCS) score of 8 or below was given a high weighting because it may indicate severe impairment of consciousness and a potentially unstable patient. Patients with significantly reduced levels of consciousness often require immediate medical assessment and intervention.

A systolic blood pressure below 90 mmHg was treated as a high-risk finding because it may indicate shock, severe dehydration, blood loss, or poor organ perfusion. These conditions can rapidly become life-threatening if not addressed promptly.

Pulse rates below 60 bpm or above 100 bpm were identified as abnormal because they may indicate cardiovascular instability, infection, pain, shock, or other underlying medical conditions. More extreme pulse values were given additional weighting due to their increased clinical significance.

Increased FiO₂ requirements were considered important because patients who require supplemental oxygen are often experiencing respiratory compromise. A patient requiring a high FiO₂ may be at greater risk of respiratory failure and may require urgent intervention.

Critical warning signs such as severe trauma, chest pain, major bleeding, stroke symptoms, unconsciousness, and severe shortness of breath received the highest weighting because these presentations often require immediate assessment and treatment in the emergency department.

These thresholds are intended to support triage decisions and identify potentially high-risk patients. Final clinical decisions should always remain with qualified healthcare professionals.

**Algorithm Design Rationale**

A scoring-based approach was chosen because patient deterioration is rarely caused by a single abnormal measurement. In many situations, several moderately abnormal findings occurring together may indicate a serious clinical condition.

For example, a patient with a mildly elevated pulse rate, increased oxygen requirements, and an abnormal respiratory rate may be at greater risk than a patient with only one isolated abnormal value. By assigning points to multiple findings, the system can consider the overall clinical picture rather than relying on a single measurement.

The model also includes a nurse review step for missing data. This was incorporated because healthcare datasets are often incomplete, and important clinical decisions should not be based solely on missing or uncertain information. Human oversight remains essential to ensure safe and accurate triage decisions.

The purpose of the algorithm is to provide decision support, improve consistency, and help healthcare professionals prioritize patients efficiently while maintaining clinical judgment and patient safety.

**Explanation**

This digital triage model uses patient information to identify possible signs of clinical deterioration. Measurements such as GCS, blood pressure, pulse rate, respiratory rate, temperature, and oxygen support can provide healthcare workers with important information about how stable or unstable a patient may be.

The system works by assigning points to abnormal or concerning values. The more serious the abnormal finding, the more points are added to the risk score. For example, a patient with a very low GCS, low blood pressure, and high oxygen requirements would receive a high risk score because these signs may indicate serious illness or instability.

The model also includes a safety step for missing or unusual data. If an important value is missing, the system flags the patient record for nurse review instead of ignoring the issue. This is important because digital triage systems should support clinical judgment rather than replace it.

Overall, this system helps organize patient information, identify abnormal findings, and categorize patients into risk levels. By doing so, it can support faster triage decisions and help healthcare workers prioritize patients who may require urgent attention.
