# E-Commerce Sales Analytics Pipeline

An end-to-end sales data pipeline built with Python that extracts, transforms, and visualizes e-commerce sales data with daily and category-level analytics.

![Daily Revenue Trend](screenshots/daily_revenue.png)
![Category Revenue](screenshots/category_revenue.png)

## Features

- **Complete ETL Pipeline**: Extract → Transform → Aggregate → Load workflow
- **Trend Analysis**: 7-day rolling averages for daily revenue tracking
- **Export Ready**: Aggregated CSV outputs for downstream analytics
- **Reliability**: Built-in data validation and logging
- **Production Ready**: Clean, reproducible code structure

## Technologies

- **Python 3.10+**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Data visualization

## Getting Started

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/achraf-oubakouz/E-commerce-Pipeline.git
cd E-commerce-Pipeline
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

> **Note**: Requires Python 3.10 or higher

### Generate Sample Data

Create synthetic sales and product data for testing:

```bash
python generate_data.py
```

This generates:
- `data/raw_sales.csv` - Simulated transaction data
- `data/products.csv` - Product reference data

### Run the Pipeline

Execute the complete analytics pipeline:

```bash
python run_pipeline.py
```

The pipeline will:
1. **Extract** raw sales and product data
2. **Transform** and clean the data (calculate totals, handle missing values)
3. **Aggregate** daily and category-level metrics
4. **Load** results to CSV files
5. **Visualize** trends with charts

## Output

### Data Files

Generated in `data/`:
- `daily_sales.csv` - Daily revenue with 7-day rolling averages
- `category_sales.csv` - Total revenue and quantity per category

### Visualizations

Saved in `screenshots/`:
- `daily_revenue.png` - Daily revenue trend line chart
- `category_revenue.png` - Revenue by category bar chart

## Project Structure

```
E-commerce-Pipeline/
├── data/
│   ├── raw_sales.csv
│   ├── products.csv
│   ├── daily_sales.csv
│   └── category_sales.csv
├── screenshots/
│   ├── daily_revenue.png
│   └── category_revenue.png
├── generate_data.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
