import requests
import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "korede"
GRAPH1 = "graph1"
TOKEN = "hnfjicnednnfkwen"
parameters = dict(token="hnfjicnednnfkwen", username=USERNAME, agreeTermsOfService="yes", notMinor="yes",
                  thanksCode="thanks-code")
graph_config = {
    "id": "graph1",
    "name": "habit",
    "unit": "km",
    "type": "float",
    "color": "ichou"
}

header = {
    "X-USER-TOKEN": TOKEN
}
#create a user
# results = requests.post(url=pixela_endpoint, json=parameters)
# print(results.text)

#create a graph
# graph_definition = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_definition, json=graph_config, headers=header)

dt = datetime.datetime.now()
#convert date to pure string.
today = (dt.strftime("%Y%m%d"))


body = {
    "date": today,
    "quantity": "20"
}

#post on the graph today.
post_ENDPOINT = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1}"
post_graph = requests.post(url=post_ENDPOINT, json=body, headers=header)

# update the graph
update_endpoint2 = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1}/{today}"

request_body = {
    "quantity": input("how many commit did you make today"
)}

response = requests.put(url=update_endpoint2, json=request_body, headers=header)

#delete a request


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1}/{today}"
delete_pixel = requests.delete(url=delete_endpoint, json=request_body, headers=header)
print(delete_pixel.text)