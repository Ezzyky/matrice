def clear_avec_msg(msg="Appuyez sur n'importe quel bouton pour sortir..."):
    import msvcrt
    import os
    print(msg)
    msvcrt.getch()
    os.system("cls")