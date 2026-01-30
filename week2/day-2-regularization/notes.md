# Day 2: Regularization — Study Notes

## Goal of Day 2

- Understand **why regularization is needed** (overfitting, variance)
- Learn L2 (Ridge), L1 (Lasso), and ElasticNet penalties
- Implement models:
  - **From scratch** (gradient descent + penalty)
  - **Using scikit-learn** (Ridge, Lasso, ElasticNet)
- Compare model behavior, sparsity, and generalization

---

## 1️⃣ Why Regularization

- Linear regression can **overfit** when features are noisy or correlated
- Regularization adds a **penalty term** to control model complexity
- Goal: **trade a small bias** for a **large variance reduction**

---

## 2️⃣ Ridge Regression (L2)

### Objective Function

$J(w,b) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} w_j^2$

- Penalizes **large weights**
- Shrinks coefficients but **rarely makes them zero**
- Works well with **multicollinearity**

### Gradient (for scratch)

$\frac{\partial J}{\partial w} = \frac{2}{n} X^T(Xw + b - y) + 2\lambda w$

$\frac{\partial J}{\partial b} = \frac{2}{n} \sum_{i=1}^{n} (Xw + b - y)$

---

## 3️⃣ Lasso Regression (L1)

### Objective Function

$J(w,b) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} |w_j|$

- Encourages **sparsity** (drives some weights to zero)
- Can act as **feature selection**
- Optimization is **non-smooth** at zero

### Subgradient (for scratch)

$\frac{\partial J}{\partial w} = \frac{2}{n} X^T(Xw + b - y) + \lambda \; \text{sign}(w)$

$\frac{\partial J}{\partial b} = \frac{2}{n} \sum_{i=1}^{n} (Xw + b - y)$

---

## 4️⃣ ElasticNet (L1 + L2)

### Objective Function

$J(w,b) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \left( \alpha \sum |w_j| + (1-\alpha) \sum w_j^2 \right)$

- Combines **sparsity** (L1) and **stability** (L2)
- Useful when features are **correlated**
- Controlled by:
  - $\lambda$ → overall strength
  - $\alpha$ → balance between L1 and L2

### Subgradient (for scratch)

$\frac{\partial J}{\partial w} = \frac{2}{n} X^T(Xw + b - y) + \lambda\left( \alpha\,\text{sign}(w) + 2(1-\alpha)w \right)$

$\frac{\partial J}{\partial b} = \frac{2}{n} \sum_{i=1}^{n} (Xw + b - y)$

---

## 5️⃣ Scaling is Mandatory

- Regularization depends on coefficient size
- If features are not scaled, the penalty is **unfair**
- Standardization is the common choice

$X_{\text{scaled}} = \frac{X - \mu}{\sigma}$

---

## 6️⃣ Workflow (Scratch vs sklearn)

### Scratch Workflow

1. Split data
2. Scale features using training mean/std
3. Initialize $w, b$
4. Compute predictions
5. Compute loss = MSE + penalty
6. Update parameters with gradient descent
7. Evaluate train/test error

### sklearn Workflow

1. Train/test split
2. Build preprocessing pipeline
3. Fit Ridge / Lasso / ElasticNet
4. Evaluate with MSE/RMSE
5. Compare train vs test performance

---

## 7️⃣ Evaluation & Interpretation

- **Train RMSE vs Test RMSE**
  - Large gap → overfitting
  - Similar and low → good generalization
- **Coefficient behavior**
  - Ridge: small but non-zero weights
  - Lasso: many zeros
  - ElasticNet: mix of shrinkage + sparsity
- **Visualization**
  - Predicted vs Actual: points near diagonal indicate good fit

---

## 8️⃣ Key Understandings & Limitations

- Regularization improves **generalization**, not raw training fit
- Ridge is stable with **multicollinearity**
- Lasso performs **feature selection** but can be unstable
- ElasticNet balances sparsity and stability
- Results are sensitive to **lambda** and **alpha**
- Always scale features when using regularization
