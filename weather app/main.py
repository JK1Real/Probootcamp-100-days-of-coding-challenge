import requests
import smtplib
from email.message import EmailMessage

my_email ="thisisnotallowed384@gmail.com"
my_password = "nvac rskh sale yvmm"


msg = EmailMessage()
msg["Subject"] = "Rain"
msg.set_content("Bring a umbrella")

api_key = "85f365ed35a59926ae2400b7661e5a29"

lat = 10.850516
lon = 76.271080

url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'cnt':4,
}


response = requests.get(url=url, params=parameters)
print(response.raise_for_status)

weather_data = response.json()
lenght = len(weather_data['list'])

will_rain = False
for id_number in range(0, lenght):
    id_code = weather_data['list'][id_number]['weather'][0]['id']
    print(id_number,id_code)
    if id_code<700:
        will_rain=True

with smtplib.SMTP("smtp.gmail.com") as message:
    message.starttls()
    message.login(user=my_email, password=my_password)
    
    if will_rain:
        message.send_message(msg=msg, from_addr=my_email, to_addrs=my_email)