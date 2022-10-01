import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls055386972/"

response = requests.get(url, headers={"Accept-Language": "en"})
soup = BeautifulSoup(response.content, "html.parser")

movies_html = soup.find_all(class_="lister-item-content")

for movie_html in movies_html[0:5]:
    title = movie_html.a.text
    duration = int(movie_html.find(class_="runtime").text.strip(" min"))

    movie = {"title": title, "duration": duration}
    print(movie)
