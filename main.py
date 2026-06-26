from matrice_io import *
from gauss import *
from menu_txtes import *
from operations import *
from utils import *
import os
import sys
os.system("cls") 
while True:

    home()
    clear_avec_msg()
    titre("Veuillez entrer la matrice initiale.")
    flag=0
    try:
        matrice=prenant_matrice()
    except ValueError:
                print()
                print("Veuillez entrer un nombre valide !(un nombre entier).")
                clear_avec_msg()
                flag=1
                continue
    if flag!=1:
        #affichage de menu et input d option et clear
        os.system("cls")
        menu()
        try:
            option = int(input("Choisissez une option : "))
        except ValueError:
            clear_avec_msg("Option invalide.")
            continue
        os.system("cls") 


        #option 6 = reduction de gauss
        if option==6:
                lignes=len(matrice)
                colonnes=len(matrice[0])
                titre("   Réduction de Gauss")
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
                    clear_avec_msg()
                    continue
                #affichge de resulta fianle
                print("resulta finale:")
                affichage(matrice)
                print()
                clear_avec_msg()

        #option 2 = Méthode de Gauss-Jordan
        elif option==2:
            pass
        
        #option 3 = Calcul du déterminant
        elif option==3:
             pass
        
        #option 4 = Inverse d'une matrice
        elif option==4:
             pass
        
        #option 1 = Addition 
        elif option==1:
            titre("Addition de matrices.")
            try:
                matrice_pour_add=prenant_matrice(nom="B")
            except ValueError:
                    print("Veuillez entrer un nombre valide !(un nombre entier).")
                    print()
                    clear_avec_msg()
                    continue
            
            os.system("cls")
            lignes_B=len(matrice_pour_add)
            colonnes_B=len(matrice_pour_add[0])
            if len(matrice)!=lignes_B or len(matrice[0])!=colonnes_B:
                print("Addition impossible : dimensions incompatibles.")
                clear_avec_msg()
                continue
            
            print("Matrice initiale :")
            print()
            affichage(matrice)
            print()
            print("Matrice à ajouter :")    
            print()
            affichage(matrice_pour_add)
            print()
            print("la methode:")
            adition_matrice=addition(matrice,matrice_pour_add)
            print()
            print("Résultat de l'addition :")
            print()
            affichage(adition_matrice)
            if all(all(x==0 for x in lignes)for lignes in adition_matrice ):
                print("-----> La matrice est une matrice nulle!")
            clear_avec_msg()

        #option 2 = Soustraction de matrices
        elif option==2:
            print("""
            =========================================================
                              Soustraction de matrices
            =========================================================
    """)
            try:
                matrice_pour_sost=prenant_matrice(nom="B")
            except ValueError:
                    print("Veuillez entrer un nombre valide !(un nombre entier).")
                    print()
                    clear_avec_msg()
                    continue
            
            os.system("cls")
            lignes_B=len(matrice_pour_sost)
            colonnes_B=len(matrice_pour_sost[0])
            if len(matrice)!=lignes_B or len(matrice[0])!=colonnes_B:
                print("----->Soustraction impossible : dimensions incompatibles.")
                clear_avec_msg()
                continue
            
            print("Matrice initiale :")
            print()
            affichage(matrice)
            print()
            print("Matrice à soustraire :")
            affichage(matrice_pour_sost)
            print()
            print("La méthode :")
            soustraction_matrice = souetraction(matrice, matrice_pour_sost)
            
            print()
            print("Résultat de la soustraction :")
            print()
            affichage(soustraction_matrice)
            if all(all(x==0 for x in lignes)for lignes in soustraction_matrice ):
                print("-----> La matrice est une matrice nulle!")
            clear_avec_msg()

        #option 7 = Multiplication de matrices
        elif option==7:
             pass
        #option 8 = Soustraction de matrices
        elif option==8:
             pass
            
        #option 9 = Transposée d'une matrice
        elif option==9:
             pass
        
        #option 10 = Rang d'une matrice
        elif option==8:
             pass
        
        #option 11 = Résolution d'un système linéaire
        elif option==11:
             pass
        
        #option 0 = Quitter
        elif option==0:
            print("GOOD BYE!")
            sys.exit()
        os.system("cls")
