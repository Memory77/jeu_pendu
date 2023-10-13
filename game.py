import random
import ascii
from ascii import fonction
# un chiffre est donné au hasard qui sera le nombre de tentative qu'on a pour trouver le mot
# chat gpt peut me generer une serie de mot à deviner
# je peux faire un tableau contenant les niveaux (8 étapes) afficchez un dessin du pendu à chaque tentative tarée
# chaque étape contient un moment du pendu, si le caractere que met la personne ne se trouve pas dans le mot selectionné, 
# alors il passe a l'etape suivante

difficulte = int(input("Renseignez le niveau difficulté: \n  1 = Facile \n  2 = Intermediaire \n  3 = Difficile \n"))

if difficulte == 1:
    liste_mot = ["fruit", "voyage", "etoile", "volcan","chat", "chien", "livre","ami"]
    nombre_tentative = 8
elif difficulte == 2:
    liste_mot = ["etoile","vacances","cascade", "montagne", "maison", "plage"]
    nombre_tentative = 6
elif difficulte == 3:
    liste_mot = ["ordinateur", "bibliotheque", "television","elephant","girafe","rhinoceros","refrigerateur","microphone","papillon"]
    nombre_tentative = 4
else:
    print("vous devez renseigner un niveau de difficulté (1 2 ou 3)")
    
print(f"tu as {nombre_tentative} tentative(s) pour trouver le mot !")



mot_a_deviner = random.choice(liste_mot)
#print(mot_a_deviner)

mot_a_jour = ["_"] * len(mot_a_deviner)

print(mot_a_jour)
compteur = 0
while nombre_tentative > 0:
    input_utilisateur = input("entrez une lettre : ")
    
    if input_utilisateur in mot_a_deviner:
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == input_utilisateur:
                mot_a_jour[i] = input_utilisateur
                print(mot_a_jour)
    else:
        nombre_tentative -= 1
        print(nombre_tentative)
        print(f"Il vous reste {nombre_tentative} tentative(s).")
        compteur += 1
        print(fonction(compteur))
        print(mot_a_jour)
        if compteur > 4:
            indice = random.choice(mot_a_deviner)
            print(f"indice : {indice}")
            
    if "_" not in mot_a_jour:
        print("Bravo, vous avez trouvé le mot !")
        break

if "_" in mot_a_jour:
    print(f"Désolé, tu n'as pas réussi à trouver le mot. Le mot était : {mot_a_deviner}")
