import pandas as pd

def load_data(file_path):
    df = pd.read_excel(file_path, sheet_name="Raw Data")

    df = df[
        [
            "Fund_ID",
            "Fund_Name",
            "Fund_Type",
            "Primary_Sector",
            "Geographic_Focus",
            "Fund_Net_Assets_USD_M",
            "Return_1Y_Pct",
            "Volatility_1Y_Pct",
            "Max_Drawdown_Pct",
            "Tariff_Risk_Score",
            "Trade_War_Resilience_Score"
        ]
    ]

    df.columns = [
        "Fund_ID",
        "Fund_Name",
        "Fund_Type",
        "Sector",
        "Region",
        "AUM",
        "One_Year_Return",
        "Volatility",
        "Max_Drawdown",
        "Tariff_Exposure",
        "Resilience_Score"
    ]

    return df


def create_tariff_risk(df):
    df["Tariff_Risk"] = pd.qcut(
        df["Tariff_Exposure"],
        q=3,
        labels=["Low", "Medium", "High"]
    )
    return df


def create_aum_bucket(df):
    df["AUM_Bucket"] = pd.qcut(
        df["AUM"],
        q=3,
        labels=["Small", "Medium", "Large"]
    )
    return df


def prepare_data(file_path):
    df = load_data(file_path)
    df = create_tariff_risk(df)
    df = create_aum_bucket(df)
    return df
