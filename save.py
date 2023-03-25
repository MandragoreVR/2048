# Fonctionnalité de sauvegarde de la grille en cours

import os
from grid_2048 import init_grid
os.getcwd()

if __name__ == "__main__":
    os .mkdir("Saves")
os.chdir("Saves")

def file_exists(n): # Vérifie si le fichier de sauvegarde numéro n existe
    try:
        f = open("save" + str(n) + ".txt", 'r')
        return True
    except:
        return False

def premier_fichier_non_existant():
    i = 1
    while file_exists(i):
        i += 1
    return i
# Cette dernière fonction permet au système de sauvegarde de savoir sur quel fichier sauvegarder la partie en cours
# i.e. si les fichiers 1, 2, 3, ..., 10 sont déjà pris, cela sera sauvegardé sur le 11è


def sauvegarde(grid, theme, nombre):  # Sauvegarde la grille grid dans fichier de sauvegarde n° nombre 
    try:
        f = open('save' + str(nombre) + '.txt', 'x')
        n = len(grid)
        f.write(theme + '\n') # On stocke le thème pour un futur affichage
        for i in range(n):
            for j in range(n):
                f.write(str(grid[i][j]) + ",")
            f.write("\n")
        f.close()
    except:
        print("Une sauvegarde existe déjà à la place du fichier " + str(nombre))


def ecraser_sauvegarde(string):
    os.remove(string)


def recuperation(string):
    f = open(string, 'r')
    file = f.read().split("\n")
    f.close()
    n = len(file) - 2 # Taille de la grille, qui est carrée (-2 car la première ligne contient le thème, et la dernière contient '')
    grid = [[0 for i in range(n)] for i in range(n)]
    for i in range(1, n+1):
        valeurs = file[i].split(',')
        valeurs.pop(-1) # Le dernier élément de valeurs est '', on n'en veut pas
        for j in range(n):
            grid[i-1][j] = int(valeurs[j])
    return grid, file[0]
