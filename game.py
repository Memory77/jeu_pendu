import random
from PIL import Image
import ascii
# un chiffre est donné au hasard qui sera le nombre de tentative qu'on a pour trouver le mot
# chat gpt peut me generer une serie de mot à deviner
# je peux faire un tableau contenant les niveaux (8 étapes) afficchez un dessin du pendu à chaque tentative tarée
# chaque étape contient un moment du pendu, si le caractere que met la personne ne se trouve pas dans le mot selectionné, 
# alors il passe a l'etape suivante

nombre_tentative = random.randint(1,8)
print(f"tu as {nombre_tentative} tentative(s) pour trouver le mot !")

liste_mot = ["ordinateur", "bibliotheque", "television","elephant","girafe","rhinoceros","etoile","volcan","cascade","refrigerateur","microphone","vacances","papillon"]

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
        # print(compteur)
        if compteur == 1:
            print(ascii.ascii_1)
        elif compteur == 2:
            print(ascii.ascii_2)
        elif compteur == 3:
            print(ascii.ascii_3)
        elif compteur == 4:
            print(ascii.ascii_4)
        elif compteur == 5:
            print(ascii.ascii_5)
        print(mot_a_jour)
        
    if "_" not in mot_a_jour:
        print("Bravo, vous avez trouvé le mot !")
        break

if "_" in mot_a_jour:
    print(f"Désolé, tu n'as pas réussi à trouver le mot. Le mot était : {mot_a_deviner}")
