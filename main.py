import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
from etl import extract, transform, load_to_csv, load_to_db, run_query, log_progress

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country", "GDP_USD_millions"]
db_name = './outputs/World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = './outputs/Countries_by_GDP.csv'
plot_path = './outputs/top10_gdp.png'

log_progress('Starting ETL process')

df = extract(url, table_attribs)
log_progress('Data extraction complete.')

df = transform(df)
log_progress('Data transformation complete.')

load_to_csv(df, csv_path)
log_progress('Data saved to CSV file.')

sql_connection = sqlite3.connect(db_name)
log_progress('SQL connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database.')

query_statement = f"SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100"
query_output = run_query(query_statement, sql_connection)
log_progress('Query executed successfully.')

# Visualization
top10 = df.sort_values(by="GDP_USD_billions", ascending=False).head(10)
sns.barplot(data=top10, x="GDP_USD_billions", y="Country", palette="Blues_d")
plt.title("Top 10 Economies by GDP (Billions USD)")
plt.tight_layout()
plt.savefig(plot_path)
plt.show()

log_progress('Process complete.')
sql_connection.close()
