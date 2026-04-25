---
source: thesis_fast.md
file: ch04_06_workflow.md
title: ## **4.6 Block Diagram of the ELM-PSO Neural Network**
---

## **4.6 Block Diagram of the ELM-PSO Neural Network**

```mermaid
flowchart TD
    A([START]) --> B[/Load Data:<br/>final_data_with_lag.csv/]
    B --> C[Split Data: 80% Train, 20% Test]
    C --> D[Define PSO Parameters]
    D --> Dn[Pop_size=50, Max_iter=50<br/>w=0.7, c1=1.5, c2=1.5]
    Dn --> E[Initialize Particles<br/> - Random Position X and Velocity V]

    E --> F{"Iteration &lt; 50?"}

    %% Loop branch
    F -- Yes --> G[For each Particle j]
    G --> H[Decode Position to<br/>Weights W and Bias b]
    H --> I[Calculate Hidden Layer H<br/> - Sigmoid Activation]
    I --> J[Calculate Output Weights Beta<br/> - Moore-Penrose Pseudoinverse]
    J --> K[Calculate Fitness<br/> - MSE on Training Set]

    K --> L{"Fitness &lt; P_best?"}
    L -- Yes --> M[Update P_best]
    L -- No --> N{"Fitness &lt; G_best?"}
    M --> N

    N -- Yes --> O[Update G_best]
    N -- No --> P[Update Velocity & Position]
    O --> P
    P --> F

    %% Final branch
    F -- No --> Q[Update Velocity & Position]
    Q --> R[Compute Final Beta<br/>using Training Set]
    R --> S[Predict on Test Set]
    S --> T[Denormalize Data<br/> - Convert back to MW]
    T --> U[Range: 18041, 41015]
    U --> V[Calculate Performance Metrics<br/> - MAPE, RMSE]
    V --> W[/Plot Comparison &<br/>Convergence/]
    W --> X([END])

    classDef startEnd fill:#d9ead3,stroke:#7aa56f,color:#000;
    classDef endNode fill:#f4cccc,stroke:#cc7a7a,color:#000;
    classDef decision fill:#fce5cd,stroke:#c9a227,color:#000;
    classDef note fill:#d9d9d9,stroke:#b7b7b7,color:#000;
    classDef io fill:#f3f3f3,stroke:#666,color:#000;
    classDef process fill:#f3f3f3,stroke:#666,color:#000;

    class A startEnd;
    class X endNode;
    class F,L,N decision;
    class Dn,U note;
    class B,W io;
    class C,D,E,G,H,I,J,K,M,O,P,Q,R,S,T,V process;
```

_Figure 4.4 Block diagram of the ELM-PSO Neural Network_

The flowchart illustrates the operational workflow of the electrical load forecasting program using the hybrid PSO-ELM model. The process is divided into three main phases:

## **4.6.1 Initialization and Data Processing Phase**

- **Load Data:** The program initiates by loading the final_data_with_lag.csv file.

- **Data Splitting:** The dataset is split sequentially (without random shuffling to preserve temporal order) into **80% for Training** and **20% for Testing** .

- **PSO Parameter Setup:** Operational parameters for the Particle Swarm Optimization algorithm are set according to the source code:

   - Population size: 50 particles.

   - Max iterations: 50.

   - Inertia weight (𝑤 **):** 0.7.

   - Acceleration coefficients (𝑐1, 𝑐2): Both set to 1.5 **.**

- **Swarm Initialization:** Random positions (representing weights 𝑊 and biases 𝑏) and initial velocities are generated for particles within the search space [−1, 1].

## **4.6.2 Optimization Loop Phase (PSO Loop)**

This is the core of the algorithm, executed for 50 iterations:

- **Particle Decoding:** In each iteration, the position of every particle is decoded into the input weight matrix W and bias vector b of the ELM network.

- **ELM Computation:**

   - Compute the hidden layer matrix 𝐻 using the **Sigmoid activation function** .

   - Compute the output weights 𝛽 using the **Moore–Penrose Pseudoinverse** method.

- **Fitness Evaluation:** Calculate the **Mean Squared Error (MSE)** between the predicted and actual values on the **Training set** .

- **Update:**

   - Compare the current fitness with the **Personal Best** (𝑃𝑏𝑒𝑠𝑡) and **Global Best** (𝐺𝑏𝑒𝑠𝑡), update them if a better solution is found.

   - Calculate new velocities and move particles to new positions based on the PSO velocity update formula.

## **4.6.3 Forecasting and Evaluation Phase**

- **Optimal Model Construction:** After the loops conclude, the best parameter set from 𝐺𝑏𝑒𝑠𝑡 is extracted to construct the final ELM network.

- **Prediction:** The network performs forecasting on the Test set (unseen data).

- **Denormalization:** The forecast results (currently in normalized 0-1 form) are converted back to actual power units (MW) based on the range [18041, 41015].

- **Termination:** Calculate MAPE and RMSE metrics, and plot comparison charts.
