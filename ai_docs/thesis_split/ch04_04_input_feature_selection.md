---
source: thesis_fast.md
file: ch04_04_input_feature_selection.md
title: ## **4.4 Input Feature Selection**
---

## **4.4 Input Feature Selection**

The selection of input features plays a decisive role in the learning capability and accuracy of the neural network. Based on an analysis of factors influencing electrical load and the characteristics of time series data, this thesis has identified and constructed an input vector consisting of **13 features** (excluding the target variable), categorized into four main groups as follows:

## **4.4.1 Historical Load Features**

Electrical load data exhibits strong inertia and periodicity. To enable the model to capture these patterns, four critical lag variables were selected:

- **Lt-1:** The load at the immediately preceding hour. This is the most significant variable, representing the current state of the system and instantaneous fluctuation trends.

- **Lt-24 and Lt-48:** The load at the same hour on the previous day and the day before that. These variables help the neural network learn **daily seasonality** , i.e., the repetitive behavior of consumption every 24 hours.

- **Lt-168:** The load at the same hour in the previous week (1 week = 24 × 7 = 168 hours). This variable helps the model capture **weekly seasonality** , distinguishing the differences between working days and weekends.

## **4.4.2 Weather Features**

Temperature is the most significant exogenous factor affecting energy demand due to the usage of cooling (air conditioning) or heating devices. To enhance forecasting accuracy for the aggregated national load, input temperature data is selected from 5 cities representing 5 distinct climate zones of Spain. This diversity enables the model to capture varying consumption trends across the country:

- **Madrid (Central Region - Continental Climate):** Represents the central plateau with high thermal amplitude (cold winters, hot summers). As the capital and economic hub, its temperature fluctuations have the highest correlation with the system load.

- **Seville (Southern Region - Extreme Heat):** Represents the Andalusia region, known for the hottest summers in Europe. This is a critical predictor for **summer peak loads** due to intensive air conditioning usage.

- **Bilbao (Northern Region - Oceanic Climate):** Represents the Atlantic coast with mild, humid weather. It reflects the consumption behavior of the industrial North, which is less driven by summer cooling but sensitive to winter heating.

- **Barcelona & Valencia (Eastern Region - Coastal Mediterranean):** These cities represent a coastal climate with high humidity. As major industrial and tourism centers, they contribute to a stable and high baseload demand driven by the Heat Index.

**Conclusion:** Using a vector of temperatures from these 5 specific locations allows the ELM-PSO network to learn a **spatial weight matrix** , effectively balancing the impact of regional weather extremes on the total national energy demand.

𝑇𝑣𝑒𝑐𝑡𝑜𝑟 = [𝑇𝑀𝑎𝑑𝑟𝑖𝑑, 𝑇𝑆𝑒𝑣𝑖𝑙𝑙𝑒, 𝑇𝐵𝑖𝑙𝑏𝑎𝑜, 𝑇𝐵𝑎𝑟𝑐𝑒𝑙𝑜𝑛𝑎, 𝑇𝑉𝑎𝑙𝑒𝑛𝑐𝑖𝑎]

## **4.4.3 Time Features**

Temporal information dictates human activities and routines. However, instead of using standard integers (0-23 hours), this thesis applies **Cyclical Encoding** techniques to help the neural network understand the true cyclical nature of time:

- **hour_sin:** Transforms the hour of the day using a sine function. This helps the model understand that 23:00 and 00:00 are temporally very close (their sine values are close), a relationship that the integers 0 and 23 fail to represent.

- **day_of_week_sin:** Transforms the day of the week using trigonometric functions to preserve the cyclical transition from Sunday to Monday.

- **is_holiday:** A binary variable (0 or 1) to mark special holidays. On these days, the load typically drops significantly and follows a completely different profile from regular days.

## **4.4.4 Economic Features**

- **price (Electricity Price):** In a competitive electricity market, price impacts consumer behavior (demand tends to decrease when prices are high and vice versa). Including the price variable helps the model reflect the actual supply-demand relationship.

## **Summary:**

The input vector at time t for the neural network is defined as:

$$
X_t = [L_{t-1}, L_{t-24}, L_{t-48}, L_{t-168}, T_{Bar}, T_{Bil}, T_{Mad}, T_{Sev}, T_{Val}, Price_t, \\
Hour_{sin}, Day_{sin}, Holiday]
$$

Output vector (Target) is the load at the forecasted time: 𝑌𝑡 = 𝐿𝑡.

For performance evaluation, the dataset was partitioned into a training set containing 80% of the samples and a testing set containing the remaining 20%.

The table below presents the normalized data corresponding to the first 20 hours of the study period.

| load   | is_holiday | price   | temp_Barcelona | temp_Bilbao | temp_Madrid | temp_Seville | temp_Valencia | hour_sin | day_of_week_sin | load_lag_1h | load_lag_24 | load_lag_48 | load_lag_168 |
|--------|------------|---------|----------------|-------------|--------------|---------------|----------------|----------|------------------|-------------|-------------|-------------|--------------|
| 0.13023 | 0 | 0.42477 | 0.50448 | 0.20056 | 0.09683 | 0.14132 | 0.45415 | 0.50000 | 0.09903 | 0.19235 | 0.23783 | 0.33555 | 0.24284 |
| 0.08427 | 0 | 0.40970 | 0.53763 | 0.18072 | 0.09683 | 0.14132 | 0.44470 | 0.62941 | 0.09903 | 0.13023 | 0.19796 | 0.29246 | 0.19870 |
| 0.05868 | 0 | 0.40281 | 0.51052 | 0.17576 | 0.09066 | 0.12750 | 0.28628 | 0.75000 | 0.09903 | 0.08427 | 0.18003 | 0.26756 | 0.18064 |
| 0.04723 | 0 | 0.37071 | 0.54807 | 0.22753 | 0.08450 | 0.11367 | 0.45651 | 0.85355 | 0.09903 | 0.05868 | 0.17341 | 0.25242 | 0.16923 |
| 0.05040 | 0 | 0.35954 | 0.51468 | 0.20366 | 0.08100 | 0.11542 | 0.26384 | 0.93301 | 0.09903 | 0.04723 | 0.19087 | 0.26069 | 0.18081 |

_Table 4.2 Normalized data corresponding to the first 20 hours_
