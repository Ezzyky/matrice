def multiplication_scalaire(matrice,scalaire):
    matrice_m=[[None for i in range(len(matrice[0]))]for i in range(len(matrice))]
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            matrice_m[i][j]=scalaire*matrice[i][j]
            print(f"{matrice[i][j]} X {scalaire}  ",end="")
            print()
    return matrice_m
    
def addition(matrice1,matrice2):
    matrice_add=[[None for i in range(len(matrice2[0]))]for i in range(len(matrice2))]
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):

            matrice_add[i][j]=matrice1[i][j]+matrice2[i][j]
            print(f"{matrice1[i][j]} + {matrice2[i][j]}  ",end="")
            print()
    return matrice_add

def souetraction(matrice1,matrice2):
    matrice_add=[[None for i in range(len(matrice2[0]))]for i in range(len(matrice2))]
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):

            matrice_add[i][j]=matrice1[i][j]-matrice2[i][j]
            print(f"{matrice1[i][j]}-{matrice2[i][j]}  ",end="")
            print()
    return matrice_add