from functions import *
import msvcrt
import os
import sys
os.system("cls") 


while True:

    print("""
            =========================================================
                BIENVENUE DANS LE PROGRAMME D'ALGÈBRE LINÉAIRE
            =========================================================

            Ce programme permet d'effectuer plusieurs opérations sur
            les matrices et les systèmes linéaires.

            Veuillez d'abord saisir la matrice initiale, puis choisir
            l'opération souhaitée dans le menu suivant.

    """)
    print("Appuyez sur n'importe quel bouton pour contune...")
    msvcrt.getch()
    os.system("cls")
    print("""
            =========================================================
                    Veuillez entrer la matrice initiale.
            =========================================================
    """)
    flag=0
    try:
        matrice=prenant_matrice()
    except ValueError:
                print("Veuillez entrer un nombre valide !(un nombre entier).")
                print()
                print("Appuyez sur n'importe quel bouton pour sortir...")
                msvcrt.getch()
                os.system("cls")
                flag=1
                continue
    if flag!=1:
        #affichage de menu et input d option et clear
        os.system("cls")
        menu()
        option=int(input("Choisissez une option : "))
        os.system("cls") 


        #option 1 = reduction de gauss
        if option==1:
                lignes=len(matrice)
                colonnes=len(matrice[0])
                print("""
    =========================================================
                    Réduction de Gauss
    =========================================================
                """)
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
                else:
                    print()
                    print("La matrice contient une seule ligne. Aucune élimination n'est nécessaire.")
                    option=int(input("Choisissez une option : "))
                    os.system("cls")
                #affichge de resulta fianle
                print("resulta finale:")
                affichage(matrice)
                print()
                print("Appuyez sur n'importe quel bouton pour sortir...")
                msvcrt.getch()
                os.system("cls")

        #option 2 = Méthode de Gauss-Jordan
        elif option==2:
            pass
        #option 5 = Addition de matrices

        if option==5:
            flag=0
            try:
                matrice=prenant_matrice()
            except ValueError:
                    print("Veuillez entrer un nombre valide !(un nombre entier).")
                    print()
                    print("Appuyez sur n'importe quel bouton pour sortir...")
                    msvcrt.getch()
                    os.system("cls")
                    flag=1
                    continue
            if flag!=1:
                os.system("cls")


        if option==0:
            print("GOOD BYE!")
            sys.exit()
        print("Appuyez sur n'importe quel bouton pour continuer...")
        msvcrt.getch()
        os.system("cls")
