import random
# un chiffre est donné au hasard qui sera le nombre de tentative qu'on a pour trouver le mot
# chat gpt peut me generer une serie de mot à deviner
# je peux faire un tableau contenant les niveaux (8 étapes) afficchez un dessin du pendu à chaque tentative tarée
# chaque étape contient un moment du pendu, si le caractere que met la personne ne se trouve pas dans le mot selectionné, 
# alors il passe a l'etape suivante

nombre_tentative = random.randint(1,8)
print(f"tu as {nombre_tentative} tentative(s) pour trouver le mot !")

liste_mot = ["ordinateur", "bibliotheque", "television","elephant","girafe","rhinoceros","etoile","volcan","cascade","refrigerateur","microphone","vacances","papillon"]

mot_a_deviner = random.choice(liste_mot)
print(mot_a_deviner)

mot_a_jour = "_" * len(mot_a_deviner)

print(mot_a_jour)

while nombre_tentative > 0:
    input_utilisateur = input("entrez une lettre")
    
    if input_utilisateur == mot_a_deviner:
        print("vous avez gagné !") 
    elif input_utilisateur in mot_a_deviner:
            mot_a_jour = mot_a_jour.replace("_",input_utilisateur)
    else:
        nombre_tentative -= 1



print("vous avez trouvé !")
