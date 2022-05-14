import constants
player_roster = constants.balance_teams(constants.clean_data(constants.PLAYERS), constants.TEAMS)

def get_teams(roster):
    all_teams = set()
    for player in roster:
        all_teams.add(player.get("team"))
    for team in all_teams:
        print(team)




def print_roster(roster):
    for players in roster:
        # print(players.get("team"))
        print(players)


def team_stats(team):
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
            team_roster.append(player_name) # adds player name to list
            guardian_name = player.get("guardians")
            team_guardians.append(guardian_name)
            total_height = player.get("height") + total_height
            if player.get("experience") == True:
                experienced_players += 1
            elif player.get("experience") == False:
                inexperienced_players += 1


    print(team.upper())
    print(f"Total Players: {total_players}")
    print(f"Experienced Players: {experienced_players}")
    print(f"Inexperienced Players: {inexperienced_players}")
    print(f"Average Height: {total_height/total_players} inches")
    print("\nPlayers: ")
    for players in team_roster:
        print(players)
    print("\nGuardians: ")
    for guardians in team_guardians:
        guardian = guardians.pop()
        print(guardian)


while True: #Main Loop of the Program.


    print("Hello, welcome to the basketball stats program."
          " Please select from the following teams to learn more about them:\n")
    get_teams(player_roster)
    team_selection = input("\nPlease enter the name of a team:   ").title()
    team_stats(team_selection)
    print("\nWould you like continue?")
    team_selection = input("Enter C to continue. Enter Q to quit.\n").lower()
    try: #Broken Another while loop needed?
        if team_selection == "c":
            continue

        elif team_selection == "q":
            print("Thank you for using the basketball stats tool! Goodbye!")
            break
    except(ValueError): #Broken
        print(ValueError)
        # print("Invalid entry. Please try again.")


# team_stats("Panthers")
