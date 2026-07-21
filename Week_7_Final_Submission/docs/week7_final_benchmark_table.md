# Week 7 Final Benchmark Table

| Model               |   Accuracy |   Macro Precision |   Macro Recall |   Macro F1 |   ESI 1 Recall |   Training Time (s) |   Inference Time per Prediction (ms) | Interpretability   |
|:--------------------|-----------:|------------------:|---------------:|-----------:|---------------:|--------------------:|-------------------------------------:|:-------------------|
| Logistic Regression |      0.667 |             0.582 |          0.463 |      0.492 |          0.25  |              13.581 |                               0.0103 | High               |
| Decision Tree       |      0.585 |             0.481 |          0.295 |      0.303 |          0.062 |               0.368 |                               0.001  | High               |
| Random Forest       |      0.497 |             0.407 |          0.557 |      0.398 |          0.5   |               7.301 |                               0.0235 | Medium             |
| LightGBM Base       |      0.673 |             0.589 |          0.436 |      0.472 |          0.125 |               2.456 |                               0.0325 | Medium             |
| XGBoost Base        |      0.614 |             0.579 |          0.35  |      0.377 |          0.188 |               3.566 |                               0.0075 | Medium             |
| Optimised LightGBM  |      0.664 |             0.521 |          0.516 |      0.518 |          0.25  |               3.908 |                               0.0574 | Medium             |
