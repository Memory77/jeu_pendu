import random
# un chiffre est donné au hasard qui sera le nombre de tentative qu'on a pour trouver le mot
# chat gpt peut me generer une serie de mot à deviner
# je peux faire un tableau contenant les niveaux (8 étapes) afficchez un dessin du pendu à chaque tentative tarée
# chaque étape contient un moment du pendu, si le caractere que met la personne ne se trouve pas dans le mot selectionné, 
# alors il passe a l'etape suivante

nombre_tentative = random.randint(1,8)
print(f"tu as {nombre_tentative} tentative(s) pour trouver le mot !")

