import pandas as pd

mydataset = {
  'Joueur': ["PLURALISTICBOSSA#NOVA", "Bambousin#BAMBZ"],
  'Poste': ["Adc", "Mid"]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
