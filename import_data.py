import requests
import json

response = requests.get("https://statsapi.web.nhl.com/api/v1/teams/6/roster")

print("Get request status code: " + str(response.status_code))


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())
