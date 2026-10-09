import numpy as np
import pandas as pd
customer=pd.read_csv('Datasets/olist_customers_dataset.csv')
seller=pd.read_csv('Datasets/olist_sellers_dataset.csv')
orders=pd.read_csv('Datasets/olist_orders_dataset.csv')
products=pd.read_csv('Datasets/olist_products_dataset.csv')
orderItems=pd.read_csv('Datasets/olist_order_items_dataset.csv')
payments=pd.read_csv('Datasets/olist_order_payments_dataset.csv')
reviews=pd.read_csv('Datasets/olist_order_reviews_dataset.csv')
print(customer.head())
print(seller.head())
print(orders.head())
print(products.head())
print(orderItems.head())
print(payments.head())
print(reviews.head())


