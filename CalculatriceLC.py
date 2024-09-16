print("Choissisez l'opération souhaitée parmis cette liste")
print("Addition : +")
print("Soustraction : -")
print("Multiplication : *")
print("Division : /")
print("Modulo : %")
print("Division entière : //")
print("Puissance : **")

a=(input("Opérateur selectionné : "))
operation=["+","-","/","//","**","*","%"]

def Demander_valeurs():
        b=(int(input("Choisis la premiere valeur ")))
        c=(int(input("Choisis la seconde valeur ")))
        return b,c
        

def Additionner():
            b,c = Demander_valeurs()
            Addition = b + c
            print("le résultat est",Addition)
            return()
def Soustraire():
            b,c = Demander_valeurs()
            Soustraction = b - c
            print("le résultat est",Soustraction)
            return()
def Diviser():
            b,c = Demander_valeurs()
            if c == 0 : 
                    print("La division est impossible") 
                    Diviser()
            else:
                Division = b / c
                print("le résultat est", Division)           
            return()
def Euclidienne():
            b,c = Demander_valeurs()
            if c == 0 : 
                    print("La division est impossible") 
                    Euclidienne()
            else:
                Euclide = b // c
                print("le résultat est",Euclide)
            return()
def Puissance():
            b,c = Demander_valeurs()
            Power = b ** c
            print("le résultat est",Power)
            return()
def Multiplier():
            b,c = Demander_valeurs()
            Multiplication = b * c
            print("le résultat est",Multiplication)
            return()
def Modulo():
            b,c = Demander_valeurs()
            if c == 0 : 
                    print("La division est impossible") 
                    Modulo()
            else:
                Reste = b % c
                print("le résultat est ",Reste)
            return()

while a not in operation:
    print("Mauvais opérateur, recommencez")
    a=(input("Opérateur selectionné : "))
if a == "+":
    print("Vous avez selectionner une addition : ")
    Additionner()
elif a == "-":
    print("Vous avez selectionner une soustraction : ")
    Soustraire()
elif a == "/":
    print("Vous avez selectionner une division : ")
    Diviser()
elif a == "//":
    print("Vous avez selectionner une division euclidienne : ")
    Euclidienne()
elif a == "**":
    print("Vous avez selectionner une puissance : ")
    Puissance()
elif a == "*":
    print("Vous avez selectionner une multiplication : ")
    Multiplier()
elif a == "%":
    print("Vous avez selectionner un modulo : ")
    Modulo()












