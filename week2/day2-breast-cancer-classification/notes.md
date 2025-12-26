# Day 2 - Breast Cancer Classification

## Objective
Build a binary classification workflow to predict whether a tumor is malignant or benign, focusing on medically relevant metrics like recall and ROC AUC.

## Dataset
Breast cancer dataset from `datasets/breast_cancer.csv` with `diagnosis` as the target (M/B) and tumor feature measurements as inputs.

## Key Techniques
- Problem framing and metric selection for medical diagnostics (precision, recall, F1, ROC AUC).
- Basic EDA: class distribution, feature histograms, boxplots by diagnosis.
- Correlation analysis with a numeric target mapping and heatmap.
- Train/test split with stratification and target encoding (M=1, B=0).
- Standardization via a preprocessing pipeline.
- Model comparison with Logistic Regression, SGDClassifier, and Random Forest.
- Cross-validated metrics and confusion matrices to compare recall and false negatives.
- ROC curve analysis using cross-validated probabilities.
- Hyperparameter tuning for Logistic Regression with `GridSearchCV` and recall-focused scoring.
- Final evaluation on a held-out test set with metrics and ROC curve.

## Key Insights
- Recall is prioritized to minimize missed malignant cases, even at the cost of more false alarms.
- Logistic Regression is more stable and better calibrated than SGD for this dataset.
- Cross-validated ROC AUC and F1 support Logistic Regression as the best baseline.
- Tuned Logistic Regression generalizes well on the test set.

## Business Questions Answered
- Which model best detects malignant tumors while minimizing false negatives?
- How do precision/recall tradeoffs compare across baseline classifiers?
- Does tuning Logistic Regression improve recall-focused performance?

## What I Learned
- Medical classification should prioritize recall and ROC AUC over raw accuracy.
- Confusion matrices make the cost of false negatives explicit.
- Even simple linear models can perform very well with proper scaling and tuning.
