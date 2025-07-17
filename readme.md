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
## 📁 Project Structure
 credit-scoring-ml/
│
├── data/
│   └── user_transactions.json             # Raw transaction data
│
├── output/
│   ├── wallet_features.csv                # Extracted wallet-level features
│   ├── wallet_features_labeled.csv        # Features with rule-based labels
│   ├── wallet_predicted_scores.csv        # Final output scores
│   └── score_distribution.png             # Score distribution plot
│
├── models/
│   └── credit_score_model.pkl             # Trained RandomForestRegressor model
│
├── extract_features.py                    # Feature extraction logic
├── generate_labels.py                     # Heuristic rule-based label generator
├── train_model.py                         # Training and saving the model
├── predict_scores.py                      # Scoring new wallet data
│
├── analysis.md                            # Analysis of scoring results
├── readme.md                              # Project overview and guide
├── requirements.txt                       # Python dependencies






---

## ⚙️ Workflow of the Project

1. **Data Collection**  
   Collect raw transaction data from DeFi wallets in `user_transactions.json`.

2. **Feature Extraction**  
   Run `extract_features.py` to process transaction data into structured features like:
   - Total borrowed
   - Total repaid
   - Deposit to borrow ratio
   - Number of liquidations, etc.

3. **Label Generation**  
   Run `generate_labels.py` to create rule-based credit score labels (0–1000) using heuristics:
   - High deposit-to-borrow ratio: higher score
   - Many liquidations or missed repayments: lower score

4. **Model Training**  
   Run `train_model.py` to train a `RandomForestRegressor` on the labeled features and save it to `models/credit_score_model.pkl`.

5. **Score Prediction**  
   Run `predict_scores.py` to generate credit scores for new/unlabeled wallets.

6. **Analysis**  
   - Save predictions to `wallet_predicted_scores.csv`.
   - Generate `score_distribution.png` to visualize distribution of scores.
   - Add insights into `analysis.md`.

---

## 📊 ML Model Details

- **Model**: `RandomForestRegressor` (from `sklearn`)
- **Target**: Predict scores between **0 and 1000**
- **Training Data**: Rule-labeled wallets using behavioral heuristics:
  - Repayment history
  - Deposit vs Borrow ratio
  - Number of Liquidations
- **Saved Model**: `models/credit_score_model.pkl`

---

## 🔁 Project Flowchart

```text
                 ┌────────────────────────────┐
                 │ user_transactions.json     │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ extract_features.py        │
                 │ → wallet_features.csv      │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ generate_labels.py         │
                 │ → wallet_features_labeled  │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ train_model.py             │
                 │ → credit_score_model.pkl   │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ predict_scores.py          │
                 │ → wallet_predicted_scores  │
                 └────────────┬───────────────┘
                              │
                              ▼
                 ┌────────────────────────────┐
                 │ analysis.md & distribution │
                 └────────────────────────────┘


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


## 🛠️ How to Run the Project

# 1. Install dependencies
pip install -r requirements.txt

# 2. Extract features
python extract_features.py

# 3. Generate labels
python generate_labels.py

# 4. Train the model
python train_model.py

# 5. Predict scores
python predict_scores.py


### 1. Clone the repository
```bash
git clone https://github.com/Mrpranjalarya/credit-score.git