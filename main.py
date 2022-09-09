import smtplib

import requests
import lxml
from bs4 import BeautifulSoup


SMTP_ADDRESS = 'smtp.gmail.com'
BUY_PRICE = 930
EMAIL = 'anhthuanzw@gmail.com'
PASSWORD = 'lukaku20'

url = "https://www.amazon.ca/dp/B09R8ZNJY1/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=cf0c1ba2321e01011d538c09615dee04&content-id=amzn1.sym.2391ded4-5342-4a72-ab16-54835c13e968%3Aamzn1.sym.2391ded4-5342-4a72-ab16-54835c13e968&hsa_cr_id=1503537800801&pd_rd_plhdr=t&pd_rd_r=3e0da02b-ff88-4823-aaa8-83f4145cdcf1&pd_rd_w=KZc9Z&pd_rd_wg=RAbgo&qid=1662693846&ref_=sbx_be_s_sparkle_mcd_asin_0_img&sr=1-1-a094db1c-5033-42c6-82a2-587d01f975e8"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="apex_desktop").get_text()
price_without_currency = float(price.split("$")[1])
print(price_without_currency)

if price_without_currency < BUY_PRICE:
    message = f"{title} is now price"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login("anhthuanzw@gmail.com", 'lukaku20')
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f'Subject: Amazon Price Alert!\n\n{message}\n{url}'
        )
