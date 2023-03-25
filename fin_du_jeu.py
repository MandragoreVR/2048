# Fonctionnalité 5
from grid_2048 import init_grid
from affichage_grille import display_grid_themes

n = 4
grille = init_grid(n)
grille_pleine = [[2 for i in range(n)] for i in range(n)]

def is_grid_full(grid): # Indique si la grille est pleine ou non
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ' ' or grid[i][j]==0:
                return False
    return True

def move_down_possible(grid):
    n = len(grid)
    for i in range(1, n):
        for j in range(n):
            if grid[i][j] != 0 and grid[i-1][j] == grid[i][j]: # Si deux éléments consécutifs dans une colonne sont égaux, on peut
                # bouger vers le bas
                return True
    for j in range(n):
        colonne = [grid[i][j] for i in range(n)]
        for i in range(n):
            if colonne[i] == 0 and colonne[:i] != [0]*i:
                return True
    return False

def move_up_possible(grid): # Le fonctionnement est sensiblement le même, seules les bornes des boucles changent
    n = len(grid)
    for i in range(n-1):
        for j in range(n):
            if grid[i][j] == grid[i+1][j] and grid[i][j] != 0:
                return True
    for j in range(n):
        colonne = [grid[i][j] for i in range(n)]
        for i in range(n):
            if colonne[i] == 0 and colonne[i:] != [0]*(n-i):
                return True
    return False

def move_right_possible(grid): # même chose mais verticalement
    n = len(grid)
    for i in range(n):
        for j in range(1, n):
            if grid[i][j] != 0 and grid[i][j-1] == grid[i][j]:
                return True
        for j in range(n):
            if grid[i][j] == 0 and grid[i][:j] != [0]*j:
                return True
    return False

def move_left_possible(grid): # Indique si un mouvement à gauche est possible
    n = len(grid)
    for i in range(n):
        for j in range(n-1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1]:
                return True
        for j in range(n):
            if grid[i][j] == 0 and grid[i][j:] != [0]*(n-j):
                return True
            # idem de l'autre côté
    return False

if __name__ == "__main__":
    None


def move_possible(grid):
    # Indique si le mouvement est possible à [haut, bas, droite, gauche]
    return [move_up_possible(grid), move_down_possible(grid), move_right_possible(grid), move_left_possible(grid)]


# Test de la fin du jeu

def is_game_over(grid):
    return is_grid_full(grid) and move_possible(grid) == [False]*4


# Récupération de la tuile maximale pour savoir si le jeu est gagnant

def get_grid_tile_max(grid):
    tile_max = 0
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] > tile_max:
                tile_max = grid[i][j]
    return tile_max

def est_gagnante(grid):
    return get_grid_tile_max(grid) >= 2048