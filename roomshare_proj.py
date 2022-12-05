from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(
    "https://www.gumtree.com.au/s-flatshare-houseshare/adelaide/c18294l3006878?sort=price_asc&price=__200.00",
    headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link = []
all_heading = []
all_price = []
all_location = []
all_listed_date = []
for listings_wrapper in soup.find_all("div", class_="user-ad-collection-new-design__wrapper--row"):
    for listing in listings_wrapper.find_all("a", class_="user-ad-row-new-design link link--base-color-inherit link--hover-color-none link--no-underline"):
        # Getting the Link, Heading, Price, Location, Listed Date from the Webpage
        link = listing.get("href")
        heading, price, third = listing.get("aria-label").split("\n")
        location, listed_date = third.split(". Ad listed ")
        # Storing them in a list after some basic data cleaning using slicing
        all_link.append(f"https://www.gumtree.com.au{link}")
        all_heading.append(heading[:-2])
        all_price.append(price[16:-1])
        all_location.append(location[18:])
        all_listed_date.append(listed_date[:-1])


print(all_heading)
print(all_location)
print(all_price)
print(all_listed_date)
print(all_link)