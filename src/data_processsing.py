import pandas as pd

stores_data = pd.read_csv('./data/stores.csv')
sales_data = pd.read_csv('./data/sales.csv')
calendar_data = pd.read_csv('./data/calendar.csv')
customers_data = pd.read_csv('./data/customers.csv')
products_data = pd.read_csv('./data/products.csv')


stores_sales_data = pd.merge(
    stores_data, sales_data, 
    on='store_id', 
    how='inner'
    )

sales_calendar_data = pd.merge(
    sales_data, calendar_data,
    left_on = 'order_date',
    right_on= 'date',
    how='inner'
)

products_sales_data = pd.merge(
    products_data, sales_data,
    on='product_id',
    how='inner'
)

sales_customers_data = pd.merge(
    sales_data, customers_data,
    on='customer_id',
    how='inner'
)

checking_data = [stores_sales_data, sales_calendar_data, products_sales_data, sales_customers_data]
data_series = pd.Series(checking_data)

print('Checking for null values in the merged datasets:')
print(data_series.isnull().sum())

print('Checking for duplicates in the merged datasets:')
print(data_series.duplicated().sum())