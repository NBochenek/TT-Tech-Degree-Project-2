TEAMS = [
    'Panthers',
    'Bandits',
    'Warriors',
]

PLAYERS = [{
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Matt Gill',
        'guardians': 'Charles Gill and Sylvia Gill',
        'experience': 'NO',
        'height': '40 inches'
    },
    {   'name': 'Sammy Adams',
        'guardians': 'Jeff Adams and Gary Adams',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Chloe Alaska',
        'guardians': 'David Alaska and Jamie Alaska',
        'experience': 'NO',
        'height': '47 inches'
    },
    {
        'name': 'Bill Bon',
        'guardians': 'Sara Bon and Jenny Bon',
        'experience': 'YES',
        'height': '43 inches'
    },
    {
        'name': 'Joe Kavalier',
        'guardians': 'Sam Kavalier and Elaine Kavalier',
        'experience': 'NO',
        'height': '39 inches'
    },
    {
        'name': 'Phillip Helm',
        'guardians': 'Thomas Helm and Eva Jones',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Les Clay',
        'guardians': 'Wynonna Brown',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Sal Dali',
        'guardians': 'Gala Dali',
        'experience': 'NO',
        'height': '41 inches'
    },
    {
        'name': 'Suzane Greenberg',
        'guardians': 'Henrietta Dumas',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Jill Tanner',
        'guardians': 'Mark Tanner',
        'experience': 'YES',
        'height': '36 inches'
    },
    {
        'name': 'Arnold Willis',
        'guardians': 'Claire Willis',
        'experience': 'NO',
        'height': '43 inches'
    },
    {
        'name': 'Herschel Krustofski',
        'guardians': 'Hyman Krustofski and Rachel Krustofski',
        'experience': 'YES',
        'height': '45 inches'
    },
    {
        'name': 'Eva Gordon',
        'guardians': 'Wendy Martin and Mike Gordon',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Ben Finkelstein',
        'guardians': 'Aaron Lanning and Jill Finkelstein',
        'experience': 'NO',
        'height': '44 inches'
    },
    {
        'name': 'Joe Smith',
        'guardians': 'Jim Smith and Jan Smith',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Diego Soto',
        'guardians': 'Robin Soto and Sarika Soto',
        'experience': 'YES',
        'height': '41 inches'
    },
    {
        'name': 'Kimmy Stein',
        'guardians': 'Bill Stein and Hillary Stein',
        'experience': 'NO',
        'height': '41 inches'
    }
]


def sort_by_experience(roster):  # Sorts roster by experience to ensure those with experience are equally distributed.
    return roster["experience"]

def calculate_experience(roster):  # Determines the number of players with experience on each team to ensure equality.
    total_experienced_players = 0
    for player in roster:
        if player.get("experience") == True:
            total_experienced_players += 1
    return total_experienced_players


def clean_data(list):  # Cleans constants data according to parameters defined in README.
    players_cleaned = []
    for item in list:
        dict_cleaned = {}
        dict_cleaned["name"] = item["name"]
        dict_cleaned["guardians"] = item["guardians"].split(" and ")
        if item["experience"] == "YES":
            dict_cleaned["experience"] = True
        if item["experience"] == "NO":
            dict_cleaned["experience"] = False
        dict_cleaned["height"] = int(item["height"].split(" ")[0])
        players_cleaned.append(dict_cleaned)
    return players_cleaned


def balance_teams(roster, teams):  # Balances Teams according to parameters defined in README.
    team_assignment = ""
    players_panthers = 0
    players_bandits = 0
    players_warriors = 0
    exp_players_panthers = 0
    exp_players_bandits = 0
    exp_players_warriors = 0
    players_per_team = len(roster) / len(teams)
    experienced_players_per_team = int(calculate_experience(roster) / len(teams))
    players_balanced = roster.copy()
    players_balanced.sort(reverse=True, key=sort_by_experience)
    for player in players_balanced:
        if player.get("experience") == True and exp_players_panthers < experienced_players_per_team:
            team_assignment = "Panthers"
            exp_players_panthers += 1
            players_panthers += 1
        elif player.get("experience") == True and exp_players_bandits < experienced_players_per_team:
            team_assignment = "Bandits"
            exp_players_bandits += 1
            players_bandits += 1
        elif player.get("experience") == True and exp_players_warriors < experienced_players_per_team:
            team_assignment = "Warriors"
            exp_players_warriors += 1
            players_warriors += 1
        elif players_panthers < players_per_team:
            team_assignment = "Panthers"
            players_panthers += 1
        elif players_bandits < players_per_team:
            team_assignment = "Bandits"
            players_bandits += 1
        elif players_warriors < players_per_team:
            team_assignment = "Warriors"
            players_warriors += 1
        player.update({"team" : team_assignment})


    return players_balanced







if __name__ == "__main__":  #  Dunder Main statement
    for players in balance_teams(clean_data(PLAYERS), TEAMS):
        print(players.get("team"))
