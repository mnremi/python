import random
import time

# Based on https://vimeo.com/38610344

liste = []
maxrange = int(input("Quelle est la valeur maximale possible acquise dans la liste ? "))
maxliste = int(input("De combien d'entiers la liste sera composée ? "))

def generation():
    for i in range(0, maxliste):
        liste.append(random.randint(1, maxrange))

def affichage():
    print("")
    print(liste)
    print("")

def inversion(rang):
    temp = liste[rang-1]
    liste[rang-1] = liste[rang]
    liste[rang] = temp

def tri_insertion():
    for i in range(1, maxliste):
        for j in range(1, maxliste):
            if (i-j)!= -1 and liste[i-j+1] < liste[i-j]:
                inversion(i-j+1)
            else:
                break

generation()
affichage()

ini = time.time()
tri_insertion()
end = time.time()

affichage()
print("Sorting duration : %f" % (end-ini))
