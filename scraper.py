from selectolax.parser import HTMLParser
from cache_request import cache_request
import re
from models import Product


def extract_digits(string) -> float:
    return float(re.sub(r"[^\d.]", "", string))


def parserer(parser: HTMLParser, css_selector: str) -> str:
    return parser.css_first(css_selector).text().strip()


def flipkart_scraper(url: str) -> Product:
    resp = cache_request(url)
    parser = HTMLParser(resp.content)
    product_name = parser.css_first("h1.yhB1nd").text().strip()
    price = extract_digits(parser.css_first("._30jeq3._16Jk6d").text().strip())
    regular_price = extract_digits(parser.css_first("._3I9_wc._2p6lqe").text())
    discount_percentage = extract_digits(
        parser.css_first("._3Ay6Sb._31Dcoz").text().strip()
    )
    rating = extract_digits(parser.css_first("._3LWZlK").text().strip())
    rating_count = extract_digits(
        parser.css_first("._2_R_DZ > span > span:first-child").text().strip()
    )
    reviews_count = extract_digits(
        parser.css_first("._2_R_DZ > span > span:nth-child(3)").text().strip()
    )
    return Product(
        name=product_name,
        price=price,
        regular_price=regular_price,
        discount_percentage=discount_percentage,
        rating=rating,
        rating_count=rating_count,
        reviews_count=reviews_count,
    )
