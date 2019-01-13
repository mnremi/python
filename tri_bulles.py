import random
import time

# Based on https://vimeo.com/38607795

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

def tri_bulles():
    maxloop = maxliste-1
    for i in range(0, maxloop):
        for j in range(1, maxloop):
            if liste[j] < liste[j-1]:
                inversion(j)
        if maxloop > 0 and liste[maxloop] > liste[maxloop-1]:
            maxloop -= 1
            
generation()
affichage()

ini = time.time()
tri_bulles()
end = time.time()

affichage()
print("Sorting duration : %f" % (end-ini))
