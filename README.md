ELT Pipeline Using dbt and Airflow
📄 Project Overview
This project showcases the creation of a modern ELT (Extract, Load, Transform) data pipeline. The objective was to build a robust and automated system to ingest data from CSV files into a Snowflake data warehouse and then transform it using dbt (data build tool) for analysis. The entire process is orchestrated by Apache Airflow.

🎯 Problem Statement and Goal
The Problem: Unstructured data residing in local CSV files needs to be ingested and transformed into a structured, analysis-ready format for business intelligence and reporting.

The Goal: To design and implement a scalable, automated pipeline that extracts data from CSVs, loads it into Snowflake, and uses dbt to perform transformations, ensuring data integrity and usability.

🏛️ Project Architecture
The architecture follows a modern ELT approach, where data is first loaded into the data warehouse and then transformed entirely within the warehouse using SQL.

Extract & Load: Four key datasets (customers, orders, order_items, and products) are extracted from CSV files and loaded into a Snowflake data warehouse.

Transform (dbt):

Staging: dbt is used to create staging views for each of the four raw tables. This is the initial transformation step, where columns are renamed to be more descriptive and consistent.

Fact Table: A central fact table is created by joining the stg_orders and stg_order_items tables, providing a single source of truth for order-related analytics.

Data Testing: dbt's testing framework is used to ensure data quality and integrity at key points in the pipeline.

Orchestration: All of these tasks—from loading the data to running dbt models and tests—are managed and automated by Apache Airflow, using the Astronomer CLI for local development.

🛠️ Technologies and Tools Used
Snowflake: The cloud-native data warehouse where all data is stored and transformed.

dbt (data build tool): Used for all data modeling and transformation, leveraging SQL and Jinja to build, test, and document the data warehouse.

Apache Airflow: The orchestration platform that schedules and manages the entire pipeline, from loading data to running dbt commands.

Astronomer CLI: To easily spin up and manage a local Airflow environment using Docker.

CSV Files: The source data for the project.

🔄 Data Model & Transformations
The project creates a simple, yet effective data model for analytics, including staging models and a final fact table.

Staging Models:

stg_customers: Cleans and renames columns from the raw customers data.

stg_orders: Cleans and renames columns from the raw orders data.

stg_order_items: Cleans and renames columns from the raw order_items data.

stg_products: Cleans and renames columns from the raw products data.

Fact Table:

A fact table is created by joining stg_orders and stg_order_items to provide a comprehensive view of orders and their associated items.

✅ Data Quality & Testing
To ensure data reliability, dbt tests were implemented on the staging models. These tests automatically check for common data quality issues.

version: 2

models:
  - name: stg_orders
    columns:
      - name: order_status
        tests:
          - accepted_values:
              values: ['Completed', 'Pending', 'Cancelled']
  - name: stg_customers
    columns:
      - name: customer_id
        tests:
          - unique

The tests verify:

order_status: The order_status column in stg_orders only contains valid values (Completed, Pending, Cancelled).

customer_id: The customer_id column in stg_customers has unique values, preventing duplicate customer records.

🚀 How to Run the Project
Prerequisites:

Docker Desktop

Astronomer CLI

Access to a Snowflake account.

Setup and Execution Steps:

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Start the local Airflow environment:

astro dev start

This command will create the necessary Docker containers. You can access the Airflow UI at http://localhost:8080.

Run dbt via Airflow:

Create a DAG in Airflow that includes tasks to:

Load the CSV files into Snowflake.

Run dbt debug to check the connection.

Run dbt run to build all the dbt models.

Run dbt test to execute the data quality tests.

Check Results:

Log into your Snowflake account to see the newly created tables and views.

Check the Airflow logs for the dbt tasks to verify they ran successfully.

📈 Results and Achievements
Successfully built a complete, functional ELT data pipeline from raw files to an analysis-ready data warehouse.

Demonstrated proficiency with key data engineering tools like dbt and Airflow.

Implemented automated data quality checks, ensuring a reliable data output.

Created a structured data model that is easy to query and understand.

💡 Future Improvements
Schedule the pipeline to run automatically on a recurring basis.

Integrate a version control system like Git into the Airflow DAG for better CI/CD practices.

Add more extensive dbt tests to cover a wider range of data quality issues.

Build a downstream dashboard using a BI tool like Tableau or Power BI.
