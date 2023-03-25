
###################################################################################################################

def deplacement_ligne_gauche(L) :
    longueur_ligne = len(L)
    for i in range (longueur_ligne):                                    #on somme les cases qui doivent être sommées ensemble
        v = L[i]
        for j in range (i+1,longueur_ligne):    
            if L[j]!=v and L[j]!=0 and L[j]!=' ':
                break              
            elif L[j]==v:
                L[i]=2*v
                L[j]=0
                break

    indices_cases_remplies=[]                                             #on cherche quelles cases sont non vides
    for i in range (longueur_ligne):
        if L[i]!=0 and L[i]!=' ':
            indices_cases_remplies.append(i)
        
    T=L.copy()
    for i in range (1,longueur_ligne):
        k=i
        while k>0 and (T[k-1]==0 or T[k-1]==' '):
            k-=1
        T[i],T[k]=T[k],T[i]
    return T

#############################################################################################################

def deplacement_ligne_droite(L) :
    T=[]
    R=[]
    for i in range(len(L)):
        T.append(L[-i-1])
    X = deplacement_ligne_gauche(T)
    for i in range(len(L)):
        R.append(X[-i-1])
    return R


import numpy as np
def deplacement_col_up(I) :
    J=np.array(I)
    Y=J.transpose()
    L=Y.tolist()[0]
    
    longueur_ligne = len(L)
    for i in range (longueur_ligne):                                    #on somme les cases qui doivent être sommées ensemble
        v = L[i]
        for j in range (i+1,longueur_ligne):
            if L[j]!=v and L[j]!=0 and L[j]!=' ':
                break
            elif L[j]==v:
                L[i]=2*v
                L[j]=0
                break
    indices_cases_remplies=[]                                             #on cherche quelles cases sont non vides
    for i in range (longueur_ligne):
        if L[i]!=0 and L[i]!=' ':
            indices_cases_remplies.append(i)
    T=L.copy()
    for i in range (1,longueur_ligne):
        k=i
        while k>0 and (T[k-1]==0 or T[k-1]==' '):
            k-=1
        T[i],T[k]=T[k],T[i]

    X=np.array(T)
    K=X.transpose()
    P=K.tolist()
    
    G=[[i]for i in P]
    
    return(G)

############################################################################################################

def deplacement_col_down(I) :
    J=np.array(I)
    Y=J.transpose()
    L=Y.tolist()[0]

    T=[]
    R=[]
    for i in range(len(L)):
        T.append(L[-i-1])
    X = deplacement_ligne_gauche(T)
    for i in range(len(L)):
        R.append(X[-i-1])

    Z=np.array(R)
    K=Z.transpose()
    P=K.tolist()

    G=[[i]for i in P]

    return(G)

#########################################################################################################

def move_grid(grid,d):
    n = len(grid)
    if d=='left':
        for i in range (n):
            grid[i]=deplacement_ligne_gauche(grid[i])
    elif d =='right':
        for i in range (n):
            grid[i]=deplacement_ligne_droite(grid[i])
    elif d =='up':
        for i in range(n):
            L=[[grid[j][i]] for j in range (n)]
            L=deplacement_col_up(L)
            for j in range(n):
                grid[j][i]=L[j][0]
    elif d =='down':
        for i in range(n):
            L=[[grid[j][i]] for j in range (n)]
            L=deplacement_col_down(L)
            for j in range(n):
                grid[j][i]=L[j][0]
    return(grid)

