import requests
from bs4 import BeautifulSoup
def ravnica_scrape():
    html_page = requests.get("https://ravnicabg.rs/shop/")
    page_number = 1
    while html_page.status_code == 200:
        soup = BeautifulSoup(html_page.content, 'html.parser')
        game_names = soup.select(".woocommerce-loop-product__title")
        game_prices = soup.select(".woocommerce-Price-amount")
        for index, name in enumerate(game_names):
            print(name.text, game_prices[index].text)
        page_number += 1
        html_page = requests.get(f"https://ravnicabg.rs/shop/page/{page_number}/")