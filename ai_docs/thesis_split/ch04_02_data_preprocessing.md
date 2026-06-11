---
source: thesis_fast.md
file: ch04_02_data_preprocessing.md
title: ## **4.2 Data Preprocessing**
---

## **4.2 Data Preprocessing**

Input data plays a decisive role in the accuracy of neural network forecasting models. The initial raw dataset often contains noise, missing values, and large discrepancies on scale among different measurement units. Therefore, the data processing procedure in this project is carried out through systematic steps, including data cleaning, feature transformation, and normalization. Specifically, three primary issues inherent in raw data that negatively impact the neural network training process are analyzed as follows [13]:

## **4.2.1 Noise and Outliers**

In real-world data collection, objective factors such as sensor errors, measurement device inaccuracies, or interference from the transmission environment often led to the appearance of noise. Noise consists of random fluctuations that do not reflect the true nature of the target variable. The presence of noise and outliers causes the neural network to prone to "learn" these errors (a phenomenon known as overfitting), thereby reducing its generalization capabilities and accuracy when forecasting on new datasets [14].

## **4.2.2 Missing Values**

Input data is frequently discontinuous due to incidents such as signal transmission loss, system maintenance, or server storage errors. For time-series forecasting models, data continuity is a critical factor for the model to capture temporal dependencies. Leaving these values empty results in immediate computational errors, while arbitrary imputation (such as filling with zero) can distort the statistical distribution of the dataset.

## **4.2.3 Large Scale Discrepancies**

Input features often possess vastly different units of measurement and value ranges. For instance, one variable may fluctuate within the range of [0, 1], while another may contain values in the thousands or millions. If left unaddressed, variables with larger magnitudes will dominate the weights of the neural network, causing the model to prioritize them over variables with smaller values, even if their informational importance is equal. Furthermore, this discrepancy causes the

error surface to become steep and irregular, making it difficult for optimization algorithms (such as Gradient Descent) to converge, or causing them to converge very slowly.

To mitigate the impact of these scale discrepancies and ensure numerical stability during the training process, the **Min-Max Normalization** technique is applied to all input variables. This transformation linearly scales the original data values into a fixed range of [0, 1], preventing features with larger magnitudes from dominating the learning process. The normalization formula is defined as follows:

$$
x_{\mathrm{norm}}=\frac{x-x_{\min}}{x_{\max}-x_{\min}}
$$

Where:

- 𝑥 is the original value of the input feature.

- 𝑥𝑚𝑖𝑛 and 𝑥𝑚𝑎𝑥represent the minimum and maximum values of that feature in the dataset, respectively.

- 𝑥𝑛𝑜𝑟𝑚 denotes the normalized value used as input for the neural network.

This step is particularly critical for the ELM model, as it ensures that the input signals fall within the active region of the Sigmoid activation function, thereby improving the convergence speed and forecasting accuracy.
