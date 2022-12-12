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
import random

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
                    pos_x (int): coordonnée x de la case dont la fonction calcule les voisins
                    pos_y (int): coordonnée y de la case dont la fonction calcule les voisins

            Return:
                    neighbors (list): list de tuples de deux entiers correspondant aux positions des
                                      cases adjacentes
    """
    i = k = -1  # i détermine les voisins de haut et k de gauche
    j = l = 2  # j détermine les voisins de bas et l de droite

    nb_col, nb_li = get_size(board)  # Donne le nombre de colonnes et de lignes du tableau

    #  Instruction qui détermine quelles cases n'éxistent pas
    if pos_y == 0:
        i = 0
    if pos_y == nb_li - 1:
        j = 1
    if pos_x == 0:
        k = 0
    if pos_x == nb_col - 1:
        l = 1

    neighbors = []  # Liste des coordonnées de toutes les cases voisines
    for change_pos_y in range(i, j):  # Itération a travers les lignes du tableau
        for change_pos_x in range(k, l):  # Itération a travers les colonnes du tableau
            if not(change_pos_x == 0 and change_pos_y == 0):  # If pour ne pas comptabiliser case de départ comme voisin
                neighbors.append((pos_x + change_pos_x, pos_y + change_pos_y))  # Ajout a la liste des voisins

    return neighbors

def place_mines(reference_board: list, number_of_mines: int, first_pos_x: int, first_pos_y: int):
    """
    Fonction qui place aléatoire les mines sur le reference_board après que le joueur
    ait choisi une première case à dévoiler

            Parameters:
                    reference_board (list): list de list de chaîne de charactère
                                  correspondant au tableau de jeux de référence
                    number_of_mines (int): nombre de mines à placer sur le tableau
                    first_pos_x (int): coordonnée x de la case choisie comme case de départ par le joueur
                    first_pos_y (int): coordonnée y de la case choisie comme case de départ par le joueur

            Return:
                    pos_mines (list): list de tuples de deux entiers correspondant aux positions des
                                    mines sur le plateau de jeux
    """
    nb_col, nb_li = get_size(reference_board)  # Donne le nombre de colonnes et de lignes du tableau
    pos_mines = []  # Liste contenant les positions des mines
    pos_interdites = get_neighbors(reference_board, first_pos_x, first_pos_y)  # Liste de cases ou mines ne peuvent être
    pos_interdites.append((first_pos_x, first_pos_y))  # La liste doit aussi contenire la première case dévoilé

    for _ in range(number_of_mines):  # Creation de chaque mine une par une
        pos_x_mines = random.randint(0, nb_col - 1)
        pos_y_mines = random.randint(0, nb_li - 1)
        while (pos_x_mines, pos_y_mines) in pos_interdites:  # Permet de ne pas avoir de mines avec pos interdites
            pos_x_mines = random.randint(0, nb_col - 1)
            pos_y_mines = random.randint(0, nb_li - 1)
        reference_board[pos_y_mines][pos_x_mines] = "X"  # Ajoute la mine dans le tableau de référence
        pos_interdites.append((pos_x_mines, pos_y_mines))  # Après avoir posé une mine sur une case la case est interdites pour la prochaîne
        pos_mines.append((pos_x_mines, pos_y_mines))  # Ajout de la postion de la mine dans la liste contenant ces pos

    return pos_mines


def fill_in_board(reference_board: list):
    """
    Fonction qui calcule le nombre de mines présentes dans le voisinage de chaque case et
    modifie ensuite le plateau de référence pour y faire apparaître ces nombres.

            Parameters:
                    reference_board (list): list de list de chaîne de charactère
                                  correspondant au tableau de jeux de référence

            Return:
                    None
    """
    nb_col, nb_li = get_size(reference_board)  # Donne le nombre de colonnes et de lignes du tableau
    for pos_y in range(nb_li):  # Itération a travers les lignes du tableau
        for pos_x in range(nb_col):  # Itération a travers les colonnes du tableau
            if reference_board[pos_y][pos_x] != "X":  # vérifie si il y a déjà une mine sur la case
                neighbors = get_neighbors(reference_board, pos_x, pos_y)  # positions du voisinage
                nb_neighbors = len(neighbors)  # Nombre de voisin a la case
                nb_mines = 0  # Nombre de mines dans le voisinage d'une case
                for index in range(nb_neighbors):
                    if reference_board[neighbors[index][1]][neighbors[index][0]] == "X":  # check si case contient une mine
                        nb_mines += 1
                reference_board[pos_y][pos_x] = f"{nb_mines}"  # change la case en y métant le nombre de mines voisines

    return None

def main():
    """
    Fonction qui démarre l'éxécution du jeux
    :return: None
    """
    x = create_board(LONG, LARG)
    print_board(x)
    pos_mines = place_mines(x, NB_MINES, 6, 5)
    fill_in_board(x)
    print_board(x)


##################################################
#                                                #
#                   #main                        #
#                                                #
##################################################

if __name__ == "__main__":  # Permet d'importer la fonctions dans d'autres fichiers sans anomalies
    main()
