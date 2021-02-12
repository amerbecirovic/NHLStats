import requests
import json


def get_all_teams():
    raw_data = []
    teams = {}
    for i in range(0, 31):
        response = requests.get("https://statsapi.web.nhl.com/api/v1/teams/")
        raw_data.append(create_dict(response))
        teams[raw_data[0]['teams'][i]['name']] = raw_data[0]['teams'][i]['id']
    return teams
    # print("Get request status code: " + str(response.status_code))


def create_dict(response):
    # create a Python dictionary of json data
    raw_data_dict = json.loads(json.dumps(response.json()))
    return raw_data_dict


class Import:
    def __init__(self, team_number):
        self.team = team_number
        self.player_ids = self.get_player_ids()
        self.player_data = self.get_player_data()
        self.player_gap_data = self.get_gap_data_skaters()
        # print(self.player_gap_data)

    # Isolate all player ids from the json data
    def get_player_ids(self):
        roster_request = requests.get("https://statsapi.web.nhl.com/api/v1/teams/" + str(self.team) + "/roster")
        roster_data = create_dict(roster_request)
        roster_count = len(roster_data['roster'])
        player_ids = []
        for i in range(0, roster_count):
            player_ids.append(roster_data['roster'][i]['person']['id'])
        return player_ids

    # Get the individual player data based on a list of all player IDs on the roster.
    def get_player_data(self):
        ids = self.player_ids
        player_list = []
        for id in ids:
            player_request = requests.get("https://statsapi.web.nhl.com/api/v1/people/" + str(id) + "?hydrate=stats("
                                                                                                    "splits=statsSingleSeason)")
            player_list.append(create_dict(player_request))
        return player_list

    # function to get goals, assists, points, and age for each skater on the roster, in the form of:
    # {"Player Name": [Age: W, Goals: X, Assists: Y, Points: Z]}
    # separate function for goalies

    def get_gap_data_skaters(self):
        player_list = self.player_data
        gap_data = {}

        for i in range(0, len(player_list)):

            position_code = player_list[i]['people'][0]['primaryPosition']['code']
            player_name = player_list[i]['people'][0]['fullName']
            age = player_list[i]['people'][0]['currentAge']

            if position_code != "G":
                try:
                    player_list[i]['people'][0]['stats'][0]['splits'][0]['stat']['points']
                    goals = player_list[i]['people'][0]['stats'][0]['splits'][0]['stat']['goals']
                    assists = player_list[i]['people'][0]['stats'][0]['splits'][0]['stat']['assists']
                    points = player_list[i]['people'][0]['stats'][0]['splits'][0]['stat']['points']
                    # print(position_code)
                    # print(goals)
                    gap_data[player_name] = ["Age: " + str(age), "Goals: " + str(goals), "Assists: " + str(assists),
                                             "Points: " + str(points)]
                except IndexError:
                    gap_data[player_name] = ["Goals: N/A", "Assists: N/A", "Points: N/A"]

        return gap_data


