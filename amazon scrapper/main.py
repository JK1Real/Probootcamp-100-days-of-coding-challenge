from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

user_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
accept_language = "en-US,en;q=0.9,ml;q=0.8"
FORWARDED_IPS = [
    "203.0.113.1",
    "198.51.100.14",
    "192.0.2.45",
    "203.0.113.78",
    "198.51.100.89",
    "192.0.2.34",
]
headers={
    "User-Agent":user_Agent,
    "Accept-Language":accept_language,
    "X-Forwarded-For": FORWARDED_IPS[0]
}
response = requests.get(url=url, headers=headers)
print(response.raise_for_status)
content = response.content


soup= BeautifulSoup(content, "lxml")

price = soup.find(class_="a-offscreen")
print(price)
