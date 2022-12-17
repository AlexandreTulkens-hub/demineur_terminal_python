"""
Auteur: Alexandre Tulkens
Matricule: 000575251
Date: 06-12-2022
                            Info-F-106 Projet 1 - Démineur
ce jeux est un jeux à 1 joueur sur une grille de taille variable et dont certaines cases contiennent des mines. Le
but du jeu est de dévoiler petit-à-petit les cases vides de la grille jusqu’à localiser toutes les mines
et les “désamorcer”. Le joueur perd s’il dévoile une case contenant une mine.
"""
# import
import sys
import random


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
    board = [['.' for x in range(m)] for y in range(n)]  # utilisation de compréhension de liste
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
    long_tab, larg_tab = get_size(board)  # Le nombre de lignes et de colonnes du tableau
    sep_max_10 = " "
    sep_min_10 = "  "

    col_min_10 = " "
    col_max_10 = " "

    # Partie calcule
    for i in range(larg_tab):  # Pour chaque indice
        indice = i // 10  # On prend le chiffre de poids fort
        if indice == 0:  # Si c'est 0
            col_min_10 += "  "  # On le représente par un espace
        else:  # sinon
            col_min_10 += f" {indice}"  # On le représente normalement
        indice = i % 10  # On prend le chiffre de poids faible
        col_max_10 += f" {indice}"  # On le représente normalement

    col_bords = "___"
    for _ in range(larg_tab):  # Pour chaque indice
        col_bords += "__"  # deux lignes rayées sont ajoutées

    # Partie print
    if long_tab <= 10:  # Pour une longueur plus petite que 11
        if larg_tab > 10:  # Pour une potentielle largeur plus grande que 10
            print(sep_max_10, col_min_10)  # On print d'abord les poids forts des indices
        print(sep_max_10, col_max_10)  # On print les poids faibles
        print(sep_max_10, col_bords)  # On print le bord
    else:  # Pour une longueur plus grande que 10
        if larg_tab > 10:
            print(sep_min_10, col_min_10)
        print(sep_min_10, col_max_10)
        print(sep_min_10, col_bords)

    for y in range(long_tab):  # Pour chaque ligne
        if y < 10 < long_tab:  # Si l'indice est moins de 10 et que le total de lignes est plus de 10
            print(f' {y} |', end="")  # on ajoute une espace au début de la chaîne de caractère
        else:  # Sinon
            print(f'{y} |', end="")  # on imprime simplement l'indice et le bord
        for x in range(larg_tab):  # Pour chaque colonne
            print(f" {board[y][x]}", end="")  # on imprime le contenu de la case
        print(" |")  # on finie par imprimer le bord droit

    # Puis on imprime la limite du bas du tableau
    if long_tab <= 10:
        print(sep_max_10, col_bords)
    else:
        print(sep_min_10, col_bords)


def get_size(board: list):
    """
    Fonction qui renvoie les dimensions du plateau donné en entrée.

            Parameters:
                    board (list): list de list de chaîne de caractères
                                  correspondant au tableau de jeux

            Return:
                    (n, m) (tuple): un tuple de deux entiers correspondant aux dimensions du plateau
    """
    # La fonction len permet d'avoir le nombre d'éléments dans une liste qui ici représente
    n = len(board)  # Sa longueur/ le nombre de lignes
    m = len(board[0])  # Sa largeur/ le nombre de colonnes
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

    nb_li, nb_col = get_size(board)  # Le nombre de lignes et de colonnes du tableau

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
            if not (change_pos_x == 0 and change_pos_y == 0):  # évite d'ajouter ça propre case comme un voisin
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
    nb_li, nb_col = get_size(reference_board)  # Le nombre de lignes et de colonnes du tableau
    pos_mines = []  # Liste contenant les positions des mines
    pos_interdites = get_neighbors(reference_board, first_pos_x, first_pos_y)  # Liste de cases ou mines ne peuvent être

    pos_interdites.append((first_pos_x, first_pos_y))  # Ajout de la première case dévoilé

    for _ in range(number_of_mines):  # Creation de chaque mine une par une
        pos_x_mines = random.randint(0, nb_col - 1)
        pos_y_mines = random.randint(0, nb_li - 1)
        while (pos_x_mines, pos_y_mines) in pos_interdites:  # Vérification de la pos pour ne pas avoir de pos déjà
            # employée
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
                    reference_board (list): list de list de chaîne de caractères
                                  correspondant au tableau de jeux de référence

            Return:
                    None
    """
    nb_li, nb_col = get_size(reference_board)  # Le nombre de lignes et de colonnes du tableau

    # Pour chaque case du tableau
    for pos_y in range(nb_li):
        for pos_x in range(nb_col):
            if reference_board[pos_y][pos_x] != "X":  # Vérifie si la case ne contient pas de mine
                nb_mines = 0  # Remise à zéro des mines dans le voisinage
                neighbors = get_neighbors(reference_board, pos_x, pos_y)  # Calcule de toutes les positions du voisinage
                for index in neighbors:  # Pour chaque voisin
                    npos_x = index[0]
                    npos_y = index[1]
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
            for index in neighbors:  # Pour chaque voisin
                npos_x = index[0]
                npos_y = index[1]
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
    possibilite = ["c", "f", "F", "C"]
    ch_de_car = input("Donner moi l'action que vous voulez faire suivit de la case (ex :f pos_x pos_y) :")

    action = ch_de_car.split(" ")  # transformer la réponse en liste de str
    while len(action) != 3 or not(0 <= int(action[2]) < n) or not(0 <= int(action[1]) < m) or not(action[0] in possibilite):  # Tant
        # que le nombre d'arg est faux, que l'indice donné est out of range ou que l'action est fausse on redemande
        print("veuillez réessayer, l'indice de la case donnée est out of range")
        ch_de_car = input("Donner moi l'action que vous voulez faire suivit de la case (ex :f 0 4) :")
        action = ch_de_car.split(" ")

    for i in range(1, 3):  # Transformer les éléments(str) contenant les coordonnées en int
        action[i] = int(action[i])
    action[0] = action[0].upper()  # Être sûr que l'action est en cap
    action = tuple(action)  # Transformer le tout en tuple
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
    game_status = False  # On part du fait que la condition de victoire est fausse

    nb_mines = len(mines_list)
    if total_flags == nb_mines:  # S'il y a autant de mines que de drapeaux
        game_status = True  # La condition de victoire est probablement remplie
        for mine in mines_list:  # Mais si pour chaque mine
            if game_board[mine[1]][mine[0]] != "F":  # Il y en a au moins une qui ne contient pas de drapeau
                game_status = False  # La condition de victoire n'est pas remplie
    else:
        case_inconnue = 0  # Nombre de cases non dévoilées
        for lignes in game_board:  # Pour chaque ligne,
            for colonne in lignes:  # Chaque case
                if colonne == "." or colonne == "F":  # Si non dévoilée
                    case_inconnue += 1  # On l'ajoute au nombre de cases non dévoilées

        if case_inconnue == nb_mines:  # S'il y a autant de mines que de cases non dévoilées
            game_status = True  # La condition de victoire est remplie
    return game_status


def init_game(n: int, m: int, number_of_mines: int):
    """
    Fonction qui initialise les paramètres du jeu

            Parameters:
                    n (int): nombre de cases en longueur du tableau
                    m (int): nombre de cases en largeur du tableau
                    number_of_mines (int): nombre de mines dans le plateau de jeu

            Return:
                    game_board (list):  list de list de chaîne de caractères correspondant au tableau de jeux
                    reference_board (list): list de list de chaîne de caractères correspondant
                                            au tableau de jeux de référence
                    mines_list (list): liste de tuples de deux entiers correspondant aux positions des mines
                                        sur le plateau de jeux
    """
    game_board = create_board(n, m)  # Initialise le tableau de jeu
    reference_board = create_board(n, m)  # Initialise le tableau de référence
    print("Votre première action.")
    first_click = parse_input(n, m)  # Demande au joueur quelle va être son action
    mines_list = place_mines(reference_board, number_of_mines, first_click[1], first_click[2])  # Remplie le tableau
    # de référence avec les mines après la première case dévoiler
    fill_in_board(reference_board)  # Remplie le tableau de référence avec le nombre de mines dans le voisinage
    propagate_click(game_board, reference_board, first_click[1], first_click[2])  # Propager le premier click
    print_board(game_board)  # imprimer le tableau

    return game_board, reference_board, mines_list


##################################################
#                                                #
#                   #main                        #
#                                                #
##################################################

def main():
    """
    Fonction principale du jeu qui appelle la fonction qui initialise le jeu et qui avec une boucle
    permet au joueur de rentrer chaque nouvelle action afin de faire avancer le jeu

            Parameters:
                    none

            Return:
                    ress (int): gives if game won or lost
    """
    ress = "pas de rep"  # Donne si le jeu est gagné
    m = int(sys.argv[1])  # Nombre de cases en largeur du plateau
    n = int(sys.argv[2])  # Nombre de cases en longueur du plateau
    number_of_mines = int(sys.argv[3])  # Nombre de mines dans le plateau

    game_param = init_game(n, m, number_of_mines)  # Renvoi le game_board, le reference_board et la mines_list

    nb_flags = 0
    game_continue = False if check_win(game_param[0], game_param[1], game_param[2], nb_flags) else True

    if not game_continue:
        ress = 1
        print("Vous avez trouvez toute les mines bien jouer")

    while game_continue:  # tant que le jeu continue
        action = parse_input(n, m)  # Le joueur est demandé une action
        if action[0] == "F":  # Si l'action est mettre
            # un drapeau
            if not (46 < ord(game_param[0][action[2]][action[1]]) < 57):  # et que la case n'est pas encore dévoilée
                if game_param[0][action[2]][action[1]] == "F":  # S'il y a déjà un drapeau
                    game_param[0][action[2]][action[1]] = "."
                    nb_flags -= 1  # Le nombre de drapeaux diminue de 1
                else:  # sinon
                    game_param[0][action[2]][action[1]] = action[0]
                    nb_flags += 1  # le nombre de drapeaux augmente de 1
        else:  # Si c'est dévoilé une case
            if action[0] == "C" and game_param[1][action[2]][action[1]] == "X":  # Et que le joueur tombe sur une mine
                ress = 0  # Le jeu est perdu
                game_continue = False  # Le jeu est arrêté
                print("Vous êtes tombé sur une mine, le jeux est terminer")
            else:  # Sinon
                propagate_click(game_param[0], game_param[1], action[1], action[2])  # le tableau est modifié

        print_board(game_param[0])

        if check_win(game_param[0], game_param[1], game_param[2], nb_flags):  # Si la condition de victoire est remplie
            ress = 1  # Le jeu est gagné
            game_continue = False  # Le jeu est arrêté
            print("Vous avez trouvez toute les mines bien jouer")
            print("         ||                 ||")
            print("")
            print("       __                     __")
            print("         __                 __")
            print("           -----------------")

    return ress


if __name__ == "__main__":  # Permet d'importer la fonction dans d'autres fichiers sans anomalies
    main()
