import requests
from bs4 import BeautifulSoup

url = "https://www.lewagon.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

print(soup.find("h1").text)
print(soup.h1.text)
