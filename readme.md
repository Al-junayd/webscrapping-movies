## 1. Movies Webscrapping

# 1.1 Objectives:

1. Use the requests and BeautifulSoup libraries to extract the contents of a web page

2. Analyze the HTML code of a webpage to find the relevant information

3. Extract the relevant information and save it in the required form

# 1.2 Installation:

1. Run the following commands

```
 python3.11 -m pip install pandas
 python3.11 -m pip install bs4
```

# 1.3 Scenario

Consider that you have been hired by a Multiplex management organization to extract the information of the top 50 movies with the best average rating from the web link shared below.

https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films

1. The information required is `"Average Rank"`, `"Film"`, and `"Year"`.

# 1.4 Steps

You are required to write a:

1. Python script webscraping_movies.py that extracts the information and
2. Saves it to a CSV file top_50_films.csv.
3. Save the same information to a database Movies.db under the table name Top_50.
4. Filter the output to print only the films released in the 2000s (additional task for more practice)
