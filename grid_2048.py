from random import *


def create_grid(nombre_cases):
    grille = []
    for i in range(nombre_cases):
        grille.append([])
        for j in range(nombre_cases):
            grille[i].append(
                0
            )  #On remplit la grille de listes vides, que l'on remplit elles-mêmes de chaînes de caractères vides ' '
    return grille


def init_grid(n):
    grid = create_grid(n)
    position = position_de_new_tile(grid)
    grid = add_new_tile(grid, position) # ajout de la première tuile
    position = position_de_new_tile(grid)
    grid = add_new_tile(grid, position) # ajout de la deuxième
    return(grid)


def get_empty_tiles_positions(grid):
    nb_de_lignes = len(grid)

    liste_des_positions = []
    for i in range(nb_de_lignes):
        for j in range(nb_de_lignes):

            if grid[i][j] == 0 or grid[i][j] == ' ':
                liste_des_positions.append((i, j))

    return liste_des_positions


def position_de_new_tile(grid):
    liste_des_positions = get_empty_tiles_positions(grid)
    taille_list_posi_libres = len(liste_des_positions)
    i = randint(0, taille_list_posi_libres - 1)
    position_nouvelle_tuile = liste_des_positions[i]
    return position_nouvelle_tuile


def get_value_new_tile():
    i = randint(0, 9)
    if i == 9:
        return 4
    else:
        return 2


def add_new_tile(grid, position):
    valeur = get_value_new_tile()
    grid[position[0]][position[1]] = valeur
    return grid
