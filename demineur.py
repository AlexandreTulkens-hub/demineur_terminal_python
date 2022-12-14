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
    Fonction qui initialise un tableau de taille n × m où chaque case contient le caractère correspondant
    à une case inexplorée

            Parameters:
                    n (int): nombre de cases en longueur du tableau
                    m (int): nombre de cases en largeur du tableau

            Return:
                    board (list): list de list de chaîne de caractères
                                  correspondant au tableau de jeux
    """
    board = [['.' for x in range(n)] for y in range(m)]  # utilisation de compréhension de liste
    return board


def print_board(board: list):
    """
    Fonction qui affiche le plateau de jeu
    
            Parameters:
                    board (list): list de list de chaîne de caractères
                                  correspondant au tableau de jeux

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
                    board (list): list de list de chaîne de caractères
                                  correspondant au tableau de jeux

            Return:
                    (n, m) (tuple): un tuple de deux entiers correspondant aux dimensions du plateau
    """
    # la fonction len permet d'avoir le nombre d'éléments dans une liste qui ici représente
    n = len(board[0])  # ça largeur/ le nombre de colonnes
    m = len(board)  # ça longueur/ le nombre de lignes
    return n, m


def get_neighbors(board: list, pos_x: int, pos_y: int):
    """
    Fonction qui calcule les coordonnées de tous les voisins de la case donnée et en renvoie une liste

            Parameters:
                    board (list): list de list de chaîne de caractères
                                  correspondant au tableau de jeux
                    pos_x (int): coordonnée x de la case dont la fonction calcule les voisins
                    pos_y (int): coordonnée y de la case dont la fonction calcule les voisins

            Return:
                    neighbors (list): list de tuples de deux entiers correspondant aux positions des
                                      cases adjacentes
    """
    i = k = -1  # i cert à calculer les voisins de haut et k ceux de gauche
    j = l = 2  # j cert à calculer les voisins de bas et l ceux de droite

    nb_col, nb_li = get_size(board)  # le nombre de colonnes et de lignes du tableau

    #  Instruction qui détermine quelles lignes et colonnes ont de façon sûre pas de voisins
    if pos_y == 0:
        i = 0
    if pos_y == nb_li - 1:
        j = 1
    if pos_x == 0:
        k = 0
    if pos_x == nb_col - 1:
        l = 1

    neighbors = []  # Liste des coordonnées de toutes les cases voisines
    for change_pos_y in range(i, j):  # Change de ligne pour calculer la position y des voisins
        for change_pos_x in range(k, l):  # Change de colonne pour calculer la position x des voisins
            if not(change_pos_x == 0 and change_pos_y == 0):  # évite d'ajouter ça propre case comme un voisin
                neighbors.append((pos_x + change_pos_x, pos_y + change_pos_y))  # Ajout a la liste la position calculer
                # d'un voisin

    return neighbors


def place_mines(reference_board: list, number_of_mines: int, first_pos_x: int, first_pos_y: int):
    """
    Fonction qui place aléatoire les mines sur le reference_board après que le joueur
    ait choisi une première case à dévoiler

            Parameters:
                    reference_board (list): liste de liste de chaîne de caractères
                                  correspondant au tableau de jeux de référence
                    number_of_mines (int): nombre de mines à placer sur le tableau
                    first_pos_x (int): coordonnée x de la case choisie comme case de départ par le joueur
                    first_pos_y (int): coordonnée y de la case choisie comme case de départ par le joueur

            Return:
                    pos_mines (list): liste de tuples de deux entiers correspondant aux positions des
                                    mines sur le plateau de jeux
    """
    nb_col, nb_li = get_size(reference_board)  # Donne le nombre de colonnes et de lignes du tableau
    pos_mines = []  # Liste contenant les positions des mines
    pos_interdites = get_neighbors(reference_board, first_pos_x, first_pos_y)  # Liste de cases ou mines ne peuvent être

    pos_interdites.append((first_pos_x, first_pos_y))  # Ajout de la première case dévoilé

    for _ in range(number_of_mines):  # Creation de chaque mine une par une
        pos_x_mines = random.randint(0, nb_col - 1)
        pos_y_mines = random.randint(0, nb_li - 1)
        while (pos_x_mines, pos_y_mines) in pos_interdites:  # Vérification de la pos pour ne pas avoir de pos déjà
            # employee
            pos_x_mines = random.randint(0, nb_col - 1)
            pos_y_mines = random.randint(0, nb_li - 1)

        reference_board[pos_y_mines][pos_x_mines] = "X"  # Ajout de la mine dans le tableau de référence
        pos_interdites.append((pos_x_mines, pos_y_mines))  # Rendre cette pos ensuite interdite
        pos_mines.append((pos_x_mines, pos_y_mines))  # Et l'ajouter dans la liste contenant la pos de chaque mine

    return pos_mines


def fill_in_board(reference_board: list):
    """
    Fonction qui calcule le nombre de mines présentes dans le voisinage de chaque case et
    modifie ensuite le plateau de référence pour y faire apparaître ces nombres.

            Parameters:
                    reference_board (list): list de list de chaîne de ccaractères
                                  correspondant au tableau de jeux de référence

            Return:
                    None
    """
    nb_col, nb_li = get_size(reference_board)  # Donne le nombre de colonnes et de lignes du tableau

    # Pour chaque case du tableau
    for pos_y in range(nb_li):
        for pos_x in range(nb_col):
            if reference_board[pos_y][pos_x] != "X":  # Vérifie si la case ne contient pas de mine
                nb_mines = 0  # Remise à zéro des mines dans le voisinage
                neighbors = get_neighbors(reference_board, pos_x, pos_y)  # Calcule de toutes les positions du voisinage
                nb_neighbors = len(neighbors)
                for index in range(nb_neighbors):  # Pour chaque voisin
                    npos_x = neighbors[index][0]
                    npos_y = neighbors[index][1]
                    if reference_board[npos_y][npos_x] == "X":  # check si case contient une mine
                        nb_mines += 1  # Ajout au nombre de mines dans le voisinage
                reference_board[pos_y][pos_x] = f"{nb_mines}"  # change la case en y mettant le nombre de mines voisines

    return None


def propagate_click(game_board: list, reference_board: list, pos_x: int, pos_y: int):
    """
    Fonction qui met à jour le plateau de jeu en dévoilant d’un coup toutes les cases adjacentes à la case dévoilée
    après un clic, lorsque celles-ci n’ont aucune mine dans leur voisinage

            Parameters:
                    game_board (list):  list de list de chaîne de caractères correspondant au tableau de jeux
                    reference_board (list): list de list de chaîne de caractères correspondant
                                            au tableau de jeux de référence
                    pos_x (int): coordonnée x de la case dont la fonction calcule les voisins
                    pos_y (int): coordonnée y de la case dont la fonction calcule les voisins

            Return:
                    None
    """
    if reference_board[pos_y][pos_x] != game_board[pos_y][pos_x]:  # Check si récursivité est déjà passée par cette case
        if reference_board[pos_y][pos_x] == "0":  # Si la case n'a pas de mines dans son voisinage
            game_board[pos_y][pos_x] = reference_board[pos_y][pos_x]  # La case prend la valeur du plateau de ref.
            neighbors = get_neighbors(reference_board, pos_x, pos_y)  # Toutes les positions du voisinage sont calculés
            nb_neighbors = len(neighbors)
            for index in range(nb_neighbors):  # Pour chaque voisin
                npos_x = neighbors[index][0]
                npos_y = neighbors[index][1]
                propagate_click(game_board, reference_board, npos_x, npos_y)  # On relance le processus
        else:  # si la case a au moins une mine dans son voisinage
            game_board[pos_y][pos_x] = reference_board[pos_y][pos_x]  # On affiche ce nombre sur la case
    return None


def parse_input(n: int, m: int):
    """
    Fonction qui permet au joueur de rentrer une chaîne de caractères et qui sera ensuite
    interprété et découpé en un tuple [action, pos_x, pos_y]

            Parameters:
                    n (int): nombre de cases en longueur du tableau
                    m (int): nombre de cases en largeur du tableau

            Return:
                    action (tuple): tuple de str et int contenant l'action du joueur sur la case choisie
    """
    # Demande au joueur l'action qu'il veut faire
    ch_de_car = input("Donner moi l'action que vous voulez faire suivit de la case (ex :f 0 4) :")
    action = ch_de_car.split(" ")  # transformer la réponse en liste de str
    for i in range(1, 3):  # transformer les éléments(str) contenant les coordonnées en int
        action[i] = int(action[i])
    action = tuple(action)  # transformer le tout en tuple

    return action


def check_win(game_board: list, reference_board: list, mines_list: list, total_flags: int):
    """
    Fonction qui vérifie si la condition de victoire est remplie

            Parameters:
                    game_board (list):  list de list de chaîne de caractères correspondant au tableau de jeux
                    reference_board (list): list de list de chaîne de caractères correspondant
                                            au tableau de jeux de référence
                    mines_list (list): liste de tuples de deux entiers correspondant aux positions des mines
                                        sur le plateau de jeux
                    total_flags (int): nombre de drapeaux dans le tableau de jeu

            Return:
                    game_status (bool): booléen qui est True quand la partie est gagnée, False sinon
    """
    game_status = True  # On part du fait que la condition de victoire est remplie

    nb_mines = len(mines_list)
    if total_flags == nb_mines:  # S'il y a autant de mines que de drapeaux
        for mine in mines_list:  # Mais que pour chaque mine
            if game_board[mine[1]][mine[0]] != "F":  # Il y en a au moins une qui ne contient pas de drapeau
                game_status = False  # La condition de victoire n'est pas remplie
    else:
        case_inconnue = 0  # Nombre de cases non dévoilées
        for lignes in game_board:  # Pour chaque ligne,
            for colonne in lignes:  # Chaque case
                if colonne == "." or colonne == "F":  # Si non dévoilée
                    case_inconnue += 1  # On l'ajoute au nombre de cases non dévoilées

        if case_inconnue == nb_mines:  # S'il y a autant de mines que de cases non dévoilées
            for mine in mines_list:  # Mais que pour chaque mine
                if game_board[mine[1]][mine[0]] != ".":  # Il y en a au moins une qui ne l'est pas
                    game_status = False  # La condition de victoire n'est pas remplie


def init_game(n :int, m: int, number_of_mines: int):
def main():
    """
    Fonction qui démarre l'éxécution du jeu
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
