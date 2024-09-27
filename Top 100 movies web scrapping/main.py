import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)
contents = response.content

soup = BeautifulSoup(contents, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movie_list = [movie.text for movie in movies]

print(movie_list)


with open(file="Movie list.txt", mode="a") as file:
    for movie in movie_list[::-1]:
        file.write(f"{movie}\n")
