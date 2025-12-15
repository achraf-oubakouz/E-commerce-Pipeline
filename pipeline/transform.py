import numpy as np
import pandas as pd

def transform(df):
    df = df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df[(df["quantity"] > 0) & (df["price"] > 0)]
    df["total_sales"] = np.multiply(df["quantity"], df["price"])
    df["category"] = df["category"].fillna("Unknown")

    if df["total_sales"].isnull().any():
        raise ValueError("Found missing total_sales values")
    if (df["total_sales"] < 0).any():
        raise ValueError("Negative total_sales detected")

    return df
