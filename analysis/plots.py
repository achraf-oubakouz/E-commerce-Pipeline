import matplotlib.pyplot as plt

def plot_daily_sales(daily_sales):
    plt.figure(figsize=(10,5))
    plt.plot(daily_sales["order_date"], daily_sales["revenue"], marker='o')
    plt.plot(daily_sales["order_date"], daily_sales["revenue_7day_avg"], color='red', label="7-Day Avg")
    plt.title("Daily Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("screenshots/daily_revenue.png", dpi=300)
    plt.close() 

def plot_category_sales(category_sales):
    plt.figure(figsize=(8,5))
    plt.bar(category_sales["category"], category_sales["revenue"], color='skyblue')
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("screenshots/category_revenue.png", dpi=300)
    plt.close()
