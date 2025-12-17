import streamlit as st

def apply_filters(df):
    st.sidebar.header("Filter Funds")

    tariff_risk = st.sidebar.multiselect(
        "Tariff Risk Level",
        options=sorted(df["Tariff_Risk"].unique()),
        default=sorted(df["Tariff_Risk"].unique())
    )

    sector = st.sidebar.multiselect(
        "Primary Sector",
        options=sorted(df["Sector"].unique()),
        default=sorted(df["Sector"].unique())
    )

    region = st.sidebar.multiselect(
        "Geographic Region",
        options=sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique())
    )

    fund_type = st.sidebar.multiselect(
        "Fund Type",
        options=sorted(df["Fund_Type"].unique()),
        default=sorted(df["Fund_Type"].unique())
    )

    aum_bucket = st.sidebar.multiselect(
        "AUM Size Bucket",
        options=sorted(df["AUM_Bucket"].unique()),
        default=sorted(df["AUM_Bucket"].unique())
    )

    filtered_df = df[
        (df["Tariff_Risk"].isin(tariff_risk)) &
        (df["Sector"].isin(sector)) &
        (df["Region"].isin(region)) &
        (df["Fund_Type"].isin(fund_type)) &
        (df["AUM_Bucket"].isin(aum_bucket))
    ]

    return filtered_df
