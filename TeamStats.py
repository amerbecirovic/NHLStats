import import_data
import requests
import json


class TeamStats:
    def __init__(self, team_name):
        self.team_name = team_name
        self.team_id = self.get_team_id()
        self.team_stats = self.create_dict()
        self.shooting_pct = self.get_shooting_pct()
        self.save_pct = self.get_save_pct()
        # self.exgoals = self.get_exgoals()
        self.pp_pct = self.get_pp_pct()
        self.pk_pct = self.get_pk_pct()
        # print("\nStatistics for {team_name}:\n\nShooting Percentage: {shot_pct}\nSave Percentage: {save_pct}"
             # "\nPower Play Percentage: {pp_pct}\nPenalty Kill Percentage: {pk_pct}".format
              # (team_name=self.team_name,shot_pct=self.shooting_pct,save_pct=self.save_pct,
              # pp_pct=self.pp_pct,pk_pct=self.pk_pct))

    def get_team_id(self):
        all_teams = import_data.get_all_teams()
        return all_teams[self.team_name]

    def create_dict(self):
        # create a Python dictionary of json data
        response = requests.get("https://statsapi.web.nhl.com/api/v1/teams/" + str(self.team_id) + "/stats")
        raw_data_dict = json.loads(json.dumps(response.json()))
        return raw_data_dict

    def get_shooting_pct(self):
        return self.team_stats['stats'][0]['splits'][0]['stat']['shootingPctg']

    def get_save_pct(self):
        return self.team_stats['stats'][0]['splits'][0]['stat']['savePctg']

    def get_exgoals(self):
        pass

    def get_pp_pct(self):
        return self.team_stats['stats'][0]['splits'][0]['stat']['powerPlayPercentage']

    def get_pk_pct(self):
        return self.team_stats['stats'][0]['splits'][0]['stat']['penaltyKillPercentage']


