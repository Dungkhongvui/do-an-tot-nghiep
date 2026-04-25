---
source: thesis_fast.md
file: ch06_conclusion_future_work.md
title: ## **CHAPTER 6. CONCLUSION AND RECOMMENDATIONS**
---

## **CHAPTER 6. CONCLUSION AND RECOMMENDATIONS**

## **6.1 Conclusion**

Short-term electrical load forecasting is a vital component in the operation and planning of power systems. This thesis addressed the specific challenge of improving forecasting stability and accuracy by proposing a hybrid model combining the **Extreme Learning Machine (ELM)** and **Particle Swarm Optimization (PSO)** . While ELM is renowned for its rapid learning speed and simple structure, it suffers from instability due to the random initialization of input weights and hidden biases. The integration of PSO was employed to optimally tune these parameters, thereby mitigating the stochastic nature of the standard ELM. Based on the theoretical analysis and comprehensive experimental results presented in Chapter 5, the following conclusions can be drawn:

- **Superior Forecasting Accuracy:** The proposed PSO-ELM model demonstrated a consistent improvement in prediction accuracy over the standard ELM model.

   - The experimental results showed that the **Mean Absolute Percentage Error (MAPE)** was reduced from an average of **2.1852%** (Standard ELM) to **2.0174%** (PSO-ELM).

   - In the best-case scenario, the PSO-ELM model achieved a MAPE as low as **1.9626%** , proving its capability to capture the nonlinear and complex characteristics of the electrical load profile.

- **Enhanced Model Stability and Robustness:** The most significant contribution of this study lies in the improvement of model reliability.

   - Standard ELM models exhibit high variance in performance across different trials due to random initialization. The experiments revealed that the **Standard Deviation** of the MAPE for the Standard ELM was **0.0510%** .

   - The PSO-ELM model significantly minimized this fluctuation, achieving a standard deviation of only **0.0279%** . This **45% reduction in instability** confirms that the PSO algorithm successfully navigated the parameter space to find a stable and optimal network configuration, rather than relying on chance.

- **Feasibility for Practical Application:** Although the optimization process via PSO introduces additional computational time compared to the single step learning of standard ELM, the convergence analysis indicated that the model converges rapidly within the first 20 iterations. Thesidering the trade-off between a slight increase in training time and a substantial gain in

reliability, the PSO-ELM model is a highly viable solution for daily operational planning where accuracy and consistency are paramount.

## **6.2 Limitations**

Despite the encouraging results, this study has several limitations that should be acknowledged:

- **Scope of Forecasting:** The model focuses exclusively on short-term load forecasting at the system level. The applicability of the proposed approach to medium-term or long-term forecasting scenarios, or to individual household levels, has not been investigated.

- **Input Feature Set:** The input features are primarily based on historical load patterns and dry-bulb temperature. Although this choice ensures model simplicity, it may restrict the ability of the model to fully capture external influences under extreme weather conditions or abnormal social events.

- **Simulation Environment:** The experiments were conducted in an offline simulation environment using historical data. Real-time deployment aspects, such as online learning capability and computational constraints in operational control centers, were not fully addressed in this study.

## **6.3 Recommendations and Future Work**

To further enhance the applicability and precision of the forecasting system, several avenues for future research are recommended:

1. **Expansion of Input Features:** The current model relies heavily on historical load data and temperature. However, electricity demand is also sensitive to other meteorological and socio-economic factors. Future studies should be incorporated:

   - **Humidity and Heat Index:** As noted in related studies on load forecasting (e.g., Dang Quang Khoa, 2017 [9]), humidity significantly impacts human comfort and air conditioning usage.

   - **Special Events Calendar:** Encoding features for specific holidays, festivals, or major sporting events could help the model better anticipate abnormal load drops or spikes that statistical periodicity fails to capture.

2. **Investigation of Advanced Optimization Algorithms:** This thesis utilized Particle Swarm Optimization (PSO) due to its simplicity and global search capability. Future work could compare PSO with newer meta-heuristic algorithms such as the **Grey Wolf Optimizer (GWO)** or **Whale Optimization Algorithm (WOA)** , or evolutionary strategies like **Genetic Algorithms (GA)** , to potentially achieve faster convergence rates.

3. **Development of Deep Hybrid Models:** Recent benchmarks (Nguyen Thi Hoai Thu et al., 2024) [10] suggest that while Deep Learning models like LSTM generally require longer training times, they excel at capturing longterm temporal dependencies. A promising direction is to develop hybrid **LSTM-PSO** architecture. This would combine the deep memory capabilities of LSTM with the parameter optimization strengths of PSO, potentially offering a superior balance for medium-term forecasting horizons.

4. **Real-time Deployment and Online Learning:** Future development should focus on deploying the model as a web-based dashboard or integrating it into a SCADA system. Implementing an **Online ELM (OS-ELM)** mechanism would allow the model to update its weight continuously as new data streams in, ensuring the forecast remains accurate over time without the need for periodic retraining.
