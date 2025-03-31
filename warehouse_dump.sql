PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    unitprice REAL
    yearadded INTEGER,
    storesection TEXT
);
CREATE TABLE Sales (
    transaction_id INTEGER PRIMARY KEY,
    saledate INTEGER,
    customer_id INTEGER,
    product_id INTEGER,
    store_id REAL,
    campaign_id DATE,
    saleamount REAL,
    discountpercentage REAL,
    state TEXT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    region TEXT,
    joindate INTEGER,
    loyaltypoints INTEGER,
    preferredcontactmethod TEXT
);
COMMIT;
