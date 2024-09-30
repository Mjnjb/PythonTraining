from acces import get_nominvoc, get_historique, role_joueur
from collections import Counter
import csv

# Dictionnaire pour stocker les rôles des joueurs
player_roles = {}  ####

# Demander à l'utilisateur d'entrer 10 noms d'invocateurs
def get_multiple_summoners(nb_summoners=10):
    summoners = []  # Liste pour stocker les informations des invocateurs
    for i in range(nb_summoners):
        print(f"Entrez les informations du joueur {i+1} :")
        summoner = get_nominvoc()  # Récupérer les informations du joueur via l'API
        summoners.append(summoner)  ####
    return summoners

# Fonction pour traiter chaque joueur et obtenir son rôle principal
def process_summoner(summoner, nb_match=10):
    # Affiche l'id des dernières games de lol
    summoner_match_ids = get_historique(summoner['puuid'], nb_match)
    
    positions = []
    role_counts = {
        "Top": 0,
        "Jungle": 0,
        "Mid": 0,
        "Adc": 0,
        "Support": 0,
    }

    # Affiche les "roles" des dernières games et assigne un rôle au joueur
    for match_id in summoner_match_ids:
        role = role_joueur(summoner["puuid"], match_id)

        if role == "TOP":
            role = "Top"
        elif role == "JUNGLE":
            role = "Jungle"
        elif role == "MIDDLE":
            role = "Mid"
        elif role == "BOTTOM":
            role = "Adc"
        elif role == "UTILITY":
            role = "Support"

        positions.append(role)

        if role in role_counts:
            role_counts[role] += 1
        else:
            print("Role non trouvé")

    # Compter le rôle le plus joué
    occu = Counter(positions)
    positions = sorted(positions, key=occu.get, reverse=True)

    if positions:
        for role, count in role_counts.items():
            print(f"{role}: {count} fois")

    # Ajouter le joueur et son rôle principal au dictionnaire
    if positions:
        player_roles[summoner['gameName']] = positions[0]  ####
        print(f"{summoner['gameName']} est un main {positions[0]}.")  ####

# Récupérer les informations de 10 invocateurs
summoners = get_multiple_summoners(1)  ####

# Traiter chaque invocateur et obtenir son rôle principal
for summoner in summoners:  ####
    process_summoner(summoner)  ####

# Afficher les rôles des 10 invocateurs
print("\nRésumé des joueurs et de leurs rôles :")
for player, role in player_roles.items():
    print(f"{player} joue principalement {role}.")

csv_content = ""
for player, role in player_roles.items():
    csv_content += f"{player},,{role}\n"

csv_file_path = "C:\\Users\\Rayane\\Documents\\API Python\\csvhtml\\resultats_partie.csv"  

existing_players = set()  #### Utilisation d'un ensemble pour éviter les doublons
try:
    with open(csv_file_path, mode='r', newline='') as file:  
        reader = csv.reader(file, delimiter=';')
        next(reader)  
        for row in reader:
            existing_players.add(row[0])  #### Ajouter le nom du joueur à l'ensemble
except FileNotFoundError:
    print("Le fichier n'existe pas encore, il sera créé.")


with open(csv_file_path, mode='a', newline='') as file: 
    writer = csv.writer(file, delimiter=';')  
    for player, role in player_roles.items():
        if player not in existing_players:
            writer.writerow([player, role])  
            print(f"{player} a été ajouté au fichier CSV.")