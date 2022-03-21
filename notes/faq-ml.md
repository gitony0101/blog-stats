# Machine Learning FAQ

## 1. Linear Regression

### 1.1. Likelihood function

$$
\begin{aligned}
    L(θ) &= ∏_{i=1}^m p(y^{(i)} ∣ x^{(i)}; θ) \\
    &= ∏_{i=1}^m \frac1{\sqrt{2π} σ} \exp \left(-\frac{(y^{(i)} - θ^{T} x^{(i)})^2}{2 σ^2}\right)
\end{aligned}
$$

### 1.2. Gridient Descent

$$
J(θ_0, θ_1) = \frac1{2m} ∑_{i=1}^m(h_{θ}(x^{(i)})-y^{(i)})
$$

## 2. Tree

### 2.1. Entropy

$$
H_i = -∑_{k = 1 \atop p_{i, k ≠ 0}}^n p_{i, k} \log_2 p_{i, k}
$$

### 2.2. Pruning

## 3. Random Forest

## 4. LightGBM

## 5. PCA

## 6. K-Means

$$
\min ∑_{i=1}^{\mathrm{K}} ∑_{x ∈ C_i} \mathrm{dist}(c_i, x)^2
$$

### 6.1. Inertia curve

### 6.2. Silouette score

## 7. DBSCAN

- do not need appoint the number of clusters
