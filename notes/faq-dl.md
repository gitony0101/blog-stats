# Deep Learning FAQ

- ![inverview](inverview.pdf)

## 1. Pipeline

### 1.1. Normalization

- Standardize
- Reduce data redundancy
- Rescale to particular range for better convergence
- Restructure data and improve integrity

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

### 3.2. Tanh

- range: `[-1, 1]`
- center: `(0, 0)`

### 3.3. ReLU

- range: `[0, ∞]`
- jump: `(0, 0)`

## 4. Cost Function

Measurement of model performance

> also refered as `loss` or `error`

### 4.1. Mean Squared Error

## 5. Optimization

### 5.1. Gridient Descent

### 5.2. Backpropagation

backpropagates the error and updates the weights to reduce the error

## 6. Feedforward Neural Network

- signals travel in one direction (no feedback)
- considers only the current input and do not memorize the previous ones

## 7. Recurrent Neural Network

## 8. Restricted Boltzman Machine

Make stochastic decisions

### 8.1. Structure

- visible layer
- hidden layer
