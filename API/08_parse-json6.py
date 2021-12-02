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
        # Print specified info
        print("API Status:      " + str(json_status) + " = A successful route call.\n")
        print("Directions from  " + (orig) + " to " + (dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))

        # Convert the distance and fuelUsed values to the metric system.
        print("Kilometers:      " + str("{:.2f}".format(json_data["route"]["distance"] * 1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format(json_data["route"]["fuelUsed"] * 3.78)))
        
        # Iterate maneuvers
        print("\n=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print("\t- " + (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")