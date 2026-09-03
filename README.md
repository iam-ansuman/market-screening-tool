# Market Expansion and Risk Screening Tool

A data science project built to answer one real business question properly, instead of many questions shallowly.

**Can public economic and business data identify attractive markets and provide early warning of deteriorating conditions for companies considering international expansion?**

## Try it live

**Interactive dashboard:** https://market-screening-tool-yxrncln59tvsupsellsazw.streamlit.app/

## What this actually is

This is a screening tool, not a final investment decision maker. Public macroeconomic data cannot account for a company's specific industry regulation, competitors, tax position, or local partners. So the goal here is to help identify which markets deserve deeper investigation, not to make that final call for anyone.

## How it works

Every country is scored across three connected dimensions.

**Market Attractiveness** looks at demand potential, economic momentum, and how realistic it is for a business to actually operate and scale there.

**Market Risk** looks for early warning signals in inflation, governance, and currency trends, using level, trend, and acceleration together rather than a single snapshot value.

**Resilience** looks at how each market recovered from real past shocks, specifically the 2008 financial crisis and the 2020 COVID shock.

Attractiveness and Risk are combined into a simple 2 by 2 matrix rather than one blended score.

| | Low Risk | High Risk |
|---|---|---|
| High Attractiveness | Priority Market | Investigate |
| Low Attractiveness | Watch | Elevated Risk / Low Priority |

## Scope

Countries covered: China, India, Bangladesh, Sri Lanka, Nepal, Singapore, Malaysia, Indonesia, Thailand, Vietnam, Philippines, Myanmar, Cambodia, Laos, and Brunei.

Time range: 2000 to present.

Data sources: World Bank Open Data, IMF World Economic Outlook, and the Worldwide Governance Indicators. All free and publicly available.

## Features

An interactive Streamlit dashboard with a country overview page and a detailed country breakdown page. A Tableau dashboard aimed at a business audience. Automatically generated one page PDF reports for every country, downloadable directly from the app.

## Built with

SQL style data handling and Python (pandas, scikit-learn) for the scoring logic and anomaly detection. Streamlit for the interactive dashboard. Tableau for the business facing dashboard. Reportlab for the automated PDF reports.

## Project layout

The data folder holds raw pulls, cleaned tables, and the generated country reports separately. Notebooks are split by build phase rather than kept in one large file. Pages holds the Streamlit application pages. Docs holds the project plan and reflection reports.

## Where this stands

Complete through data collection, scoring, dashboarding, and automated reporting. Final packaging in progress.

## Built by

Ansuman Jaiswal ([iam-ansuman](https://github.com/iam-ansuman))
Heming Yuan ([14955442HY](https://github.com/14955442HY))
