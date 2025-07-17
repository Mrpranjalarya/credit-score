# extract_features.py
import json
import pandas as pd
from collections import defaultdict

def extract_features(txns_by_wallet):
    results = []

    for wallet, txns in txns_by_wallet.items():
        deposit_amt = borrow_amt = repay_amt = 0
        borrow_count = repay_count = liquidation_count = 0

        for tx in txns:
            action = tx['action'].lower()
            amount = float(tx.get('amount', 0) or 0)  # Default to 0 if missing or null

            if action == 'deposit':
                deposit_amt += amount
            elif action == 'borrow':
                borrow_amt += amount
                borrow_count += 1
            elif action == 'repay':
                repay_amt += amount
                repay_count += 1
            elif action == 'liquidationcall':
                liquidation_count += 1

        repay_to_borrow = repay_amt / borrow_amt if borrow_amt > 0 else 0
        deposit_to_borrow = deposit_amt / borrow_amt if borrow_amt > 0 else 0

        results.append({
            "wallet": wallet,
            "deposit_amt": deposit_amt,
            "borrow_amt": borrow_amt,
            "repay_amt": repay_amt,
            "borrow_count": borrow_count,
            "repay_count": repay_count,
            "liquidation_count": liquidation_count,
            "repay_to_borrow_ratio": repay_to_borrow,
            "deposit_to_borrow_ratio": deposit_to_borrow
        })

    return pd.DataFrame(results)

if __name__ == "__main__":
    with open("data/user_transactions.json", "r") as f:
        raw_txns = json.load(f)

    # Step 1: Group transactions by wallet address
    txns_by_wallet = defaultdict(list)
    for tx in raw_txns:
        wallet = tx.get("userWallet")
        if wallet:
            # Flatten amount if inside actionData
            if 'actionData' in tx and 'amount' in tx['actionData']:
                tx['amount'] = tx['actionData']['amount']
            txns_by_wallet[wallet].append(tx)

    # Step 2: Extract features
    df = extract_features(txns_by_wallet)

    # Step 3: Save to output
    df.to_csv("output/wallet_features.csv", index=False)
    print("✅ Saved to output/wallet_features.csv")
