def menu():

    print("""
                =========================================================
                              APPLICATION D'ALGÈBRE LINÉAIRE
                 =========================================================

[A] Opérations sur les matrices                   [B] Réduction et résolution
    [1]. Addition                                     [6]. Réduction de Gauss
    [2]. Soustraction                                 [7]. Méthode de Gauss-Jordan
    [3]. Multiplication                               [8]. Résolution système linéaire
    [4]. Multiplication par scalaire                  [9]. Rang
    [5]. Transposée


[C] Propriétés et analyse                         [D] Algèbre linéaire avancée
   [10]. Déterminant                                    [16]. Valeurs propres
   [11]. Inverse                                        [17]. Vecteurs propres
   [12]. Trace                                          [18]. Noyau Ker(A)
   [13]. Vérifier inversible                            [19]. Image Im(A)
   [14]. Vérifier symétrique                            [20]. Décomposition LU
   [15]. Vérifier diagonale                             [21]. SVD


[E] Outils
   [22]. Générer matrice aléatoire
   [23]. Sauvegarder                                [0] Quitter
   [24]. Charger
   [25]. Historique
          """)

def home():
     print("""
            =========================================================
                BIENVENUE DANS LE PROGRAMME D'ALGÈBRE LINÉAIRE
            =========================================================

            Ce programme permet d'effectuer plusieurs opérations sur
            les matrices et les systèmes linéaires.

            Veuillez d'abord saisir la matrice initiale, puis choisir
            l'opération souhaitée dans le menu suivant.

    """)
def titre(b):
     print(f"""
            =========================================================
                        {b}
            =========================================================
    """)