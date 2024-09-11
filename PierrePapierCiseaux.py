import random

a = ["pierre","papier","ciseaux"]
pierre = "pierre"
papier = "papier"
ciseaux = "ciseaux"

def pierre_feuille_ciseaux():
    print ("Faites un choix entre pierre , papier ou ciseaux")
    choix = input()
    if choix == pierre or choix == papier or choix == ciseaux :
        res=random.choice(a)
        print(res)

    #    JEUX:
        if choix == res:
            print("Match Nul")
            pierre_feuille_ciseaux()
        elif choix == papier and res == ciseaux:
            print("C'est perdu !")
        elif choix == ciseaux and res == papier:
            print("C'est gagné !")    
        elif choix == pierre and res == papier:
            print("C'est perdu !")
        elif choix == papier and res == pierre:
            print("C'est gagné !")
        elif choix == ciseaux and res == pierre:
            print("C'est perdu !")
        elif choix == pierre and res == ciseaux:
            print("C'est gagné !")
    else : 
        pierre_feuille_ciseaux()

    
pierre_feuille_ciseaux()
        
    
        


