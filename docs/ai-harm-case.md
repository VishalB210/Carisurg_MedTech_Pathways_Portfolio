# AI Harm / Near-Miss Case Study: Epic Sepsis Model

**Primary source:** Wong et al. (2021), *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients*, JAMA Internal Medicine.

This case is a documented AI safety near-miss rather than a single confirmed patient injury. The system 
was the Epic Sepsis Model, a proprietary prediction model used to identify hospitalised patients at risk 
of sepsis. Sepsis is time-sensitive, so a tool that misses high-risk patients or sends too many false alerts 
can create real clinical danger. In an external validation study at Michigan Medicine, the model 
performed worse than expected. The study found poor discrimination and calibration, and at the 
evaluated threshold the model failed to identify many patients who developed sepsis while also 
producing a large number of alerts. 
The immediate failure was that the model did not reliably separate patients who would develop sepsis 
from those who would not. In plain language, the system was not accurate enough for the clinical task it 
was supporting. It missed many sepsis cases and produced alerts that could add work for clinicians. For 
an emergency department triage or early-warning environment, this matters because nurses and 
doctors already work under time pressure. A weak alerting system can create two safety problems at 
the same time: missed deterioration and alert fatigue. 
The deeper root cause was not simply that the model “made wrong predictions.” The deeper design 
assumption was that a proprietary model developed elsewhere could be widely implemented before 
strong independent local validation. The model was embedded in a large electronic health record 
system, but its performance was not adequately proven across every hospital workflow and patient 
population where it might be used. This is the same risk the Mercer proposal must avoid. An AI triage 
model trained at one site may not safely generalise to another hospital without local testing. 
This failure is both technical and human-factors related. It is technical because the model’s prediction 
performance and calibration were weak in the validation setting. It is also human-factors related 
because alerts do not operate in isolation: they enter a real clinical workflow where staff may become 
overloaded, ignore frequent alerts, or assume that a system built into the EHR has already been fully 
validated. 
A safeguard that would have caught this earlier is mandatory external validation before live clinical use. 
For the proposed AI-assisted ED triage system, the equivalent control would be a silent pilot at every 
new hospital. During the silent pilot, the model would generate risk flags in the background while 
clinicians continue normal triage. The Clinical AI Unit would compare the model’s Level 1 and Level 2 
recall, false-alert rate, and subgroup performance against predefined thresholds. If the model misses 
too many high-risk patients or produces too many low-value alerts, deployment should pause until the 
model is recalibrated or redesigned. 
The main lesson is that “implemented” does not mean “safe.” A model can be widely used and still be 
unsafe for a specific hospital unless its performance is checked in that exact setting (Wong et al., 2021).
