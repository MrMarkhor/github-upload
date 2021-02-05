import requests
import json
URL = "http://127.0.0.1:8000/insert/"

data = {
    'name': 'Abubakar',
    'roll_no': 12,
    'city': 'Gujranwala'
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)