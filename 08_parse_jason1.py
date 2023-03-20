import urllib.parse
import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Kyiv"
dest = "Kharkiv"
key = "EYpPUZU66ho8FCpwUSv2WnwKZM2A42Pj"

url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})

json_data = requests.get(url).json()
print("Url: \n" + url + "\n")
print(json_data)
