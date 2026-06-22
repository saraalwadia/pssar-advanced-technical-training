# Visual Research Report — Key Findings

This report presents key insights derived from exploratory data analysis of three datasets: Chess Games, Netflix Titles, and Global Temperature (GISTEMP). The findings are supported by visualizations created using Matplotlib and Seaborn.

---

## Finding 1 — Chess Game Outcomes

White has a consistent but small advantage in win rate compared to Black, as shown in the AQ1 bar chart. Draw games, although less frequent, last significantly longer than games ending in resignation or checkmate. This indicates that balanced positions lead to extended gameplay.

Game duration is not strongly correlated with player rating, as shown in the scatter plot (AQ2-style analysis), suggesting that strategy and game dynamics matter more than skill level in determining game length.

---

## Finding 2 — Netflix Content Growth

The histogram analysis shows that most Netflix movies fall between 80–120 minutes, indicating standardization in production length.

The stacked bar chart (2013–2021) reveals a strong increase in content addition after 2015, aligning with Netflix’s expansion into original content. A noticeable slowdown is observed around 2020–2021, likely due to COVID-19 disruptions.

Country analysis shows that the United States leads content production, followed by India and the United Kingdom, highlighting global distribution patterns in streaming content.

---

## Finding 3 — Global Temperature Trend

The GISTEMP time-series (AQ3) clearly shows a long-term warming trend. The 10-year rolling average confirms that temperature anomalies have steadily increased since 1950.

The hottest recorded years occur in the most recent decade, indicating accelerating climate change.

---

## Finding 4 — Seasonal vs Systemic Warming

The heatmap (AQ5) shows temperature anomalies across months and decades. All months exhibit consistent warming in recent decades, confirming that global warming is not seasonal but systemic across the entire year.

---

## Finding 5 — Overall Insight

Across all datasets, a consistent pattern emerges: long-term trends are only visible when data is aggregated and visualized correctly. Rolling averages, pivot tables, and grouped charts are essential tools for revealing hidden structure in data.

---

## Conclusion

Exploratory Data Analysis shows that:
- Chess outcomes show structural advantages but weak predictive relationships.
- Netflix content expanded rapidly after 2015 with clear global production patterns.
- Global temperatures show a clear and accelerating warming trend across all time periods.

These findings demonstrate the importance of visualization in transforming raw data into meaningful insights.