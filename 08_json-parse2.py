import urllib.parse
import requests

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Kyiv"
dest = "Kharkiv"
key = "EYpPUZU66ho8FCpwUSv2WnwKZM2A42Pj"

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})

# Print the constructed URL
print("URL: " + url)

# Parse the JSON data and get the status code
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

# Print the status code and a message if the request is successful
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")