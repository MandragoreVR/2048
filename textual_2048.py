import mise_en_orchestre

def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas), s (sauvegarder), q (quitter)): ")
    while move not in ['g', 'd', 'h', 'b', 's', 'q']: 
        move=input("Entrez une commande reconnue : ")
    return move

def read_size_grid():
    size = input("Avec quelle taille de grille voulez-vous jouer ? Entrez un entier supérieur à 2 : ")
    try :
        int(size)
        if int(size)>=2:
            return(int(size))
        else:
            print("La valeur que vous avez indiquée n'est pas valide. La valeur par défaut a donc été mise (grille 4*4)")
            return(4)
    except(ValueError):
        print("La valeur que vous avez indiquée n'est pas valide. La valeur par défaut a donc été mise (grille 4*4)")
        return(4)

def read_theme_grid():
    theme = input("Avec quel thème voulez-vous jouer ? Entrez 0 pour le thème classique, 1 pour le thème chimie et 2 pour le thème alphabet : ")
    while theme!='2' and theme!='1' and theme!='0':
            theme=input("Les seuls thèmes possibles sont 0 (Classique), 1 (Chimie), 2 (Alphabet). Entrez l'un de ces thèmes pour jouer :")
    return theme


if __name__ == '__main__':
    mise_en_orchestre.game_play()
    exit(1)  
