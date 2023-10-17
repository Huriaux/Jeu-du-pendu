# LE JEU DU PENDU

# 1. créer une liste de mots

# 2. créer un fonction qui choisi un mot de ma liste au hasard

# 3. afficher le mot en remplaçant chaque caractère par "_"

# 4. créer une entrée qui permet au joueur d'entrer une première lettre :

    # créer un compteur d'erreur (x6) = lettre qui n'est pas dans le mot choisi
        # retournera "il vous reste '' chance(s)"
        # si les 6 chances sont épuisées, la console renvoi "PERDU !" et le jeu s'arrête

    # à chaque fois qu'une lettre entrée par le joueur est correct, elle doit remplacer le '_' correspondant

    # si le joueur a trouvé le mot il peut l'entrer entièrement
        #  la console renvoi "GAGNE !!"


# -------------------------
# import random

# # générer une liste de mots = 1000
# words_list = [
#     "arbre", "avion", "ballon", "bébé", "chien", "cheval", "chat", "cinéma", "coeur", "dent",
#     "dîner", "école", "étoile", "fleur", "football", "fruit", "guitare", "hôpital", "maison",
#     "montagne", "musique", "ordinateur", "oiseau", "peinture", "paysage", "personne", "poisson",
#     "porte", "voiture", "voyage", "abricot", "ananas", "aubergine", "avocat", "banane",
#     "champignon", "clémentine", "concombre", "courgette", "fraise", "framboise", "fruit de la passion",
#     "glace", "kiwi", "mandarine", "melon", "mûre", "olive", "orange", "pamplemousse", "pêche",
#     "poire", "pomme", "prune", "raisin", "rhubarbe", "salade", "tomate",

#     "amour", "ami", "arbre", "argent", "armoire", "aéroport", "assiette", "ascenseur", "automne",
#     "avenir", "avion", "abeille", "abricot", "aveugle", "avocat", "anniversaire", "argent",
#     "armée", "arrosoir", "assiette", "ascenseur", "automne", "avenir", "avion", "abeille",
#     "abricot", "aveugle", "avocat", "anniversaire", "argent", "armée", "arrosoir",

#     "baleine", "banane", "ballon", "balcon", "bande", "banque", "bar", "barbe", "bateau",
#     "beau", "bébé", "beurre", "bicyclette", "bien", "bisous", "blanc", "bleu", "bois",
#     "bombe", "bonbon", "bouche", "bouton", "bras", "brocoli", "brun", "bureau", "bus",

#     "cachette", "cahier", "camarade", "campagne", "canard", "car", "caramel", "carte", "cartable",
#     "casquette", "chat", "chemise", "chemin", "chien", "chocolat", "chaussure", "ciel", "cinéma",
#     "ciseaux", "citron", "clown", "coeur", "coin", "coller", "costume", "coton", "crayon",
#     "crème", "crocodile",

#     "danser", "dé", "dent", "dessert", "dessin", "diable", "dinosaure", "docteur", "doudou",
#     "dragon", "drapeau", "drap", "douche",

#     "eau", "école", "écureuil", "escalier", "escargot", "étoile", "et", "éventail", "œil",
#     "éléphant", "enfant",

#     "fée", "faim", "famille", "fantôme", "farine", "fête", "feu", "feuille", "femme", "fer",
#     "figue", "film", "fin", "fleur", "folie", "football", "forêt", "four", "fourchette", "fraise",
#     "fromage",

#     "gant", "garage", "gaz", "glace", "guitare", "girafe", "garçon", "gateau", "gomme",
#     "grand", "grappe", "gris",

#     "hôtel", "hôpital", "icône", "imaginaire", "indice", "insecte", "intelligent", "interdiction",
#     "itinéraire", "ivoire",

#     "jeu", "journal", "jouet", "jus",

#     "lapin", "langue", "lait", "livre", "loup", "lune",

#     "manteau", "maman", "maison", "mer", "métro", "miroir", "montagne", "montre", "moto",
#     "mouton",

#     "nain", "nez", "noël", "nuage",

#     "oiseau", "œil", "orange", "ordinateur",

#     "pain", "papillon", "parc", "papa", "papier", "parapluie", "parc", "patte", "perle",
#     "personne", "poisson", "porte", "voiture", "voyage",

#     "qualité", "queue",

#     "radio", "raisin", "rouge",

#     "sable", "sac", "saint", "salade", "salut", "sang", "sandale", "satellite", "saucisson", "savon", "sèche-cheveux", "serpent", "serviette", "singe", "sirène", "soleil", "souris", "sport", "surprise",

#     "table", "tambour", "tapis", "tasse", "télescope", "téléphone", "télévision", "terre", "train", "triangle",

#     "usine", "vélo", "vert", "voiture",

#     "wagon", "walrus",

#     "écharpe", "éléphant", "étoile",

#     "xylophone",

#     "yoyo",

#     "zoologie",
# ]



# illustration console:

# # debut
# print("  ==========Y=\n  ||/       |\n  ||         \n  ||           \n  ||           \n /||          \n =============")

# # reste 5
# print("  ==========Y=\n  ||/       |\n  ||        0\n  ||        |  \n  ||           \n /||          \n =============")

# # reste 4
# print("  ==========Y=\n  ||/       |\n  ||        0\n  ||       /|  \n  ||           \n /||          \n =============")

# # reste 3
# print("  ==========Y=\n  ||/       |\n  ||        0\n  ||       /|\ \n  ||           \n /||          \n =============")

# # reste 1
# print("  ==========Y=\n  ||/       |\n  ||        0\n  ||       /|\ \n  ||       /   \n /||          \n =============")

# # perdu
# print("  ==========Y=\n  ||/       |\n  ||        0\n  ||       /|\ \n  ||       / \ \n /||          \n =============")


# dictionnaire
    # avec 3 catégories : 
        # facile = 200 mots < 6 lettres
        # moyen = 200 mots entre 6 et 9 lettres
        # difficle = 200 mots de 10 lettres et plus

# words_dico = {
#     "facile" : [
#         "abeille",
#         "abri",
#         "accord",
#         "actif",
#         "album",
#         "aller",
#         "amour",
#         "arbre",
#         "argent",
#         "avion",
#         "bébé",
#         "bien",
#         "bleu",
#         "bois",
#         "bon",
#         "bouc",
#         "bout",
#         "bruit",
#         "chat",
#         "chien",
#         "dire",
#         "école",
#         "faire",
#         "haut",
#         "jour",
#         "livre",
#         "main",
#         "mal",
#         "mer",
#         "mètre",
#         "mot",
#         "noir",
#         "nuit",
#         "ombre",
#         "oui",
#         "pain",
#         "père",
#         "petit",
#         "pluie",
#         "rouge",
#         "salle",
#         "sang",
#         "seul",
#         "table",
#         "temps",
#         "tête",
#         "tirer",
#         "vert",
#         "voir"
#         ],

#     "moyen" : [
#         "Chocolat",
#         "Lapinous",
#         "Bonjourn",
#         "Jardinier",
#         "Montagne",
#         "Aviation",
#         "Bateaux",
#         "Livretsin",
#         "Caméras",
#         "Tapisser",
#         "Étoiles",
#         "Pluviomètre",
#         "Châteaux",
#         "Violente",
#         "Pianiste",
#         "Alphabet",
#         "Cascade",
#         "Aventure",
#         "Banquier",
#         "Cuisiner",
#         "Liberté",
#         "Randonnée",
#         "Trésorerie",
#         "Anniversaire",
#         "Caméléon",
#         "Danseuse",
#         "Explosion",
#         "Eau-forte",
#         "Horloge",
#         "Jalouse",
#         "Kangourou",
#         "Mélodie",
#         "Papillon",
#         "Théière"
#         ],

#     "difficile" : [
#         "Bibliothèque",
#         "Chocolaterie",
#         "Anticonstitutionnellement",
#         "Incompréhensibilité",
#         "Indivisibilité",
#         "Phénoménologiquement",
#         "Électroencéphalographie",
#         "Parallélogramme",
#         "Hypothalamique",
#         "Supercalifragilisticexpialidocious",
#         "Constitutionnalité",
#         "Thermodynamiquement",
#         "Démocratiquement",
#         "Inintelligibilité",
#         "Inconstitutionnalité",
#         "Intercontinentalité",
#         "Rhinocéros",
#         "Philosophiquement",
#         "Autoantonyme",
#         "Hippopotame"
#         ]
# }

# debut  = "  ==========Y=\n  ||/        \n  ||         \n  ||           \n  ||           \n /||          \n ============="
# reste5 = "  ==========Y=\n  ||/       |\n  ||         \n  ||           \n  ||           \n /||          \n ============="
# reste4 = "  ==========Y=\n  ||/       |\n  ||        0\n  ||        |  \n  ||           \n /||          \n ============="
# reste3 = "  ==========Y=\n  ||/       |\n  ||        0\n  ||       /|  \n  ||           \n /||          \n ============="
# reste2 = "  ==========Y=\n  ||/       |\n  ||        0\n  ||       /|\ \n  ||           \n /||          \n ============="
# reste1 = "  ==========Y=\n  ||/       |\n  ||        0      ATTENTION !!\n  ||       /|\ \n  ||       /   \n /||          \n ============="



# print(f"Bienvenue au JEU DU PENDU\n{debut} \nCommençons :\n")

# # ajout du choix de la difficulté:
# def retrieve_values_dico(dico):
#     print("Choisissez le niveau de difficulté :\nTapez 1 pour le niveau FACILE\n      2 pour MOYEN\n   et 3 pour DIFFICILE")
#     level_choice = input("Votre choix => ")
#     while level_choice not in ["1", "2", "3"]:
#         print("Erreur: veuillez choisir un choix valide.")
#         level_choice = input("Votre choix => ")
#     return level_choice

# level_choice = retrieve_values_dico()

# def choice_difficulty_level():
#     if level_choice == "1":
#         dico_values = words_dico["facile"]
#         print("On y va doucement")
#     elif level_choice == "2":
#         dico_values = words_dico["moyen"]
#         print("Un peu plus difficile !")
#     elif level_choice == "3":
#         dico_values = words_dico["difficile"]
#         print("Mode WARRIOR !!")

#     return dico_values
# # print(choice_difficulty_level())
