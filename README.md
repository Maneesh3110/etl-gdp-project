# ETL GDP Project

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** for **Country GDP data**.  
The pipeline fetches GDP data from Wikipedia, cleans and transforms it, saves the data to CSV and SQLite, and visualizes the **Top 10 economies** using Python’s `seaborn` and `matplotlib`.  

**Key Features:**
- Extract GDP data from web pages using `requests` and `BeautifulSoup`
- Transform GDP values from millions to billions
- Load data to CSV and SQLite database
- Run SQL queries on the dataset
- Visualize Top 10 economies with a professional bar chart
- Logs progress to track pipeline execution

---

## Project Structure

etl-gdp-project/
│── etl.py # ETL functions
│── main.py # Pipeline runner
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── outputs/ # CSV, DB, plots
│── etl_project_log.txt # ETL logs
│── .gitignore # Files to ignore in Git

1. Clone the repository:

``bash
git clone https://github.com/Maneesh3110/etl-gdp-project.git
cd etl-gdp-project
2. Install dependencies:
python3 -m pip install -r requirements.txt

**Usage**
Run the ETL pipeline:
python3 main.py
Outputs will be saved in the outputs/ folder:

Countries_by_GDP.csv → Cleaned GDP data

World_Economies.db → SQLite database

top10_gdp.png → Top 10 GDP bar chart

Example Output
Top 10 Economies by GDP

SQL Queries
You can query the SQLite database:
SELECT * FROM Countries_by_GDP WHERE GDP_USD_billions >= 100;

This will return all countries with GDP >= 100 Billion USD.

**Technologies Used**
Python 3

pandas, numpy – data manipulation

requests, BeautifulSoup – web scraping

sqlite3 – database management

matplotlib, seaborn – visualization

Author
Maneesh Reddy Yanala
[GitHub](https://github.com/Maneesh3110/)
Passionate about Data Engineering & Application Development
