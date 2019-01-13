import random
import time

# Based on https://vimeo.com/38609513

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

def permutation(remplacant, rang):
    temp = liste[rang]
    liste[rang] = liste[remplacant]
    liste[remplacant] = temp

def tri_selection():
    for i in range(0, maxliste):
        for j in range(0, maxliste):
            if liste[j] > liste[i]:
                permutation(i, j)

generation()
affichage()

ini = time.time()
tri_selection()
end = time.time()

affichage()
print("Sorting duration : %f" % (end-ini))
