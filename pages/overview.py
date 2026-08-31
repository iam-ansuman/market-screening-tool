import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Market Screening Overview")

master = pd.read_csv("data/processed/master_scores.csv")

st.subheader("All Countries Ranking")

sort_by = st.selectbox(
    "Sort by",
    [
        "attractiveness_score",
        "risk_score",
        "resilience_score",
    ],
)

ranking = (
    master[
        [
            "country",
            "attractiveness_score",
            "risk_score",
            "resilience_score",
            "classification",
        ]
    ]
    .sort_values(sort_by, ascending=False)
    .reset_index(drop=True)
)

st.dataframe(ranking, use_container_width=True)

st.subheader("Attractiveness vs Risk Matrix")

fig, ax = plt.subplots(figsize=(10, 6))

colors_map = {
    "Priority Market": "green",
    "Investigate": "orange",
    "Watch": "blue",
    "Elevated Risk / Low Priority": "red",
}

for label, group in master.groupby("classification"):
    ax.scatter(
        group["attractiveness_score"],
        group["risk_score"],
        label=label,
        color=colors_map.get(label, "gray"),
        s=70,
        alpha=0.8,
    )

    for _, row in group.iterrows():
        ax.annotate(
            row["country"],
            (row["attractiveness_score"], row["risk_score"]),
            xytext=(4, 4),
            textcoords="offset points",
            fontsize=8,
        )

ax.set_xlabel("Attractiveness Score")
ax.set_ylabel("Risk Score")
ax.legend()
ax.grid(alpha=0.2)

st.pyplot(fig)
