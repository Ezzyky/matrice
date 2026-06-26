
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

