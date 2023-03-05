# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import requests
# import io
# from PIL import Image

# PATH = "C:\\Users\\DELL\\instant-deposit-intenship\\chromedriver.exe"
# service = Service(PATH)

# wd = webdriver.Chrome(service=service)

# image_url = "https://unnportal.unn.edu.ng/Modules/Applications/PUTME/PUTMEResults/PUTMEResultSlip.aspx?sent=741E07CD0EEF481A944381913F4F0FD5"

# def download_image(download_path, url, file_name):
#     image_content = requests.get(url).content
#     image_file = io.BytesIO(image_content)
#     image = Image.open(image_file)
#     file_path = download_path + file_name

#     with open(file_path, "wb") as f:
#         image.save(f, "JPEG")

#     print("successful")

# download_image("", image_url, "result.jpg")


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import requests
# import io
# from PIL import Image

# PATH = "C:\\Users\\DELL\\instant-deposit-intenship\\chromedriver.exe"
# service = Service(PATH)

# wd = webdriver.Chrome(service=service)

# image_urls = [
#     "https://unnportal.unn.edu.ng/Modules/Applications/PUTME/PUTMEResults/PUTMEResultSlip.aspx?sent=741E07CD0EEF481A944381913F4F0FD5",
#     "https://example.com/image2.jpg",
#     "https://example.com/image3.jpg"
# ]

# def download_images(download_path, urls):
#     for i, url in enumerate(urls):
#         image_content = requests.get(url).content
#         image_file = io.BytesIO(image_content)
#         image = Image.open(image_file)
#         file_path = download_path + f"result_{i}.jpg"

#         with open(file_path, "wb") as f:
#             image.save(f, "JPEG")

#         print(f"Successfully downloaded {file_path}")

# download_images("", image_urls)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import io
from PIL import Image

PATH = "C:\\Users\\DELL\\instant-deposit-intenship\\chromedriver.exe"
service = Service(PATH)

wd = webdriver.Chrome(service=service)

# read image urls from text file
with open("image_urls.txt", "r") as f:
    image_urls = f.read().splitlines()

def download_images(download_path, urls):
    for i, url in enumerate(urls):
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + f"result_{i}.jpg"

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print(f"Successfully downloaded {file_path}")

download_images("", image_urls)