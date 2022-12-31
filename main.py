import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features"
                            "/best-movies-2/")

movies = response.text

soup = BeautifulSoup(movies, "html.parser")
first_movie = soup.find_all(name="h3", class_="title")
movies_list = [movie.get_text() for movie in first_movie]

movies_list.reverse()

with open("Movies.txt", "a", encoding="utf-8") as file:
    for movies in movies_list:
        file.write(f"{movies}\n")













