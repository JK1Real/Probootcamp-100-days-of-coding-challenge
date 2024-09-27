
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_url = "https://api.sheety.co/05481cd4412a1ee23dfaac8e3aa214f2/flightDeals/prices"

    def sheety_read_data(self):
        response = requests.get(url=self.sheety_url)
        print(response.raise_for_status())
        print(response.json())



data_manager = DataManager()

data_manager.sheety_read_data()


