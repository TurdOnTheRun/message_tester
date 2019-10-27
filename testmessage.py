# importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://127.0.0.1:8000/deletelater/json"
TEAM = 'team3'


while True:
    text = input("Enter a message: ")
    PARAMS = {'text':text, 'team': TEAM} 
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    print (data['result'])