import requests
from bs4 import BeautifulSoup
import random
# Define parameters provided by Brightdata
host = 'brd.superproxy.io'
port = 22225
username = 'brd-customer-hl_65585269-zone-web_unlocker1'
password = 't3relsszkw5p'
session_id = random.random()

# Function to scrape product prices from a URL
def scrape_price(url, proxies):
    try:
        response = requests.get(url, proxies=proxies)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Modify these selectors according to the structure of the website
        price_element = soup.find('span', class_='product-price')
        if price_element:
            return float(price_element.text.strip().replace('$', '').replace(',', ''))
        else:
            print(f"No price found for {url}")
            return None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# List of URLs to scrape
urls = ['https://www.amazon.ca/', 'https://www.walmart.ca/en',]

# Format your proxy
proxy_url = ('http://{}-session-{}:{}@{}:{}'.format(username, session_id, password, host, port))

# Define your proxies in dictionary
proxies = {'http': proxy_url, 'https': proxy_url}

# Scrape prices for each URL
prices = {}
for url in urls:
    price = scrape_price(url, proxies)
    if price is not None:
        prices[url] = price

# Find the cheapest price and URL
if prices:
    cheapest_url = min(prices, key=prices.get)
    cheapest_price = prices[cheapest_url]

    # Print the cheapest price and URL
    print(f"The cheapest price is ${cheapest_price} at URL: {cheapest_url}")
else:
    print("No prices found for the given URLs.")