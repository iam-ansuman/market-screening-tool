import streamlit as st
import pandas as pd

st.title("Country Detail View")

master = pd.read_csv('data/processed/master_scores.csv')
risk_full = pd.read_csv('data/processed/risk_scores.csv')
attractiveness_full = pd.read_csv('data/processed/attractiveness_scores.csv')

country_list = sorted(master['country'].unique())
selected_country = st.selectbox("Choose a country", country_list)

row = master[master['country'] == selected_country].iloc[0]

st.header(selected_country)
st.subheader(f"Classification: {row['classification']}")

col1, col2, col3 = st.columns(3)
col1.metric("Attractiveness Score", round(row['attractiveness_score'], 1))
col2.metric("Risk Score", round(row['risk_score'], 1))
col3.metric("Resilience Score", round(row['resilience_score'], 1))

st.subheader("What is driving the Attractiveness score")
latest_year = attractiveness_full['year'].max()
att_row = attractiveness_full[(attractiveness_full['country'] == selected_country) & (attractiveness_full['year'] == latest_year)]
if not att_row.empty:
    att_row = att_row.iloc[0]
    st.write(f"Demand Potential: {round(att_row['demand_potential_score'], 1)}")
    st.write(f"Economic Momentum: {round(att_row['economic_momentum_score'], 1)}")
    st.write(f"Business Capacity: {round(att_row['business_capacity_score'], 1)}")
    st.write(f"Data components available: {att_row['attractiveness_components_available']} out of 3")

st.subheader("What is driving the Risk score")
risk_latest = risk_full[(risk_full['country'] == selected_country) & (risk_full['year'] == latest_year)]
if not risk_latest.empty:
    risk_latest = risk_latest.iloc[0]
    st.write(f"Risk score this year: {round(risk_latest['risk_score'], 1)}")
    if 'is_unusual_change' in risk_full.columns:
        st.write(f"Unusual change flagged by anomaly detection: {risk_latest['is_unusual_change']}")
