from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    "/Users/joycho/.wdm/drivers/chromedriver/mac64/90.0.4430.24/chromedriver"
)
url = "https://www.safeway.com"


def item_url(search_term):
    base_url = "https://www.safeway.com/shop/search-results.html?q={ITEM}"
    search_term = search_term.replace(" ", "+")
    return base_url.replace("{ITEM}", search_term)


url = item_url(sys.argv[1])
driver.get(url)

hsoup = soup(driver.page_source, "html.parser")

products = hsoup.findAll("product-item-v2")

for product in products:
    name = product.select(".product-title")[0].text
    price = product.select(".product-price-qty")[0].text
    print(f"{name}: {price}")
