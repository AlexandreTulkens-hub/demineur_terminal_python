"""
Auteur: Alexandre Tulkens
Date: 06-12-2022
                                Projet1 INFO-F106 - Démineur

Le démineur est un jeu à 1 joueur sur une grille de taille variable et dont certaines cases contiennent des mines.
Le but du jeu est de dévoiler petit-à-petit les cases vides de la grille jusqu’à localiser toutes les mines
et les “désamorcer”. Le joueur perd s’il dévoile une case contenant une mine.
"""
#imports
import sys

#constants
longueur_plat = sys.argv[1]
largeur_plat = sys.argv[2]
number_of_mines = sys.argv[3]


#functions

def main():
    """
    fonction principale qui éxécute le jeux
    :return: none
    """

if __name__ == "__main__": #permet d'importer la fonctions dans d'autres fichiers
    main()