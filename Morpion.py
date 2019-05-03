import sys

#Liste des valeurs du tableau:
choix = []

#La liste représentant le tableau prends les valeurs de 0 à 8 (qui représentent alors les cases du tableau).
for x in range (0, 9):
    choix.append(x)

#Fonction permettant l'affichage du tableau qui sera mis à jour après chaque tour
def tableau():
    print("") #choix esthétique : plus espacé
    print(choix[0], choix[1], choix[2]) #ligne 1 du tableau
    print(choix[3], choix[4], choix[5]) #ligne 2 du tableau
    print(choix[6], choix[7], choix[8]) #ligne 3 du tableau
    print("") #choix esthétique

print("Ce jeu est un jeu de morpion classique. Veuillez entrer un chiffre de 0 à 8 qui correspondra au numéro de la case où vous voulez placer votre symbole. Le joueur 1 sera représenté par le symbole 'X' et le joueur 2 par le symbole 'O'.")

tableau() #Affiche le tableau de début (avec seulement les chiffres)

def tourJ1():
    J1=int(input("Joueur 1: ")) #Joueur 1 choisit la case où il veut placer son symbole. ATTENTION : un caractère autre qu'un chiffre va arrêter le programme.
    if J1 in choix: #Vérification du saisi du joueur 1:
        for x in range (0,9): #Le numéro de case choisi par le joueur 1 sera remplacé par "X" si c'est un chiffre compris entre 0 et 8 (9-1).
            if choix[J1]==x:
                choix[J1]="X"
    else: #Lorsque le chiffre saisi n'est pas un chiffre/nombre compris entre 0 et 8 où qu'il est déjà pris, le joueur 1 devra rejouer.
        print("")
        print("Pas possible. Saisissez un chiffre entre 0 et 8 qui n'est pas déjà pris.")
        print("")
        tourJ1()

def tourJ2(): #Similaire à la fonction tourJ1()
    J2=int(input("Joueur 2: "))
    if J2 in choix:
        for x in range (0,9):
          if choix[J2]==x:
            choix[J2]="O"
    else:
        print("")
        print("Pas possible. Saisissez un chiffre entre 0 et 8 qui n'est pas déjà pris.")
        print("")
        tourJ2()

def tour():
    x=1 #Nombre de tours
    while x<=9: #Tant qu'il n'y a pas d'égalité
        if not gagnant(): #S'il n'y a pas de gagnant
            if x%2==0: #Le nombre de tours sera pair lorsque c'est le tour du joueur 2 et impair lorsque c'est le tour du joueur 1
                tourJ2()
            else:
                tourJ1()
            tableau()
            x=x+1
        if x>=10:
            print("Egalité! Recommencez le programme pour un nouveau jeu.")

def gagnant(): #On teste toutes les combinaisons possibles permettant la victoire.
    if choix[0]==choix[1]==choix[2]=="X" or choix[3]==choix[4]==choix[5]=="X" or choix[6]==choix[7]==choix[8]=="X" or choix[0]==choix[3]==choix[6]=="X" or choix[1]==choix[4]==choix[7]=="X" or choix[2]==choix[5]==choix[8]=="X" or choix[0]==choix[4]==choix[8]=="X" or choix[2]==choix[4]==choix[6]=="X": #Pour tester si le joueur 1 a gagné
        sys.exit("Joueur 1, vous avez gagné! :)")
    elif choix[0]==choix[1]==choix[2]=="O" or choix[3]==choix[4]==choix[5]=="O" or choix[6]==choix[7]==choix[8]=="O" or choix[0]==choix[3]==choix[6]=="O" or choix[1]==choix[4]==choix[7]=="O" or choix[2]==choix[5]==choix[8]=="O" or choix[0]==choix[4]==choix[8]=="O" or choix[2]==choix[4]==choix[6]=="O": #Pour tester si le joueur 2 a gagné
        sys.exit("Joueur 2, vous avez gagné! :)")

tour()
gagnant()
