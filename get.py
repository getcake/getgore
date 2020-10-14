##########################################
#  Downloads videos from bestgore.com
#  by getcake (https://github.com/getcake)
##########################################

from bs4 import BeautifulSoup
from random import randint as ri
import requests

link = input("Enter the link of the vide you wish to download\n> ")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
}
page_resp = requests.get(link, headers=headers)
soup = BeautifulSoup(page_resp.text, "lxml")
main = soup.find("div", class_="entry-content")
e = main.find("iframe")["src"]
e_resp = requests.get(e)
e_soup = BeautifulSoup(e_resp.text, "lxml")
e_link = e_soup.find("video").source["src"]
e_link_resp = requests.get(e_link, stream=True)

try:
    name = "video{}.mp4".format(str(ri(1, 42069)))
    with open(name, "wb") as v:
        for chunk in e_link_resp.iter_content(chunk_size=1024*1024):
            if chunk:
                v.write(chunk)
    print("Completed")

except Exception as e:
    print("Error downloading file")
    pass
