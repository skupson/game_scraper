from urllib.error import HTTPError
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def conflux_scrape():
    try:
        site = "https://www.conflux.rs//drustvene-igre"
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        game_names = soup.select(".main-products-wrapper .name a")
        game_prices = soup.select(".main-products-wrapper .price")
        page_number = 1
        while 1:
            for index, name in enumerate(game_names):
                print(name.text, game_prices[index].text)
            site = f"https://www.conflux.rs//drustvene-igre?page={page_number}"
            hdr = {'User-Agent': 'Mozilla/5.0'}
            req = Request(site, headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page, 'html.parser')
            game_names = soup.select(".main-products-wrapper .name a")
            game_prices = soup.select(".main-products-wrapper .price")
            page_number += 1
    except HTTPError:
        return 0