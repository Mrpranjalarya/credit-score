# 🔍 Wallet Score Analysis – DeFi Credit Scoring

## 📊 Score Distribution

The distribution below shows how predicted credit scores (0–1000) are spread across all wallets.

| Score Range | Number of Wallets | Description |
|-------------|--------------------|-------------|
| 0–100       | 85                 | Extremely risky or likely bots |
| 101–200     | 123                | High-risk, poor usage behavior |
| 201–300     | 298                | Below average repayment or behavior |
| 301–400     | 487                | Slightly poor usage, missed repayments |
| 401–500     | 812                | Average users, occasional issues |
| 501–600     | 1935               | Reliable, but not high volume |
| 601–700     | 2938               | Responsible usage, small amounts |
| 701–800     | 1083               | High-volume, well-behaved wallets |
| 801–900     | 614                | Excellent usage, consistent repayments |
| 901–1000    | 312                | Ideal DeFi citizens |

> *Note: Replace counts above with your real histogram after plotting.*

---

## 📈 Visualization (Python Snippet)

You can generate the actual plot using:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/wallet_scores_predicted.csv")

plt.figure(figsize=(10, 6))
plt.hist(df["predicted_score"], bins=10, range=(0, 1000), color='skyblue', edgecolor='black')
plt.title("Distribution of Wallet Credit Scores")
plt.xlabel("Credit Score")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.savefig("output/score_distribution.png")
plt.show()
