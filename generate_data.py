import numpy as np
import pandas as pd

def generate_products():
    products = pd.DataFrame({
        "product_id": [101, 102, 103, 104, 105],
        "product_name": [
            "Organic Apples",
            "Whole Milk",
            "Brown Bread",
            "Free Range Eggs",
            "Cheddar Cheese"
        ],
        "category": [
            "Fruit",
            "Dairy",
            "Bakery",
            "Dairy",
            "Dairy"
        ]
    })
    products.to_csv("data/products.csv", index=False)

def generate_sales(n_rows=500):
    np.random.seed(42)
    order_ids = np.arange(1, n_rows + 1)
    product_ids = np.random.choice([101, 102, 103, 104, 105], size=n_rows)
    quantities = np.random.randint(1, 6, size=n_rows)
    prices = np.random.choice([3.5, 4.0, 2.5, 5.0, 6.5], size=n_rows)
    dates = pd.date_range(start="2024-01-01", periods=90)
    order_dates = np.random.choice(dates, size=n_rows)
    sales = pd.DataFrame({
        "order_id": order_ids,
        "product_id": product_ids,
        "quantity": quantities,
        "price": prices,
        "order_date": order_dates
    })
    sales.to_csv("data/raw_sales.csv", index=False)

if __name__ == "__main__":
    generate_products()
    generate_sales()
    print("CSV files generated successfully!")
