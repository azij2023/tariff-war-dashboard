import pandas as pd
from utils.data_loader import prepare_data

# Load data
df = prepare_data("data/funds_data.xlsx")

# Create resilience bucket (reuse logic)
df["Resilience_Bucket"] = pd.qcut(
    df["Resilience_Score"],
    q=2,
    labels=["Low_Resilience", "High_Resilience"]
)

# Create strategy segment
def assign_segment(row):
    if row["Tariff_Risk"] == "Low" and row["Resilience_Bucket"] == "High_Resilience":
        return "Core Defensive"
    elif row["Tariff_Risk"] == "Medium" and row["Resilience_Bucket"] == "High_Resilience":
        return "Balanced Growth"
    elif row["Tariff_Risk"] == "High" and row["Resilience_Bucket"] == "High_Resilience":
        return "Opportunistic Alpha"
    elif row["Tariff_Risk"] == "Low" and row["Resilience_Bucket"] == "Low_Resilience":
        return "Stable but Fragile"
    elif row["Tariff_Risk"] == "Medium" and row["Resilience_Bucket"] == "Low_Resilience":
        return "Cyclical Risk"
    else:
        return "High Risk – Avoid"

df["Strategy_Segment"] = df.apply(assign_segment, axis=1)

# Summary
segment_summary = df["Strategy_Segment"].value_counts()
print(segment_summary)

# Save for reporting
df.to_excel("outputs/fund_strategy_segments.xlsx", index=False)
# ----------------------------------------
# TASK 4 STEP 3: Fund Selection
# ----------------------------------------

# Load best-positioned funds
best_funds = pd.read_excel("outputs/best_positioned_funds.xlsx")

# Merge strategy segments
best_funds = best_funds.merge(
    df[["Fund_ID", "Strategy_Segment"]],
    on="Fund_ID",
    how="left"
)

# Filter investable segments
investable_segments = [
    "Core Defensive",
    "Balanced Growth",
    "Opportunistic Alpha"
]

portfolio_candidates = best_funds[
    best_funds["Strategy_Segment"].isin(investable_segments)
]

# Rank funds within each segment by return & resilience
portfolio_candidates["Selection_Score"] = (
    0.6 * portfolio_candidates["One_Year_Return"] +
    0.4 * portfolio_candidates["Resilience_Score"]
)

selected_funds = (
    portfolio_candidates
    .sort_values(
        ["Strategy_Segment", "Selection_Score"],
        ascending=[True, False]
    )
    .groupby("Strategy_Segment")
    .head(5)
)

print("\nSelected Portfolio Funds:")
print(
    selected_funds[
        [
            "Fund_Name",
            "Strategy_Segment",
            "Sector",
            "Region",
            "One_Year_Return",
            "Volatility",
            "Resilience_Score"
        ]
    ]
)

# Save final selection
selected_funds.to_excel("outputs/selected_portfolio_funds.xlsx", index=False)
