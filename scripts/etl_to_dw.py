import pandas as pd
import sqlite3
import pathlib
import sys

# For local imports, temporarily add project root to sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Constants
DW_DIR = pathlib.Path("data").joinpath("dw")
DB_PATH = DW_DIR.joinpath("smart_sales.db")
PREPARED_DATA_DIR = pathlib.Path("data").joinpath("prepared")

def create_schema(cursor: sqlite3.Cursor) -> None:
    """Create tables in the data warehouse if they don't exist."""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            region TEXT,
            join_date TEXT,
            loyalty_points INTEGER,
            preferred_contact_method TEXT      
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            unit_price NUMERIC,
            year_added INTEGER,
            store_section TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sale (
            sale_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_id INTEGER,
            sale_amount REAL,
            sale_date TEXT,
            store_id INTEGER,
            campaign_id INTEGER,
            discount_percent NUMERIC,
            state TEXT,
            FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
            FOREIGN KEY (product_id) REFERENCES product (product_id)
        )
    """)

def delete_existing_records(cursor: sqlite3.Cursor) -> None:
    """Delete all existing records from the customer, product, and sale tables."""
    cursor.execute("DELETE FROM customer")
    cursor.execute("DELETE FROM product")
    cursor.execute("DELETE FROM sale")

def insert_customers(customers_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    customers_df.rename(columns={
        "CustomerID": "customer_id",
        "Name": "name",
        "Region": "region",
        "JoinDate": "join_date",
        "LoyaltyPoints": "loyalty_points",
        "PreferredContactMethod": "preferred_contact_method"
    }, inplace=True)

    print("Customers DataFrame shape:", customers_df.shape)
    print("Customers columns:", customers_df.columns)

    try:
        customers_df.to_sql("customer", cursor.connection, if_exists="append", index=False)
        print("✅ Inserted customers data.")
    except Exception as e:
        print("❌ Error inserting customers data:", e)

def insert_products(products_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    products_df.rename(columns={
        "productid": "product_id",
        "productname": "product_name",
        "category": "category",
        "unitprice": "unit_price",
        "yearadded": "year_added",
        "storesection": "store_section"
    }, inplace=True)

    print("Products DataFrame shape:", products_df.shape)
    print("Products columns:", products_df.columns)

    try:
        products_df.to_sql("product", cursor.connection, if_exists="append", index=False)
        print("✅ Inserted products data.")
    except Exception as e:
        print("❌ Error inserting products data:", e)

def insert_sales(sales_df: pd.DataFrame, cursor: sqlite3.Cursor) -> None:
    sales_df.rename(columns={
        "TransactionID": "sale_id",
        "CustomerID": "customer_id",
        "ProductID": "product_id",
        "SaleAmount": "sale_amount",
        "SaleDate": "sale_date",
        "StoreID": "store_id",
        "CampaignID": "campaign_id",
        "DiscountPercent": "discount_percent",
        "State": "state"
    }, inplace=True)

    print("Sales DataFrame shape:", sales_df.shape)
    print("Sales columns:", sales_df.columns)

    try:
        sales_df.to_sql("sale", cursor.connection, if_exists="append", index=False)
        print("✅ Inserted sales data.")
    except Exception as e:
        print("❌ Error inserting sales data:", e)

def load_data_to_db() -> None:
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create schema and clear existing records
        create_schema(cursor)
        delete_existing_records(cursor)

        # Load CSVs into DataFrames
        customers_df = pd.read_csv(PREPARED_DATA_DIR / "customers_data_prepared.csv")
        products_df = pd.read_csv(PREPARED_DATA_DIR / "products_data_prepared.csv")
        sales_df = pd.read_csv(PREPARED_DATA_DIR / "sales_data_prepared.csv")

        print("✅ CSVs loaded.")

        # Insert into tables
        insert_customers(customers_df, cursor)
        insert_products(products_df, cursor)
        insert_sales(sales_df, cursor)

        conn.commit()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    load_data_to_db()
