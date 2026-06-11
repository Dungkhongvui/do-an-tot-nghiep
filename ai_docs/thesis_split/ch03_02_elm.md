---
source: thesis_fast.md
file: ch03_02_elm.md
title: ## **3.2 Extreme Learning Machine (ELM)**
---

## **3.2 Extreme Learning Machine (ELM)**

The Extreme Learning Machine (ELM) [11] is a learning algorithm developed for **single-hidden-layer feedforward neural networks (SLFNs)** , aiming to overcome the main limitations of conventional backpropagation-based training methods. Unlike traditional neural networks, ELM randomly assigns the input weights and hidden-layer biases and determines the output weights analytically in a single step [11]. This characteristic significantly reduces training time while maintaining good generalization performance.

## **3.2.1 Architecture of Extreme Learning Machine**

The structure of an ELM is similar to that of a single-hidden-layer feedforward neural network, consisting of an input layer, one hidden layer, and an output layer. However, the key difference lies in the training mechanism. In ELM, the **input weights and hidden-layer biases are randomly generated and fixed** , while only the output weights are calculated during the learning process.

Let 𝐱𝑗 ∈ℝ[𝑛] be the input vector of the 𝑗-th sample, and 𝑦𝑗 ∈ℝ be the corresponding target output. The output of the ELM model can be expressed as:

$$
\sum_{i=1}^{L} \beta_i\, g\left(w_i \cdot x_j + b_i\right) = y_j, 
\qquad j = 1,2,\ldots,N \tag{3.2}
$$

where

𝐿 is the number of hidden neurons,

𝐰𝑖and 𝑏𝑖 are the randomly assigned input weight vector and bias of the 𝑖-th hidden neuron,

𝑔(⋅) is the activation function, and

𝛽𝑖 represents the output weight.

## **3.2.2 Training Algorithm of ELM**

The ELM training process can be described in matrix form as:

$$
H\beta = Y \tag{3.3}
$$

where

𝐇 is the hidden-layer output matrix,

𝜷 is the vector of output weights, and

𝐓 is the target output matrix.

The hidden-layer output matrix 𝐇 is defined as:

$$
H =
\begin{bmatrix}
g(w_1 \cdot x_1 + b_1) & \cdots & g(w_L \cdot x_1 + b_L) \\
\vdots & \ddots & \vdots \\
g(w_1 \cdot x_N + b_1) & \cdots & g(w_L \cdot x_N + b_L)
\end{bmatrix} \tag{3.4}
$$

The output weights are computed analytically using the **Moore–Penrose pseudoinverse** :

$$
\beta = H^{\dagger} Y \tag{3.5}
$$

This closed-form solution eliminates the need for iterative learning, leading to extremely fast training compared to traditional neural networks.

## **3.2.3 Advantages and Limitations of ELM**

ELM offers several advantages over conventional feedforward neural networks:

- **Fast training speed** due to the absence of iterative weight updates

- **Simple network structure** and easy implementation

- **Good generalization capability** when properly configured

These advantages make ELM particularly suitable for **short-term load forecasting** , where rapid model training and real-time adaptability are required. However, ELM also has certain limitations. Since the input weights and biases are randomly generated, the forecasting performance may vary between different runs. Additionally, the selection of the number of hidden neurons has a significant

impact on model accuracy and stability. These issues may lead to suboptimal solutions and reduced robustness.

To address these limitations, optimization techniques such as **Particle Swarm Optimization (PSO)** can be employed to optimize the hidden-layer parameters of ELM. This hybrid approach enhances forecasting accuracy and stability, which will be discussed in detail in the following section.
