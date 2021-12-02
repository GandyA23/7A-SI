# imports
import urllib.parse
import requests

# Variables
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "Put you key here 8))"
url = main_api + urllib.parse.urlencode({"key" : key, "from" : orig, "to" : dest})

print("URL: " + (url))

# Do request
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

# Check status
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")