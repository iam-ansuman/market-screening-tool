import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Market Screening Overview")

master = pd.read_csv('data/processed/master_scores.csv')

st.subheader("All Countries Ranked by Attractiveness")
sort_by = st.selectbox("Sort by", ["attractiveness_score", "risk_score", "resilience_score"])
st.dataframe(master[['country', 'attractiveness_score', 'risk_score', 'resilience_score', 'classification']].sort_values(sort_by, ascending=False))

st.subheader("Attractiveness vs Risk Matrix")

color_map = {
    "Priority Market": "#2ecc71",
    "Investigate": "#f39c12",
    "Watch": "#3498db",
    "Elevated Risk / Low Priority": "#e74c3c"
}

fig = px.scatter(
    master,
    x="attractiveness_score",
    y="risk_score",
    color="classification",
    color_discrete_map=color_map,
    text="country",
    size_max=15,
    hover_data={"attractiveness_score": True, "risk_score": True, "resilience_score": True, "classification": True},
)

fig.update_traces(marker=dict(size=14, line=dict(width=1, color='white')), textposition='top center')
fig.update_layout(
    xaxis_title="Attractiveness Score",
    yaxis_title="Risk Score",
    legend_title="Classification",
    height=600,
    font=dict(size=13),
)

st.plotly_chart(fig, use_container_width=True)
