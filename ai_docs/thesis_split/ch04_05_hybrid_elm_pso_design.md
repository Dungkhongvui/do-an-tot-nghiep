---
source: thesis_fast.md
file: ch04_05_hybrid_elm_pso_design.md
title: ## **4.5 Hybrid ELM-PSO Model Design**
---

## **4.5 Hybrid ELM-PSO Model Design**

To overcome the instability issues inherent in traditional ELM networks, this thesis proposes a hybrid **PSO-ELM** model. This model leverages the rapid computational speed of ELM and the global search capability of Particle Swarm Optimization (PSO) to determine the most optimal network configuration.

## **4.5.1 The ELM Problem: Randomness of Hidden Layer Weights**

The Extreme Learning Machine (ELM) is a type of Single-Hidden Layer Feedforward Network (SLFN). Assuming the network has 𝑁 input nodes and 𝐾 hidden nodes. For an input data sample 𝑥, the output of the 𝑗-th hidden node is calculated via the Sigmoid activation function as follows:

$$
h_j(x)=\frac{1}{1+e^{-(w_j\cdot x+b_j)}}
$$

Where:

- 𝑤𝑗: Weight vector connecting the input layer to the 𝑗-th hidden node.

- 𝑏𝑗: Bias value of the 𝑗-th hidden node.

The output weight vector 𝛽 connecting the hidden layer to the output layer is calculated analytically using the Moore–Penrose generalized inverse method:

## **Existing Problem**

In the original ELM algorithm, the input parameters (𝑤𝑗,  𝑏𝑗 ) are initialized randomly and remain fixed. This leads to two major limitations:

- **Uncertainty:** Different runs produce different forecasting results, sometimes yielding large errors if the random weights fall into a “poor” region.

- **Sub-optimality:** The lack of fine-tuning for hidden layer weights may require a very large number of hidden nodes to achieve the desired accuracy, resulting in a waste of computational resources.

## **4.5.2 Applying PSO for ELM Parameter Optimization**

To resolve the randomness issue mentioned above, the PSO algorithm is utilized to search for the parameter set (𝑊, 𝑏) that minimizes the training error. The mathematical structure of the algorithm in the program is established as follows:

## **a. Particle Representation**

Variables to Optimize:

For the proposed ELM network configured with 𝑁𝑖𝑛𝑝𝑢𝑡 = 13 input features and 𝑁ℎ𝑖𝑑𝑑𝑒𝑛 = 50 hidden neurons, the set of parameters required to be optimized includes:

- The input weight matrix W with dimensions 13×50.

- The bias vector b with dimensions 50.

Each particle in the swarm represents a candidate ELM network configuration. Since PSO operates in a vector space, the entire weight matrix 𝑊 and bias vector 𝑏 are flattened into a single position vector 𝑋. The dimensionality of a particle (𝐷𝑖𝑚) is determined by:

$$
\mathrm{Dim} = (N_{\mathrm{input}} \times N_{\mathrm{hidden}}) + N_{\mathrm{hidden}}
$$

Substituting the specific values from our model:

𝐷𝑖𝑚= 13 × 50 + 50 = 700 𝑑𝑖𝑚𝑒𝑛𝑠𝑖𝑜𝑛𝑠

The search bounds for these variables are set within the range [−1, 1].

## **b. Fitness Function**

The quality of each particle is evaluated using the **Mean Squared Error (MSE)** on the training dataset. The process for calculating the fitness value for a particle 𝑖 consists of the following steps:

1. Decode the position vector 𝑋𝑖 into the weight matrix 𝑊 and bias vector 𝑏.

2. Calculate the hidden layer output matrix 𝐻using the Sigmoid function.

3. Calculate the output weight 𝛽= pinv(𝐻) ⋅𝑌𝑡𝑟𝑎𝑖𝑛.

## 4. Calculate the prediction error:

$$
\mathrm{Fitness}(X_i)=\frac{1}{M}\sum_{k=1}^{M}\left(y_{\mathrm{actual}}^{(k)}-y_{\mathrm{predicted}}^{(k)}\right)^2
$$

The goal of the algorithm is to find the particle 𝑋𝑜𝑝𝑡 such that:

$$
\mathrm{Fitness}(X_{\mathrm{opt}}) \to \min
$$

## **c. Position and Velocity Update Mechanism**

Based on the implementation code, particles move through the search space using the following velocity and position update formulas at iteration 𝑡+ 1:

## **• Velocity Update Formula:**

$$
V_i(t+1)=w\cdot V_i(t)+c_1\cdot r_1\cdot\left(P_{best,i}-X_i(t)\right)+c_2\cdot r_2\cdot\left(G_{best}-X_i(t)\right)
\tag{4.5}
$$

Where the empirical parameters are set in the code as follows:

𝑤= 0.7: Inertia weight, helping the particle maintain its momentum to explore new spaces.

𝑐1 = 1.5: Cognitive component coefficient, representing the tendency of the particle to return to its own best position (𝑃𝑏𝑒𝑠𝑡).

𝑐2 = 1.5: Social component coefficient, representing the tendency of the particle to move towards the swarm’s best position (𝐺𝑏𝑒𝑠𝑡).

𝑟1, 𝑟2: Two random numbers uniformly distributed in the range [0, 1].

## **• Position Update Formula:**

$$
X_i(t+1)=X_i(t)+V_i(t+1)
$$

## **d. Implementation Procedure**

The optimization process takes place over **50 iterations** (𝑖𝑡𝑒𝑟𝑎𝑡𝑖𝑜𝑛𝑠= 50) with a population of **50 particles** (𝑝𝑜𝑝_𝑠𝑖𝑧𝑒= 50). In each iteration, the algorithm performs:

1. **Evaluates the accuracy (MSE)** of each particle by constructing a temporary ELM model.

2. **Updates** 𝑃𝑏𝑒𝑠𝑡 for each particle and 𝐺𝑏𝑒𝑠𝑡 for the entire swarm.

3. **Adjust the velocity and position** of particles according to the formulas above.

4. **After the final iteration** , the 𝐺𝑏𝑒𝑠𝑡 position is used as the official weight set 𝑊 and 𝑏 for the final test forecasting model.

## **4.5.3 Selection of Hidden Layer Neurons**

In the architecture of an Extreme Learning Machine (ELM), the number of neurons in the hidden layer 𝑁ℎ𝑖𝑑𝑑𝑒𝑛 is a critical hyperparameter that directly impacts the network's learning capability and generalization performance.

- **Underfitting:** If 𝑁ℎ𝑖𝑑𝑑𝑒𝑛 is too small, the network may lack the capacity to capture the complex, nonlinear relationships inherent in the electrical load data.

- **Overfitting:** Conversely, an excessive number of neurons can lead to overfitting, where the model memorizes noise in the training data rather than learning general patterns. Additionally, a large 𝑁ℎ𝑖𝑑𝑑𝑒𝑛 significantly increases the dimensionality of the optimization problem, leading to higher computational costs for the PSO algorithm.

Since there is no single analytical formula to determine the exact optimal number of hidden neurons, this study employs a **"Trial-and-Error"** approach based on empirical experiments. The selection range is also guided by reference configurations from related studies, such as Nguyen Thi Hoai Thu et al. [10], who successfully utilized 50 hidden neurons for a similar load forecasting dataset in Hanoi.

The selection procedure was conducted as follows:

1. A testing range for 𝑁ℎ𝑖𝑑𝑑𝑒𝑛 was established from 10 to 100 with an increment of 10.

2. For each configuration, the ELM-PSO model was trained, and the Root Mean Square Error (RMSE) was evaluated on the validation set.

3. The optimal value was selected based on the lowest error rate and reasonable training time.

The experimental results are summarized in Table 4.3 below:

_Table 4.3 Performance comparison with different numbers of hidden neurons_

|**Number of**<br>**Neurons (**𝑵𝒉𝒊𝒅𝒅𝒆𝒏**)**|**RMSE**<br>**(MW)**|**MAPE**<br>**(%)**|**MAE**<br>**(MW)**|**Evaluation**|
|---|---|---|---|---|
|**10**|927.95|2.43|690.83|High error<br>(Underfitting)|
|**20**|854.47|2.16|620.46|Significant<br>improvement|
|**50**|828.89|2.03|584.02|Optimal Balance|
|**100**|798.54|1.96|563.03|Diminishing<br>returns|

**Conclusion:** Based on the empirical results, **50 hidden neurons** were selected for the proposed model. This configuration achieves the lowest RMSE while maintaining computational efficiency.
