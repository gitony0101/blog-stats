# Deep Learning FAQ

- ![inverview](inverview.pdf)

## 1. Pipeline

### 1.1. Cleaning

- Standardize / Normalize
- Reduce data redundancy
- Rescale to particular range for better convergence
- Restructure data and improve integrity

### 1.2. Initalization

```py3
from numpy import random

w = random.randn(layer_size[i], layer_size[i-1])
```

### 1.3. Training

- epoch: one iteration over the entire dataset
- batch: one part of the dataset to feed
- iteration: data size / batch size

### 1.4. Batch Normalization

- normalize the inputs in every layer so that they have mean output activation of 0 and standard deviation of 1
  - trains faster
  - weights easier to initialize
  - higher learning rates
  - provides regularization
- ensure data satisfy independently identical distribution, especially for error $ϵ ∼ N(0, θ^2)$

## 2. Perceptron

### 2.1. Structure

- single layer perceptron
  - input layer
  - output layer
- multilayer perceptron
  - input layer
  - hidden layer (with activation function)
  - output layer

### 2.2. Algorithm

- single layer perceptron
  - linear separable classes
- multilayer perceptron
  - non-linear classes
  - backpropagation

## 3. Activation Function

Decides whether a neuron should be on / off

- input: the weighed sum of inputs and a bias
- output: Y

$$
Y=\sum(\mathrm{weight} * \mathrm{input}) + \mathrm{bias}
$$

### 3.1. Sigmoid

- range: `[0, 1]`
- center: `(0, 0.5)`

$$
f(z) = \frac1{1+e^{-z}}
$$

### 3.2. Tanh

- range: `[-1, 1]`
- center: `(0, 0)`

### 3.3. Softmax

- range: `[0, 1]`
- center: `(0, 0.5)`

$$
\mathrm{Softmax}(L_n)=\frac{e^{L_n}}{\|e^{L}\|}
$$

- used in output layer

### 3.4. ReLU

- range: `[0, ∞]`
- jump: `(0, 0)`

- used in hidden layer

## 4. Gridient Descent

### 4.1. Likelihood function

$$
\begin{aligned}
    L(θ) &= ∏_{i = 1}^m p(y^{(i)} ∣ x^{(i)}; θ) \\
    &= ∏_{i = 1}^m \frac1{\sqrt{2π} σ} \exp \Bigg(-\frac{(y^{(i)} - θ^⊤ x^{(i)})^2}{2 σ^2}\Bigg)
\end{aligned}
$$

Log

$$
\begin{aligned}
  \log(L(θ)) &= \sum_{i = 1}^m \log \frac1{\sqrt{2π}σ} \exp \Bigg(-\frac{(y^{(i)} - θ^⊤ x^{(i)})^2}{2σ^2}\Bigg) \\
  &= m\log \frac1{\sqrt{2π}σ} - \frac1{2σ^2} \sum_{i = 1}^m (y^{(i)} - θ^⊤ x^{(i)})^2
\end{aligned}
$$

$$
J(θ) = \frac12 \sum_{i = 1}^m (y^{(i)} - θ^⊤ x^{(i)})^2
$$

### 4.2. Cost Function

Measurement of model performance

> also refered as `loss` or `error`

$$
J(θ_0, θ_1) = \frac1{2m} ∑_{i = 1}^m(h_{θ}(x^{(i)})-y^{(i)})^2
$$

### 4.3. Backpropagation

backpropagates the error and updates the weights to reduce the error

### 4.4. Gridient Problems

- vanishing gridient
- exploding gridient

## 5. Optimization

## 6. Covolution Neural Network

- Covolution Layer
- ReLU layer
- Pooling layer
- Dense layer

### 6.1. Covolution Layer

### 6.2. Pooling layer

- down-sampling to reduce the dimensionality of feature map
- creates a pooled feature map by sliding a filter matrix over the input matrix

## 7. Overfitting

- resampling the data to estimate model accuracy (k-fold cross validation)
- having a validation dataset to evaluate the model

### 7.1. Dropout

- doubles the number of iterations needed to converge the network

## 8. Feedforward Neural Network

- signals travel in one direction (no feedback)
- considers only the current input
- can not memorize past data

## 9. Recurrent Neural Network

- signals travel in both directions
- considers the current input and the previously received input
- can memorize past data

### 9.1. Sentiment Analysis

### 9.2. Text Mining

### 9.3. Time Series

## 10. LTSM Neural Network

Special RNN that capable of learning long-term dependencies.

1. Decides what to forget and what to remember
2. Selectively update cell state values
3. Decides what part of the current state make it to the output

## 11. Restricted Boltzman Machine

Make stochastic decisions

- visible layer
- hidden layer

### 11.1. visible layer

### 11.2. hidden layer
