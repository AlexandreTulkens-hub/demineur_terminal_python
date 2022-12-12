"""
Auteur: Alexandre Tulkens
Date: 06-12-2022
                            Info-F-106 Projet 1 - Démineur
ce jeux est un jeux à 1 joueur sur une grille de taille variable et dont certaines cases contiennent des mines. Le
but du jeu est de dévoiler petit-à-petit les cases vides de la grille jusqu’à localiser toutes les mines
et les “désamorcer”. Le joueur perd s’il dévoile une case contenant une mine.
"""
#import
import sys

#constantes
LONG = int(sys.argv[1])  # nombre de cases en longueur du plateau
LARG = int(sys.argv[2])  # nombre de cases en largeur du plateau
NB_MINES = int(sys.argv[3])  # nombre de mines dans le plateau


##################################################
#                                                #
#                   #fonctions                   #
#                                                #
##################################################

def create_board(n: int, m: int):
    """
    Fontion qui initialise un tableau de taille n × m où chaque case contient le caractère correspondant
    à une case inexporée

            Parameters:
                    n (int): nombre de case en longueur du tableau
                    m (int): nombre de case en largeur du tableau

            Return:
                    board (list): tableau initialisé par fonction
    """
    board = [['.' for x in range(n)] for y in range(m)]  # utilisation de compréhension de liste
    return board


def print_board(board: list):
    """
    Fonction qui affiche le plateau de jeu
    
            Parameters:
                    board (list): tableau contenant le tableau de jeux

            Return:
                    None
    """
    long_tab = len(board)  # Largeur du tableau
    larg_tab = len(board[0])  # Longueur du tableau

    # Affiche l'indice des colones du plateau
    print("   ", end="")
    for i in range(larg_tab):
        if i < larg_tab - 1:
            print(f' {i}', end="")
        else:
            print(f' {i}')

    # Affiche délimitation du haut du plateau
    print("  _", end="")
    if larg_tab > 10:  # Quand le nombre de colones est plus grand que 10
        print("_"*(larg_tab - 10), end="")
    print("_"*(larg_tab * 2 + 2))

    # Affiche délimitation de coté + contenue du plateau
    for y in range(long_tab):
        print(f'{y} |', end="")
        for x in range(larg_tab):
            print(f" {board[y][x]}", end="")
            if x == larg_tab - 1:
                print(" |")

    # Affiche délimitation du bas du plateau
    print("  _", end="")
    if larg_tab > 10:  # Quand le nombre de colones est plus grand que 10
        print("_" * (larg_tab - 10), end="")
    print("_" * (larg_tab * 2 + 2))

def main():
    """
    Fonction qui démarre l'éxécution du jeux
    :return: None
    """
    x = create_board(LONG, LARG)
    print_board(x)


##################################################
#                                                #
#                   #main                        #
#                                                #
##################################################

if __name__ == "__main__":  # Permet d'importer la fonctions dans d'autres fichiers sans anomalies
    main()
