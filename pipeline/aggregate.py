

def aggregate(df):
    daily_sales = (
        df.groupby("order_date")
          .agg(
              revenue=("total_sales", "sum"),
              avg_order_value=("total_sales", "mean")
          )
          .reset_index()
    )

    daily_sales["revenue_7day_avg"] = daily_sales["revenue"].rolling(window=7).mean()

    category_sales = (
        df.groupby("category")
          .agg(
              revenue=("total_sales", "sum"),
              quantity=("quantity", "sum")
          )
          .reset_index()
    )

    return daily_sales, category_sales
