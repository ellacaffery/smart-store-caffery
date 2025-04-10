import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the SQLite database
DB_PATH = 'data/dw/smart_sales.db'

# Function to load sales data from the database
def load_sales_data():
    print("Loading sales data...")
    
    # Connect to the database
    conn = sqlite3.connect(DB_PATH)
    
    # SQL query to get sales by store
    query = '''
        SELECT s.store_id, SUM(s.sale_amount) AS total_sales
        FROM sale s
        GROUP BY s.store_id
    '''
    
    # Execute query and load data into DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    return df

# Create pie chart for sales by store and save it to the specified folder
def create_pie_chart(df):
    plt.figure(figsize=(8, 8))
    plt.pie(df['total_sales'], labels=df['store_id'], autopct='%1.1f%%', startangle=90)
    plt.title('Sales by Store')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Create the output directory if it doesn't exist
    output_dir = 'data/olap_cubing_outputs'
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the pie chart as a PNG file in the specified folder
    file_path = os.path.join(output_dir, "sales_by_store_pie_chart.png")
    plt.savefig(file_path, bbox_inches='tight')
    print(f"Pie chart saved as '{file_path}'")
    plt.show()

# Main function to load data and create the pie chart
def main():
    # Load sales data
    sales_data = load_sales_data()
    
    # Create pie chart for sales by store
    create_pie_chart(sales_data)

# Run the main function
if __name__ == "__main__":
    main()
