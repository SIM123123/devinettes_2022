#!/usr/bin/env python3
"""
Jeu de devinettes.
par Simon Lamarche Perrea
"""
import random
import re


class Colors:
    """
    class pour les couleurs.
    """
    ROUGE = "\033[31m"
    NORMAL = "\033[0m"
    ORANGE = "\033[33m"
    VERT = "\033[32m"
    BLEU = "\033[34m"


def main():
    """
    Fonction principale
    """
    print(Colors.ROUGE + "SLP" + Colors.NORMAL + ":" + Colors.ORANGE + " Jeu de devinette...")
    print(Colors.ROUGE + "SLP" + Colors.NORMAL + ":" + Colors.ORANGE + " Devinez le nombre entier entre 1 et 100\n")
    nbaléatoire = 45  # random.randrange(100)
    nbessai = 1
    while True:
        while True:
            entré = input(Colors.NORMAL + "Essai " + Colors.BLEU + f"{nbessai}" + Colors.NORMAL + ":" + Colors.VERT)
            if re.match(r'\d+', entré):
                nbentré = int(entré)
                break
            else:
                print("Erreur ")
        pass

        if nbentré > nbaléatoire:
            print(Colors.ROUGE + "SLP" + Colors.NORMAL + "> votre nombre est trop " + Colors.BLEU +
                  "grand" + Colors.NORMAL + "...\n")
            nbessai += 1
        elif nbentré < nbaléatoire:
            print(Colors.ROUGE + "SLP" + Colors.NORMAL + "> votre nombre est trop " + Colors.BLEU +
                  "petit" + Colors.NORMAL + "...\n")
            nbessai += 1
        else:
            break
        pass
    print(Colors.ROUGE + "SLP" + Colors.NORMAL + ">" + Colors.VERT + " Bravo, vous avez deviné le nombre!")


if __name__ == '__main__':
    main()


