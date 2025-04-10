import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import pathlib
import sys

# Optional logger import if available
try:
    from utils.logger import logger
except ImportError:
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

# Constants
DW_DIR = pathlib.Path("data").joinpath("dw")
DB_PATH = DW_DIR.joinpath("smart_sales.db")
OUTPUT_DIR = pathlib.Path("data/olap_cubing_outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    """Load sales and product data from the data warehouse."""
    conn = sqlite3.connect(DB_PATH)
    
    query = """
    SELECT s.sale_date, s.sale_amount, s.product_id, p.product_name AS product_name
    FROM sale s
    JOIN product p ON s.product_id = p.product_id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["month"] = df["sale_date"].dt.to_period("M").astype(str)

    return df

def find_top_spenders(sales_df, customer_df, top_n=10):
    """Find the top 5 customers by total spend."""
    total_spending = sales_df.groupby("customer_id")["sale_amount"].sum().reset_index()
    total_spending = total_spending.rename(columns={"sale_amount": "total_spent"})

    top_spenders = pd.merge(total_spending, customer_df, on="customer_id", how="left")
    top_spenders = top_spenders.sort_values(by="total_spent", ascending=False).head(top_n)

    return top_spenders

def visualize_top_spenders(top_customers):
    """Create and save a bar chart of top spending customers."""
    plt.figure(figsize=(10, 6))
    plt.barh(top_customers["name"], top_customers["total_spent"], color="skyblue")
    plt.xlabel("Total Spent ($)")
    plt.ylabel("Customer")
    plt.title("Top Spending Customers")
    plt.gca().invert_yaxis()  # Highest spender on top
    plt.tight_layout()

    image_path = OUTPUT_DIR.joinpath("top_spending_customers.png")
    plt.savefig(image_path)
    logger.info(f"Bar chart saved to: {image_path}")
    plt.close()

def main():
    logger.info("Loading sales and customer data...")
    sales_df, customer_df = load_data_from_dw()

    logger.info("Finding top spending customers...")
    top_customers = find_top_spenders(sales_df, customer_df)

    print("\nTop Spending Customers:")
    print(top_customers.to_string(index=False))

    csv_path = OUTPUT_DIR.joinpath("top_spending_customers.csv")
    top_customers.to_csv(csv_path, index=False)
    logger.info(f"Top customers saved to: {csv_path}")

    logger.info("Generating visualization...")
    visualize_top_spenders(top_customers)

if __name__ == "__main__":
    main()
