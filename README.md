# Market Expansion & Risk Screening Tool

A data science project built to answer one real business question properly, instead of many questions shallowly.

**Can public economic and business data identify attractive markets and provide early warning of deteriorating conditions for companies considering international expansion?**

## What this actually is

This is a screening tool, not a final investment decision maker. Public macroeconomic data cannot account for a company's specific industry regulation, competitors, tax position, or local partners. So the goal here is to help identify which markets deserve deeper investigation, not to make that final call for anyone.

## How it works

Every country is scored across three connected dimensions.

**Market Attractiveness** looks at demand potential, economic momentum, and how realistic it is for a business to actually operate and scale there.

**Market Risk** looks for early warning signals in inflation, governance, and currency trends. This considers not just where a number currently sits, but how quickly it is moving and whether that movement is speeding up.

**Resilience** looks at how each market recovered from real past shocks, specifically the 2008 financial crisis and the 2020 COVID shock.

Attractiveness and Risk are combined into a simple 2 by 2 matrix rather than one blended score, since two very different countries can otherwise end up looking identical for very different reasons.

| | Low Risk | High Risk |
|---|---|---|
| High Attractiveness | Priority Market | Investigate |
| Low Attractiveness | Watch | Elevated Risk / Low Priority |

## Scope for this first version

Countries covered: China, India, Bangladesh, Sri Lanka, Nepal, Singapore, Malaysia, Indonesia, Thailand, Vietnam, Philippines, Myanmar, Cambodia, Laos, and Brunei.

Time range: 2000 to present.

Data sources: World Bank Open Data, IMF, and Worldwide Governance Indicators. All free and publicly available, which is what makes this reusable for any country later on.

## Built with

SQL (SQLite) for the underlying country year data panel.
Python (pandas, scikit-learn) for the scoring logic and anomaly detection.
Streamlit for an interactive dashboard.
Power BI for a version aimed at a business audience.

## Project layout

The data folder holds raw pulls and cleaned tables separately. Notebooks are split by build phase rather than kept in one large file. Source holds reusable functions, and docs holds the project plan and case study writeup.

## Where this stands right now

Currently working through data collection and cleaning. More phases to follow.

## Built by

Ansuman Jaiswal ([iam-ansuman](https://github.com/iam-ansuman))
Heming Yuan ([14955442HY](https://github.com/14955442HY))
