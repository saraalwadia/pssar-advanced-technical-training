# Applied Statistics & Data Visualization Project

This project analyzes chess game data using statistical methods, hypothesis testing, confidence intervals, and data visualization techniques. The goal is to extract meaningful insights about game duration, player ratings, and game outcomes.

---

## AQ1: Descriptive Statistics

Game duration (turns) shows a wide distribution with high variability and a strong right skew. Most games last between 40 and 70 moves, with a smaller number of very long games. Rating difference is centered around zero, indicating balanced matchmaking between players.

---

## AQ2: Distribution Analysis

The distribution of game turns is highly right-skewed and non-normal (Shapiro p < 0.001). This is due to the presence of a small number of very long games. After applying a log transformation, the distribution becomes more symmetric and closer to normal. Skewness is significantly reduced, making the data more suitable for statistical analysis.

---

## AQ3: Correlation Analysis

The correlation matrix shows a moderate positive relationship between white_rating and black_rating, indicating that players are generally matched with opponents of similar skill level. However, game length (turns) shows very weak correlation with rating variables, suggesting that player strength does not strongly influence game duration in a linear way.

A key confounding factor is the opening strategy, which may influence both game duration and perceived player strength, potentially masking true relationships between variables.

---

## AQ4: Chi-Squared Test

There is a statistically significant association between rating group and White win rate (χ² test, p < 0.001). However, the effect size is small (Cramér’s V ≈ 0.11), indicating that the relationship is weak in practical terms. This shows that statistical significance does not necessarily imply a strong real-world effect.

---

## AQ5: Confidence Intervals

Rated games last significantly longer than unrated games. The 95% confidence intervals for both groups do not overlap, confirming a clear difference in mean game duration. Both parametric and bootstrap methods produce consistent results, confirming robustness.

---

## Overall Conclusion

The analysis shows that while player ratings and game outcomes have statistically significant relationships, their practical impact is often weak. Game duration is influenced more by structural and strategic factors rather than rating alone. This highlights the importance of combining statistical significance with effect size and confidence intervals for proper interpretation.

---

## Files

- Notebooks: `/notebooks/assignment.ipynb`
- Visualizations: `/images/plots/`
- Dataset: `/data/`