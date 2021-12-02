# imports
import urllib.parse
import requests

# Variables
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Put you key here 8))"

# Functions

"""
    Check if input is an option for exit
"""
def exitloop (input):
    return input == "quit" or input == "q"

# Main
while True:
    # Input origin and destination
    orig = input("Starting Location: ")
    
    # Check input
    if exitloop(orig) :
        break
    
    dest = input("Destination: ")
    
    # Check input
    if exitloop(dest) :
        break
    
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    # Do request
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    # Check status
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")