# 3rd party API
import requests
import json
URL  ="http://127.0.0.1:8000/student_create/"
data = {
    'name': 'sadik',
    'roll': '119624',
    'city': 'Dhaka',
}
json_data = json.dumps(data)

res = requests.post(url=URL, data=json_data)
data = res.json()
print(data)