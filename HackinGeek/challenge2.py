'''Vous devez "inverser" un nombre qui vous est donnée.
Explication : vous prenez en argument un nombre, vous convertissez ce dernier en binaire puis inverser l'ordre des 0 et 1 pour ensuite afficher le nombre créer.

Exemple: 6 donne 00000110, votre programme inverse l'ordre binaire -> 0110000 et retourne donc 96

Bonne Chance !'''

# Défi donné par https://github.com/RobinsonD3v

nbr = int(input("Enter number: "))

nbr = "".join(format(nbr, "b"))
nbr = "0" * (8 - len(nbr)) + nbr

print("Result\t: ", int(nbr[::-1], 2))
