a=(int(input("Valeur une : ")))
b=(int(input("Valeur deux : ")))
total = 0
suite_fibonacci = []

nombres = (input("Choississez le nombre de chiffre de la suite : "))

for x in range(int(nombres)):
    a = b
    b = total
    total = a+b
    suite_fibonacci.append(total)
    
print(suite_fibonacci)
