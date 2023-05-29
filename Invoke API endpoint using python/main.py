#pip3 install requests 
#if you don't have requests installed

import requests

URL = "https://ovnig9ruq1.execute-api.us-east-1.amazonaws.com/Dev/invoke"
# header
headers = {"Content-Type": "application/json"}
# querystring parameter
params = {"qs":"value"}
# payload
data = {"payload":"payload"}

#response
#r = requests.request("GET", URL, params = params, headers = headers) # (GET method)
#r = requests.request("POST", URL, headers = headers, data= data) # (POST method)
r = requests.request("DELETE", URL) # (DELETE method)
#Check response
print(r.text)