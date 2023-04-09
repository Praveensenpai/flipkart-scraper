from models import product_inserter
from scraper import flipkart_scraper


if __name__ == "__main__":
    url = "https://www.flipkart.com/motorola-g62-5g-midnight-gray-128-gb/p/itm88e51821facb9"
    product = flipkart_scraper(url=url)
    product_inserter(product)
