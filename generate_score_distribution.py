import pandas as pd
import matplotlib.pyplot as plt

# Load the predicted scores
df = pd.read_csv("output/wallet_scores_predicted.csv")

# Plot histogram with 10 bins (0–100, 100–200, ..., 900–1000)
plt.figure(figsize=(10, 6))
plt.hist(df["predicted_score"], bins=[0,100,200,300,400,500,600,700,800,900,1000],
         color='skyblue', edgecolor='black')

# Add labels and title
plt.title("Wallet Credit Score Distribution", fontsize=14)
plt.xlabel("Credit Score Range", fontsize=12)
plt.ylabel("Number of Wallets", fontsize=12)
plt.xticks(range(0, 1100, 100))
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig("output/score_distribution.png")

# Show the plot
plt.show()
