import json
import os
from classe import Film, Salle, Reservation

DATA_DIR = "Data"
FILMS_FILE = os.path.join(DATA_DIR, "Films.json")
SALLES_FILE = os.path.join(DATA_DIR, "Salles.json")
RES_FILE = os.path.join(DATA_DIR, "Reservations.json")

os.makedirs(DATA_DIR, exist_ok=True)

def charger_json(fichier):
    try:
        with open(fichier, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def sauvegarder_json(fichier, data):
    with open(fichier, "w") as f:
        json.dump(data, f, indent=4)

def charger_donnees():
    films_data = charger_json(FILMS_FILE)
    salles_data = charger_json(SALLES_FILE)
    reservations_data = charger_json(RES_FILE)

    films = [Film(f["titre"], f["duree"]) for f in films_data]

    salles = []
    for s in salles_data:
        film_obj = next((f for f in films if f.titre == s.get("film")), None)
        salle = Salle(s["numero"], s["capacite"], film_obj)
        salle.places_reservees = s.get("places_reservees", 0)
        salles.append(salle)

    reservations = []
    for r in reservations_data:
        film_obj = next((f for f in films if f.titre == r["film"]), None)
        salle_obj = next((s for s in salles if s.numero == r["salle"]), None)
        if film_obj and salle_obj:
            reservation = Reservation(r["client_nom"], film_obj, salle_obj, r["nb_places"])
            reservations.append(reservation)

    return films, salles, reservations

def sauvegarder_donnees(films, salles, reservations):
    films_dict = [f.to_dict() for f in films]
    salles_dict = [s.to_dict() for s in salles]
    reservations_dict = [r.to_dict() for r in reservations]

    sauvegarder_json(FILMS_FILE, films_dict)
    sauvegarder_json(SALLES_FILE, salles_dict)
    sauvegarder_json(RES_FILE, reservations_dict)
