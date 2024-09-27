import requests

MY_LAT = 20.593683
MY_LNG = 78.962883

parameters = {
    "lat" :MY_LAT,
    "lng" :MY_LNG
}
try:
    respone = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)

    respone.raise_for_status()
except Exception as e:
    raise e
else :
    data = respone.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunset)

# print(respone.json())