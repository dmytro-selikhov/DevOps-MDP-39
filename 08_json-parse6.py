import urllib.parse
import requests

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "EYpPUZU66ho8FCpwUSv2WnwKZM2A42Pj"
unit = "k"
locale = "ru_RU"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + \
        urllib.parse.urlencode(
            {"key": key, "from": orig, "to": dest, "unit": unit, "locale": locale})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) +
              " = A successful route call.\n")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
        print("Kilometers:      " +
              str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("\n")
        print("=" * 40)
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" +
                  str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    else:
        print("API status: " + str(json_status) + ". " +
              json_data["info"]["messages"][0] + "\n")
