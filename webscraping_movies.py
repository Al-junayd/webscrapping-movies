import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = 'top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0 
released_in_2000_file_path = "20000s.csv"

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')
print(data)

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

print(df)
df.to_csv(csv_path)

# ----------------

# Convert Year column to numeric to handle filtering
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Filter the DataFrame to include only films released in the 2000s
df_2000s = df[(df['Year'] >= 2000) & (df['Year'] < 2010)]

print(df_2000s)

# Save the filtered DataFrame to CSV
df_2000s.to_csv(released_in_2000_file_path, index=False)

# ----------------



conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()