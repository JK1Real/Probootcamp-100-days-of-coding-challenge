import requests
import datetime as dt


sheety_url = "https://api.sheety.co/05481cd4412a1ee23dfaac8e3aa214f2/myWorkouts/workouts"


today  =dt.datetime.now()


my_app_id = "c6a58e6d"
my_app_key = "f675de18b6b2d22c59b913c0c30fc02d"


end_point = "/v2/natural/exercise"
end_points = f"https://trackapi.nutritionix.com/{end_point}"

headers = {
    "x-app-id":my_app_id,
    "x-app-key":my_app_key
}

work_done = input("What Exercise did you do ?")
parameters = {
    "query": work_done
}

response = requests.post(url=end_points,headers=headers,json=parameters)
response.raise_for_status()
data = response.json()['exercises'][0]

headers = {
    "Authorization": "Basic Sks6SktKS0pLSktKSw=="
}

params = {'workout': 
          {'date': today.date().strftime("%d/%m/%Y"),
                'time': today.time().strftime("%H:%M:%S"),
                  'exercise': data['user_input'],
                    'duration': data['duration_min'],
                      'calories': data['nf_calories'],
                        
                        }
                        }


response1 = requests.post(url=sheety_url, json=params, headers=headers)
print(response1.raise_for_status())
print(response1.json())