from utilisateur import GestionUtilisateurs
from classe import Film, Salle, Reservation, SallePleineException
from sauvegarde import charger_donnees, sauvegarder_donnees
from utils import clear_ecran, pause_ecran 

class CinemaApp:
    def __init__(self):
        self.gestion_utilisateurs = GestionUtilisateurs()
        self.utilisateur_connecte = None
        self.films, self.salles, self.reservations, _ = charger_donnees()
    
    def afficher_menu(self, titre, options):
        """Affiche un menu avec titre et options numérotées"""
        clear_ecran()  # Efface l'écran avant d'afficher le menu
        print(f"\n{'='*50}")
        print(f"🎬 {titre}")
        print('='*50)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print(f"{len(options)+1}. Retour")
        if hasattr(self, 'utilisateur_connecte') and self.utilisateur_connecte:
            print(f"👤 Connecté en tant que : {self.utilisateur_connecte.username}")
        print('='*50)
    
    def afficher_page(self, titre, contenu):
        """Affiche une page avec un titre et du contenu"""
        clear_ecran()
        print(f"\n{'='*50}")
        print(f"🎬 {titre}")
        print('='*50)
        print(contenu)
        print('='*50)
    
    def choisir_option(self, max_option):
        """Demande à l'utilisateur de choisir une option valide"""
        while True:
            try:
                choix = input("\nVotre choix : ")
                if not choix:
                    continue
                choix_int = int(choix)
                if 1 <= choix_int <= max_option + 1:
                    return choix_int
                else:
                    print("❌ Choix invalide. Veuillez choisir un nombre dans la liste.")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")
    
    def selectionner_par_liste(self, elements, message, attr_display=None):
        """Permet de sélectionner un élément dans une liste"""
        if not elements:
            print(f"❌ Aucun élément disponible.")
            pause_ecran()
            return None
        
        clear_ecran()
        print(f"\n{message}")
        print("-" * 40)
        for i, element in enumerate(elements, 1):
            if attr_display:
                affichage = getattr(element, attr_display)
            else:
                affichage = str(element)
            print(f"{i}. {affichage}")
        print(f"{len(elements)+1}. Annuler")
        print("-" * 40)
        
        choix = self.choisir_option(len(elements))
        if choix == len(elements) + 1:
            return None
        return elements[choix - 1]
    
    def demander_nombre(self, message, min_val=1, max_val=None):
        """Demande un nombre avec validation"""
        while True:
            try:
                valeur = input(f"{message} : ")
                if not valeur:
                    continue
                nombre = int(valeur)
                if nombre < min_val:
                    print(f"❌ Le nombre doit être au moins {min_val}.")
                    continue
                if max_val and nombre > max_val:
                    print(f"❌ Le nombre ne peut pas dépasser {max_val}.")
                    continue
                return nombre
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")

    def menu_principal(self):
        while True:
            self.afficher_menu("CINÉMA PARADIS", [
                "Se connecter",
                "S'inscrire (client)"
            ])
            
            choix = self.choisir_option(2)
            
            if choix == 1:
                self.connexion()
            elif choix == 2:
                self.inscription()
            elif choix == 3:
                print("👋 Au revoir !")
                break
    
    def connexion(self):
        clear_ecran()
        print("\n🔐 CONNEXION")
        print("-" * 30)
        username = input("Nom d'utilisateur : ").strip()
        password = input("Mot de passe : ").strip()
        
        if not username or not password:
            print("❌ Veuillez remplir tous les champs.")
            pause_ecran()
            return
        
        succes, resultat = self.gestion_utilisateurs.connecter(username, password)
        if succes:
            self.utilisateur_connecte = resultat
            print(f"✅ Connecté en tant que {self.utilisateur_connecte.username} ({self.utilisateur_connecte.role})")
            pause_ecran()
            if self.utilisateur_connecte.role == "admin":
                self.menu_admin()
            else:
                self.menu_client()
        else:
            print(resultat)
            pause_ecran()
    
    def inscription(self):
        clear_ecran()
        print("\n📝 INSCRIPTION CLIENT")
        print("-" * 30)
        username = input("Choisissez un nom d'utilisateur : ").strip()
        password = input("Choisissez un mot de passe : ").strip()
        
        if not username or not password:
            print("❌ Veuillez remplir tous les champs.")
            pause_ecran()
            return
        
        succes, message = self.gestion_utilisateurs.inscrire(username, password, "client")
        print(message)
        pause_ecran()
    
    def menu_admin(self):
        while True:
            self.afficher_menu("MENU ADMINISTRATEUR", [
                "Gérer les films",
                "Gérer les salles", 
                "Programmer un film",
                "Voir les statistiques"
            ])
            
            choix = self.choisir_option(4)
            
            if choix == 1:
                self.gerer_films()
            elif choix == 2:
                self.gerer_salles()
            elif choix == 3:
                self.programmer_film()
            elif choix == 4:
                self.voir_statistiques()
            elif choix == 5:
                self.utilisateur_connecte = None
                print("👋 Déconnexion réussie !")
                pause_ecran()
                break
    
    def menu_client(self):
        while True:
            self.afficher_menu("MENU CLIENT", [
                "Voir les films à l'affiche",
                "Réserver des places",
                "Mes réservations"
            ])
            
            choix = self.choisir_option(3)
            
            if choix == 1:
                self.voir_films_client()
            elif choix == 2:
                self.reserver_places()
            elif choix == 3:
                self.mes_reservations()
            elif choix == 4:
                self.utilisateur_connecte = None
                print("👋 Déconnexion réussie !")
                pause_ecran()
                break
    
    # === METHODES ADMIN ===
    
    def gerer_films(self):
        while True:
            self.afficher_menu("GESTION DES FILMS", [
                "Ajouter un film",
                "Lister tous les films"
            ])
            
            choix = self.choisir_option(2)
            
            if choix == 1:
                self.ajouter_film()
            elif choix == 2:
                self.lister_films()
            elif choix == 3:
                break
    
    def ajouter_film(self):
        clear_ecran()
        print("\n🎬 AJOUTER UN FILM")
        print("-" * 30)
        titre = input("Titre du film : ").strip()
        if not titre:
            print("❌ Le titre ne peut pas être vide.")
            pause_ecran()
            return
        
        duree = self.demander_nombre("Durée en minutes")
        
        self.films.append(Film(titre, duree))
        sauvegarder_donnees(self.films, self.salles, self.reservations)
        print(f"✅ Film '{titre}' ajouté avec succès !")
        pause_ecran()
    
    def lister_films(self):
        if not self.films:
            self.afficher_page("LISTE DES FILMS", "❌ Aucun film disponible.")
            pause_ecran()
            return
        
        contenu = ""
        for film in self.films:
            salles_count = len([s for s in self.salles if s.film and s.film.titre == film.titre])
            contenu += f"🎬 {film.titre} ({film.duree} min) - Programmé dans {salles_count} salle(s)\n"
        
        self.afficher_page("LISTE DES FILMS", contenu)
        pause_ecran()
    
    def gerer_salles(self):
        while True:
            self.afficher_menu("GESTION DES SALLES", [
                "Créer une salle",
                "Lister toutes les salles"
            ])
            
            choix = self.choisir_option(2)
            
            if choix == 1:
                self.creer_salle()
            elif choix == 2:
                self.lister_salles()
            elif choix == 3:
                break
    
    def creer_salle(self):
        clear_ecran()
        print("\n🎭 CRÉER UNE SALLE")
        print("-" * 30)
        numero = self.demander_nombre("Numéro de la salle")
        
        # Vérifier si le numéro existe déjà
        if any(s.numero == numero for s in self.salles):
            print("❌ Une salle avec ce numéro existe déjà.")
            pause_ecran()
            return
        
        capacite = self.demander_nombre("Capacité de la salle", min_val=1)
        
        self.salles.append(Salle(numero, capacite))
        sauvegarder_donnees(self.films, self.salles, self.reservations)
        print(f"✅ Salle {numero} créée avec succès !")
        pause_ecran()
    
    def lister_salles(self):
        if not self.salles:
            self.afficher_page("LISTE DES SALLES", "❌ Aucune salle disponible.")
            pause_ecran()
            return
        
        contenu = ""
        for salle in self.salles:
            film_nom = salle.film.titre if salle.film else "Aucun film"
            places_restantes = salle.capacite - salle.places_reservees
            contenu += f"🎭 Salle {salle.numero}: {places_restantes}/{salle.capacite} places - Film: {film_nom}\n"
        
        self.afficher_page("LISTE DES SALLES", contenu)
        pause_ecran()
    
    def programmer_film(self):
        if not self.salles:
            self.afficher_page("PROGRAMMATION", "❌ Aucune salle disponible. Créez d'abord une salle.")
            pause_ecran()
            return
        
        if not self.films:
            self.afficher_page("PROGRAMMATION", "❌ Aucun film disponible. Ajoutez d'abord un film.")
            pause_ecran()
            return
        
        # Sélectionner une salle
        salle = self.selectionner_par_liste(self.salles, "Sélectionnez une salle :", "numero")
        if not salle:
            return
        
        # Sélectionner un film
        film = self.selectionner_par_liste(self.films, "Sélectionnez un film à programmer :", "titre")
        if not film:
            return
        
        salle.film = film
        sauvegarder_donnees(self.films, self.salles, self.reservations)
        
        self.afficher_page("PROGRAMMATION", f"✅ Film '{film.titre}' programmé dans la salle {salle.numero} !")
        pause_ecran()
    
    def voir_statistiques(self):
        contenu = f"🎬 Films : {len(self.films)}\n"
        contenu += f"🎭 Salles : {len(self.salles)}\n"
        contenu += f"🎫 Réservations : {len(self.reservations)}\n"
        
        total_places = sum(r.nb_places for r in self.reservations)
        contenu += f"👥 Places vendues : {total_places}\n"
        
        # Films populaires
        films_populaires = {}
        for res in self.reservations:
            films_populaires[res.film.titre] = films_populaires.get(res.film.titre, 0) + res.nb_places
        
        if films_populaires:
            contenu += "\n🏆 FILMS LES PLUS POPULAIRES :\n"
            for film, places in sorted(films_populaires.items(), key=lambda x: x[1], reverse=True):
                contenu += f"  {film} : {places} places vendues\n"
        
        self.afficher_page("STATISTIQUES DU CINÉMA", contenu)
        pause_ecran()
    
    # === METHODES CLIENT ===
    
    def voir_films_client(self):
        salles_avec_films = [s for s in self.salles if s.film]
        if not salles_avec_films:
            self.afficher_page("FILMS À L'AFFICHE", "❌ Aucun film programmé pour le moment.")
            pause_ecran()
            return
        
        # Regrouper par film
        films_info = {}
        for salle in salles_avec_films:
            film_titre = salle.film.titre
            if film_titre not in films_info:
                film_obj = next(f for f in self.films if f.titre == film_titre)
                films_info[film_titre] = {
                    'duree': film_obj.duree,
                    'salles': [],
                    'places_total': 0
                }
            
            places_restantes = salle.capacite - salle.places_reservees
            films_info[film_titre]['salles'].append({
                'numero': salle.numero,
                'places_restantes': places_restantes
            })
            films_info[film_titre]['places_total'] += places_restantes
        
        contenu = ""
        for film_titre, info in films_info.items():
            salles_str = ", ".join([f"Salle {s['numero']}" for s in info['salles']])
            contenu += f"🎬 {film_titre} ({info['duree']} min)\n"
            contenu += f"   📍 Salles : {salles_str}\n"
            contenu += f"   🎟️  Places disponibles : {info['places_total']}\n\n"
        
        self.afficher_page("FILMS À L'AFFICHE", contenu)
        pause_ecran()
    
    def reserver_places(self):
        salles_avec_films = [s for s in self.salles if s.film and (s.capacite - s.places_reservees) > 0]
        if not salles_avec_films:
            self.afficher_page("RÉSERVATION", "❌ Aucune séance disponible pour le moment.")
            pause_ecran()
            return
        
        # Regrouper par film
        films_disponibles = {}
        for salle in salles_avec_films:
            film_titre = salle.film.titre
            if film_titre not in films_disponibles:
                film_obj = next(f for f in self.films if f.titre == film_titre)
                films_disponibles[film_titre] = {
                    'film_obj': film_obj,
                    'salles': []
                }
            
            places_restantes = salle.capacite - salle.places_reservees
            films_disponibles[film_titre]['salles'].append({
                'salle_obj': salle,
                'places_restantes': places_restantes
            })
        
        # Afficher les films disponibles
        clear_ecran()
        print("\n🎬 FILMS DISPONIBLES")
        print("-" * 50)
        films_liste = list(films_disponibles.keys())
        for i, film_titre in enumerate(films_liste, 1):
            info = films_disponibles[film_titre]
            salles_count = len(info['salles'])
            print(f"{i}. {film_titre} ({info['film_obj'].duree} min) - {salles_count} salle(s) disponible(s)")
        print(f"{len(films_liste)+1}. Annuler")
        print("-" * 50)
        
        choix_film = self.choisir_option(len(films_liste))
        if choix_film == len(films_liste) + 1:
            return
        
        film_titre = films_liste[choix_film - 1]
        film_info = films_disponibles[film_titre]
        
        # Sélectionner une salle pour ce film
        clear_ecran()
        print(f"\n🎭 SALLES POUR '{film_titre}'")
        print("-" * 40)
        salles_film = film_info['salles']
        for i, salle_info in enumerate(salles_film, 1):
            salle = salle_info['salle_obj']
            places = salle_info['places_restantes']
            print(f"{i}. Salle {salle.numero} - {places} places disponibles")
        print(f"{len(salles_film)+1}. Annuler")
        print("-" * 40)
        
        choix_salle = self.choisir_option(len(salles_film))
        if choix_salle == len(salles_film) + 1:
            return
        
        salle_selectionnee = salles_film[choix_salle - 1]['salle_obj']
        places_restantes = salles_film[choix_salle - 1]['places_restantes']
        
        # Demander le nombre de places
        clear_ecran()
        print(f"\n🎟️  RÉSERVATION - {film_titre} (Salle {salle_selectionnee.numero})")
        print(f"Places disponibles : {places_restantes}")
        print("-" * 40)
        
        nb_places = self.demander_nombre("Nombre de places à réserver", min_val=1, max_val=places_restantes)
        
        try:
            reservation = Reservation(self.utilisateur_connecte.username, salle_selectionnee.film, salle_selectionnee, nb_places)
            reservation.confirmer()
            self.reservations.append(reservation)
            sauvegarder_donnees(self.films, self.salles, self.reservations)
            
            self.afficher_page("RÉSERVATION", f"✅ Réservation confirmée !\n\n{nb_places} place(s) pour '{film_titre}'\nSalle {salle_selectionnee.numero}")
            pause_ecran()
            
        except SallePleineException as e:
            print(f"❌ {e}")
            print("💡 Veuillez réessayer avec un nombre de places inférieur.")
            pause_ecran()
    
    def mes_reservations(self):
        mes_res = [r for r in self.reservations if r.client_nom == self.utilisateur_connecte.username]
        if not mes_res:
            self.afficher_page("MES RÉSERVATIONS", "❌ Vous n'avez aucune réservation.")
            pause_ecran()
            return
        
        contenu = ""
        for i, res in enumerate(mes_res, 1):
            contenu += f"{i}. {res.nb_places} place(s) pour '{res.film.titre}' (Salle {res.salle.numero})\n"
        
        self.afficher_page("MES RÉSERVATIONS", contenu)
        pause_ecran()
    def sauvegarder_tout(self):
        """Sauvegarde toutes les données incluant les utilisateurs"""
        utilisateurs_data = [u.to_dict() for u in self.gestion_utilisateurs.utilisateurs]
        sauvegarder_donnees(self.films, self.salles, self.reservations, utilisateurs_data)

if __name__ == "__main__":
    app = CinemaApp()
    app.menu_principal()