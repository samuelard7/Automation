from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

header = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    "Accept-Language": 'en-US,en;q=0.9,ar;q=0.8,it;q=0.7,hi;q=0.6'
}

link = requests.get('https://appbrewery.github.io/Zillow-Clone/', headers=header)

content = link.text

soup = BeautifulSoup(content, 'html.parser')

link_for_listing = []
pricing_for_listing = []
address_for_listing = []

linkage = soup.select('.StyledPropertyCardPhotoBody a')
pricing = soup.find_all(name='div', class_='PropertyCardWrapper')
address = soup.find_all('address')

for lin in linkage:
    link_for_listing.append(lin.get('href'))
for name in pricing:
    pricing_for_listing.append(name.getText().strip()[0:6])
for add in address:
    address_for_listing.append(add.getText().strip())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

i = 0
while i < len(link_for_listing):
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSc3v4N-A_iiRiwJk_sJtTWHLN-Rv9faU848plHTL3WPxG8Ueg/viewform?usp=sf_link")
    time.sleep(2)
    address_of_property = driver.find_element(By.XPATH,
                                              value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_of_property = driver.find_element(By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_of_property = driver.find_element(By.XPATH,
                                           value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address_of_property.send_keys(address_for_listing[i])
    price_of_property.send_keys(pricing_for_listing[i])
    link_of_property.send_keys(link_for_listing[i])
    i = i + 1
    submit_button.click()


driver.quit()
