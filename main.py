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

        
        
        #option 1 = Addition 
        if option==1:
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
            
            print("Matrice initiale A:")
            print()
            affichage(matrice)
            print()
            print("Matrice à ajouter B:")    
            print()
            affichage(matrice_pour_add)
            print()
            print("Calcul de la addition par le matrice B :")
            adition_matrice=addition(matrice,matrice_pour_add)
            print()
            print("Résultat de l'addition :")
            print()
            affichage(adition_matrice)
            if all(all(x==0 for x in lignes)for lignes in adition_matrice ):
                print("-----> La matrice est une matrice nulle!")
            clear_avec_msg()
        
        #option 2 = Soustraction
        elif option==2:
            titre("Soustraction de matrices")
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
            
            print("Matrice initiale A :")
            print()
            affichage(matrice)
            print()
            print("Matrice à soustraire B :")
            affichage(matrice_pour_sost)
            print()
            print("Calcul de la soustraction par le matrice B :")
            soustraction_matrice = souetraction(matrice, matrice_pour_sost)
            
            print()
            print("Résultat de la soustraction :")
            print()
            affichage(soustraction_matrice)
            if all(all(x==0 for x in lignes)for lignes in soustraction_matrice ):
                print("-----> La matrice est une matrice nulle!")
            clear_avec_msg()
            
        #option 3 = Multiplication 
        elif option==3:
             pass
        
        #option 4 = Multiplication par scalaire
        elif option==4:
            titre("Multiplication par scalaire")
            try:
                scalaire=int(input("Veuillez entrer le scalaire à multiplier par la matrice: "))
            except ValueError:
                    print("Veuillez entrer un nombre valide !(un nombre entier).")
                    print()
                    clear_avec_msg()
                    continue
            print("Matrice initiale :")
            print()
            affichage(matrice)
            print()
            print("Calcul de la multiplication par le scalaire :")
            matrice_multipli_scalaire=multiplication_scalaire(matrice,scalaire)
            print("Matrice obtenue après multiplication par le scalaire :")
            print()
            affichage(matrice_multipli_scalaire)
            clear_avec_msg()
             
        
        
        #option 5 = Transposée
        elif option==5:
             pass


        #option 6 = reduction de gauss
        elif option==6:
                lignes=len(matrice)
                colonnes=len(matrice[0])
                titre("Réduction de Gauss")
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
                    for pivot in range(min(lignes, colonnes)):
                        if matrice[pivot][pivot] == 0:
                            for i in range(pivot + 1, lignes):
                                if matrice[i][pivot] != 0:
                                    matrice[pivot], matrice[i] = matrice[i], matrice[pivot]
                                    print(f"\nL{pivot+1} ↔ L{i+1}")
                                    break
                        elimination_gauss(matrice, pivot)
                        if pivot < min(lignes, colonnes) - 1:
                            affichage(matrice)
                            print()
                else:
                    print()
                    print("La matrice contient une seule ligne. Aucune élimination n'est nécessaire.")
                    clear_avec_msg()
                    continue
                #affichge de resulta fianle
                print("resulta finale:")
                print()
                affichage(matrice)
                print()
                clear_avec_msg()



        
        #option 0 = Quitter
        elif option==0:
            titre("""          Merci d'avoir utilisé notre application !
                    À bientôt !  Au revoir !""")
            sys.exit()
        os.system("cls")
