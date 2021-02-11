import requests
import json

response = requests.get("https://statsapi.web.nhl.com/api/v1/teams/6/roster")

print("Get request status code: " + str(response.status_code))


def create_dict(obj):
    # create a Python dictionary of the json roster data
    raw_roster_data = json.loads(obj)
    # print(raw_roster_data)
    return raw_roster_data


# Isolate all player ids from the json data
def get_player_ids(roster_data):
    roster_count = len(roster_data['roster'])
    player_ids = []
    for i in range(0, roster_count):
        player_ids.append(roster_data['roster'][i]['person']['id'])
    print(player_ids)
    return player_ids


roster_dict = create_dict(json.dumps(response.json()))
player_ids = get_player_ids(roster_dict)


def get_player_data(ids):
    player_list = []
    for id in ids:
        player_request = requests.get("https://statsapi.web.nhl.com/api/v1/people/" + str(id) + "?hydrate=stats("
                                      "splits=statsSingleSeason)")
        player_list.append(create_dict(json.dumps(player_request.json())))

    print(player_list)
    return player_list



player_data = get_player_data(player_ids)

# just Kase
# print(roster_dict['roster'][0]['person']['id'])
# print(roster_dict)
# print(len(roster_dict['roster']))
