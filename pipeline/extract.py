import pandas as pd

def extract():
    sales = pd.read_csv("data/raw_sales.csv")
    products = pd.read_csv("data/products.csv")
    merged_df = sales.merge(products, on="product_id", how="left")
    return merged_df
