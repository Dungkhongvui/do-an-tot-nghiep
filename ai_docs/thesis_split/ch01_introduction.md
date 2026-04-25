---
source: thesis_fast.md
file: ch01_introduction.md
title: ## **CHAPTER 1. INTRODUCTION**
---

## **CHAPTER 1. INTRODUCTION**

## **1.1 Rationale and Objectives**

Electricity is a flexible and widely used energy source that plays a vital role in daily life and industrial production. Compared to conventional energy sources such as coal, oil, and natural gas, electricity is more efficient and environmentally friendly. In recent years, the increasing importance of electricity has made power demand forecasting a crucial research topic. Unlike other commodities, electricity cannot be stored in large quantities and must be generated in real time to meet demand [1]. Furthermore, rapid growth in electricity consumption due to population increase and industrial development has created significant challenges for power system operation. Therefore, accurate load forecasting is essential for effective power generation planning.

Electrical load forecasting has been widely studied using various approaches, which can be broadly classified into traditional statistical methods and artificial intelligence–based techniques. Conventional statistical methods such as linear regression and time series models are simple and interpretable, but they often fail to capture the nonlinear and complex characteristics of electrical load demand [2]. In recent years, artificial intelligence methods, including artificial neural networks, support vector machines, and deep learning models, have demonstrated superior performance in modeling nonlinear relationships and handling large-scale datasets. However, many of these methods suffer from high computational cost, slow training speed, and sensitivity to parameter selection. Therefore, there is a growing demand for forecasting models that achieve high accuracy while maintaining computational efficiency and stability.

Extreme Learning Machine (ELM) has attracted significant attention due to its fast-training speed, simple network structure, and strong generalization capability, as it randomly assigns hidden-layer parameters and analytically determines output weights. This characteristic makes ELM particularly suitable for large-scale and real-time load forecasting problems. However, the randomness of hidden-layer weights may lead to unstable prediction performance. Particle Swarm Optimization (PSO), a population-based metaheuristic algorithm, is effective in global optimization with fast convergence and easy implementation [3]. By integrating PSO to optimize the hidden-layer parameters of ELM, the hybrid ELMPSO model enhances prediction accuracy and robustness while maintaining high computational efficiency.

## **1.2 Object and Scope**

The experimental data used in this study contains hourly records covering the period from **December 2014** to **December 2018** . The dataset includes:

- Total electric load demand (MW),

- Electricity price,

- Temperature data from five Spanish major cities: **Barcelona, Bilbao, Madrid, Seville, and Valencia** ,

- Time-related information with hourly resolution.

This dataset reflects realistic short-term load characteristics, such as daily load cycles, strong nonlinearity, and sensitivity to weather conditions. Therefore, it is suitable for evaluating advanced short-term load forecasting models.

The scope of the study is limited to **short-term forecasting with an hourly time horizon** . The research concentrates on **system-level load forecasting** , without considering regional or individual customer-level demand. Input variables are restricted to historical load data, time-related features, and temperature variables provided in the dataset. Other factors, such as economic indicators, population growth, or long-term policy impacts, are not considered.

The study aims to evaluate the effectiveness of a hybrid **Extreme Learning Machine–Particle Swarm Optimization (ELM–PSO)** model in improving forecasting accuracy. The model performance is assessed through offline experiments using standard evaluation metrics, including **MAE, MAPE, and RMSE** , under controlled experimental conditions.

## **1.3 Methodology**

The research methodology adopted in this study follows a **data-driven modeling approach** and consists of several main stages, as illustrated below.

## **Data Preparation**

Historical load and temperature data are collected and examined for missing values and abnormal observations. Data cleaning techniques are applied to ensure consistency and reliability. All input variables are normalized using **Min–Max normalization** to improve numerical stability during model training.

## **Feature Selection**

Input features are selected based on their relevance to short-term load demand. These include:

- Previous load values to capture temporal dependency

- Hourly time information

- Temperature data from multiple locations to represent weather influence

## **Model Development**

A conventional Extreme Learning Machine (ELM) is first constructed as a baseline forecasting model. To overcome the randomness of hidden-layer parameters in ELM, **Particle Swarm Optimization (PSO)** is applied to optimize the input weights and biases of the network.

## **Model Training and Testing**

The dataset is divided into training and testing subsets. PSO is used during the training phase to minimize forecasting error on the training data. The optimized ELM–PSO model is then evaluated on the testing dataset to assess its generalization performance.

## **Performance Evaluation**

The forecasting results are evaluated using **MAE, MAPE, and RMSE** . A comparative analysis is conducted between the conventional ELM and the proposed ELM–PSO model to demonstrate the effectiveness of the hybrid approach.

The research methodology adopted in this study follows a **data-driven modeling approach** and consists of several main stages, as illustrated below.

## **Data Preparation**

Historical load and temperature data are collected and examined for missing values and abnormal observations. Data cleaning techniques are applied to ensure consistency and reliability. All input variables are normalized using **Min–Max normalization** to improve numerical stability during model training.

## **Feature Selection**

Input features are selected based on their relevance to short-term load demand. These include:

- Previous load values to capture temporal dependency

- Hourly time information

- Temperature data from multiple locations to represent weather influence

## **Model Development**

A conventional Extreme Learning Machine (ELM) was first constructed as a baseline forecasting model. To overcome the randomness of hidden-layer parameters in ELM, **Particle Swarm Optimization (PSO)** is applied to optimize the input weights and biases of the network.

## **Model Training and Testing**

The dataset is divided into training and testing subsets. PSO is used during the training phase to minimize forecasting errors on the training data. The optimized ELM–PSO model is then evaluated on the testing dataset to assess its generalization performance.

## **Performance Evaluation**

The forecasting results are evaluated using **MAE, MAPE, and RMSE** . A comparative analysis is conducted between the conventional ELM and the proposed ELM–PSO model to demonstrate the effectiveness of the hybrid approach.
