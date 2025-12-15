def load(daily_sales, category_sales):
    daily_sales.to_csv("data/daily_sales.csv", index=False)
    category_sales.to_csv("data/category_sales.csv", index=False)
    print("Aggregated CSVs saved in data/ folder")
