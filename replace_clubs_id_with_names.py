import csv

# Wczytanie zawodników
with open('players.csv', 'r', encoding='utf-8') as players_file:
    players_reader = csv.DictReader(players_file)
    players = list(players_reader)

# Wczytanie klubów
with open('clubs.csv', 'r', encoding='utf-8') as clubs_file:
    clubs_reader = csv.DictReader(clubs_file)
    clubs = {club['club_id']: club['club_name'] for club in clubs_reader}

# Wczytanie lig
with open('leagues.csv', 'r', encoding='utf-8') as leagues_file:
    leagues_reader = csv.DictReader(leagues_file)
    leagues = {league['league_id']: league['league_name'] for league in leagues_reader}

# Podmiana id klubów na nazwy klubów wśród zawodników
for player in players:
    player['club'] = clubs.get(player['club'], 'Nieznany klub')

# Podmiana id lig na nazwy lig wśród zawodników
for player in players:
    player['league'] = leagues.get(player['league'], 'Nieznana liga')

# Zapisanie zmienionych danych zawodników do nowego pliku CSV
with open('final_players_info.csv', 'w', newline='', encoding='utf-8') as output_file:
    fieldnames = players[0].keys()
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(players)

print("Zakończono podmianę id klubów i id lig na nazwy klubów i nazwy lig.")
