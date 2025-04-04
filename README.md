# smart-store-caffery
A project designed for inventory management. The goal is to use Git for version control and document our workflow.

## Table of Contents
- [smart-store-caffery](#smart-store-caffery)
  - [Table of Contents](#table-of-contents)
  - [Project Setup](#project-setup)
  - [Git Workflow](#git-workflow)
  - [Key Files](#key-files)
  - [Using a Virtual Environment](#using-a-virtual-environment)
  - [Running Python Scripts](#running-python-scripts)
  - [Updating and Pushing Changes](#updating-and-pushing-changes)
  - [Final Notes](#final-notes)
  - [P3 - Data Cleaning \& Prepare for ETL](#p3---data-cleaning--prepare-for-etl)
  - [P4 - Create and Populate a DW](#p4---create-and-populate-a-dw)

## Project Setup
1. Clone the Repository
To get started, clone the repository from GitHub:

git clone https://github.com/ellacaffery/smart-store-caffery.git

Navigate into the project folder:
cd smart-store-caffery

1. Open Project in VS Code
    Open VS Code.
    Use File > Open Folder and select the project folder.
    Verify that key files such as README.md, .gitignore, and requirements.txt are present.

## Git Workflow
1. Checking the Current Branch
Before making changes, check your current branch:
git branch
Ensure you are on the main branch.

2. Pulling the Latest Changes
Always fetch the latest changes before making updates:
git pull origin main --rebase

3. Making Changes and Saving Files
Edit files as needed and save your work in VS Code (Ctrl + S or Cmd + S).

4. Staging and Committing Changes
After editing, add your changes to Git:
git add .
git commit -m "Descriptive commit message"

5. Pushing Changes to GitHub
Once committed, push updates to GitHub:
git push origin main

## Key Files
- README.md → Project documentation and workflow tracking.
- .gitignore → Specifies files to exclude from version control.
- requirements.txt → Lists Python packages required for the project.
- utils/logger.py → Contains logging utilities (to be added).
- scripts/data_prep.py → Data preparation script (to be added).

## Using a Virtual Environment
A virtual environment isolates dependencies for the project.

1. Create the Virtual Environment
python -m venv .venv

2. Activate the Virtual Environment
Windows (PowerShell)
.venv\Scripts\Activate

1. Install Dependencies
pip install -r requirements.txt

## Running Python Scripts
To execute the data_prep.py script:
py scripts\data_prep.py

## Updating and Pushing Changes
After making updates to your project or README file, follow these steps:

git add .
git commit -m "Update README with workflow and commands"
git push origin main

## Final Notes
- Always pull (git pull origin main --rebase) before pushing changes to avoid conflicts.
- Use descriptive commit messages to track progress.
- If you get merge conflicts, resolve them manually and commit again.

## P3 - Data Cleaning & Prepare for ETL

Objectives
- Employ Python pandas to perform some common cleaning and prep tasks. 
- Wrap this functionality into a reusable DataScrubber class. 
- Use Python unittest (from the Python Standard Library) to verify our DataScrubber class methods have been correctly defined and perform the necessary work correctly. 
- Finish the TODO items in the provided DataScrubber class. 
- Run the test data scrubber script to verify ALL tests pass 100%. 
- Use the DataScrubber class in your data prep script. 

Data Cleaning Process (using Python pandas)
1. Initial Data Inspection and Profiling
df.info(): Check data types and identify missing values.
df.describe(): Get summary statistics for numerical columns.
df.head() and df.sample(): Inspect the structure and sample of the data.
2. Handle Missing Data
Identify missing values: df.isnull().sum()
Drop missing values: df.dropna()
Fill missing values: df.fillna(value)
3. Remove Duplicates
Identify duplicates: df.duplicated()
Drop duplicates: df.drop_duplicates()
4. Filter or Handle Outliers
Identify outliers: df.describe() and box plot visualization.
Filter outliers: df[df['column'] < upper_bound]
5. Data Type Conversion and Standardization
Convert data types: df.astype()
Parse dates: pd.to_datetime(df['column'])
6. Standardize and Format Data
Apply string formatting: df['column'].str.lower() and df['column'].str.strip()
Rename columns: df.rename(columns={'old_name': 'new_name'})
7. Column Management
Drop unnecessary columns: df.drop(columns=['column'])
Reorder columns: df = df[['col1', 'col2', ...]]
8. Data Integration and Aggregation
Merge data: pd.merge(df1, df2, on='key_column')
Aggregate data: df.groupby().agg()

ETL Preperation
- Verify attribute names are clear with units for numerical traits.
- Attribute names have been standardized where possible.
- Verify all rows have the correct number of entries.
- Verify all duplication has been removed.
- Verify all bad, missing, or out of range records have been removed.
- Verify each column adheres to the expected data type (e.g., dates are in date/time formats, identifiers like phone numbers are consistent).
- Verify that collection and usage comply with relevant laws and regulations.

## P4 - Create and Populate a DW

Objectives:
- Understand the role of a data warehouse in business intelligence.
- Design a schema that effectively organizes data for analysis.
- Implement the schema using a database system to create a functional data warehouse.
- Write and execute an ETL script to populate the warehouse.
- Verify and document the schema and data.

Succesfully designed a star schema and loaded data sets from "customers_data_prepared", "products_data_prepared", and "sales_data_preprared" into a data warehouse names "smart_sales.db"