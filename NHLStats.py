import import_data
from import_data import Import


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


# function to list the roster from the selected team as a pick list.
def list_roster(team_number):
    # match the selected team/ team number from the user, to the unsorted dictionary
    selected_team = sorted_teams[team_number]
    team_id = unsorted_teams[selected_team]

    # new Import object for team selected
    import_obj = Import(team_id)
    roster_dict = import_obj.player_gap_data

    roster_sorted = sorted(roster_dict)
    printed_roster = []
    i = 1
    for player in roster_sorted:
        printed_roster.append("{} - {}".format(str(i), player))
        i += 1

    for player in printed_roster:
        print(player)

    return roster_sorted, import_obj, printed_roster


def get_player(player_number):
    player_name = sorted_roster[player_number]
    try:
        player_data = gap_data[player_name]
        print("\n{name}, {age} \n{goals}, {assists}, {points}\n"
              .format(name=player_name, age=player_data[0], goals=player_data[1], assists=player_data[2],
                      points=player_data[3]))
        while True:
            again = input("Would you like to see stats for another player? Enter 'y/n': ")
            if again == 'y':
                for player in printed_roster:
                    print(player)
                new_player = input("\nSelect another player number: ")
                get_player(int(new_player) - 1)
            elif again == 'n':
                break
            else:
                print("\nInvalid entry. Try again.\n")
                continue

    except KeyError:
        new_input = input("\nNumber invalid. Enter 'Exit' to exit, or try another player: ")
        if new_input == "Exit" or new_input == "exit":
            return
        else:
            get_player(int(new_input) - 1)


# list_roster(select_team)
# get_player(enter_name)

unsorted_teams, sorted_teams = init_teams()
select_team = input("\nPlease choose a team's corresponding number: ")

sorted_roster, import_obj, printed_roster = list_roster(int(select_team) - 1)
gap_data = import_obj.player_gap_data

select_player = input("\nPlease choose a player's corresponding number: ")
get_player(int(select_player) - 1)
