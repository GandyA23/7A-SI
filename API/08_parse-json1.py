# imports
import urllib.parse
import requests

# Variables
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "Put you key here 8))"
url = main_api + urllib.parse.urlencode({"key" : key, "from" : orig, "to" : dest})

# Do request
json_data = requests.get(url).json()

# Print json
print(json_data)
