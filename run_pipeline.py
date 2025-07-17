# run_pipeline.py

import os
import json
import pandas as pd
import joblib
from collections import defaultdict

# ====== CONFIG ======
JSON_PATH = "data/user_transactions.json"
MODEL_PATH = "models/credit_score_model.pkl"
OUTPUT_PATH = "output/wallet_scores_predicted.csv"
# =====================

# ---------- STEP 1: Load Transactions ----------
with open(JSON_PATH, "r") as f:
    data = json.load(f)

wallet_stats = defaultdict(lambda: {
    "deposit_amt": 0,
    "borrow_amt": 0,
    "repay_amt": 0,
    "borrow_count": 0,
    "repay_count": 0,
    "liquidation_count": 0,
})

# ---------- STEP 2: Feature Extraction ----------
for tx in data:
    wallet = tx.get("userWallet")
    action = tx.get("action")
    value = 0

    try:
        value = float(tx.get("actionData", {}).get("amount", 0))
    except:
        pass

    if action == "deposit":
        wallet_stats[wallet]["deposit_amt"] += value
    elif action == "borrow":
        wallet_stats[wallet]["borrow_amt"] += value
        wallet_stats[wallet]["borrow_count"] += 1
    elif action == "repay":
        wallet_stats[wallet]["repay_amt"] += value
        wallet_stats[wallet]["repay_count"] += 1
    elif action == "liquidationcall":
        wallet_stats[wallet]["liquidation_count"] += 1

# Convert to DataFrame
features = []
for wallet, stats in wallet_stats.items():
    borrow_amt = stats["borrow_amt"]
    repay_amt = stats["repay_amt"]
    deposit_amt = stats["deposit_amt"]

    stats["repay_to_borrow_ratio"] = (repay_amt / borrow_amt) if borrow_amt > 0 else 0
    stats["deposit_to_borrow_ratio"] = (deposit_amt / borrow_amt) if borrow_amt > 0 else 0
    stats["wallet"] = wallet
    features.append(stats)

df = pd.DataFrame(features)

# Save intermediate features (optional)
df.to_csv("output/wallet_features.csv", index=False)

# ---------- STEP 3: Load Model and Predict ----------
model = joblib.load(MODEL_PATH)
X = df.drop(columns=["wallet"])
df["predicted_score"] = model.predict(X).round(2)

# ---------- STEP 4: Save Final Output ----------
df[["wallet", "predicted_score"]].to_csv(OUTPUT_PATH, index=False)
print(f"✅ All scores saved to: {OUTPUT_PATH}")
