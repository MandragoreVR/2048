# Fichier de test pour le fichier fin_du_jeu.py

from grid_2048 import init_grid
from fin_du_jeu import *

def test_is_full_grid():
    grille = init_grid(4)
    grille_pleine = [[2 for i in range(n)] for i in range(n)]
    assert not is_grid_full(grille)
    assert is_grid_full(grille_pleine)

def test_moves():
    grille_a = [[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]
    grille_b = [[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]
    grille_c = [[2, 4, 8, 16], [16, 8, 8, 2], [2, 4, 8, 16], [16, 8, 4, 2]]
    assert move_down_possible(grille_a) == True
    assert move_down_possible(grille_b) == False
    assert move_up_possible(grille_a) == True
    assert move_up_possible(grille_b) == False
    assert move_left_possible(grille_a) == True
    assert move_left_possible(grille_b) == False
    assert move_left_possible(grille_c) == True
    assert move_right_possible(grille_c) == True
    assert move_right_possible(grille_a) == True
    assert move_right_possible(grille_b) == False
    assert move_possible(grille_a) == [True, True, True, True]
    assert move_possible(grille_b) == [False, False, False, False]

def test_is_game_over():
    grille_a = [[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]
    grille_b = [[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]
    assert is_game_over(grille_b)
    assert not is_game_over(grille_a)

def test_get_grid_tile_max():
    grille_a = [[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]
    grille_b = [[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]
    assert get_grid_tile_max(grille_a) == 32
    assert get_grid_tile_max(grille_b) == 16

def test_est_gagnante():
    grille_a = [[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]
    grille_b = [[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 4092], [16, 8, 4, 2]]
    assert not est_gagnante(grille_a)
    assert est_gagnante(grille_b)
