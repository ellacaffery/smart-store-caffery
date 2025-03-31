-- Create Fact Table (Sales)
CREATE TABLE Sales (
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    quantity_sold INTEGER,
    total_price REAL,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create Dimension Table (Products)
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL
);

-- Create Dimension Table (Customers)
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    location TEXT,
    age INTEGER
);
