import pandas as pd
import numpy as np

from data_processsing import (
    stores_sales_data,
    sales_calendar_data,
    products_sales_data,
    sales_customers_data,
    customers_data,
)

sales_by_store = stores_sales_data.groupby('store_id')
quantity_by_store = sales_by_store['quantity'].sum()
revenue_by_store = sales_by_store['revenue'].sum()
profit_by_store = sales_by_store['profit'].sum()

best_day_of_week = sales_calendar_data.groupby('day_of_week')['revenue'].sum().idxmax()
best_month = sales_calendar_data.groupby('month')['revenue'].sum().idxmax()
best_year = sales_calendar_data.groupby('year')['revenue'].sum().idxmax()
best_day_month = sales_calendar_data.groupby('day')['revenue'].sum().idxmax()

season_counts = {
    'Spring': sales_calendar_data['month'].isin([3, 4, 5]).sum(),
    'Summer': sales_calendar_data['month'].isin([6, 7, 8]).sum(),
    'Autumn': sales_calendar_data['month'].isin([9, 10, 11]).sum(),
    'Winter': sales_calendar_data['month'].isin([12, 1, 2]).sum()
}
best_season = max(season_counts, key=season_counts.get)

best_store = revenue_by_store.idxmax()
best_product = products_sales_data.groupby('product_id')['revenue'].sum().idxmax()
median_weight = products_sales_data['weight_g'].median()
price_by_weight = products_sales_data.groupby('weight_g')['price'].mean()

loyalty = customers_data.groupby('loyalty_member').size().rename('Customer Count')
loyalty_percentage = loyalty / loyalty.sum() * 100

loyalty_new = loyalty.to_frame()
loyalty_new['Bool'] = loyalty_new.index.astype(bool)

median_age = customers_data['age'].median()
modage = customers_data['age'].mode()[0]