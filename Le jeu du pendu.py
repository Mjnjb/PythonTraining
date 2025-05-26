import random

def scrabble():    
    with open("sowpods.txt","r") as f:
        return f.readlines()

compteur = 0
goodguess = []
line = scrabble()
sow = list(random.choice(line).strip())
print("Bienvenue dans le jeu du pendu : ")

while set(goodguess) != set(sow):
    affichage = [lettre if lettre in goodguess else '_' for lettre in sow]
    print("Mot : ", ' '.join(affichage))
    
    n = input("Lettre : ").strip().upper()

    if n in sow:
        print("Bonne réponse !")
        compteur +=1
        if n not in goodguess:
            goodguess.append(n)
    else:
        print("Raté !")
        compteur += 1

print("Mot : ", ' '.join(sow))
print("Félicitations, vous avez trouvé le mot en", compteur, "essais !")