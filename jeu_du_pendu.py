import random
import sys
# from words import words_importation
# words_importation(dico=)


words_dico = {
    "facile" : [
        "abeille",
        "abri",
        "accord",
        "actif",
        "album",
        "aller",
        "amour",
        "arbre",
        "argent",
        "avion",
        "bébé",
        "bien",
        "bleu",
        "bois",
        "bon",
        "bouc",
        "bout",
        "bruit",
        "chat",
        "chien",
        "dire",
        "école",
        "faire",
        "haut",
        "jour",
        "livre",
        "main",
        "mal",
        "mer",
        "mètre",
        "mot",
        "noir",
        "nuit",
        "ombre",
        "oui",
        "pain",
        "père",
        "petit",
        "pluie",
        "rouge",
        "salle",
        "sang",
        "seul",
        "table",
        "temps",
        "tête",
        "tirer",
        "vert",
        "voir"
        ],

    "moyen" : [
        "Chocolat",
        "Lapinous",
        "Bonjourn",
        "Jardinier",
        "Montagne",
        "Aviation",
        "Bateaux",
        "Livretsin",
        "Caméras",
        "Tapisser",
        "Étoiles",
        "Pluviomètre",
        "Châteaux",
        "Violente",
        "Pianiste",
        "Alphabet",
        "Cascade",
        "Aventure",
        "Banquier",
        "Cuisiner",
        "Liberté",
        "Randonnée",
        "Trésorerie",
        "Anniversaire",
        "Caméléon",
        "Danseuse",
        "Explosion",
        "Eau-forte",
        "Horloge",
        "Jalouse",
        "Kangourou",
        "Mélodie",
        "Papillon",
        "Théière"
        ],

    "difficile" : [
        "Bibliothèque",
        "Chocolaterie",
        "Anticonstitutionnellement",
        "Incompréhensibilité",
        "Indivisibilité",
        "Phénoménologiquement",
        "Électroencéphalographie",
        "Parallélogramme",
        "Hypothalamique",
        "Supercalifragilisticexpialidocious",
        "Constitutionnalité",
        "Thermodynamiquement",
        "Démocratiquement",
        "Inintelligibilité",
        "Inconstitutionnalité",
        "Intercontinentalité",
        "Rhinocéros",
        "Philosophiquement",
        "Autoantonyme",
        "Hippopotame"
        ]
}

debut  = "  ==========Y=\n  ||/        \n  ||         \n  ||           \n  ||           \n /||          \n ============="
reste5 = "  ==========Y=\n  ||/       |\n  ||         \n  ||           \n  ||           \n /||          \n ============="
reste4 = "  ==========Y=\n  ||/       |\n  ||        0\n  ||        |  \n  ||           \n /||          \n ============="
reste3 = "  ==========Y=\n  ||/       |\n  ||        0\n  ||       /|  \n  ||           \n /||          \n ============="
reste2 = "  ==========Y=\n  ||/       |\n  ||        0\n  ||       /|\ \n  ||           \n /||          \n ============="
reste1 = "  ==========Y=\n  ||/       |\n  ||        0      ATTENTION !!\n  ||       /|\ \n  ||       /   \n /||          \n ============="


print(f"Bienvenue au JEU DU PENDU\n{debut} \nCommençons :\n")


# ajout du choix de la difficulté:
def words_importation(dico):
    print("Choisissez le niveau de difficulté :\nTapez 1 pour le niveau FACILE\n      2 pour MOYEN\n   et 3 pour DIFFICILE")
    level_choice = input("Votre choix => ")
    while level_choice not in ["1", "2", "3"]:
        print("Erreur: veuillez choisir un choix valide.")
        level_choice = input("Votre choix => ")
    return level_choice

level_choice = words_importation(dico=words_dico)

def choice_difficulty_level():
    if level_choice == "1":
        dico_values = words_dico["facile"]
        print("On y va doucement\n")
    elif level_choice == "2":
        dico_values = words_dico["moyen"]
        print("Un peu plus difficile !\n")
    elif level_choice == "3":
        dico_values = words_dico["difficile"]
        print("Mode WARRIOR !!\n")
    return dico_values
# print(choice_difficulty_level())


# faire apparaitre les mots au hasard
word_random = random.choice(choice_difficulty_level())
# print(word_random) # montre le mot choisi
display = []
tried_letter = []


# le compteur du nombre d'erreurs
error = 0
# cacher les lettres
for i in word_random:
    display.append('_')
print(" ".join(display))

while error < 6:
    reste = 5 - error
    letter = 0
# demander au joueur d'entrer un lettre : 
    letter_player = (input("--------------------------\nChoisissez une lettre : "))
    if letter_player in tried_letter:
        error +=1
        print(f"Vous avez déjà tenter cette lettre '{letter_player}', il vous reste {reste} chances\n")
    else:
        tried_letter.append(letter_player)
        if letter_player in word_random:
            for i in word_random:
                if letter_player == i:
                    display[letter] = letter_player
                letter = letter + 1
            print(f"vous avez trouvé la lettre '{letter_player}'\n")
            print(" ".join(display))
        else:
            error += 1
            print(f"NON ! '{letter_player}' n'est pas dans ce mot ! Il vous reste {reste} chances\n")

    if error == 1:
        print(reste5, " ".join(display))
    elif error == 2:
        print(reste4, " ".join(display))
    elif error == 3:
        print(reste3, " ".join(display))
    elif error == 4:
        print(reste2, " ".join(display))
    elif error == 5:
        print(reste1, " ".join(display))
    elif error == 6:
        print("  ==========Y=\n  ||/       |\n  ||        0" + "      PERDU ! Le mot été '{}'.".format(word_random) + "\n  ||       /|\       Retente ta chance !!\n  ||       / \ \n /||          \n =============")
        break
    elif not "_" in display :
        print("  ==========Y=\n  ||/        \n  ||               BRAVO ! Vous avez gagné !!\n  ||           \n  ||           \n /||          \n =============")
        sys.exit()

