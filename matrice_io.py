from menu_txtes import *
from utils import *
import sys
#ajout un exception pour les errors
class MatrixSizeError(Exception):
    pass

def prenant_matrice(nom="A"):
    print(f"Saisissez la taille de la matrice {nom}:")
    
    lignes=int(input("Nombre de lignes : "))
    colonnes=int(input("Nombre de colonnes : "))
    if lignes<=0 or colonnes<=0:
       raise MatrixSizeError("Le nombre de lignes et de colonnes doit être strictement positif.")
    Matrice=[[None for i in range(colonnes)]for i in range (lignes)]
    for i in range(lignes):
        for j in range (colonnes):
            Matrice[i][j]=int(input(f"M[{i+1}][{j+1}] = "))
        return Matrice
#to exept the error out fo size tables
def demander_matrice():
    
    while True:
        titre("Veuillez entrer la matrice initiale.")
        try:
             return prenant_matrice()
        except ValueError:
            print("Veuillez entrer un nombre valide (un entier).")
            clear_avec_msg()
        except MatrixSizeError as e:
            print(e)
            clear_avec_msg()

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


    
# i dont need it for now
def swap(matrice):
    lignes=len(matrice)
    colonnes=len(matrice[0])
    if matrice[0][0]==0:
        for i in range(lignes):
            if matrice[i][0]!=0:
                index=i
                break
        for i in range(colonnes):
            temp=matrice[0][i]
            matrice[0][i]=matrice[index][i]
            matrice[index][i]=temp
        print("_________Opérations effectuées sur les lignes :_________")
        print()
        print(f"L1 ​↔ L​{index+1}")
    return matrice

def trace(matrice):
    if len(matrice)!=len(matrice[0]):
        raise ValueError
    t=0
    for i in range(len(matrice)):
        t+=matrice[i][i]
    return t
def options():
    try:
            option = int(input("Choisissez une option : "))
    except ValueError:
        clear_avec_msg("Option invalide.")
        
    if option==0:
         titre("""          Merci d'avoir utilisé notre application !
                    À bientôt !  Au revoir !""")
         sys.exit()
    if option==1:
        pass
    if option==2:
        pass