import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os

# Path to the database
DB_PATH = "data/dw/smart_sales.db"

# Output path for the image
OUTPUT_PATH = "data/olap_cubing_outputs/monthly_sales_trend.png"

# Ensure the output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Function to load the sales data
def load_sales_data():
    conn = sqlite3.connect(DB_PATH)
    
    # SQL query to get monthly sales data
    query = '''
        SELECT 
            strftime('%Y-%m', sale_date) AS month, 
            SUM(sale_amount) AS total_sales
        FROM sale
        GROUP BY month
        ORDER BY month
    '''
    
    # Read data into a pandas DataFrame
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df

# Function to create the plot
def create_monthly_sales_trend_plot(df):
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df['month'], df['total_sales'], marker='o', linestyle='-', color='b')
    
    # Customize the plot
    plt.title('Monthly Sales Trend', fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Sales', fontsize=12)
    plt.xticks(rotation=45)
    
    # Save the plot to the output path
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

# Main function
def main():
    print("Loading sales data...")
    sales_data = load_sales_data()
    
    print("Creating monthly sales trend plot...")
    create_monthly_sales_trend_plot(sales_data)
    
    print(f"Sales trend plot saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
