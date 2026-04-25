---
source: thesis_fast.md
file: ch03_04_metrics.md
title: ## **3.4 Error Evaluation Metrics**
---

## **3.4 Error Evaluation Metrics**

To evaluate the performance of load forecasting models, appropriate **error evaluation metrics** are required. These metrics quantify the difference between the actual load values and the predicted results, thereby providing an objective basis for comparing different forecasting models. In this study, three widely used error metrics are adopted: **Mean Absolute Error (MAE)** , **Mean Absolute Percentage Error (MAPE)** , and **Root Mean Square Error (RMSE)** .

## **3.4.1 Mean Absolute Error (MAE)**

Mean Absolute Error measures the average magnitude of errors between predicted and actual values without considering their direction. It is defined as:

$$
\mathrm{MAE} = \frac{1}{N}\sum_{i=1}^{N}\left|y_i - \hat{y}_i\right|
$$

where

𝑦𝑖 is the actual load value,

𝑦̂𝑖 is the predicted load value, and

𝑁 is the total number of samples.

MAE is easy to interpret and provides a direct indication of the average forecasting error in the same unit as the load data. However, it does not penalize large errors more heavily than small ones.

## **3.4.2 Mean Absolute Percentage Error (MAPE)**

Mean Absolute Percentage Error expresses the forecasting error as a percentage, making it independent of the data scale. It is calculated as:

$$
\mathrm{MAPE} = \frac{100}{N}\sum_{i=1}^{N}\left|\frac{y_i-\hat{y}_i}{y_i}\right|
$$

MAPE is widely used in electric load forecasting due to its intuitive interpretation and suitability for comparing forecasting performance across different datasets. Nevertheless, MAPE may become unstable when the actual load values are close to zero.

## **3.4.3 Root Mean Square Error (RMSE)**

Root Mean Square Error emphasizes larger errors by squaring the deviations before averaging. It is defined as:

$$
\mathrm{RMSE}=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i-\hat{y}_i)^2}
$$

RMSE is sensitive to large forecasting errors and is particularly useful for assessing model robustness under peak load conditions. A lower RMSE indicates better overall forecasting performance.

## **3.4.4 Discussion on Metric Selection**

Each evaluation metric highlights different aspects of forecasting performance. MAE reflects average error magnitude, MAPE provides a relative error measure, and RMSE penalizes large deviations more strongly. Therefore, using multiple evaluation metrics allows for a more comprehensive assessment of model accuracy and reliability.

In this study, MAE, MAPE, and RMSE are jointly used to evaluate and compare the performance of the proposed ELM–PSO model with other forecasting approaches. The evaluation results are presented and discussed in Chapter 5.
