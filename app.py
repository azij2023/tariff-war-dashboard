import streamlit as st
from utils.data_loader import prepare_data
from utils.filters import apply_filters
from utils.charts import tariff_risk_distribution
from utils.charts import avg_return_by_tariff_risk
from utils.charts import aum_vs_tariff_exposure
from utils.charts import resilience_vs_tariff_risk
from utils.charts import volatility_by_sector, drawdown_by_sector


st.set_page_config(
    page_title="Tariff Risk & Fund Dashboard",
    layout="wide"
)

st.title("Trade Uncertainty & Fund Performance Dashboard")

# Load and prepare data
df = prepare_data("data/funds_data.xlsx")

# Apply sidebar filters
filtered_df = apply_filters(df)

# Main page content
st.subheader("Filtered Fund Data")
st.write(f"Number of funds selected: {filtered_df.shape[0]}")

st.dataframe(filtered_df.head(20))
st.subheader("Tariff Risk Distribution by Sector")
fig1 = tariff_risk_distribution(filtered_df)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Average 1-Year Returns by Tariff Risk and Sector")
fig2 = avg_return_by_tariff_risk(filtered_df)
st.plotly_chart(fig2, use_container_width=True)
st.subheader("AUM vs Tariff Exposure")
fig3 = aum_vs_tariff_exposure(filtered_df)
st.plotly_chart(fig3, use_container_width=True)
st.subheader("Resilience Score vs Tariff Risk")
fig4 = resilience_vs_tariff_risk(filtered_df)
st.plotly_chart(fig4, use_container_width=True)
st.subheader("Risk Profile by Sector")

fig5 = volatility_by_sector(filtered_df)
st.plotly_chart(fig5, use_container_width=True)

fig6 = drawdown_by_sector(filtered_df)
st.plotly_chart(fig6, use_container_width=True)
