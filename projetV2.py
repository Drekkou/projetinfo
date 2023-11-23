#Partie 1

def init(n: int):
    """Recoit en argument un entier n (le nombre de disques), et qui renvoie la liste représentant la configuration initiale du plateau"""
    discs = []
    for i in range (n, 0, -1):
        discs.append(i)

    return [discs, [], []]


def nbDisques(plateau: list[list[int] | list], numtour: int):
    """Renvoie le nombre de disques sur la tour indiquée"""
    if 0 < numtour > 2:
        return f"ERROR : Numtour must be between 0 and 2"
    return len(plateau[numtour])


def disqueSup(plateau: list[list[int] | list], numtour: int):
    """Renvoie le numéro du disque au sommet de la tour indiquée"""
    if not plateau[numtour] or len(plateau[numtour]) == 0:
        return -1
    return plateau[numtour][len(plateau[numtour]) - 1]


def posDisque(plateau: list[list[int] | list], numdisque: int):
    """Renvoie le numéro de la tour sur laquelle se trouve un disque"""
    if numdisque in plateau[0]:
        return 0
    elif numdisque in plateau[1]:
        return 1
    elif numdisque in plateau[2]:
        return 2
    else:
        return -1


def posDisque_edited(plateau, numdisque):
    for i in plateau:
        for x in i:
            if numdisque == x:
                return plateau.index(i), i.index(x)    #retourne d'abord la n-tour, et ensuite la n-position dans la tour

#Partie 2
import turtle
turtle.speed(100)
plateau=[[3,2,1],[],[]]
t=turtle.Screen()
    
# Fonction pour dessiner le plateau avec trois tours
def dessinePlateau(n):              #J'en ai une autre qui fait des tours plus larges mais c'est plus chiant pour les tracer et pour la suite
    largeur_plateau = 40+30*n        #Mais demandes moi si tu la veux
    hauteur_plateau = 20
    hauteur_tour = 20*n+30

    # Dessiner le plateau
   
    ##turtle.fillcolor("brown")
    ##turtle.begin_fill()
    for i in range(2):
        turtle.forward(largeur_plateau)
        turtle.left(90)
        turtle.forward(hauteur_plateau)
        turtle.left(90)
    ##turtle.end_fill()

    # Dessiner les tours
    for i in range(3):
        turtle.penup()
        x_tour = (largeur_plateau / 6) + i * (largeur_plateau / 3)
        y_tour = hauteur_plateau 
        turtle.goto(x_tour , y_tour)
        turtle.pendown()
        turtle.fillcolor("gray")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(0)
            turtle.left(90)
            turtle.forward(hauteur_tour)
            turtle.left(90)
        turtle.end_fill()

    turtle.hideturtle()

# Sous fonction pour obtenir l'emplacement du disque dans la liste
def trouver_emplacement(element, plateau):
    for index, sous_liste in enumerate(plateau):
        if element in sous_liste:
            return [index , sous_liste.index(element)] # Renvoie l'indice de la sous-liste où l'élément est présent
    return None  # Renvoie None si l'élément n'est pas trouvé dans le plateau

#Fonction pour tracer le disque (ça marche pas à partir de turtle)
def dessineDisque(nd, plateau, n):
    #Dimension plateau
    largeur_plateau = 40+30*n
    hauteur_plateau = 20
    hauteur_tour = 20*n+30
    
    #Tracer un disque
    longueur_disque = nd*10
    hauteur_disque = 20
    i=trouver_emplacement(nd,plateau)
    print(i)
    xdisque = (largeur_plateau / 6) + i[0] * (largeur_plateau / 3)
    ydisque = hauteur_plateau+hauteur_plateau*i[1]
    
    turtle.penup()
    turtle.goto(xdisque,ydisque)
    turtle.pendown()
    turtle.forward(longueur_disque/2)
    turtle.left(90)
    turtle.forward(hauteur_disque)
    turtle.left(90)
    turtle.forward(longueur_disque)
    turtle.left(90)
    turtle.forward(hauteur_disque)
    turtle.left(90)
    turtle.forward(longueur_disque/2)
  #Les autre choses demandées dans la partie 2 dépendent de la fonction qui marche pas donc j'ai pas pus faire
#Partie C

#Fonction qui initialise l'emplacement des disques de départs et d'arrivé (j'ai pas pus tester pck j'arrive pas à tracer les disques
def lireCoords(plateau):
    while True:
        # Demande le numéro de la tour de départ
        tour_depart = -1
        while tour_depart not in range(1, 4) or len(plateau[tour_depart - 1]) == 0:
            tour_depart = int(input("Entrez le numéro de la tour de départ (1, 2, 3) : "))
            if tour_depart not in range(1, 4):
                print("Le numéro de la tour doit être entre 1 et 3.")
            elif len(plateau[tour_depart - 1]) == 0:
                print("La tour de départ est vide. Choisissez une autre tour.")

        # Demande le numéro de la tour d'arrivée
        tour_arrivee = -1
        while tour_arrivee not in range(1, 4) or (len(plateau[tour_arrivee - 1]) > 0 and plateau[tour_arrivee - 1][-1] < plateau[tour_depart - 1][-1]):
            tour_arrivee = int(input("Entrez le numéro de la tour d'arrivée (1, 2, 3) : "))
            if tour_arrivee not in range(1, 4):
                print("Le numéro de la tour doit être entre 1 et 3.")
            elif len(plateau[tour_arrivee - 1]) > 0 and plateau[tour_arrivee - 1][-1] < plateau[tour_depart - 1][-1]:
                print("Le disque sélectionné ne peut pas être placé sur cette tour. Choisissez une autre tour.")

        return tour_depart , tour_arrivee 


dessinePlateau(3)
dessineDisque(3,plateau,3)
dessineDisque(2,plateau,3)
dessineDisque(1,plateau,3)
turtle.mainloop()