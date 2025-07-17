# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# Load labeled features
df = pd.read_csv("output/wallet_features_labeled.csv")

# Features & Target
X = df.drop(columns=["wallet", "score"])
y = df["score"]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"✅ Model trained successfully!")
print(f"📊 MAE: {mae:.2f}")
print(f"📈 R² Score: {r2:.2f}")

# Save the model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/credit_score_model.pkl")
print("💾 Model saved to models/credit_score_model.pkl")
