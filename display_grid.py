import tkinter as tk
from grid_2048 import init_grid, add_new_tile, position_de_new_tile
from deplacements import move_grid
from fin_du_jeu import is_game_over, is_grid_full, est_gagnante


## Constantes
# grid = [[2, 4, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 4096], [8192, 8, 2, 2]]
grid = init_grid(4)
n = len(grid)
taille = 400 # Taille de la fenêtre
color_tuile={2:'antique white', 4:'bisque', 8: 'tan1', 16:'orange', 32:'tomato', 64:'orange red', 128 :'lemon chiffon', 256 :'khaki', 512 :'yellow', 1024:'gold', 2048:'gold2', 4096:'MediumOrchid1', 8192:'purple1'}


## Indicateurs 
player_wants_to_continue = True
player_has_saved = True # indicateur pour savoir si le joueur a sauvegardé


## Initialisation de la fenêtre de jeu
root = tk.Tk()
f1 = tk.Frame(root, bd=1, relief='solid')
primary_window = tk.Toplevel(f1)
primary_window.title("top2048")
root.title("2048")
background = tk.Frame(root)
grille = tk.Canvas(background, bg = "#ABA39B", height = taille, width = taille)


# Fonctions concernant l'interface graphique 

def graphical_grid_init_2048(n, grille): # Initialisation des lignes
    for i in range(0, n+1):
        _ = grille.create_line(i*taille/n, 0, i*taille/n, taille, fill = "#A49C8C", width = 3)
        _ = grille.create_line(0, i*taille/n, taille, i*taille/n, fill = "#A49C8C", width = 3)

def remplir_grille_avec_valeurs(grid, grille):
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                _ = grille.create_rectangle((j*taille/n, i*taille/n), ((j+1)*taille/n, (i+1)*taille/n), fill = color_tuile[grid[i][j]])
                _ = grille.create_text(j*taille/n + 50, i*taille/n + 50, text=str(grid[i][j]), font="Arial")


def key_press_event(evt):
    event = evt.keysym
    global player_wants_to_continue
    global player_has_saved
    global grid
    global n
    Liste_des_grilles=[]
    grille.delete("all") # On supprime la grille de l'écran pour en afficher une nouvelle
    if event=='Left' or event=='KP_Left':
        move_grid(grid, "left")
        player_has_saved = False
        Liste_des_grilles.append(grid)
    if event=='Right' or event=='KP_Right':
        move_grid(grid, "right")
        player_has_saved = False
        Liste_des_grilles.append(grid)
    if event=='Up' or event=='KP_Up':
        move_grid(grid, "up")
        player_has_saved = False
        Liste_des_grilles.append(grid)
    if event=='Down' or event=='KP_Down' :
        move_grid(grid, "down")
        player_has_saved = False
        Liste_des_grilles.append(grid)
    
    L = ['Down', 'KP_Down', 'Left', 'KP_Left', 'Right', 'KP_Right', 'Up', 'KP_Up']
    if not is_grid_full(grid) and event in L: # on ne rajoute pas de tuile si le joueur sauvegarde ou quitte
        position = position_de_new_tile(grid)
        grid = add_new_tile(grid, position)
    if player_wants_to_continue:
        graphical_grid_init_2048(n, grille)
        remplir_grille_avec_valeurs(grid, grille)
    if is_game_over(grid):
        if est_gagnante(grid):
            print("Victoire !") # Peut-être mettre une petite fenêtre pop-up pour dire bravo ?
        else:
            print("Défaite !")

# grid, theme, k = interface_debut() # n est le numéro du fichier de sauvegarde
    # Ce k permet de re-sauvegarder la partie au même endroit la prochaine fois


         
#     elif choix == 's':
#         i = 0
#         if k > 0: # Si ce n'est pas une nouvelle partie
#             choice = input("Voulez-vous écraser le dernier fichier de sauvegarde (entrez 0) ou en créer un nouveau (entrez 1)")
#             verifier_format(choice)
#             if int(choice) == 0:
#                 ecraser_sauvegarde("save" + str(k) + ".txt")
#                 sauvegarde(grid, theme, k)
#             else:
#                 i = premier_fichier_non_existant()
#                 sauvegarde(grid, theme, i)
#         else:
#             i = premier_fichier_non_existant()
#             sauvegarde(grid, theme, i)
#         print("La partie a été sauvegardée sur la partie " + str(max(i, k)))
#         player_has_saved = True
#     elif choix == 'q':
#         if not player_has_saved:
#             do_you_want_to_leave = input("Vous n'avez pas sauvegardé, voulez-vous tout de même quitter ? (oui : 1, non : 2) ")
#             verifier_format(do_you_want_to_leave)
#             if int(do_you_want_to_leave) == 1:
#                 player_wants_to_continue = False
#         else:
#             player_wants_to_continue = False
    

graphical_grid_init_2048(n, grille)
remplir_grille_avec_valeurs(grid, grille)
grille.bind_all('<Key>', key_press_event)


background.pack()
grille.pack()
root.mainloop()

