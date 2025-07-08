# final_project
Python course final dashboard

# Measles Vaccine Coverage & Child Mortality (2000–2023) (Work in progress, do not share)
Author: Moudo Macina
Project Type: Interactive Data Dashboard
Tools: Quarto · Python · Plotly · pandas · Gapminder data

# Overview
This dashboard explores global trends in measles vaccine coverage (MCV1) and under-five child mortality between 2000 and 2023. It highlights how expanded immunization—especially in low-income settings—has driven substantial improvements in child survival.

The dashboard visualizes [View the Dashboard](https://mascogit.github.io/final_project/):

-Changes in MCV1 coverage and child mortality over time

-Country-level and income-group comparisons

-The correlation between vaccination rates and mortality decline

-Top and bottom performers in child health outcomes

# Structure
-Welcome Page: Poster-style image and introduction

-Home Tab: Key insights and interactive graphs

-Progress Tabs: Value boxes, scatter plots, maps, and trend lines

-Comparative Views: Income group disparities and box plots

-Data Description: Methodology and download of cleaned dataset

# Data Sources
Data is sourced from Gapminder and includes:

-MCV1 (Measles-Containing Vaccine) coverage (% of 1-year-olds)

-Child mortality (under age 5, per 1,000 live births)

-GDP per capita (PPP, current international $)

Data has been cleaned, transformed, and merged for longitudinal and cross-country comparison.

## How to Use
Launch the Quarto dashboard by opening index.qmd and rendering with quarto preview

Interact with sliders, tabs, and plots to explore country trends

Download the full dataset directly from the "Data Description" tab, 
[View data preparation code](data_prep.html)

## License
This project is released for non-commercial, public health, and educational purposes. Data belongs to their respective sources (Gapminder). Dashboard authored by Moudo Macina.
