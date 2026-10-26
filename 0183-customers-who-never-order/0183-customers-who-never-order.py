import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:


    order = customers['id'].isin(orders['customerId']) == False
    return customers.loc[order, ['name']].rename(columns={'name': 'Customers'})
