from Player import Player
import import_data


class Team:
    def __init__(self, name):
        self.name = name
        self.roster = self.get_roster()
        self.venue = self.get_venue()
        self.conference = self.get_conference()

    def get_roster(self):
        roster = []
        for name in import_data.self.roster_gap_data.keys():
            roster.append(name)
        return roster

    def get_venue(self):
        pass

    def get_conference(self):
        pass

    def get_division(self):
        pass
