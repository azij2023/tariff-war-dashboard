🌍 Tariff Wars: Resilient Equity Fund Strategy
📌 Project Overview

Global trade tensions, tariffs, and supply-chain disruptions have introduced structural uncertainty into equity markets. Traditional diversification alone is no longer sufficient to manage these risks.

This project develops a data-driven, resilience-focused equity investment strategy that helps investors navigate tariff wars by identifying vulnerable funds, resilient opportunities, and optimal portfolio construction under trade uncertainty.

🎯 Objectives

The project aims to help a portfolio manager:

Understand which funds and sectors are most vulnerable to tariff shocks

Identify resilient funds that can outperform during trade tensions

Build a balanced investment strategy grounded in data

Define an appropriate investment horizon and rebalancing approach

📊 Interactive Dashboard

An interactive Streamlit dashboard allows real-time exploration of fund characteristics, risk, and performance.
## 📊 Interactive Dashboard (Visual Overview)

### 🔹 Dashboard Overview
![Dashboard Overview](images/newplot%20(2).png)

---

### 🔹 Resilience vs Tariff Risk
![Resilience vs Tariff Risk](images/newplot%20(3).png)

---

### 🔹 Fund AUM vs Tariff Exposure
![Fund AUM vs Tariff Exposure](images/newplot%20(5).png)

---

### 🔹 Filtered Fund Table
![Filtered Fund Table](images/newplot%20(7).png)

---

📌 *The dashboard supports interactive filtering by tariff risk, sector, region, fund type, and AUM size.*

🔗 Live Dashboard

👉 Dashboard URL:

https://<your-streamlit-app-name>.streamlit.app


(Replace with your actual deployed link)

🎛️ Dashboard Features

Interactive Filters

Tariff Risk Level (Low / Medium / High)

Sector

Geographic Region

Fund Type (ETF / Mutual Fund)

AUM Size Bucket

Key Visualizations

Tariff Risk Distribution across Sectors

Resilience vs Tariff Risk

Fund AUM vs Tariff Exposure

Performance & Risk comparison

Dynamic Fund Table

Displays filtered fund-level metrics (top 20 rows for clarity)

📄 Detailed dashboard usage is documented in
Interactive_Dashboard_Documentation.pdf

🧠 Data & Methodology
Dataset

300+ global mutual funds and ETFs

Features include:

Tariff exposure metrics

Resilience scores

Returns, volatility, drawdowns

Sector, region, AUM, fund type

Analytical Approach

Exploratory Data Analysis (EDA)

Identify patterns across tariff risk, resilience, sector, and region

Regression Analysis

Validate drivers of returns and risk under trade uncertainty

Strategic Segmentation

Segment funds by Tariff Risk × Resilience

Portfolio Construction

Build a resilient, scenario-robust equity portfolio

📈 Key Insights

Tariff exposure materially impacts fund performance, but outcomes vary widely

Resilience is the key differentiator within each tariff risk category

High tariff risk does not automatically imply poor performance

Regression confirms tariff exposure and resilience as statistically significant drivers of returns

💼 Investment Strategy Summary

The proposed strategy segments funds into three investable buckets:

Segment	Weight	Role
Core Defensive	45%	Stability & drawdown control
Balanced Growth	35%	Primary return engine
Opportunistic Alpha	20%	Selective upside

Focuses on high-resilience funds

Avoids persistent negative outliers

Designed for robustness across multiple trade scenarios

⏱️ Investment Horizon & Rebalancing

Horizon: Medium-to-long term (3–5 years)

Rebalancing: Semi-annual + event-driven (tariff changes, resilience shifts)

📁 Repository Structure
tariff_dashboard/
│
├── app.py                     # Streamlit dashboard app
├── eda.py                     # Exploratory Data Analysis
├── task3.py                   # Regression: drivers of returns & risk
├── task4.py                   # Strategy & portfolio construction
│
├── utils/
│   ├── data_loader.py
│   ├── charts.py
│   └── filters.py
│
├── outputs/                   # Processed analysis outputs
│   ├── best_positioned_funds.xlsx
│   ├── fund_strategy_segments.xlsx
│   ├── positive_return_outliers.xlsx
│   ├── negative_return_outliers.xlsx
│   ├── sector_level_summary.xlsx
│   ├── region_level_summary.xlsx
│   ├── performance_by_risk_and_resilience.xlsx
│   └── regression_results.txt
│
├── requirements.txt
├── README.md

▶️ How to Run Locally
# Create environment
conda create -n ds python=3.10
conda activate ds

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run app.py

📦 Deliverables

📊 Interactive dashboard (live link)

📄 7-slide PDF presentation

🧾 Executive Summary

📈 Processed Excel outputs

🧠 Well-commented Python analysis code

👤 Author

Sohel (Azijur Rahaman)
MSc Data Science & Management
IIM Amritsar
🏁 Final Note

This project reframes tariff uncertainty from a risk to be avoided into a dimension to be managed through resilience, enabling more consistent risk-adjusted equity outcomes in a volatile global trade environment.
