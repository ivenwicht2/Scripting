annee = input(" saisir une année : ")
annee = int(annee)
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100!= 0):
    print(1)
else : 
    print(2)
