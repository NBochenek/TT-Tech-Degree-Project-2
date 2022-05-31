import constants
player_roster = constants.balance_teams(constants.clean_data(constants.PLAYERS), constants.TEAMS)  # Cleans data and
# balances teams using constants data.


def get_teams(roster):  # Prints all the teams in the roster and returns the set of all teams.
    all_teams = set()
    for player in roster:
        all_teams.add(player.get("team"))
    print("Teams:\n")
    for team in all_teams:
        print(team)
    return all_teams


# def print_roster(roster):
#     for players in roster:
#         # print(players.get("team"))
#         print(players)


def team_stats(team):  # Returns team stats based on clean and balanced roster.
    total_players = 0
    experienced_players = 0
    inexperienced_players = 0
    total_height = 0
    team_roster = []
    team_guardians = []
    for player in player_roster:
        if player["team"] == str(team):     # Filters out all players who aren't on specified team.
            total_players += 1              # Tracks how many players are on the team
            player_name = player.get("name")# gets player's name from dictionary
            team_roster.append(player_name) # adds player name to list ** Why doesnt this need .copy?
            guardian_name = player.get("guardians")
            team_guardians.append(guardian_name.copy())  # adds guardian names to list ** Why does this need .copy?
            total_height = player.get("height") + total_height
            if player.get("experience") == True:
                experienced_players += 1
            elif player.get("experience") == False:
                inexperienced_players += 1


    print(team.upper())
    print(f"Total Players: {total_players}")
    print(f"Experienced Players: {experienced_players}")
    print(f"Inexperienced Players: {inexperienced_players}")
    print(f"Average Height: {round(total_height/total_players, 2)} inches")
    print("\nPlayers: ")
    for players in team_roster:
        print(players)
    print("\nGuardians: ")
    for guardians in team_guardians:
        guardian = guardians.pop()
        print(guardian)


print("Hello, welcome to the basketball stats program."
" Please select from the following teams to learn more about them:\n")

while True:  # Main Loop of the Program.

    all_teams = get_teams(player_roster)  # Function prints all teams.
    team_selection = input("\nPlease enter the name of a team:   ").title()
    try:
        if team_selection == "Q":  # Quit Program
            print("Thank you for using the basketball stats tool! Goodbye!")
            break
        elif team_selection in all_teams:  # If valid input, user can enter another input.
            team_stats(team_selection)
            print("\nWould you like continue? Enter Q to quit or enter a team name to continue.\n")
            continue
        else:  # If input is not a valid team name, prompts again.
            raise ValueError("That is not a valid team name. Please try again.\n")
            continue

    except ValueError as err:
        print(f"{err}")
        continue
    except ZeroDivisionError as err:
        print(f"{err}")
        continue
    else:
        break






