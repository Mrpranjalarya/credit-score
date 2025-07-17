# predict_scores.py

import pandas as pd
import joblib
import os

MODEL_PATH = "models/credit_score_model.pkl"
FEATURE_PATH = "output/wallet_features.csv"
OUTPUT_PATH = "output/wallet_scores_predicted.csv"

# Load trained model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Trained model not found. Run train_model.py first.")

model = joblib.load(MODEL_PATH)

# Load wallet features (without labels)
df = pd.read_csv(FEATURE_PATH)

X = df.drop(columns=["wallet"])  # Features only
wallets = df["wallet"]

# Predict scores
predicted_scores = model.predict(X)

# Combine with wallet addresses
output_df = pd.DataFrame({
    "wallet": wallets,
    "predicted_score": predicted_scores.round(2)
})

# Save result
output_df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Predicted scores saved to: {OUTPUT_PATH}")
