---
source: thesis_fast.md
file: ch05_03_comparison.md
title: ## **5.3 Comparative Evaluation between Standard ELM and PSO–ELM**
---

## **5.3 Comparative Evaluation between Standard ELM and PSO–ELM**

To comprehensively evaluate the **accuracy and stability** of the proposed hybrid model, both the conventional ELM and the PSO–ELM models were executed **20 independent times** under identical experimental conditions. The Mean Absolute Percentage Error (MAPE) obtained in each run is reported in table 5.1.

_Table 5.1 Comparison of MAPE Results between Standard ELM and PSO-ELM across 20 Independent Runs_

|**Run**|**Standard ELM (%MAPE)**|**PSO-ELM (%MAPE)**|
|---|---|---|
|**1**|2.1723%|2.0000%|
|**2**|2.2765%|1.9800%|
|**3**|2.2014%|2.0100%|
|**4**|2.1256%|2.0500%|
|**5**|2.1805%|2.0349%|
|**6**|2.1808%|2.0159%|
|**7**|2.1727%|2.0394%|
|**8**|2.2662%|2.0657%|
|**9**|2.1742%|2.0130%|
|**10**|2.1427%|2.0130%|
|**11**|2.1484%|2.0674%|
|**12**|2.1193%|2.0430%|
|**13**|2.1439%|2.0059%|
|**14**|2.1563%|2.0363%|
|**15**|2.1959%|2.0061%|
|**16**|2.3058%|2.0060%|
|**17**|2.1565%|2.0273%|
|**18**|2.2628%|1.9626%|

|**19**|2.1554%|1.9683%|
|---|---|---|
|**20**|2.1675%|2.0031%|

The results clearly show that the PSO–ELM model consistently achieves lower MAPE values than the Standard ELM in all experimental runs. This demonstrates that optimizing the hidden-layer parameters of ELM using PSO effectively reduces forecasting error and improves model reliability.

To further quantify the performance improvement, a statistical summary of the experimental results is presented in Table 5.2.

_Table 5.2 Statistical performance evaluation and stability comparison_

|**Method**|**Best (Min**<br>**MAPE)**|**Worst**<br>**(Max**<br>**MAPE)**|**Average**<br>**(Mean**<br>**MAPE)**|**Std Dev**<br>**(Stability)**|**Range**<br>**(Max -**<br>**Min)**|
|---|---|---|---|---|---|
|**Standard**<br>**ELM**|2.1193%|2.3058%|2.1852%|0.0510%|0.1865%|
|**PSO-**<br>**ELM**|1.9626%|2.0674%|2.0174%|0.0279%|0.1048%|

Several important observations can be made:

- **Accuracy:** PSO-ELM outperforms Standard ELM in every single run. Even the worst case of PSO-ELM (2.0674%) is better than the best case of Standard ELM (2.1193%).

- **Stability:** The Standard Deviation of PSO-ELM (0.0279%) is nearly half that of Standard ELM (0.0510%), proving that the hybrid model is much more reliable and consistent.

- **Reliability** : The narrower MAPE range of PSO–ELM confirms that the hybrid model effectively mitigates the randomness issue inherent in conventional ELM.

These results clearly demonstrate that integrating PSO into the ELM framework leads to substantial improvements in both forecasting accuracy and stability.
