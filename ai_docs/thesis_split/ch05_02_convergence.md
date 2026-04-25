---
source: thesis_fast.md
file: ch05_02_convergence.md
title: ## **5.2 Convergence Behavior of the PSO Algorithm**
---

## **5.2 Convergence Behavior of the PSO Algorithm**

To further analyze the training process, the convergence characteristic of the Particle Swarm Optimization algorithm is presented in Figure 5.2.

Figure 5.2 depicts the fitness curve of the Particle Swarm Optimization algorithm over 50 iterations. The vertical axis represents the Mean Squared Error (MSE) of the training set (Loss function), while the horizontal axis represents the number of iterations.

The convergence process can be divided into two distinct phases, reflecting the balance between Exploration.

**Rapid Descent Phase (Iterations 0-20):** In the initial phase, the MSE drops sharply from approximately 0.00142 to 0.00130. This indicates the "Exploration" capability of the swarm, where particles quickly move from random positions towards promising regions in the search space. The steep slope proves that the PSO algorithm efficiently navigates the complex 700dimensional parameter space (weights and biases) of the ELM network.

**Stabilization Phase (Iterations 20-50):** From iteration 20 onwards, the curve flattens, indicating the "Exploitation" phase. The particles fine-tune their positions around the global optimum. The stability of the curve in the final iterations suggests that the model has successfully converged and avoided

premature stagnation (getting trapped in local minima), which is a common issue in standard gradient-based training methods.

Ultimately, the algorithm identifies the optimal weight configuration at the end of the 50th iteration, ensuring the ELM network is fully optimized for the forecasting task.
