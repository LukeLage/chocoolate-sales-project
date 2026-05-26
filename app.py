import streamlit as st
from pathlib import Path
import sys

# ensure `src/` is on sys.path so internal modules import correctly
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from data_wrangling import (
	sales_by_store,
	quantity_by_store,
	revenue_by_store,
	profit_by_store,
	total_revenue,
	total_profit,
	best_day_of_week,
	best_month,
	best_year,
	best_day_month,
	season_counts,
	best_season,
	best_store,
	best_product,
	median_weight,
	loyalty,
	loyalty_percentage,
	loyalty_new,
	median_age,
	modage,
	customers_age_distribution,
	customers_gender,
)

st.title("Chocolate Sales Dashboard")

st.sidebar.title('Filters')
sidebar = st.sidebar

metrics1, metrics2, metrics3 = st.columns(3)
metrics1.container(border= True).metric('Total Revenue in Millions', '${:,.2f}'.format(total_revenue / 1000000))
metrics2.container(border= True).metric('Total Profit in Millions', '${:,.2f}'.format(total_profit / 1000000))
metrics3.container(border= True).metric('Best Store by Revenue', best_store)