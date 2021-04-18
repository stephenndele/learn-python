import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
# print the data to see the keys and values
# print('json') 
print("The niggas in space are:\n")

for person in json['people']:
    print(person['name'])