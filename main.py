from utilisateur import GestionUtilisateurs
from classe import Film, Salle, Reservation, SallePleineException
from sauvegarde import charger_donnees, sauvegarder_donnees

class CinemaApp:
    def __init__(self):
        self.gestion_utilisateurs = GestionUtilisateurs()
        self.utilisateur_connecte = None
        self.films, self.salles, self.reservations = charger_donnees()
    
    def menu_principal(self):
        while True:
            print("\n --- CINÉMA  ---")
            print("1. Se connecter")
            print("2. S'inscrire (client)")
            print("3. Quitter")
            
            choix = input("Choix : ")
            
            if choix == "1":
                self.connexion()
            elif choix == "2":
                self.inscription()
            elif choix == "3":
                print(" Au revoir !")
                break
            else:
                print("❌ Choix invalide.")
    
    def connexion(self):
        print("\n🔐 CONNEXION")
        username = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")
        
        succes, resultat = self.gestion_utilisateurs.connecter(username, password)
        if succes:
            self.utilisateur_connecte = resultat
            print(f" Connecté en tant que {self.utilisateur_connecte.username} ({self.utilisateur_connecte.role})")
            if self.utilisateur_connecte.role == "admin":
                self.menu_admin()
            else:
                self.menu_client()
        else:
            print(resultat)
    
    def inscription(self):
        print("\n INSCRIPTION CLIENT")
        username = input("Choisissez un nom d'utilisateur : ")
        password = input("Choisissez un mot de passe : ")
        
        succes, message = self.gestion_utilisateurs.inscrire(username, password, "client")
        print(message)
    
    def menu_admin(self):
        while True:
            print("\n  --- MENU ADMINISTRATEUR ---")
            print("1. Gérer les films")
            print("2. Gérer les salles")
            print("3. Programmer un film")
            print("4. Voir les statistiques")
            print("5. Se déconnecter")
            
            choix = input("Choix : ")
            
            if choix == "1":
                self.gerer_films()
            elif choix == "2":
                self.gerer_salles()
            elif choix == "3":
                self.programmer_film()
            elif choix == "4":
                self.voir_statistiques()
            elif choix == "5":
                self.utilisateur_connecte = None
                break
            else:
                print("❌ Choix invalide.")
    
    def menu_client(self):
        while True:
            print(f"\n --- MENU CLIENT ({self.utilisateur_connecte.username}) ---")
            print("1. Voir les films")
            print("2. Réserver des places")
            print("3. Mes réservations")
            print("4. Se déconnecter")
            
            choix = input("Choix : ")
            
            if choix == "1":
                self.voir_films_client()
            elif choix == "2":
                self.reserver_places()
            elif choix == "3":
                self.mes_reservations()
            elif choix == "4":
                self.utilisateur_connecte = None
                break
            else:
                print(" Choix invalide.")
    
    # === METHODES ADMIN ===
    
    def gerer_films(self):
        while True:
            print("\n  GESTION DES FILMS")
            print("1. Ajouter un film")
            print("2. Lister les films")
            print("3. Retour")
            
            choix = input("Choix : ")
            
            if choix == "1":
                titre = input("Titre du film : ")
                duree = input("Durée (min) : ")
                self.films.append(Film(titre, duree))
                sauvegarder_donnees(self.films, self.salles, self.reservations)
                print(" Film ajouté !")
            elif choix == "2":
                self.voir_films()
            elif choix == "3":
                break
            else:
                print("❌ Choix invalide.")
    
    def gerer_salles(self):
        while True:
            print("\n GESTION DES SALLES")
            print("1. Créer une salle")
            print("2. Lister les salles")
            print("3. Retour")
            
            choix = input("Choix : ")
            
            if choix == "1":
                numero = int(input("Numéro de salle : "))
                capacite = int(input("Capacité : "))
                self.salles.append(Salle(numero, capacite))
                sauvegarder_donnees(self.films, self.salles, self.reservations)
                print(" Salle créée !")
            elif choix == "2":
                self.voir_salles()
            elif choix == "3":
                break
            else:
                print("❌ Choix invalide.")
    
    def programmer_film(self):
        if not self.salles:
            print("❌ Aucune salle disponible.")
            return
        if not self.films:
            print("❌ Aucun film disponible.")
            return
            
        print("Salles disponibles :")
        for s in self.salles:
            film_actuel = s.film.titre if s.film else "Aucun"
            print(f"- Salle {s.numero} (Film actuel: {film_actuel})")
        
        numero_salle = int(input("Numéro de la salle : "))
        salle = next((s for s in self.salles if s.numero == numero_salle), None)
        
        if not salle:
            print("❌ Salle non trouvée.")
            return
            
        print("Films disponibles :")
        for f in self.films:
            print(f"- {f.titre} ({f.duree} min)")
        
        titre_film = input("Titre du film à programmer : ")
        film = next((f for f in self.films if f.titre == titre_film), None)
        
        if not film:
            print("❌ Film non trouvé.")
            return
            
        salle.film = film
        sauvegarder_donnees(self.films, self.salles, self.reservations)
        print(f" Film '{film.titre}' programmé dans la salle {salle.numero} !")
    
    def voir_statistiques(self):
        print("\n STATISTIQUES")
        print(f"Nombre de films : {len(self.films)}")
        print(f"Nombre de salles : {len(self.salles)}")
        print(f"Nombre de réservations : {len(self.reservations)}")
        
        total_places_vendues = sum(r.nb_places for r in self.reservations)
        print(f"Total places vendues : {total_places_vendues}")
        
        # Films les plus populaires
        films_populaires = {}
        for res in self.reservations:
            films_populaires[res.film.titre] = films_populaires.get(res.film.titre, 0) + res.nb_places
        
        if films_populaires:
            print("\n  FILMS LES PLUS POPULAIRES :")
            for film, places in sorted(films_populaires.items(), key=lambda x: x[1], reverse=True):
                print(f"- {film} : {places} places vendues")
    
    # === METHODES CLIENT ===
    
    def voir_films_client(self):
        films_programmes = [s.film for s in self.salles if s.film]
        if not films_programmes:
            print("❌ Aucun film programmé pour le moment.")
            return
            
        print("\n🎬 FILMS À L'AFFICHE :")
        films_vus = set()
        for film in films_programmes:
            if film.titre not in films_vus:
                salles_film = [s for s in self.salles if s.film and s.film.titre == film.titre]
                places_total = sum(s.capacite - s.places_reservees for s in salles_film)
                print(f"- {film.titre} ({film.duree} min) - {len(salles_film)} salle(s) - {places_total} places disponibles")
                films_vus.add(film.titre)
    
    def reserver_places(self):
        films_programmes = list(set(s.film for s in self.salles if s.film))
        if not films_programmes:
            print("❌ Aucun film programmé pour le moment.")
            return
            
        print("Films disponibles :")
        for film in films_programmes:
            print(f"- {film.titre}")
        
        titre_film = input("Choisissez un film : ")
        film = next((f for f in films_programmes if f.titre == titre_film), None)
        
        if not film:
            print("❌ Film non trouvé.")
            return
            
        salles_film = [s for s in self.salles if s.film and s.film.titre == film.titre]
        print("Salles disponibles :")
        for s in salles_film:
            places_restantes = s.capacite - s.places_reservees
            print(f"- Salle {s.numero} ({places_restantes} places restantes)")
        
        numero_salle = int(input("Numéro de la salle : "))
        salle = next((s for s in salles_film if s.numero == numero_salle), None)
        
        if not salle:
            print("❌ Salle non trouvée.")
            return
            
        try:
            nb_places = int(input("Nombre de places : "))
            if nb_places <= 0:
                print("❌ Le nombre de places doit être positif.")
                return
                
            reservation = Reservation(self.utilisateur_connecte.username, film, salle, nb_places)
            reservation.confirmer()
            self.reservations.append(reservation)
            sauvegarder_donnees(self.films, self.salles, self.reservations)
            
        except SallePleineException as e:
            print(f"❌ {e}")
        except ValueError:
            print("❌ Nombre de places invalide.")
    
    def mes_reservations(self):
        mes_res = [r for r in self.reservations if r.client_nom == self.utilisateur_connecte.username]
        if not mes_res:
            print("❌ Vous n'avez aucune réservation.")
            return
            
        print("\n MES RÉSERVATIONS :")
        for res in mes_res:
            print(f"- {res.nb_places} place(s) pour '{res.film.titre}' (Salle {res.salle.numero})")
    
    # === METHODES COMMUNES ===
    
    def voir_films(self):
        if not self.films:
            print("Aucun film disponible.")
        else:
            print("\n  FILMS :")
            for film in self.films:
                salles_film = [s for s in self.salles if s.film and s.film.titre == film.titre]
                print(f"- {film.titre} ({film.duree} min) - Programmé dans {len(salles_film)} salle(s)")
    
    def voir_salles(self):
        if not self.salles:
            print("Aucune salle disponible.")
        else:
            print("\n  SALLES :")
            for salle in self.salles:
                film_nom = salle.film.titre if salle.film else "Aucun film programmé"
                places_restantes = salle.capacite - salle.places_reservees
                print(f"- Salle {salle.numero}: {salle.capacite} places, {salle.places_reservees} réservées, {places_restantes} restantes - Film: {film_nom}")

if __name__ == "__main__":
    app = CinemaApp()
    app.menu_principal()
