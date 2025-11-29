class Film:
    def __init__(self, titre, duree):
        self.titre = titre
        self.duree = duree
    
    def to_dict(self):
        return {"titre": self.titre, "duree": self.duree}

class Salle:
    def __init__(self, numero, capacite, film=None):
        self.numero = numero
        self.capacite = capacite
        self.film = film
        self.places_reservees = 0

    def reserver_place(self, nb):
        if self.places_reservees + nb > self.capacite:
            raise SallePleineException("Salle pleine !")
        self.places_reservees += nb
    
    def to_dict(self):
        return {
            "numero": self.numero,
            "capacite": self.capacite,
            "film": self.film.titre if self.film else None,
            "places_reservees": self.places_reservees
        }

class SallePleineException(Exception):
    pass

class FilmInexistantException(Exception):
    pass

class Reservation:
    def __init__(self, client_nom, film, salle, nb_places):
        self.client_nom = client_nom
        self.film = film
        self.salle = salle
        self.nb_places = nb_places

    def confirmer(self):
        self.salle.reserver_place(self.nb_places)
        print(f"Réservation confirmée pour {self.client_nom} ({self.nb_places} places pour {self.film.titre})")
    
    def to_dict(self):
        return {
            "client_nom": self.client_nom,
            "film": self.film.titre,
            "salle": self.salle.numero,
            "nb_places": self.nb_places
        }