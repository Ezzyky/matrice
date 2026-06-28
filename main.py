from matrice_io import *
from gauss import *
from menu_txtes import *
from operations import *
from utils import *
import os
import sys

#la premire page 
home()
clear_avec_msg()

#une liste pour l'option 25 
historique=[]
while True:
    
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
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")         
            historique.append("Addition")
            titre("Addition de matrices.")
            try:
                matrice_pour_add=prenant_matrice("B")
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
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            historique.append("Soustraction")
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
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            historique.append("Multiplication")
            titre("Multiplication")
            try:
                matrice_pour_m=prenant_matrice("B")
            except ValueError:
                    print("Veuillez entrer un nombre valide !(un nombre entier).")
                    print()
                    clear_avec_msg()
                    continue
            
            print("Matrice initiale A :")
            print()
            affichage(matrice)
            print()
            print("Matrice à multiplier B :")
            print()
            affichage(matrice_pour_m)
            print()
            print("Calcul de la Multiplication par le matrice B :")
            print()
            try:
                matrice_multiple_par_Matrice=multiplication(matrice,matrice_pour_m)
            except ValueError:
                 print("Multiplication impossible : le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la deuxième.")
                 print()
                 clear_avec_msg()
                 continue
            print( "Résultat de la multiplication")
            print()
            affichage(matrice_multiple_par_Matrice)
            print()
            if all(all(x==0 for x in lignes)for lignes in matrice_multiple_par_Matrice ):
                print("-----> La matrice est une matrice nulle!")
            clear_avec_msg()

        #option 4 = Multiplication par scalaire
        elif option==4:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            historique.append("Multiplication par scalaire")
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
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            historique.append("Transposée")
            titre("Transposée")
            print("Matrice initiale :")
            print()
            affichage(matrice)
            matrice_Transpose=Transpose(matrice)
            print("Résultat de la transposition :")
            print()
            affichage(matrice_Transpose)
            print()
            clear_avec_msg()

        #option 6 = reduction de gauss
        elif option==6:
                matrice=demander_matrice()
                clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
                historique.append("reduction de gauss")
                lignes=len(matrice)
                colonnes=len(matrice[0])
                titre("Réduction de Gauss")
                print("Matrice initiale :")
                print()
                affichage(matrice)
                # Permutation des lignes L1 et la première ligne dont le premier élément est non nul
                index=0
                if lignes>=2:
                    
                    for pivot in range(min(lignes, colonnes)):
                        if matrice[pivot][pivot] == 0:
                            for i in range(pivot + 1, lignes):
                                if matrice[i][pivot] != 0:
                                    matrice[pivot], matrice[i] = matrice[i], matrice[pivot]
                                    print(f"\nL{pivot+1} ↔ L{i+1}")
                                    affichage(matrice)
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
        
        #option 12 : trace
        elif option==12:
            matrice=demander_matrice()
            clear_avec_msg("Appuyez sur n'importe quel bouton pour contune...")
            try:
                trace(matrice)
            except ValueError:
                print("La matrice doit être carrée.")
                print()
                clear_avec_msg()
                continue
            titre("Trace")
            historique.append("Trace")
            print("Matrice initiale :")
            print()
            affichage(matrice)
            print()
            print("Résultat de la trace :")
            print("Tr(A)=",trace(matrice))
            clear_avec_msg()
        
        #option 25 : historique
        elif option == 25:
            titre("Historique")
            if len(historique) == 0:
                print("Aucune opération effectuée.")
            else:
                for i, operation in enumerate(historique, start=1):
                    print(f"{i}. {operation}")
            clear_avec_msg()

        #infos
        elif option==26:
             titre("INFOS")
             infos()
             clear_avec_msg()
        
        #option 0 = Quitter
        elif option==0:
            titre("""          Merci d'avoir utilisé notre application !
                    À bientôt !  Au revoir !""")
            sys.exit()

        else:
             titre("pas de option!")
             clear_avec_msg()