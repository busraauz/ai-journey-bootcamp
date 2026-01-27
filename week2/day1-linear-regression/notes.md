# Day 1: Linear Regression — Study Notes

## Goal of Day 1

- Understand **linear regression** from both a **statistical** and **optimization** perspective
- Implement linear regression:
  - **From scratch** (gradient descent)
  - **Using scikit-learn** (closed-form solution)
- Learn the **full ML workflow** with proper preprocessing, evaluation, and visualization

---

## 1️⃣ Linear Regression Model (Statistical Foundation)

### Model Equation

$\hat{y} = Xw + b$

Where:

- **X** → feature matrix
- **w** → weight vector (feature coefficients)
- **b** → bias (intercept)
- **y_hat** → predicted value

### Interpretation

- Each weight represents the **linear contribution** of a feature
- Bias shifts the prediction baseline
- Assumes a **linear relationship** between features and target

---

## 2️⃣ Loss Function

### Mean Squared Error (MSE)

$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$

### Root Mean Squared Error (RMSE)

$\text{RMSE} = \sqrt{\text{MSE}}$

- MSE is used during optimization
- RMSE is easier to interpret (same unit as target)

---

## 3️⃣ Optimization Layer (From-Scratch Learning)

### Objective

Minimize the loss function by finding optimal **w** and **b**.

### Gradients (Partial Derivatives)

For MSE loss:

**Gradient w.r.t. weights**
$\frac{\partial L}{\partial w}
= \frac{2}{n} X^T (Xw + b - y)$

**Gradient w.r.t. bias**
$\frac{\partial L}{\partial b}
= \frac{2}{n} \sum_{i=1}^{n} (Xw + b - y)$

- Gradients are computed **separately** for weights and bias
- Weights and bias affect the loss differently

### Gradient Descent Update Rules

$w := w - \alpha \frac{\partial L}{\partial w}$

$b := b - \alpha \frac{\partial L}{\partial b}$

Where:

- $\alpha$ → learning rate

### Learning Rate

- Controls step size during optimization
- Too large → divergence
- Too small → slow convergence

### Number of Epochs

- One epoch = one full pass over training data
- Too few → underfitting
- Too many → unnecessary computation / overfitting

### Early Stopping

- Stops training when loss improvement becomes negligible
- Prevents overfitting and saves computation

Example condition:
$|L_t - L_{t-1}| < \varepsilon$

### Scaling (MANDATORY for Gradient Descent)

- Gradient descent is **scale-sensitive**
- Without scaling, large-scale features dominate gradients
- Scaling is required for:
  - Gradient descent
  - Regularization
  - Distance-based models

---

## 4️⃣ Preprocessing (Feature Preparation)

Preprocessing prepares raw data for machine learning models and must be applied **before modeling**.

### Handling Missing Values

- Models cannot handle `NaN` values
- Strategies:
  - Fill missing values (preferred)
  - Drop rows/columns (only if missing is minimal)

**scikit-learn tools**

- `SimpleImputer`
- `KNNImputer`

### Numerical Features

#### Standardization

Centers data at mean 0 with unit variance.

$X_{\text{scaled}} = \frac{X - \mu}{\sigma}$

- Improves optimization stability
- Required for regularization

**sklearn**

- `StandardScaler`

#### Normalization (Min–Max Scaling)

Scales features to a fixed range \\([0, 1]\\).

$X_{\text{scaled}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$

**sklearn**

- `MinMaxScaler`

### Categorical Features

#### One-Hot Encoding

- Used for **nominal** categories
- No ordering assumption
- Creates binary indicator columns

**Important concepts**

- Dummy variable trap
- Reference category
- Handling unseen categories

**sklearn**

- `    OneHotEncoder(drop=\"first\", handle_unknown=\"ignore\")`

---

## 5️⃣ scikit-learn Linear Regression (Production Approach)

### Key Difference from Scratch

- Does **not** use gradient descent
- Uses **closed-form least squares solution**
- Solved via numerically stable linear algebra (SVD)

### Why Gradient Descent Is Not Needed

- MSE loss is convex
- Exact global minimum exists
- Closed-form solution is faster and more stable

---

## 6️⃣ Pipeline-Based Workflow (Correct ML Flow)

### End-to-End Steps

1. Raw data
2. Train/Test split
3. Feature preprocessing
   - Imputation
   - Scaling
   - Encoding
4. Model fitting
5. Evaluation
6. Visualization

**sklearn tools**

- `Pipeline`
- `ColumnTransformer`

Pipelines prevent **data leakage** and ensure correctness.

---

## 7️⃣ Model Evaluation

### Metrics

- Train RMSE
- Test RMSE

## 8️⃣ Key Understandings & Takeaways

- Linear regression is a **baseline model**
- Scratch implementation teaches optimization mechanics
- sklearn implementation is **production-ready**
- Preprocessing shapes the feature space
- Scaling is mandatory for optimization & regularization
- Pipelines prevent silent bugs and leakage
