import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up headers
# Get your User-Agent and Accept-Language from http://myhttpheader.com/
HEADERS = {
    "User-Agent": "",
    "Accept-Language": ""
}


def get_product_price(url):
    try:
        # Send request
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        # Parse HTML content
        soup = BeautifulSoup(response.content, "lxml")

        # Extract the price
        price = soup.select_one('span.aok-offscreen')
        print(price)

        if price:
            # Remove any currency symbols or commas and convert to float
            price_text = price.getText().replace("$", "").replace(",", "")
            logger.info("Price scraped Successfully.")
            return float(price_text)
        else:
            logger.error("Price element not found on the page.")
            return None

    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logger.error(f"An error occurred: {err}")
    return None
