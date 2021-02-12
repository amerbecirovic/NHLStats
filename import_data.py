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
    return player_ids


roster_dict = create_dict(json.dumps(response.json()))
player_ids = get_player_ids(roster_dict)


def get_player_data(ids):
    player_list = []
    for id in ids:
        player_request = requests.get("https://statsapi.web.nhl.com/api/v1/people/" + str(id) + "?hydrate=stats("
                                                                                                "splits=statsSingleSeason)")
        player_list.append(create_dict(json.dumps(player_request.json())))
    return player_list


player_data = get_player_data(player_ids)

# function to get goals, assists, points, and age for each skater on the roster, in the form of:
# {"Player Name": [Age: W, Goals: X, Assists: Y, Points: Z]}
# separate function for goalies

def get_gap_data_skaters(player_list):
    gap_data = {}

    for i in range(0, len(player_list)):

        position_code = player_list[i]['people'][0]['primaryPosition']['code']
        player_name = player_list[i]['people'][0]['fullName']
        age = player_data[i]['people'][0]['currentAge']

        if position_code != "G":
            try:
                player_data[i]['people'][0]['stats'][0]['splits'][0]['stat']['points']
                goals = player_data[i]['people'][0]['stats'][0]['splits'][0]['stat']['goals']
                assists = player_data[i]['people'][0]['stats'][0]['splits'][0]['stat']['assists']
                points = player_data[i]['people'][0]['stats'][0]['splits'][0]['stat']['points']
                # print(position_code)
                # print(goals)
                gap_data[player_name] = ["Age: " + str(age), "Goals: " + str(goals), "Assists: " + str(assists), "Points: " + str(points)]
            except IndexError:
                gap_data[player_name] = ["Goals: N/A", "Assists: N/A", "Points: N/A"]

    # print(gap_data)
    return gap_data


roster_gap_data = get_gap_data_skaters(player_data)
