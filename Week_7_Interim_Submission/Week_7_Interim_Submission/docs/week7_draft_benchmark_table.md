# Week 7 Interim Draft Benchmark Table

**Student:** Vishal Baboolal  
**Complex model:** Random Forest  
**Split:** Same Week 6 80/20 stratified split  
**Random seed:** `42`

| Model                                |   Accuracy |   Macro Precision |   Macro Recall |   Macro F1 |   ESI 1 Recall |   Training Time (s) |   Inference Time per Prediction (ms) | Interpretability   |
|:-------------------------------------|-----------:|------------------:|---------------:|-----------:|---------------:|--------------------:|-------------------------------------:|:-------------------|
| Logistic Regression (Week 6)         |      0.667 |             0.582 |          0.463 |      0.492 |          0.25  |              14.043 |                               0.0096 | High               |
| Decision Tree, max_depth=12 (Week 6) |      0.585 |             0.481 |          0.295 |      0.303 |          0.062 |               0.567 |                               0.0012 | High               |
| Random Forest, 200 trees (Week 7)    |      0.497 |             0.407 |          0.557 |      0.398 |          0.5   |               9.324 |                               0.0222 | Medium             |

## Initial interpretation

- Logistic regression remains the strongest model on overall accuracy and macro F1.
- The random forest improves ESI Level 1 recall to **50.0%**, compared with **25.0%** for logistic regression.
- This improvement comes with lower overall accuracy and lower macro F1, which means the model catches more critical cases but creates more errors elsewhere.
- Random-forest inference is still fast per patient, but the model is less directly explainable than logistic regression or a single decision tree.
- These timings are wall-clock measurements from one runtime and must be rerun in the same deployment environment before making a final cost recommendation.

## Interpretability scale

- **High:** a single prediction can be explained using model coefficients or one decision path.
- **Medium:** global feature importance is available, but 200 trees do not provide one simple patient-level story.
- **Low:** a separate explanation method, such as SHAP, would normally be required.
