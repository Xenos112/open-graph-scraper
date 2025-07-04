import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from pydantic import BaseModel


class Body(BaseModel):
    url: str = ""

app = FastAPI()


@app.post("/")
def load(body: Body):
    data = {"image": "", "title": "", "description": ""}

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }

    res = requests.get(body.url,headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    og_image = soup.find("meta", property="og:image")
    og_description = soup.find("meta", property="og:description")

    if og_image:
        data["image"] = og_image["content"]

    if og_description:
        data["description"] = og_description["content"]

    if soup.title.strin:
        data["title"] = soup.title.string

    print(data)
    return data
