import requests
import datetime as dt


today = dt.datetime(year=2024, month=5, day=13)
print(today.strftime("%Y%m%d"))

pixela_end_point = "https://pixe.la/v1/users" 

user_name = "magicuser"
token = "thisissecret"

parameters = {"token":token,
                "username":user_name,
                "agreeTermsOfService":"yes",
                "notMinor":"yes"}


# response = requests.post(url=pixela_end_point, json=parameters)
# print(response.text)

pixela_graph_end_point = f"{pixela_end_point}/{user_name}/graphs"

params = {"id":"test-graph",
          "name":"cycling graph",
          "unit":"Km",
          "type":"float",
          "color":"shibafu"}

headers = {
    "X-USER-TOKEN":token
}
# response1 = requests.post(url=pixela_graph_end_point, json=params, headers=headers)
# print(response1.text)

post_value_graph_end_point = f"{pixela_graph_end_point}/test-graph"

params1 = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"21"
}

# response2 = requests.post(url=post_value_graph_end_point, json=params1, headers=headers)
# print(response2.text)
para = {
    "quantity":"50"
}

# response = requests.put(url=f"{post_value_graph_end_point}/{today.strftime('%Y%m%d')}", headers=headers, json=para)
# print(response.text)

response3 = requests.delete(url=f"{post_value_graph_end_point}/{today.strftime('%Y%m%d')}", headers=headers)
print(response3.text)