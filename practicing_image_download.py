import requests
from bs4 import BeautifulSoup

#link download.
response = requests.get("https://www.youtube.com/watch?v=fJN-HEM-cjw")


bsoup = BeautifulSoup(response.text,'html.parser')

all_links = bsoup.findAll('a')

for link in all_links:
    print(link.get('href'))