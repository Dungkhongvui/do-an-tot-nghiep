---
source: thesis_fast.md
file: ch04_03_data_analysis.md
title: ## **4.3 Data Analysis**
---

## **4.3 Data Analysis**

Before training the forecasting models, an exploratory data analysis (EDA) was conducted to examine the statistical characteristics and relationships among the input variables. This step aims to ensure data reliability and to provide insights into the dependency between electric load and influencing factors.

## **Correlation Analysis**

```mermaid
flowchart TB
    linkStyle default stroke:transparent,fill:none

    subgraph HEAD["Correlation Matrix"]
        direction LR
        h0[" "]:::label --- h1["load"]:::label --- h2["price"]:::label --- h3["temp_Barcelona"]:::label --- h4["temp_Bilbao"]:::label --- h5["temp_Madrid"]:::label --- h6["temp_Seville"]:::label --- h7["temp_Valencia"]:::label
    end

    subgraph R1["load"]
        direction LR
        r11["1.00"]:::diag --- r12["0.44"]:::mid --- r13["0.17"]:::low --- r14["0.20"]:::low --- r15["0.19"]:::low --- r16["0.20"]:::low --- r17["0.22"]:::low
    end

    subgraph R2["price"]
        direction LR
        r21["0.44"]:::mid --- r22["1.00"]:::diag --- r23["0.09"]:::vlow --- r24["0.07"]:::vlow --- r25["0.09"]:::vlow --- r26["0.05"]:::vlow --- r27["0.09"]:::vlow
    end

    subgraph R3["temp_Barcelona"]
        direction LR
        r31["0.17"]:::low --- r32["0.09"]:::vlow --- r33["1.00"]:::diag --- r34["0.87"]:::high --- r35["0.90"]:::high --- r36["0.84"]:::high --- r37["0.92"]:::high
    end

    subgraph R4["temp_Bilbao"]
        direction LR
        r41["0.20"]:::low --- r42["0.07"]:::vlow --- r43["0.87"]:::high --- r44["1.00"]:::diag --- r45["0.87"]:::high --- r46["0.82"]:::high --- r47["0.85"]:::high
    end

    subgraph R5["temp_Madrid"]
        direction LR
        r51["0.19"]:::low --- r52["0.09"]:::vlow --- r53["0.90"]:::high --- r54["0.87"]:::high --- r55["1.00"]:::diag --- r56["0.91"]:::high --- r57["0.91"]:::high
    end

    subgraph R6["temp_Seville"]
        direction LR
        r61["0.20"]:::low --- r62["0.05"]:::vlow --- r63["0.84"]:::high --- r64["0.82"]:::high --- r65["0.91"]:::high --- r66["1.00"]:::diag --- r67["0.86"]:::high
    end

    subgraph R7["temp_Valencia"]
        direction LR
        r71["0.22"]:::low --- r72["0.09"]:::vlow --- r73["0.92"]:::high --- r74["0.85"]:::high --- r75["0.91"]:::high --- r76["0.86"]:::high --- r77["1.00"]:::diag
    end

    h0 --- r11
    r11 --- r21 --- r31 --- r41 --- r51 --- r61 --- r71

    classDef label fill:#ffffff,stroke:#ffffff,color:#111,font-size:11px;
    classDef diag fill:#b11226,stroke:#ffffff,color:#ffffff;
    classDef high fill:#de7c5a,stroke:#ffffff,color:#ffffff;
    classDef mid fill:#b7c9e8,stroke:#ffffff,color:#111111;
    classDef low fill:#6f8fe8,stroke:#ffffff,color:#ffffff;
    classDef vlow fill:#3f57c6,stroke:#ffffff,color:#ffffff;
```

_Figure 4.1 Correlation Matrix of Load, Electricity Price, and Temperatures_

As shown in Figure 4.1, the electric load exhibits a clear correlation with temperature variables, confirming the strong influence of weather conditions on electricity consumption. Temperature data from different cities show high mutual correlation, indicating similar climatic patterns across regions. In contrast, the electricity price demonstrates weaker correlation with load demand, suggesting that price plays a secondary role in short-term load variation compared to meteorological factors.

These observations justify the selection of **temperature and historical load data** as key input features for the forecasting model.

## **Distribution Analysis of Load and Price**

To further examine the statistical distribution of the main variables, Figure 4.2 illustrates the **histograms and boxplots of electric load and electricity price** .

The load distribution shows a relatively concentrated range with moderate skewness, reflecting stable consumption behavior with occasional peak demand periods. The boxplot indicates that extreme outliers have been effectively handled during the data cleaning process.

In contrast, electricity price exhibits a wider distribution and higher variability, with several extreme values. This volatility further supports the decision to treat electricity price as a supplementary variable rather than a primary driver in shortterm load forecasting.

## **Comparison of Temperature Distributions Across Cities**

Figure 4.3 compares the **temperature distributions of different cities** included in the dataset.

The figure shows that temperature ranges across cities are consistent and realistic, covering both seasonal cold and hot extremes. Despite minor regional differences, the overall distribution patterns are similar, indicating that the temperature data are reliable and representative of actual climatic conditions.

This consistency ensures that temperature variables can be effectively used as explanatory inputs without introducing bias due to abnormal or unrealistic measurements.

## **Data Verification and Quality Assessment**

After data cleaning and exploration analysis, the dataset was re-verified to ensure its suitability for model training. The verification results are summarized in Error! R eference source not found..

|**Verification**<br>**Criteria**|**Statistical**<br>**Indicator**|**Actual Result**|**Evaluation**|
|---|---|---|---|
|**Data Size**|Total<br>Samples<br>(Rows)|35,064 samples|Sufficient for Deep<br>Learning|
|**Integrity**|Missing Values<br>(NaN)|0|Pass (100% Clean)|
||Duplicate Rows|0|Pass|
|**Continuity**|Time Period|01/01/2015<br>-<br>31/12/2018|4 continuous years|
||Resolution|1 hour (Hourly)|Stable|
|**Value Range**|Load|18,041<br>MW<br>-<br>41,015 MW|Reasonable|
||Price|9.33 EUR - 116.80<br>EUR|Reasonable|
||Temperature|Min:<br>-10.91°C;<br>Max: 42.45°C|Consistent<br>with<br>actual climate|

_Table 4.1 Summary of Input Data Verification Results_

The verification results indicate that the dataset contains **35,064 hourly samples** , corresponding exactly to four continuous years from **January 1, 2015 to**

**December 31, 2018** . No missing values or duplicate records are detected, confirming complete data integrity.

Furthermore, all variables fall within reasonable physical ranges. The electric load varies from **18,041 MW to 41,015 MW** , while temperature values range from **– 10.91°C to 42.45°C** , which are consistent with real-world operating and climatic conditions. These results demonstrate that outliers and unrealistic values have been effectively addressed during preprocessing.

Overall, the dataset satisfies the requirements for short-term load forecasting and provides a reliable foundation for training and evaluating the proposed ELM–PSO model.
