import import_data
from import_data import Import
from Player import Player
from Team import Team


# get all 31 teams in dictionary form {Team: NHL API ID} from import_data to preserve ID numbers for API access.
# Create and print sorted list to console as pick list, alphabetical for ease of use.
def init_teams():
    teams_unsorted = import_data.get_all_teams()
    teams_sorted = sorted(teams_unsorted)
    i = 1
    for sorted_team in teams_sorted:
        print("{} - {}".format(str(i), sorted_team))
        i += 1
    return teams_unsorted, teams_sorted


# initialize the Team and Players(roster) for the selected team.
def init_roster(team_number):
    # match the selected team/ team number from the user, to the unsorted dictionary
    selected_team = sorted_teams[team_number]
    team_id = unsorted_teams[selected_team]

    # new Import object for team selected, use Team method print_roster() to print the roster.
    import_obj = Import(team_id)
    team = import_obj.create_team()
    sorted_roster = team.print_roster()

    # turn the roster into a dictionary so we can match the user's selection to a name.
    roster_dict = {}
    i = 1
    for player in sorted_roster:
        roster_dict[i] = player
        i += 1

    return roster_dict, team


def get_player(player_number):
    player_name = roster_dict[player_number]
    try:
        team.get_player_stats(player_name)
        again = input("Would you like to see stats for another player? Enter 'y/n': ")
        if again == 'y':
            team.print_roster()
            new_player = input("\nSelect another player number: ")
            get_player(int(new_player))
        elif again == 'n':
            return

    except KeyError:
        new_input = input("\nNumber invalid. Enter 'Exit' to exit, or try another player: ")
        if new_input == "Exit" or new_input == "exit":
            return
        else:
            get_player(int(new_input))


unsorted_teams, sorted_teams = init_teams()
select_team = input("\nPlease choose a team's corresponding number: ")

roster_dict, team= init_roster(int(select_team) - 1)

select_player = input("\nPlease choose a player's corresponding number: ")
get_player(int(select_player))
