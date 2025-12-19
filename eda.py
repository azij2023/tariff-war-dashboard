import pandas as pd
import os

from utils.data_loader import prepare_data

# Load prepared data
df = prepare_data("data/funds_data.xlsx")

# Sector-level summary
sector_summary = (
    df.groupby("Sector")
    .agg(
        Avg_Tariff_Exposure=("Tariff_Exposure", "mean"),
        Avg_Resilience=("Resilience_Score", "mean"),
        Avg_1Y_Return=("One_Year_Return", "mean"),
        Avg_Volatility=("Volatility", "mean"),
        Fund_Count=("Fund_ID", "count")
    )
    .sort_values("Avg_Tariff_Exposure", ascending=False)
)

print(sector_summary)

os.makedirs("outputs", exist_ok=True)
sector_summary.to_excel("outputs/sector_level_summary.xlsx")

# -------------------------------
# EDA Step 2.1: Correlation Check
# -------------------------------

corr = df["Tariff_Exposure"].corr(df["One_Year_Return"])
print("\nCorrelation between Tariff Exposure and 1Y Return:")
print(round(corr, 3))
# ----------------------------------------
# EDA Step 2.2: Returns by Tariff Risk Tier
# ----------------------------------------

risk_return_summary = (
    df.groupby("Tariff_Risk")
    .agg(
        Avg_1Y_Return=("One_Year_Return", "mean"),
        Median_1Y_Return=("One_Year_Return", "median"),
        Avg_Volatility=("Volatility", "mean"),
        Fund_Count=("Fund_ID", "count")
    )
)

print("\nReturn & Risk Summary by Tariff Risk Level:")
print(risk_return_summary)
risk_return_summary.to_excel("outputs/return_by_tariff_risk.xlsx")
# ----------------------------------------
# EDA Step 3.1: Create Resilience Buckets
# ----------------------------------------

df["Resilience_Bucket"] = pd.qcut(
    df["Resilience_Score"],
    q=2,
    labels=["Low_Resilience", "High_Resilience"]
)
# ---------------------------------------------------
# EDA Step 3.2: Performance by Risk & Resilience
# ---------------------------------------------------

risk_resilience_summary = (
    df.groupby(["Tariff_Risk", "Resilience_Bucket"])
    .agg(
        Avg_1Y_Return=("One_Year_Return", "mean"),
        Avg_Volatility=("Volatility", "mean"),
        Fund_Count=("Fund_ID", "count")
    )
)

print("\nPerformance by Tariff Risk and Resilience Level:")
print(risk_resilience_summary)
risk_resilience_summary.to_excel(
    "outputs/performance_by_risk_and_resilience.xlsx"
)
# ----------------------------------------
# EDA Step 4.1: Geographic (Region) Summary
# ----------------------------------------

region_summary = (
    df.groupby("Region")
    .agg(
        Avg_Tariff_Exposure=("Tariff_Exposure", "mean"),
        Avg_Resilience=("Resilience_Score", "mean"),
        Avg_1Y_Return=("One_Year_Return", "mean"),
        Avg_Volatility=("Volatility", "mean"),
        Avg_Max_Drawdown=("Max_Drawdown", "mean"),
        Fund_Count=("Fund_ID", "count")
    )
    .sort_values("Avg_Tariff_Exposure", ascending=False)
)

print("\nRegion-Level Summary:")
print(region_summary)
region_summary.to_excel("outputs/region_level_summary.xlsx")
# -------------------------------------------------
# EDA Step 5.1: Risk-Adjusted Benchmarks by Risk
# -------------------------------------------------

risk_benchmarks = (
    df.groupby("Tariff_Risk")
    .agg(
        Avg_Return=("One_Year_Return", "mean"),
        Avg_Volatility=("Volatility", "mean")
    )
)

print("\nBenchmarks by Tariff Risk Level:")
print(risk_benchmarks)
# Merge benchmarks
df = df.merge(
    risk_benchmarks,
    left_on="Tariff_Risk",
    right_index=True,
    how="left"
)
# ----------------------------------------
# EDA Step 5.3: Identify Best-Positioned Funds
# ----------------------------------------

# High resilience flag
df["High_Resilience_Flag"] = df["Resilience_Score"] >= df["Resilience_Score"].median()

# Outperformance flags
df["Return_Outperformance"] = df["One_Year_Return"] > df["Avg_Return"]
df["Risk_Outperformance"] = df["Volatility"] < df["Avg_Volatility"]

# Final best-positioned flag
df["Best_Positioned_Fund"] = (
    df["High_Resilience_Flag"] &
    df["Return_Outperformance"] &
    df["Risk_Outperformance"]
)
best_funds = df[df["Best_Positioned_Fund"]].sort_values(
    ["Tariff_Risk", "One_Year_Return"],
    ascending=[True, False]
)

print("\nBest-Positioned Funds (Sample):")
print(
    best_funds[
        [
            "Fund_Name",
            "Tariff_Risk",
            "Sector",
            "Region",
            "One_Year_Return",
            "Volatility",
            "Resilience_Score"
        ]
    ].head(10)
)
best_funds.to_excel("outputs/best_positioned_funds.xlsx", index=False)
# ----------------------------------------
# EDA Step 6.1: Return Outliers (Z-score)
# ----------------------------------------

df["Return_Z"] = (
    (df["One_Year_Return"] - df["One_Year_Return"].mean()) /
    df["One_Year_Return"].std()
)

positive_outliers = df[df["Return_Z"] > 2]
negative_outliers = df[df["Return_Z"] < -2]

print("\nPositive Return Outliers:")
print(
    positive_outliers[
        [
            "Fund_Name",
            "Tariff_Risk",
            "Tariff_Exposure",
            "One_Year_Return",
            "Resilience_Score"
        ]
    ].head()
)

print("\nNegative Return Outliers:")
print(
    negative_outliers[
        [
            "Fund_Name",
            "Tariff_Risk",
            "Tariff_Exposure",
            "One_Year_Return",
            "Resilience_Score"
        ]
    ].head()
)
positive_outliers.to_excel("outputs/positive_return_outliers.xlsx", index=False)
negative_outliers.to_excel("outputs/negative_return_outliers.xlsx", index=False)
# -----------------------------
# Summary statistics by tariff risk
# -----------------------------

summary_stats = (
    df.groupby("Tariff_Risk")[[
        "One_Year_Return",
        "Volatility",
        "Tariff_Exposure",
        "Resilience_Score"
    ]]
    .agg(["mean", "median", "std"])
)

summary_stats.to_excel("outputs/summary_statistics.xlsx")
