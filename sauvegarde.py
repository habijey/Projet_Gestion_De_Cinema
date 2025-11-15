import json
from classe import Film, Salle, Reservation

FILMS_FILE = "Films.json"
SALLES_FILE = "Salles.json"
RES_FILE = "Reservations.json"

# Charger un fichier JSON
def charger_json(fichier):
    try:
        with open(fichier, "r") as f:
            return json.load(f)
    except:
        return []


def sauvegarder_json(fichier, data):
    with open(fichier, "w") as f:
        json.dump(data, f)

# Charger toutes les données et créer les objets correspondants
def charger_donnees():
    films_data = charger_json(FILMS_FILE)
    salles_data = charger_json(SALLES_FILE)
    reservations = charger_json(RES_FILE)

    
    films = [Film(f["titre"], f["duree"]) for f in films_data]

    
    salles = []
    for s in salles_data:
        film_obj = next((f for f in films if f.titre == s.get("film")), None)

        salles.append(Salle(
            s["numero"],
            s["capacite"],
            film_obj,
            s["places_reservees"] 
        ))

    return films, salles, reservations

# Sauvegarder tous les objets dans les fichiers JSON
def sauvegarder_donnees(films, salles, reservations):
    films_dict = [f.to_dict() for f in films]
    salles_dict = [s.to_dict() for s in salles]

    sauvegarder_json(FILMS_FILE, films_dict)
    sauvegarder_json(SALLES_FILE, salles_dict)
    sauvegarder_json(RES_FILE, reservations)
