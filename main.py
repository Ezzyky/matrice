from functions import *
import msvcrt
import os
import sys
os.system("cls") 

#affichage de menu et input d option et clear
menu()
option=int(input())
os.system("cls") 
while True:
    #option 1 = reduction de gauss
    if option==1:
        #handling the Error of value
        flag=0
        try:
            matrice=prenant_matrice()
        except ValueError:
            print("lab")
            print("Appuyez sur n'importe quel bouton pour sortir...")
            msvcrt.getch()
            os.system("cls")
            flag=1
        if flag==0:
            lignes=len(matrice)
            colonnes=len(matrice[0])
            os.system("cls")
            print("Matrice initiale :")
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
                affichage(matrice)
                print()
            #affichge de resulta fianle
            print("resulta finale:")
            affichage(matrice)
            print()
            print("Appuyez sur n'importe quel bouton pour sortir...")
            msvcrt.getch()
            os.system("cls") 

    #affichage de menu et input d option et clear
    menu() 
    option=int(input())
    os.system("cls")
    #option 2 = Méthode de Gauss-Jordan
    if option==2:
        pass