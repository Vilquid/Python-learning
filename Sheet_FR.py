# DATA SCIENCE CHEAT SHEET - Français


# s - Une variable string
# i - Une variable integer
# f - Une variable float
# l - Une variable list
# d - Une variable dictionnaire

# LISTS
l.pop(3) # Renvoie le quatrième élément de l et le supprime de la liste
l.remove(x) # Supprime le premier élément de l égal à x
l.reverse() # Inverse l'ordre dans les éléments de l
l[1::2] # Renvoie chaque seconde élément à partir de l à partir du 1er élément
l[-5] # Renvoie les 5 derniers éléments de l

# STRINGS
s.lower() # Renvoie une version minuscule de s
s.title() # Renvoie s avec la première lettre de chaque mot en majuscule
"23".zfill(4) # Renvoie "0023" en remplissant à gauche la chaîne avec des 0 pour rendre sa longueur 4
s.splitlines() # Renvoie une liste en fractionnant la chaîne sur tous les caractères de nouvelle ligne
s[:5] # Renvoie les 5 premiers caractères de s
"fri" + "end" # Renvoie "friend"
"end" in s # Renvoie True si la sous-chaîne "end" est trouvée dans s

# RANGE - Les objets Range sont utiles pour créer des séquences d'entiers pour la boucle.
range(5) # Renvoie une séquence de 0 à 4
range(2000, 2018) # Renvoie une séquence de 2000 à 2017
range(0, 11, 2) # Renvoie une séquence de 0 à 10 avec chaque élément incrémenté de 2
range(0, -10, -1) # Renvoie une séquence de 0 à -9
list(range(5)) # Renvoie une liste de 0 à 4

# DICTIONARIES
max(d, key = d.get) # Renvoie la clé qui correspond à la plus grande valeur de d
min(d, key = d.get) # Renvoie la clé qui correspond à la valeur la plus basse de d

# SETS
mv_set = set(l) # Renvoie un set d'objets contenant les valeurs uniques de l
len(my_set) # Renvoie le nombre d'objets dans mon_set ou le nombre de valeurs uniques de l
a in my_set # Renvoie True si la valeur a dans my_set

# REGULAR EXPRESSIONS
import re # Importe le module d'expressions régulières
re.search("abc", s) # Renvoie un objet mathch si l'expression rationnelle "abc" est trouvée dans s, sinon None
re.sub("abc", "xyz", s) # Renvoie une chaîne où toutes les instances correspondant à l'expression régulière "abc" sont remplacées par "xyz"

LIST COMPREHENSION # Une expression # une ligne pour une boucle
[i ** 2 for i in range(10)] # Renvoie une liste des carrés de valeurs de 0 à 9
[s.lower() for s in l_strings] # Renvoie la liste l_strings, avec chaque élément ayant la méthode .lower() appliquée
[i for i in l_floats if i < O.5] # Renvoie les éléments de l_floats inférieurs à 0,5

# FUNCTION FOR LOOPING
for i, value in enumerate(1): # Itère sur la liste l, en imprimant l'emplacement d'index de chaque élément et sa valeur
	print("The value of item {} is {}", format(i, value))
for one, two in zip(l_one, l_two): # Itère sur 2 listes, l_one et l_two et affiche chaque valeur
	print("one: {}, two: {}", format(one, two))
while x < 10: # Exécute le code dans le corps pour une boucle jusqu'à ce que la valeur de x ne soit pas inférieure à 10
	x += 1

# DATETIME
import datetime as dt # Imports the datetime module
now = dt.datetime.now() # Attribue un objet datetime représentant l'heure actuelle à now
wks4 = dt.datetime.timedelta(weeks = 4) # Attribue un objet timedelta représentant une période de 4 semaines à wks4
now - wks4 # Renvoie un objet datetime représentant le temps 4 semaines avant now
newyear_2020 = dt.datetime(year = 2020, month = 12, day = 31) # Attribue un objet datetime représentant le 25 décembre 2020 à newyear_2020
newyear_2020.strftime("%A, %b %d, %Y") # Renvoie "Thursday, Dec 31, 2020"
dt.datetime.strptime('Dec 31, 2020', "%b %d, %Y") # Renvoie un objet datetime représentant le "December 31, 2020"

# RANDOM
import random # Importe le module datetime
random.random() # Renvoie un float aléatoire entre 0.0 et 1.0
random.randint(0, 10) # Renvoie un entier aléatoire entre 0 et 10
random.choice(l) # Renvoie un élément aléatoire de la liste l

# COUNTER
from collections import Counter # Importe la classe Counter
c = Counter(l) # Assigne un objet Counter (dict-like) avec les nombres de chaque élément unique de 1 à c
c.most_common(3) # Renvoie les 3 éléments les plus courants de l

# TRY/EXCEPT - Traiter les erreurs
l_ints = [1, 2, 3, "", 5] # Attribue une liste d'entiers avec une valeur manquante à l_ints
l_floats = [] # Convertit chaque valeur de l_int en float, capture et gestion ValueError: impossible de convertir la chaîne en float: où les valeurs sont manquantes
for i in l_ints:
	try:
		l_floats.append(float(i))
	except:
		l_floats.append(i)
