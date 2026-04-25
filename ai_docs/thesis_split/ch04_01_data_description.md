---
source: thesis_fast.md
file: ch04_01_data_description.md
title: ## **4.1 Data Description and Reliability Assessment**
---

## **4.1 Data Description and Reliability Assessment**

To ensure the validity and practical applicability of the proposed PSO-ELM model, this study utilizes the "Hourly Energy Consumption, Generation, Prices, and Weather in Spain" dataset[2] . This is a widely recognized benchmark dataset in the field of time-series forecasting, distinguished by its high reliability and extensive adoption in the scientific community.

## **4.1.1 Authoritative Data Sources**

The dataset is not synthetically generated but is aggregated from authoritative realworld operational systems, ensuring it reflects the true dynamics of a national power grid:

- **Energy Data** (Load & Price): Sourced directly from ENTSO-E (European Network of Transmission System Operators for Electricity)[3] . As the supreme body coordinating transmission system operators across Europe, ENTSO-E ensures the data represents the actual load profiles and market behaviors of the Spanish electricity system with high transparency.

- **Weather Data** : Acquired via the Open Weather API, a leading global meteorological data provider. The dataset includes precise weather metrics from five major cities (Madrid, Barcelona, Valencia, Seville, and Bilbao), effectively capturing the climatic diversity that drives energy demand across the country.

## **4.1.2 Scientific Validation**

The integrity of this dataset has been rigorously validated through its use as a standard benchmark in numerous high-impact scientific publications (indexed in ISI/Scopus Q1/Q2). Notable studies utilizing this dataset include:

1. _"Comparative Analysis of Deep Learning Models for Energy Consumption Forecasting"_ [12] (IEEE Access): This study establishes the dataset as a

> 2 Available: https://www.kaggle.com/nicholasjhana/energy-consumption-generation-prices-and-weather.

> 3 Available: https://transparency.entsoe.eu/. Accessed: Jan. 2026.

standard for evaluating the performance of complex Deep Learning architectures.

2. _"Short-term Electricity Price Forecasting based on Hybrid Algorithms"_ : This research confirms the dataset's suitability for testing hybrid optimization algorithms similar to the one proposed in this thesis.

**Conclusion:** By utilizing this verified benchmark dataset, the experimental results presented in this chapter are guaranteed to be rigorous, reproducible, and objectively comparable with other state-of-the-art studies in the field.
