import import_data
from import_data import Import

from TeamStats import TeamStats

from numpy import random
from numpy import std
from numpy import mean

import matplotlib.pyplot as plt
import seaborn as sns

import pickle


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


'''
unsorted_teams, sorted_teams = init_teams()
select_team = input("\nPlease choose a team's corresponding number: ")

roster_dict, team = init_roster(int(select_team) - 1)

select_player = input("\nPlease choose a player's corresponding number: ")
get_player(int(select_player))
'''

'''
start of creating an algorithm to predict game winners. algorithm will be some combo of save percentage, 
expected goals, special team rankings, and shooting percentage. normal distributions best way to go.
easy math. All matchups for the night will be displayed. The format will be something like:
XX% Team 1 vs Team 2 YY% where XX% and YY% are their respective chances to win based on the below function.
'''


# First, need to get ALL teams data for each statistic. Turn each statistic into a normal distribution
# for the league.


def normal_distributions():
    # create a dictionary for storage of team stats for each team. Form of "Team Name": [Stats]
    # commented out for high runtime, added data persistence.
    '''
    team_stats = {}
    for team in import_data.get_all_teams():
        team_stats[team] = TeamStats(team)

    # break out each individual stat into a list of that stat for every team.
    league_shooting_pcts = []
    league_save_pcts = []
    league_pp_pcts = []
    league_pk_pcts = []
    for stats in team_stats.values():
        league_shooting_pcts.append(stats.shooting_pct)
        league_save_pcts.append(stats.save_pct)
        league_pp_pcts.append(float(stats.pp_pct))
        league_pk_pcts.append(float(stats.pk_pct))

    data = {'shooting_pct': league_shooting_pcts,
            'save_pct': league_save_pcts,
            'pp_pct': league_pp_pcts,
            'pk_pct': league_pk_pcts}

    with open(filename, 'wb') as fi:
        pickle.dump(data, fi, pickle.HIGHEST_PROTOCOL)
    '''
    with open(filename, 'rb') as fi:
        league_data = pickle.load(fi)

    print(league_data)

    # calculate mean and std deviation for each stat
    mean_shooting_pct = mean(league_data['shooting_pct'])
    std_shooting_pct = std(league_data['shooting_pct'])

    mean_save_pct = mean(league_data['save_pct'])
    std_save_pct = std(league_data['save_pct'])

    mean_pp_pct = mean(league_data['pp_pct'])
    std_pp_pct = std(league_data['pp_pct'])

    mean_pk_pct = mean(league_data['pk_pct'])
    std_pk_pct = std(league_data['pk_pct'])

    # create normal distributions
    norm_shooting_pct = random.normal(loc=mean_shooting_pct, scale=std_shooting_pct, size=1000)
    norm_save_pct = random.normal(loc=mean_save_pct, scale=std_save_pct, size=1000)
    norm_pp_pct = random.normal(loc=mean_pp_pct, scale=std_pp_pct, size=1000)
    norm_pk_pct = random.normal(loc=mean_pk_pct, scale=std_pk_pct, size=1000)

    return norm_shooting_pct, norm_save_pct, norm_pp_pct, norm_pk_pct


filename = 'league_stats.pk'

norm1, norm2, norm3, norm4 = normal_distributions()

sns.distplot(norm1, hist=True)
# sns.distplot(norm2, hist=True)
# sns.distplot(norm3, hist=True)
# sns.distplot(norm4, hist=True)

plt.show()
