# Credit Scoring System (Aave V2)

## 📌 Overview

This project builds a credit scoring pipeline for wallets interacting with the Aave V2 protocol.  
Each wallet is scored between **0 and 1000** based on its transaction behavior using machine learning.

The pipeline:
- Parses raw DeFi transactions from Aave V2
- Extracts behavior-based features
- Trains an ML model on labeled credit scores
- Predicts scores for new wallets in a one-step automated script

---

## 💡 Features Engineered

Each wallet is summarized with the following features:

| Feature | Description |
|--------|-------------|
| `deposit_amt` | Total amount deposited |
| `borrow_amt` | Total amount borrowed |
| `repay_amt` | Total repaid |
| `borrow_count` | Number of borrow actions |
| `repay_count` | Number of repay actions |
| `liquidation_count` | Number of liquidation calls (penalty) |
| `repay_to_borrow_ratio` | How much they repaid compared to what they borrowed |
| `deposit_to_borrow_ratio` | Sign of financial responsibility |

---

## 🧠 Model

- **Algorithm:** RandomForestRegressor (sklearn)
- **Target:** Score between 0 and 1000
- **Trained on:** Rule-labeled wallets based on heuristics (repayment, deposit vs borrow, liquidations)
- **Saved Model:** `models/credit_score_model.pkl`

---

## 🛠️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Mrpranjalarya/credit-score.git