import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.inecelectionresults.ng/pres/elections/63f8f25b594e164f8146a213?type=preshttps://www.inecelectionresults.ng/elections/62d1c3bb2cc4ff0df57802d1/context/pus/lga/5f0f39a34d89fc3a883de320/ward/5f0f3e428f77bb3acad0a8bb"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

images = soup.find_all("img")
with open("image_urls.txt", "a") as f:
    for image in images:
        if "src" in image.attrs:
            image_url = urljoin(url, image.attrs["src"])
            f.write(image_url + "\n")
print("successful")