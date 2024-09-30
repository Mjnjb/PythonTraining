import csv

# Chemin du fichier CSV
chemin_fichier = 'csvhtml\\123.csv'

# Initialiser un dictionnaire pour stocker les données
dictionnaire_joueurs = {}

# Lire le fichier CSV
with open(chemin_fichier, mode='r', encoding='utf-8') as fichier:
    lecteur_csv = csv.reader(fichier, delimiter=';')
    
    # Passer la première ligne si elle contient les en-têtes
    next(lecteur_csv)
    
    # Parcourir chaque ligne du fichier
    for ligne in lecteur_csv:
        nom_joueur = ligne[0].strip()  # Nom du joueur
        main_role = ligne[1].strip()    # Main role
        
        # Ajouter au dictionnaire
        dictionnaire_joueurs[nom_joueur] = main_role

# Afficher le dictionnaire
print(dictionnaire_joueurs)
