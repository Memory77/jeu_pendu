ascii_1 = """
 +------+
 |      |
 |      |
 |      |
 |      |
 |      |
 +------+
"""

ascii_2 = """
 +------+
 |      |
 |   O  |
 |      |
 |      |
 |      |
 +------+
"""

ascii_3 = """
 +------+
 |      |
 |   O  |
 |   |  |
 |      |
 |      |
 +------+
"""

ascii_4 = """
 +------+
 |      |
 |   O  |
 |  /|\ |
 |      |
 |      |
 +------+
"""

ascii_5 = """
 +------+
 |      |
 |   O  |
 |  /|\ |
 |  /   |
 |      |
 +------+
"""

ascii_6 = """
 +------+
 |      |
 |   O  |
 |  /|\ |
 |  / \ |
 |      |
 +------+
"""

ascii_7 = """
 +------+
 |      |
 |   O  |
 |  /|\ |
 |  / \ |
 |      |
 +------+
"""

ascii_8 = """
 +------+
 |      |
 |   O  |
 |  /|\ |
 |  / \ |
 |      |
 +------+
"""



def fonction(compteur):
    if compteur == 1:
        return ascii_2
    elif compteur == 2:
        return ascii_3
    elif compteur == 3:
        return ascii_4
    elif compteur == 4:
        return ascii_5
    elif compteur == 5:
        return ascii_6
    else:
        return ascii_6
