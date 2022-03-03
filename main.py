from bs4 import BeautifulSoup
import requests
import lxml

web = requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")
website = web.text
soup = BeautifulSoup(website, "lxml")
# print(soup)
all_movies = []
movies = soup.find_all(name="a", class_="xs-text-charcoal decoration-none")
for movie in movies:
    all_movies.append(movie.getText().replace("\xa0", "").replace("\n", ""))
all_movies.pop()

with open("list.txt", mode="w") as content:
    for ele in all_movies:
        content.write(f"{ele}\n")


