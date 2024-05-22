import requests
import smtplib
from bs4 import BeautifulSoup

my_email = "samuelrichard214@gmail.com"
password = "ebsv xtyp eeuc pufg"
recipients = "samuelard715@outlook.com"

al = 'en-US,en;q=0.9,ar;q=0.8,it;q=0.7,hi;q=0.6'
ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
headers = {'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8,it;q=0.7,hi;q=0.6',
           'User-Agent': ua,
           'Accept-Encoding': 'gzip, deflate, br, zstd',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}
print('')
r = requests.get(
    "https://www.amazon.in/gp/product/B09DQ14SGN/ref=ox_sc_saved_title_1?smid=A1KZF5U9TFFWBZ&psc=1", headers=headers
)

contents = r.text

soup = BeautifulSoup(contents, 'html.parser')

price = soup.find(name='span', class_='a-price-whole').getText()
print(price)

v = price.replace(',', "")

savings = 2209 - float(v)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    if float(v) < 2209:
        connection.sendmail(from_addr=my_email, to_addrs=recipients,
                            msg=f"Subject:Alert On US Polo Shoes\n\n Price is Rs.{price} Buy Now! You are saving Rs.{savings}")
    else:
        connection.sendmail(from_addr=my_email, to_addrs=recipients,
                            msg=f"Subject:US Polo Shoes\n\n Price is Rs.{price}.")
