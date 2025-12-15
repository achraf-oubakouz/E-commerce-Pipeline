import logging
from pipeline.extract import extract
from pipeline.transform import transform
from pipeline.aggregate import aggregate
from pipeline.load import load
from analysis.plots import plot_daily_sales, plot_category_sales

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def run_pipeline():
    logging.info("Step 1: Extracting data")
    raw = extract()
    logging.info(f"Extracted {len(raw)} rows")

    logging.info("Step 2: Transforming data")
    clean = transform(raw)
    logging.info(f"Cleaned data has {len(clean)} rows")

    logging.info("Step 3: Aggregating data")
    daily, category = aggregate(clean)
    logging.info("Aggregation complete")

    logging.info("Step 4: Saving CSVs")
    load(daily, category)
    logging.info("Pipeline finished successfully")

    plot_daily_sales(daily)
    plot_category_sales(category)

if __name__ == "__main__":
    run_pipeline()
