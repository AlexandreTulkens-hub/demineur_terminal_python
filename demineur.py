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
                    board (list): list de list de chaîne de charactère
                                  correspondant aux tableau de jeux
    """
    board = [['.' for x in range(n)] for y in range(m)]  # utilisation de compréhension de liste
    return board


def print_board(board: list):
    """
    Fonction qui affiche le plateau de jeu
    
            Parameters:
                    board (list): list de list de chaîne de charactère
                                  correspondant aux tableau de jeux

            Return:
                    None
    """
    larg_tab, long_tab = get_size(board)  # donne le nombre de colonnes et de lignes

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


def get_size(board: list):
    """
    Fonction qui renvoie les dimensions du plateau donné en entrée.

            Parameters:
                    board (list): list de list de chaîne de charactère
                                  correspondant aux tableau de jeux

            Return:
                    (n, m) (tuple): un tuple de deux entiers correspondant aux dimensions du plateau
    """
    # recherche la longueur et la largeur du tableau pour avoir les dimensions
    n = len(board[0])
    m = len(board)
    return n, m


def get_neighbors(board: list, pos_x: int, pos_y: int):
    """
    Fonction qui renvoie les dimensions du plateau donné en entrée.

            Parameters:
                    board (list): list de list de chaîne de charactère
                                  correspondant aux tableau de jeux

            Return:
                    neighbors (list): list de tuples de deux entiers correspondant aux positions des
                                      cases adjacentes
    """
    i = k = -1  # i détermine les voisins de haut et k de gauche
    j = l = 2  # j détermine les voisins de bas et l de droite

    nb_col, nb_li = get_size(board)  # donne le nombre de colonnes et de lignes du tableau

    #  Instruction qui détermine quelles cases n'éxistent pas
    if pos_y == 0:
        i = 0
    if pos_y == nb_li - 1:
        j = 1
    if pos_x == 0:
        k = 0
    if pos_x == nb_col - 1:
        l = 1

    neighbors = []  # list des coördonnées de toutes les cases voisines
    for change_pos_y in range(i, j):  # Itération a travers les lignes du tableau
        for change_pos_x in range(k, l):  # Itération a travers les colonnes du tableau
            if not(change_pos_x == 0 and change_pos_y == 0):  # If pour ne pas comptabiliser case de départ comme voisin
                neighbors.append((pos_x + change_pos_x, pos_y + change_pos_y))  # Ajout a la liste des voisins


def main():
    """
    Fonction qui démarre l'éxécution du jeux
    :return: None
    """
    x = create_board(LONG, LARG)
    print_board(x)
    neighbors = get_neighbors(x, 0, 6)

##################################################
#                                                #
#                   #main                        #
#                                                #
##################################################

if __name__ == "__main__":  # Permet d'importer la fonctions dans d'autres fichiers sans anomalies
    main()
