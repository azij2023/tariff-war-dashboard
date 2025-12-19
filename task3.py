import pandas as pd
import numpy as np
import statsmodels.api as sm
from utils.data_loader import prepare_data

# Load data
df = prepare_data("data/funds_data.xlsx")

# Encode Tariff Risk
tariff_risk_map = {"Low": 0, "Medium": 1, "High": 2}
df["Tariff_Risk_Encoded"] = df["Tariff_Risk"].map(tariff_risk_map)

# Log AUM
df["Log_AUM"] = np.log(df["AUM"])

# Independent variables
X = df[
    [
        "Tariff_Exposure",
        "Resilience_Score",
        "Log_AUM",
        "Tariff_Risk_Encoded"
    ]
]

X = sm.add_constant(X)

# -----------------------------
# Model 1: Drivers of Returns
# -----------------------------
y_return = df["One_Year_Return"]
model_returns = sm.OLS(y_return, X).fit()

print("\nMODEL 1: Drivers of Returns")
print(model_returns.summary())

# -----------------------------
# Model 2: Drivers of Volatility
# -----------------------------
y_vol = df["Volatility"]
model_risk = sm.OLS(y_vol, X).fit()

print("\nMODEL 2: Drivers of Volatility")
print(model_risk.summary())

# Save results
with open("outputs/regression_results.txt", "w") as f:
    f.write("MODEL 1: RETURNS\n")
    f.write(model_returns.summary().as_text())
    f.write("\n\nMODEL 2: VOLATILITY\n")
    f.write(model_risk.summary().as_text())
