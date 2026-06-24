def prenant_matrice():
    print("Saisissez la taille de la matrice:")
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
    lignes=len(matrice)
    colonnes=len(matrice[0])
    for i in range(lignes):
        for j in range(colonnes):

            print(matrice[i][j],end=" ")
        print()

def elimination_gauss(matrice, pivot):
    lignes = len(matrice)
    colonnes = len(matrice[0])

    for j in range(pivot + 1, lignes):
        if matrice[j][pivot] != 0:

            a = matrice[j][pivot]
            p = matrice[pivot][pivot]
            print(f"L{j+1} ← {p}L{j+1} - {a}L{pivot+1}")
            for i in range(pivot, colonnes):
                matrice[j][i] = matrice[j][i] * p - matrice[pivot][i] * a
