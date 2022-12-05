from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import googlemaps

URL_TO_YOUR_GOOGLE_FORM = "https://forms.gle/PNtbfbjUxQ3uyfUX6"

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
    for listing in listings_wrapper.find_all("a",
                                             class_="user-ad-row-new-design link link--base-color-inherit link--hover-color-none link--no-underline"):
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

# TODO Get distance from the address to University
# gmaps = googlemaps.Client(key='Your_API_key')


# TODO Copy data from lists to the form
chrome_driver_path = "C:/Users/adity/Development/chromedriver.exe"  # Path of the Chrome Driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_link)):
    driver.get(URL_TO_YOUR_GOOGLE_FORM)
    time.sleep(2)
    heading_f = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    location_f = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_f = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    listed_date_f = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_f = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # distance_f = driver.find_element_by_xpath(
    #     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    heading_f.send_keys(all_heading[n])
    location_f.send_keys(all_location[n])
    price_f.send_keys(all_price[n])
    listed_date_f.send_keys(all_listed_date[n])
    link_f.send_keys(all_link[n])
    # distance_f.send_keys(all_heading[n])

    submit_button.click()
