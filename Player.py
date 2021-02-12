import import_data
from import_data import Import


class Player:
    def __init__(self, name):
        self.name = name
        goals = self.get_goals()
        assists = self.get_assists()
        points = self.get_points()
        age = self.get_age()

        print("\n{name}, {age} \n{goals}, {assists}, {points}\n"
              .format(name=self.name, age=age, goals=goals, assists=assists, points=points))

    def get_age(self):
        age = import_obj.player_gap_data[self.name][0]
        return age

    def get_goals(self):
        goals = import_obj.player_gap_data[self.name][1]
        return goals

    def get_assists(self):
        assists = import_obj.player_gap_data[self.name][2]
        return assists

    def get_points(self):
        points = import_obj.player_gap_data[self.name][3]
        return points
