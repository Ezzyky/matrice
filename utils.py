from matrice_io import *
def clear_avec_msg(msg="Appuyez sur n'importe quel bouton pour sortir..."):
    import os
    print(msg)
    input()
    os.system("cls" if os.name == "nt" else "clear")
def Sauvegarder(matrice1,matrice2):
    with open("file.txt","w") as file:
        file.write(matrice1)
        file.write(affichage(matrice2))