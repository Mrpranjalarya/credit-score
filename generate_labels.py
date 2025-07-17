# generate_labels.py
import pandas as pd

def score_wallet(row):
    score = 500  # baseline score

    # Reward higher deposits
    if row['deposit_amt'] > 10000:
        score += 200
    elif row['deposit_amt'] > 5000:
        score += 100

    # Reward paying back borrowed amounts
    if row['repay_to_borrow_ratio'] >= 1.0:
        score += 200
    elif row['repay_to_borrow_ratio'] >= 0.5:
        score += 100

    # Penalize high borrow with low deposits
    if row['deposit_to_borrow_ratio'] < 0.5:
        score -= 100

    # Penalize being liquidated
    if row['liquidation_count'] > 0:
        score -= 200

    # Clamp between 0–1000
    return max(0, min(1000, score))

if __name__ == "__main__":
    df = pd.read_csv("output/wallet_features.csv")

    df["score"] = df.apply(score_wallet, axis=1)

    df.to_csv("output/wallet_features_labeled.csv", index=False)
    print("✅ Saved labeled features to output/wallet_features_labeled.csv")
