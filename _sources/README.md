# From Statistics to Statistical Learning

A Notebook Collection of the Following Data Science Books with Improved Readability:

- [Hands-on Machine Learning with Scikit-Learn, Keras & TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) (HandsOnML2, Machine Learning Sections)
- [Machine Learning with PyTorch and Scikit-Learn](https://www.amazon.ca/Machine-Learning-PyTorch-Scikit-Learn-learning/dp/1801819319) (PyTorch, Deep Learning Sections)
- [Introduction to Probability](https://www.routledge.com/Introduction-to-Probability-Second-Edition/Blitzstein-Hwang/p/book/9781138369917) (ITP, Python Translation)
- [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/) (SRT, Python Translation)

## 1. Basic Style

- Prefer `f-string` over `.format()`

```python
# good
title = "Titanic"
print(f"Scatter Plot of = {title}")

# bad
print("Scatter Plot of {}".format(title))
```

- Prefer `enumerate()` over `range(len())`

```python
xs = range(3)

# good
for ind, x in enumerate(xs):
  print(f'{ind}: {x}')

# bad
for i in range(len(xs)):
  print(f'{i}: {xs[i]}')
```

## 2. Matplotlib Style

- Prefer `Axes` object over `Figure` object
- use `constrained_layout=True` when draw subplots

```python
# good
_, axes = plt.subplots(1, 2, figsize=(10, 6))
axes[0].plot(x1, y1)
axes[1].hist(x2, y2)

# bad
plt.subplot(121)
plt.plot(x1, y1)
plt.subplot(122)
plt.hist(x2, y2)
```

- Prefer `axes.flatten()` over `plt.subplot()` in cases where subplots' data is iterable
- Prefer `zip()` or `enumerate()` over `range()` for iterable objects

```python
# good
_, ax = plt.subplots(2, 2)

for ax, x, y in zip(axes.flatten(), xs, ys):
  ax.plot(x, y)

# bad
for i in range(4):
  ax = plt.subplot(2, 2, i+1)
  ax.plot(x[i], y[i])
```

- Prefer `set()` method over `set_*()` method when there is no need to tweak many parameters
- Prefer use `plt.setp()` to tweak parameters.

```python
# good
ax.set(xlabel='x', ylabel='y')

# bad
ax.set_xlabel('x')
ax.set_ylabel('y')
```

- Prefer `ax.axis` over `ax.set(xlim, ylim)`

```python
# good
ax.axis([-1, 1, -1, 1])

# bad
ax.set(xlim=(-1, 1), ylim=(-1, 1))
```

## 3. Pandas Style

- Prefer `df['col']` over `df.col`

```python
# good
movies['duration']

# bad
movies.duration
```

- Prefer `df.query` over `df[]` or `df.loc[]` in simple-selection

```python
# good
movies.query('duration >= 200')

# bad
movies[movies['duration'] >= 200]
movies.loc[movies['duration'] >= 200, :]
```

- Prefer `df.loc` and `df.iloc` over `df[]` in multiple-selection

```python
# good
movies.loc[movies['duration'] >= 200, 'genre']
movies.iloc[0:2, :]

# bad
movies[movies['duration'] >= 200].genre
movies[0:2]
```

- Prefer `.astype('category')` over `.factorize()`

```python
# good

# bad
```

## 4. LaTeX Style

### 4.1. Multiple lines

Reduce the use of `begin{array}...end{array}`

- equations: `begin{aligned}...end{aligned}`

$$
\begin{aligned}
  y_1 = x^2 + 2*x \\
  y_2 = x^3 + x
\end{aligned}
$$

```latex
$$
\begin{aligned}
  y_1 = x^2 + 2*x \\
  y_2 = x^3 + x
\end{aligned}
$$
```

- equations with conditions: `begin{cases}...end{cases}`

$$
\begin{cases}
  y = x^2 + 2*x & x > 0 \\
  y = x^3 + x & x ≤ 0
\end{cases}
$$

```latex
$$
\begin{cases}
  y = x^2 + 2*x & x > 0 \\
  y = x^3 + x & x ≤ 0
\end{cases}
$$
```

- matrix: `begin{matrix}...end{matrix}`

$$
\begin{vmatrix}
  a + a^{′} & b + b^{′} \\ c & d
  \end{vmatrix} = \begin{vmatrix}
  a & b \\ c & d
  \end{vmatrix} + \begin{vmatrix}
  a^{′} & b^{′} \\ c & d
\end{vmatrix}
$$

```latex
$$
\begin{vmatrix}
  a + a^{′} & b + b^{′} \\ c & d
  \end{vmatrix} = \begin{vmatrix}
  a & b \\ c & d
  \end{vmatrix} + \begin{vmatrix}
  a^{′} & b^{′} \\ c & d
\end{vmatrix}
$$
```

### 4.2. Brackets

- Prefer `\Bigg...\Bigg` over `\left...\right`

$$
A\Bigg[\frac12\ \frac13\ ⋯\ \frac1{99}\Bigg]
$$

```latex
$$
A\Bigg[\frac12\ \frac13\ ⋯\ \frac1{99}\Bigg]
$$
```

- Prefer `\underset{}{}` over `\underset{}`

$$
\underset{θ}\mathrm{argmax}\ p(x_i ∣ θ)
$$

```latex
$$
\underset{θ}\mathrm{argmax}\ p(x_i ∣ θ)
$$
```

### 4.3. Expressions

- Prefer `^{\top}` over `^T` for transpose

$$
𝐀^⊤
$$

```latex
$$
𝐀^{\top}
$$
```

- Prefer `\to` over `\rightarrow` for limit

$$
\lim_{n → ∞}
$$

```latex
$$
\lim_{n\to \infty}
$$
```

- Prefer `underset{}{}` over `\limits_`

$$
\underset{w}\mathrm{argmin}\ (wx +b)
$$

```latex
$$
\underset{w}\mathrm{argmin}\ (wx +b)
$$
```

### 4.4. Fonts

- Prefer `mathrm{}` over `{\rm }` or `\mathop{}` or `\operatorname{}`

$$
θ_\mathrm{MLE} = \underset{θ}\mathrm{argmax}\ ∑_{i = 1}^{N}\log p(x_i ∣ θ)
$$

```latex
$$
θ_\mathrm{MLE} = \underset{θ}\mathrm{argmax}\ ∑_{i = 1}^{N}\log p(x_i ∣ θ)
$$
```

- Prefer `\mathbf{}` over `{\bf }`
- Prefer `\mathit{}` over `{\it }`
