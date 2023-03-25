## Fonctionnalité 6

from grid_2048 import init_grid, position_de_new_tile, add_new_tile
from deplacements import move_grid
from fin_du_jeu import is_game_over, move_possible, est_gagnante, is_grid_full, move_possible
from affichage_grille import display_grid_themes
from random import randint
from save import *
import textual_2048 as tex

## Paramètres par défaut 
# Taille de la grille 
n = 6
# Thème de la grille
t = '0'

def random_play():
    grid = init_grid(n)
    display_grid_themes(grid, t)
    while not is_game_over(grid):
        moves = move_possible(grid) 
        i = randint(0, 3)
        while not moves[i]:
            i = randint(0, 3)
        if i == 0:
            print("Mouvement vers le haut : \n")
            move_grid(grid, "up")
        elif i == 1:
            print("Mouvement vers le bas : \n")
            move_grid(grid, "down")
        elif i == 2:
            print("Mouvement vers la droite : \n")
            move_grid(grid, "right")
        elif i == 3:
            print("Mouvement vers la gauche : \n")
            move_grid(grid, "left")
        position = position_de_new_tile(grid)
        grid = add_new_tile(grid, position)
        display_grid_themes(grid, t)
    if est_gagnante(grid):
        print("Victoire !")
    else:
        print("Défaite !")

#random_play()


def game_play():
    grid, theme, k = interface_debut() # n est le numéro du fichier de sauvegarde
    # Ce k permet de re-sauvegarder la partie au même endroit la prochaine fois
    display_grid_themes(grid,theme)
    player_wants_to_continue = True
    player_has_saved = True # indicateur pour savoir si le joueur a sauvegardé
    while player_wants_to_continue and not is_game_over(grid):
        choix = tex.read_player_command()
        moves = move_possible(grid)
        if choix=='h':
            print("Mouvement vers le haut : \n")
            move_grid(grid, "up")
            player_has_saved = False
            i = 0 # Indique quel mouvement est choisi dans la liste moves
        elif choix=='b':
            print("Mouvement vers le bas : \n")
            move_grid(grid, "down")
            player_has_saved = False
            i = 1
        elif choix=='d':
            print("Mouvement vers la droite : \n")
            move_grid(grid, "right")
            player_has_saved = False
            i = 2
        elif choix=='g':
            print("Mouvement vers la gauche : \n")
            move_grid(grid, "left")
            player_has_saved = False 
            i = 3
        elif choix == 's':
            i = 0
            if k > 0: # Si ce n'est pas une nouvelle partie
                choice = input("Voulez-vous écraser le dernier fichier de sauvegarde (entrez 0) ou en créer un nouveau (entrez 1)")
                verifier_format(choice)
                if int(choice) == 0:
                    ecraser_sauvegarde("save" + str(k) + ".txt")
                    sauvegarde(grid, theme, k)
                else:
                    i = premier_fichier_non_existant()
                    sauvegarde(grid, theme, i)
            else:
                i = premier_fichier_non_existant()
                sauvegarde(grid, theme, i)
            print("La partie a été sauvegardée sur la partie " + str(max(i, k)))
            player_has_saved = True
        elif choix == 'q':
            if not player_has_saved:
                do_you_want_to_leave = input("Vous n'avez pas sauvegardé, voulez-vous tout de même quitter ? (oui : 1, non : 2) ")
                verifier_format(do_you_want_to_leave)
                if int(do_you_want_to_leave) == 1:
                    player_wants_to_continue = False
            else:
                player_wants_to_continue = False
        if not is_grid_full(grid) and choix not in ['s', 'q'] and moves[i]: # on ne rajoute pas de tuile si le joueur sauvegarde ou quitte
            # le moves[i] permet d'assurer qu'on n'ajoute pas de tuile si le mouvement demandé n'est pas possible
            position = position_de_new_tile(grid)
            grid = add_new_tile(grid, position)
        if player_wants_to_continue: # Si le joueur ne veut plus jouer, on n'affiche pas la grille
            display_grid_themes(grid, theme)
    if is_game_over(grid):
        if est_gagnante(grid):
            print("Victoire !")
        else:
            print("Défaite !")
    # Si le jeu n'est pas fini mais que le joueur a simplement voulu quitter, on ne fait rien
        

def verifier_format(config, min = 0): # Cette fonction vérifie que config est une chaîne de caractère contenant
    # un entier supérieur ou égal à min
    bool = True
    while bool: # Boucle pour s'assurer que l'on obtient un entier positif dans l'input
        try:
            if int(config) >= min: # Si config n'est pas de la forme str(n) avec n entier, il y a une erreur
                bool = False
            else:
                config = input("Veuillez entrer un entier supérieur ou égak à " + str(min) + " : ")
        except:
            config = input("La saisie ne convient pas : ")

def interface_debut():
    config = input("Pour démarrer une nouvelle partie, entrer 0. Pour charger une partie sauvegardée, entrer le numéro de la partie : \n")
    verifier_format(config)
    if int(config) == 0:
        taille = tex.read_size_grid()
        theme = tex.read_theme_grid()
        grid=init_grid(taille)
    else:
        try:
            grid, theme = recuperation("save" + config + ".txt")
        except FileNotFoundError:
            print("Le fichier " + config + " n'existe pas")
            grid, theme, config = interface_debut()
    return grid, theme, int(config)

if __name__ == "__main__":
    game_play()
    # config = 2.0
    # if config >= 0:
    #         config = int(config)
    #         bool = False
    # else:
    #     config = input("Veuillez entrer un entier positif : ")
    # print(bool, config)






####################################################################################################################



def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    while move!='g' and move!='d' and move!='h' and move!='b':
        move=input("Les seuls mouvements possibles sont g (gauche), d (droite), h (haut), b (bas). Entrez l'un de ces mouvements pour jouer :")
    return move





################################################################################################################




# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('taille')
# parser.add_argument('theme')
# args = parser.parse_args()
# if int(args.taille)>=2 and int(args.theme) in [0,1,2] :
#     grid=init_grid(int(args.taille))
#     display_grid_themes(grid,args.theme)
#     while not is_game_over(grid):
#         choix=read_player_command()
#         if choix=='h':
#             print("Mouvement vers le haut : \n")
#             move_grid(grid, "up")
#         elif choix=='b':
#             print("Mouvement vers le bas : \n")
#             move_grid(grid, "down")
#         elif choix=='d':
#             print("Mouvement vers la droite : \n")
#             move_grid(grid, "right")
#         elif choix=='g':
#             print("Mouvement vers la gauche : \n")
#             move_grid(grid, "left")
#         if not is_grid_full(grid):
#             position = position_de_new_tile(grid)
#             grid = add_new_tile(grid, position)
#         display_grid_themes(grid, args.theme)
#     if est_gagnante(grid):
#         print("Victoire !")
#     else:
#         print("Défaite !")

