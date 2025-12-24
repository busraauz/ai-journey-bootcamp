# Day 1 - Ames Housing Price Prediction

## Objective
Build an end-to-end ML regression workflow for the Ames Housing dataset with `SalePrice` as the target, from EDA to feature engineering and model selection, then evaluate the best model on a held-out test set.

## Dataset
Ames Housing from `datasets/ames_housing.csv`. The notebook inspects schema, summary stats, cardinality, and missing values before modeling.

## Key Techniques
- Train/test split with `train_test_split` to create a holdout set.
- EDA with histograms, correlations, scatter matrix, and targeted scatter plots.
- Feature engineering (age, total living area, garage age, cars-per-area).
- Custom transformer (`HousingFeatureAdder`) + `Pipeline` + `ColumnTransformer`.
- Imputation (median) + scaling for numeric data; one-hot encoding for categoricals.
- Model training and RMSE evaluation for Linear Regression, Decision Tree, and Random Forest.
- Cross-validation with `GridSearchCV` for tree-based model tuning.
- Feature importance inspection for the best Random Forest model.

## Key Insights
- SalePrice is most strongly tied to quality and size signals (Overall Qual, living area, garage capacity/area).
- Engineered features like house age and total living area improve the signal available to the model.
- Decision Tree performs very well on training data, indicating overfitting risk.
- Random Forest generalizes better after cross-validation and is selected as the final model.

## Business Questions Answered
- Which housing attributes best explain sale price?
- Does feature engineering materially improve model performance?
- Which baseline model generalizes better for house price prediction?

## What I Learned
- Column-wise preprocessing is cleaner and safer using `ColumnTransformer`.
- Custom transformers fit naturally inside pipelines for repeatable feature engineering.
- Cross-validation is essential to detect overfitting before trusting model metrics.
