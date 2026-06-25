def prenant_matrice(nom="A"):
    print(f"Saisissez la taille de la matrice {nom}:")
    
    lignes=int(input("Nombre de lignes : "))
    colonnes=int(input("Nombre de colonnes : "))
    while lignes==0 or colonnes == 0:
        print("Erreur : le nombre de lignes et de colonnes doit être supérieur à 0.")
        lignes=int(input("Nombre de lignes : "))
        colonnes=int(input("Nombre de colonnes : "))
    Matrice=[[None for i in range(colonnes)]for i in range (lignes)]
    for i in range(lignes):
        for j in range (colonnes):
            Matrice[i][j]=int(input(f"M[{i+1}][{j+1}] = "))
    return Matrice

def affichage(matrice):
    lignes =len(matrice)
    for i in range(lignes):
        if i==0:
            debut,fin="⎡", "⎤"
        elif i==lignes-1:
            debut,fin="⎣", "⎦"
        else:
            debut,fin="⎢", "⎥"
        print(debut, end=" ")
        for x in matrice[i]:
            print(x,end=" ")
        print(fin)

def elimination_gauss(matrice, pivot):

    lignes = len(matrice)
    colonnes = len(matrice[0])
    print("_________Opérations effectuées sur les lignes :_________")
    print()
    for j in range(pivot + 1, lignes):
        if matrice[j][pivot] != 0:

            a = matrice[j][pivot]
            p = matrice[pivot][pivot]
            if a<0:
                print(f"L{j+1} ← {p}L{j+1} + {a*(-1)}L{pivot+1}")
            else:
                print(f"L{j+1} ← {p}L{j+1} - {a}L{pivot+1}")
            for i in range(pivot, colonnes):
                matrice[j][i] = matrice[j][i] * p - matrice[pivot][i] * a

def menu():

    print("""
=========================================================
             APPLICATION D'ALGÈBRE LINÉAIRE
=========================================================

            1 - Réduction de Gauss
            2 - Méthode de Gauss-Jordan
            3 - Calcul du déterminant
            4 - Inverse d'une matrice
            5 - Addition de matrices
            6 - Soustraction de matrices
            7 - Multiplication de matrices
            8 - Multiplication par un scalaire
            9 - Transposée d'une matrice
            10 - Rang d'une matrice
            11 - Résolution d'un système linéaire
            0 - Quitter

=========================================================
          """)
def Multiplication_scalaire(matrice,scalaire):
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            matrice_m=[[None for i in range(len(matrice[0]))]for i in range(len(matrice))]
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