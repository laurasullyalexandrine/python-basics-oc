# Ecrivez votre code ici !

# Conditions simples
avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !")

# Comparateurs
nombre_de_sieges = 30
nombre_dinvites = 25

if nombre_dinvites < nombre_de_sieges:
    print("autoriser plus d’invités")
else:
    print("ne pas autoriser plus d’invités")

# Match cases "_" représente la valeur par défaut
fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")

nombre1 = input("Donnez moi un premier chiffre au hasard :")
nombre2 = input("Donnez moi un deuxième chiffre au hasard :")

print(nombre1, nombre2)
if not nombre1.isnumeric or not nombre2.isnumeric :
    print("Erreur ce ne sont pas des nombres entiers !")
    raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("Saisir le symbole de l'opération souhaitée ['+', '-', '*' ou '/'] : ")
print (operation)
if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")

if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    # Vérifie si la variable `nombre2` n'est pas nulle pour la division
    if nombre2 == 0:
        print("Erreur: Diviser par zéro est impoossible.")
        raise SystemExit("Fin du programme")

    resultat = round(nombre1 / nombre2, 2)

# Affiche le résultat
print(f"Le résultat de l'opération est: {round(resultat, 2)}")