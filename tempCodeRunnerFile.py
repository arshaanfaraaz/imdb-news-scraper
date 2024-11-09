import requests 
from bs4 import BeautifulSoup 


def scrape_imdb_news(): 
    url = "https://m.imdb.com/news/top/"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/91.0.4472.124 Safari/537.36"
}
    response = requests.get(url)
    print(response)