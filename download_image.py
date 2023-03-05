import requests
from wand.image import Image

url = 'https://www.inecelectionresults.ng/elections/62d1c3bb2cc4ff0df57802d1/pu/62d1c3d92cc4ff0df5780d47/document'

response = requests.get(url)

with Image(blob=response.content, resolution=300) as img:
    img.format = 'png'
    img.save(filename='result.png')
