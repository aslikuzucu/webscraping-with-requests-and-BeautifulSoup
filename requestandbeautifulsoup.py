import requests

from bs4 import BeautifulSoup

url = "https://www.obilet.com/seferler/382-429/2023-03-30"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

print(soup.find_all("div", {"class": "partner col"}))







