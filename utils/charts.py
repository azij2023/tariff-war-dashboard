import plotly.express as px

def tariff_risk_distribution(df):
    fig = px.histogram(
        df,
        x="Sector",
        color="Tariff_Risk",
        barmode="stack",
        title="Distribution of Tariff Risk Levels Across Sectors"
    )

    fig.update_layout(
        xaxis_title="Sector",
        yaxis_title="Number of Funds",
        legend_title="Tariff Risk Level"
    )

    return fig
def avg_return_by_tariff_risk(df):
    fig = px.bar(
        df,
        x="Tariff_Risk",
        y="One_Year_Return",
        color="Sector",
        barmode="group",
        title="Average 1-Year Returns by Tariff Risk and Sector"
    )

    fig.update_layout(
        xaxis_title="Tariff Risk Level",
        yaxis_title="Average 1-Year Return (%)",
        legend_title="Sector"
    )

    return fig
def aum_vs_tariff_exposure(df):
    fig = px.scatter(
        df,
        x="AUM",
        y="Tariff_Exposure",
        color="Tariff_Risk",
        size="Resilience_Score",
        hover_data=["Fund_Name", "Sector", "Region"],
        title="Fund AUM vs Tariff Exposure"
    )

    fig.update_layout(
        xaxis_title="Assets Under Management (USD Million)",
        yaxis_title="Tariff Exposure Score",
        legend_title="Tariff Risk Level"
    )

    return fig
def resilience_vs_tariff_risk(df):
    fig = px.box(
        df,
        x="Tariff_Risk",
        y="Resilience_Score",
        color="Tariff_Risk",
        points="all",
        title="Resilience Score Distribution Across Tariff Risk Levels"
    )

    fig.update_layout(
        xaxis_title="Tariff Risk Level",
        yaxis_title="Trade War Resilience Score",
        showlegend=False
    )

    return fig
def volatility_by_sector(df):
    fig = px.box(
        df,
        x="Sector",
        y="Volatility",
        title="Volatility Distribution by Sector",
        points="outliers"
    )

    fig.update_layout(
        xaxis_title="Sector",
        yaxis_title="Volatility (%)"
    )

    return fig


def drawdown_by_sector(df):
    fig = px.box(
        df,
        x="Sector",
        y="Max_Drawdown",
        title="Maximum Drawdown Distribution by Sector",
        points="outliers"
    )

    fig.update_layout(
        xaxis_title="Sector",
        yaxis_title="Max Drawdown (%)"
    )

    return fig
