
#new
#akn amra data ke update korbo
import requests
import json

URL ="http://127.0.0.1:8000/student-api/" # aita use korci amra class based view ar jnno


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url = URL, data =json_data)
    data = res.json()
    print(data)
# get_data(1)

#amra toh age GET request ar jnno likhci akn amara POST method dekhbo 
def post_data():
#   if id is not None:
    data = {
        'name':'sadik',
        'roll':150,
        'city':'ctg',
    } 
    json_data = json.dumps(data)
    res = requests.post(url = URL, data =json_data)
    data = res.json()
    print(data)

post_data()

#partial update korlam ar ai jnno amara akn a PUT use korlam ar ai code partial ba data update ar jnno

def update_data():
    # amara akn a amar data ke update korte chai
    data={
        'id':2, #amra je data ta ke upate korte chai tar id nibo
        'name': 'Jiniya', #akn je data ta ke update korbo tar nam dibo 
        'city':'Rajshahi',
    }
    json_data = json.dumps(data)
    res = requests.put(url = URL, data=json_data) # amra akn a data ta ke update korbo tai 
    data = res.json()
    print(data)
# 
#data delete ar jnno
def delete_data():
    data = {
        'id': 2,
    }
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data= json_data)
    data = res.json()
    print(data) 
