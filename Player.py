
class Player:
    def __init__(self, name, age, data):
        self.name = name
        self.age = age
        self.data = data

    def get_age(self):
        return self.age

    def get_goals(self):
        return self.data[0]

    def get_assists(self):
        return self.data[1]

    def get_points(self):
        return self.data[2]
