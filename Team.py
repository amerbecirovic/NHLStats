from Player import Player


class Team:
    def __init__(self, name, roster):
        self.name = name
        self.roster = roster
        print("\nTeam: {team_name}\n".format(team_name=self.name))

    def print_roster(self):
        player_names = []
        for player in self.roster:
            player_names.append(player.name)

        sorted_player_names = sorted(player_names)

        i = 1
        print("Roster:\n")
        for sorted_player in sorted_player_names:
            print("{} - {}".format(str(i), sorted_player))
            i += 1

        return sorted_player_names

    def get_player_stats(self, player):
        for player_obj in self.roster:
            player_name = player_obj.name
            if player == player_name:
                print("\n{name}, {age} \n{data}\n".format(name=player_obj.name, age=player_obj.age, data=player_obj.data))


