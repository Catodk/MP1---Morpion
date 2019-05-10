import random,time


#Liste des valeurs_tableau possibles du robot
liste_robot=[]


#Liste des valeurs du tableau:
valeurs_tableau = []

#Les listes prennent les valeurs de 0 à 8 (qui représentent alors les cases du tableau et les valeurs_tableau possibles du robot et du joueur).
for x in range (0, 9):
    valeurs_tableau.append(x)
    liste_robot.append(x)


#Fonction permettant l'affichage du tableau qui sera mis à jour après chaque tour
def tableau():
    print() #choix esthétique : plus espacé
    print(valeurs_tableau[0], valeurs_tableau[1], valeurs_tableau[2]) #ligne 1 du tableau
    print(valeurs_tableau[3], valeurs_tableau[4], valeurs_tableau[5]) #ligne 2 du tableau
    print(valeurs_tableau[6], valeurs_tableau[7], valeurs_tableau[8]) #ligne 3 du tableau
    print() #choix esthétique

#Fonction mise en place lorsque c'est le tour du joueur
def tour_joueur():
    J1=int(input("Quelle case choisissez-vous?  ")) #Le joueur choisit la case où il veut placer son symbole. ATTENTION : un caractère autre qu'un chiffre va arrêter le programme.

    if J1 in valeurs_tableau: #Vérification du saisi du joueur 1:

        for x in range (0,9): #Le numéro de case choisi par le joueur 1 sera remplacé par "X" si c'est un chiffre compris entre 0 et 8 (9-1).

            if valeurs_tableau[J1]==x:
                valeurs_tableau[J1]="X"
                liste_robot.remove(x) #Enlève la case choisie par le joueur des choix possibles pour le robot.
                
    else: #Lorsque le chiffre saisi n'est pas un chiffre/nombre compris entre 0 et 8 où qu'il est déjà pris, le joueur 1 devra rejouer.
        print()
        print("Pas possible. Saisissez un chiffre entre 0 et 8 qui n'est pas déjà pris.")
        print()
        tour_joueur()


#Fonction mise en place lorsque c'est le tour du robot
def tour_robot():
    J2 = random.choice(liste_robot) #le robot choisit une valeur au hasard dans la liste des choix
    print()
    print("Le robot a choisi la case ",J2,"!")
    print()
    
    for x in range (0,9):
        if valeurs_tableau[J2]==x:
            valeurs_tableau[J2]="O"
            liste_robot.remove(x) #Enlève la case choisie par le robot des choix possibles pour le robot.
        

#Fonction régulant les tours
def tour():
    tours=1 #Nombre de tours
    while tours<=9: #Tant qu'il n'y a pas d'égalité
        if tours%2==0: #Le nombre de tours sera pair lorsque c'est le tour du robot et impair lorsque c'est le tour du joueur
            tour_robot()
            tableau()
        else:
            tour_joueur()
                
        tours=tours+1

        if gagnant()==True: #Si le joueur a gagné
            tableau()
            print("Vous avez gagné! :)")
            time.sleep(2)
            exit()

        if gagnant()==False: #Si le joueur a perdu
            tableau()
            print("Vous avez perdu! :(")
            time.sleep(2)
            exit()

    print()
    print("Egalité! Recommencez le programme pour un nouveau jeu.")
    
        
        

def gagnant(): #On teste toutes les combinaisons possibles permettant la victoire.
    if valeurs_tableau[0]==valeurs_tableau[1]==valeurs_tableau[2]=="X" or valeurs_tableau[3]==valeurs_tableau[4]==valeurs_tableau[5]=="X" or valeurs_tableau[6]==valeurs_tableau[7]==valeurs_tableau[8]=="X" or valeurs_tableau[0]==valeurs_tableau[3]==valeurs_tableau[6]=="X" or valeurs_tableau[1]==valeurs_tableau[4]==valeurs_tableau[7]=="X" or valeurs_tableau[2]==valeurs_tableau[5]==valeurs_tableau[8]=="X" or valeurs_tableau[0]==valeurs_tableau[4]==valeurs_tableau[8]=="X" or valeurs_tableau[2]==valeurs_tableau[4]==valeurs_tableau[6]=="X": #Pour tester si le joueur 1 a gagné
        return True
    elif valeurs_tableau[0]==valeurs_tableau[1]==valeurs_tableau[2]=="O" or valeurs_tableau[3]==valeurs_tableau[4]==valeurs_tableau[5]=="O" or valeurs_tableau[6]==valeurs_tableau[7]==valeurs_tableau[8]=="O" or valeurs_tableau[0]==valeurs_tableau[3]==valeurs_tableau[6]=="O" or valeurs_tableau[1]==valeurs_tableau[4]==valeurs_tableau[7]=="O" or valeurs_tableau[2]==valeurs_tableau[5]==valeurs_tableau[8]=="O" or valeurs_tableau[0]==valeurs_tableau[4]==valeurs_tableau[8]=="O" or valeurs_tableau[2]==valeurs_tableau[4]==valeurs_tableau[6]=="O": #Pour tester si le joueur 2 a gagné
        return False


#Commence le jeu
print("Ce jeu est un jeu de morpion classique. Veuillez entrer un chiffre de 0 à 8 qui correspondra au numéro de la case où vous voulez placer votre symbole. Le joueur 1 sera représenté par le symbole 'X' et le joueur 2 par le symbole 'O'.")
print()
tableau() #Affiche le tableau de début (avec seulement les chiffres)
tour()
gagnant()
