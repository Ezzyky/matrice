from functions import *
import msvcrt
import os

menu()
option=int(input())
os.system("cls")    
if option==1:
    matrice=prenant_matrice()
    lignes=len(matrice)
    colonnes=len(matrice[0])
    print("Matrice initiale :")
    print()
    affichage(matrice)
    # Permutation des lignes L1 et la première ligne dont le premier élément est non nul
    index=0
    if lignes>=2:
        if matrice[0][0]==0:

            for i in range(lignes):
                if matrice[i][0]!=0:
                    index=i
                    break

            for i in range(colonnes):
                temp=matrice[0][i]
                matrice[0][i]=matrice[index][i]
                matrice[index][i]=temp
            print(f"L1 ​↔ L​{index+1}")
            affichage(matrice)
    for pivot in range(0,min(len(matrice), len(matrice[0]))):
        if matrice[pivot][pivot] == 0:
            index = -1
            for i in range(pivot + 1, lignes):
                if matrice[i][pivot] != 0:
                    index = i
                    break
            if index != -1:
                matrice[pivot], matrice[index] = matrice[index], matrice[pivot]
                print(f"L{pivot+1} ↔ L{index+1}")
                
        elimination_gauss(matrice, pivot)
        print("resulta finale:")
        affichage(matrice)
        print()
    print("entrer wzged")
    msvcrt.getch()
    os.system("cls")   
menu() 