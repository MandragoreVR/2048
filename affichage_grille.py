from grid_2048 import init_grid
from deplacements import move_grid

def long_value(grille):
    m=0
    for i in range(len(grille)):
        for j in range(len(grille)):
            if len(str(grille[i][j])) > m:
                m=len(str(grille[i][j]))
    return(m)

def display_grid(grille):
    m=max(long_value(grille),3)
    visuel_grille=''
    string_egal=' '
    for _ in range(m):
        string_egal=string_egal+'='
    for _ in range(len(grille)):
        visuel_grille=visuel_grille+string_egal
    visuel_grille=visuel_grille+'\n'

    for ligne in range(len(grille)):
        visuel_grille=visuel_grille+'|'
        for j in range(len(grille[ligne])):
            visuel_grille = visuel_grille + str((grille[ligne][j])).center(m)+'|'
        visuel_grille=visuel_grille+'\n'
        for _ in range(len(grille)):
            visuel_grille=visuel_grille+string_egal
        visuel_grille=visuel_grille+'\n'

    print(visuel_grille)

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def display_grid_themes(grille, theme='0'): #Mettre theme='0' pour le classique, '1' pour la chimie, '2' pour l'alphabet
    m=max(long_value(grille),3)
    visuel_grille=''
    string_egal=' '
    for _ in range(m):
        string_egal=string_egal+'='
    for _ in range(len(grille)):
        visuel_grille=visuel_grille+string_egal
    visuel_grille=visuel_grille+'\n'

    for ligne in range(len(grille)):
        visuel_grille=visuel_grille+'|'
        for j in range(len(grille[ligne])):
            if grille[ligne][j]==' ':
                visuel_grille = visuel_grille + str((grille[ligne][j])).center(m)+'|'
            else:
                visuel_grille = visuel_grille + THEMES[theme][grille[ligne][j]].center(m)+'|'
        visuel_grille=visuel_grille+'\n'
        for _ in range(len(grille)):
            visuel_grille=visuel_grille+string_egal
        visuel_grille=visuel_grille+'\n'

    print(visuel_grille)    

# grille = init_grid(4)
# display_grid_themes(grille)
# move_grid(grille, "up")
# print(grille)
# move_grid(grille, "right")
# print(grille)