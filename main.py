import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk

from utilisateur import GestionUtilisateurs
from classe import Film, Salle, Reservation, SallePleineException
from sauvegarde import charger_donnees, sauvegarder_donnees

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)



class CinemaApp:

    def __init__(self):
        self.gestion_utilisateurs = GestionUtilisateurs()
        self.utilisateur_connecte = None
        self.films, self.salles, self.reservations, _ = charger_donnees()

        self.root = tk.Tk()
        self.root.title("Cyné-flix")
        self.root.geometry("960x695")
        self.root.minsize(960, 695)

        self.notebook = ttk.Notebook(self.root)
        self.tabs = {}

        self._salle_options = {}
        self._programmation_salles = {}
        self._programmation_films = {}

        self._build_tabs()
        self.update_tabs()

        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.fermer)

    # === CONSTRUCTION DES ONGLETS ===

    def _build_tabs(self):
        self._build_accueil_tab()
        self._build_admin_tab()
        self._build_client_tab()
        self._build_stats_tab()

    def _build_accueil_tab(self):
        frame = ttk.Frame(self.notebook, padding=20)
        self.tabs["accueil"] = frame
        self.notebook.add(frame, text="Accueil")

        titre = ttk.Label(frame, text="Cyné-flix", font=("Arial", 20, "bold"))
        titre.pack(pady=(0, 20))

        self.info_connexion_var = tk.StringVar(value="Connectez-vous ou inscrivez-vous pour commencer.")
        ttk.Label(frame, textvariable=self.info_connexion_var).pack(pady=(0, 20))

        form_connexion = ttk.LabelFrame(frame, text="Connexion", padding=15)
        form_connexion.pack(fill="x", pady=(0, 15))

        ttk.Label(form_connexion, text="Nom d'utilisateur").grid(row=0, column=0, sticky="w")
        self.username_entry = ttk.Entry(form_connexion)
        self.username_entry.grid(row=0, column=1, sticky="ew", padx=8, pady=5)

        ttk.Label(form_connexion, text="Mot de passe").grid(row=1, column=0, sticky="w")
        self.password_entry = ttk.Entry(form_connexion, show="*")
        self.password_entry.grid(row=1, column=1, sticky="ew", padx=8, pady=5)

        form_connexion.columnconfigure(1, weight=1)

        ttk.Button(form_connexion, text="Se connecter", command=self.connexion).grid(
            row=2, column=0, columnspan=2, pady=10, sticky="ew"
        )

        form_inscription = ttk.LabelFrame(frame, text="Inscription client", padding=15)
        form_inscription.pack(fill="x")

        ttk.Label(form_inscription, text="Nom d'utilisateur").grid(row=0, column=0, sticky="w")
        self.username_insc_entry = ttk.Entry(form_inscription)
        self.username_insc_entry.grid(row=0, column=1, sticky="ew", padx=8, pady=5)

        ttk.Label(form_inscription, text="Mot de passe").grid(row=1, column=0, sticky="w")
        self.password_insc_entry = ttk.Entry(form_inscription, show="*")
        self.password_insc_entry.grid(row=1, column=1, sticky="ew", padx=8, pady=5)

        form_inscription.columnconfigure(1, weight=1)

        ttk.Button(form_inscription, text="S'inscrire", command=self.inscription).grid(
            row=2, column=0, columnspan=2, pady=10, sticky="ew"
        )

    def _build_admin_tab(self):
        frame = ttk.Frame(self.notebook, padding=15)
        self.tabs["admin"] = frame

        header = ttk.Frame(frame)
        header.pack(fill="x", pady=(0, 10))
        ttk.Label(header, text="Espace administrateur", font=("Arial", 16, "bold")).pack(side="left")
        ttk.Button(header, text="Se déconnecter", command=self.deconnexion).pack(side="right")

        content = ttk.Frame(frame)
        content.pack(fill="both", expand=True)
        content.columnconfigure((0, 1), weight=1)

        films_frame = ttk.LabelFrame(content, text="Gestion des films", padding=10)
        films_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=(0, 10))
        films_frame.columnconfigure(1, weight=1)

        ttk.Label(films_frame, text="Titre").grid(row=0, column=0, sticky="w")
        self.film_titre_entry = ttk.Entry(films_frame)
        self.film_titre_entry.grid(row=0, column=1, sticky="ew", padx=6, pady=4)

        ttk.Label(films_frame, text="Durée (min)").grid(row=1, column=0, sticky="w")
        self.film_duree_entry = ttk.Entry(films_frame)
        self.film_duree_entry.grid(row=1, column=1, sticky="ew", padx=6, pady=4)

        ttk.Button(films_frame, text="Ajouter le film", command=self.ajouter_film).grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=6
        )

        self.liste_films = tk.Listbox(films_frame, height=10)
        self.liste_films.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(10, 0))
        films_frame.rowconfigure(3, weight=1)

        salles_frame = ttk.LabelFrame(content, text="Gestion des salles", padding=10)
        salles_frame.grid(row=0, column=1, sticky="nsew", pady=(0, 10))
        salles_frame.columnconfigure(1, weight=1)

        ttk.Label(salles_frame, text="Numéro").grid(row=0, column=0, sticky="w")
        self.salle_num_entry = ttk.Entry(salles_frame)
        self.salle_num_entry.grid(row=0, column=1, sticky="ew", padx=6, pady=4)

        ttk.Label(salles_frame, text="Capacité").grid(row=1, column=0, sticky="w")
        self.salle_cap_entry = ttk.Entry(salles_frame)
        self.salle_cap_entry.grid(row=1, column=1, sticky="ew", padx=6, pady=4)

        ttk.Button(salles_frame, text="Créer la salle", command=self.creer_salle).grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=6
        )

        self.liste_salles = tk.Listbox(salles_frame, height=10)
        self.liste_salles.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(10, 0))
        salles_frame.rowconfigure(3, weight=1)

        prog_frame = ttk.LabelFrame(frame, text="Programmer un film", padding=10)
        prog_frame.pack(fill="x", pady=(0, 10))
        prog_frame.columnconfigure(1, weight=1)

        ttk.Label(prog_frame, text="Salle").grid(row=0, column=0, sticky="w")
        self.combo_salles_prog = ttk.Combobox(prog_frame, state="readonly")
        self.combo_salles_prog.grid(row=0, column=1, sticky="ew", padx=6, pady=4)

        ttk.Label(prog_frame, text="Film").grid(row=1, column=0, sticky="w")
        self.combo_films_prog = ttk.Combobox(prog_frame, state="readonly")
        self.combo_films_prog.grid(row=1, column=1, sticky="ew", padx=6, pady=4)

        ttk.Button(prog_frame, text="Programmer", command=self.programmer_film).grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=6
        )

    def _build_client_tab(self):
        frame = ttk.Frame(self.notebook, padding=15)
        self.tabs["client"] = frame

        header = ttk.Frame(frame)
        header.pack(fill="x", pady=(0, 10))
        ttk.Label(header, text="Espace client", font=("Arial", 16, "bold")).pack(side="left")
        ttk.Button(header, text="Se déconnecter", command=self.deconnexion).pack(side="right")

        content = ttk.Frame(frame)
        content.pack(fill="both", expand=True)
        content.columnconfigure((0, 1), weight=1)

        films_frame = ttk.LabelFrame(content, text="Films à l'affiche", padding=10)
        films_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=(0, 10))
        self.liste_films_affiche = tk.Listbox(films_frame, height=14)
        self.liste_films_affiche.pack(fill="both", expand=True)

        resa_frame = ttk.LabelFrame(content, text="Réserver des places", padding=10)
        resa_frame.grid(row=0, column=1, sticky="nsew", pady=(0, 10))
        resa_frame.columnconfigure(1, weight=1)

        ttk.Label(resa_frame, text="Film").grid(row=0, column=0, sticky="w")
        self.resa_film_var = tk.StringVar()
        self.combo_resa_films = ttk.Combobox(resa_frame, textvariable=self.resa_film_var, state="readonly")
        self.combo_resa_films.grid(row=0, column=1, sticky="ew", padx=6, pady=4)
        self.combo_resa_films.bind("<<ComboboxSelected>>", self._on_resa_film_change)

        ttk.Label(resa_frame, text="Salle").grid(row=1, column=0, sticky="w")
        self.resa_salle_var = tk.StringVar()
        self.combo_resa_salles = ttk.Combobox(resa_frame, textvariable=self.resa_salle_var, state="readonly")
        self.combo_resa_salles.grid(row=1, column=1, sticky="ew", padx=6, pady=4)

        ttk.Label(resa_frame, text="Nombre de places").grid(row=2, column=0, sticky="w")
        self.resa_places_entry = ttk.Entry(resa_frame)
        self.resa_places_entry.grid(row=2, column=1, sticky="ew", padx=6, pady=4)

        ttk.Button(resa_frame, text="Réserver", command=self.reserver_places).grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=6
        )

        mes_res_frame = ttk.LabelFrame(frame, text="Mes réservations", padding=10)
        mes_res_frame.pack(fill="both", expand=True)
        self.liste_reservations = tk.Listbox(mes_res_frame, height=8)
        self.liste_reservations.pack(fill="both", expand=True)

    def _build_stats_tab(self):
        frame = ttk.Frame(self.notebook, padding=15)
        self.tabs["stats"] = frame

        ttk.Label(frame, text="Statistiques du cinéma", font=("Arial", 16, "bold")).pack(anchor="w", pady=(0, 10))
        self.stats_text = tk.Text(frame, height=20, state="disabled")
        self.stats_text.pack(fill="both", expand=True)

    # === CONNEXION / INSCRIPTION ===

    def connexion(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        succes, resultat = self.gestion_utilisateurs.connecter(username, password)
        if succes:
            self.utilisateur_connecte = resultat
            messagebox.showinfo(
                "Succès", f"Connecté en tant que {self.utilisateur_connecte.username} ({self.utilisateur_connecte.role})"
            )
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.info_connexion_var.set(f"Connecté : {self.utilisateur_connecte.username} ({self.utilisateur_connecte.role})")
            self.update_tabs()
            self.rafraichir_donnees()
        else:
            messagebox.showerror("Erreur", resultat)

    def inscription(self):
        username = self.username_insc_entry.get().strip()
        password = self.password_insc_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        succes, message = self.gestion_utilisateurs.inscrire(username, password, "client")
        if succes:
            messagebox.showinfo("Succès", message)
            self.username_insc_entry.delete(0, tk.END)
            self.password_insc_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erreur", message)

    def deconnexion(self):
        self.utilisateur_connecte = None
        self.info_connexion_var.set("Connectez-vous ou inscrivez-vous pour commencer.")
        messagebox.showinfo("Déconnexion", "Vous avez été déconnecté.")
        self.update_tabs()

    # === ADMIN ===

    def ajouter_film(self):
        titre = self.film_titre_entry.get().strip()
        duree_str = self.film_duree_entry.get().strip()

        if not titre or not duree_str:
            messagebox.showerror("Erreur", "Titre et durée sont requis.")
            return
        try:
            duree = int(duree_str)
        except ValueError:
            messagebox.showerror("Erreur", "La durée doit être un nombre.")
            return

        self.films.append(Film(titre, duree))
        self.film_titre_entry.delete(0, tk.END)
        self.film_duree_entry.delete(0, tk.END)
        self._sauvegarder()
        self.rafraichir_donnees()
        messagebox.showinfo("Succès", f"Film '{titre}' ajouté.")

    def creer_salle(self):
        numero_str = self.salle_num_entry.get().strip()
        capacite_str = self.salle_cap_entry.get().strip()

        if not numero_str or not capacite_str:
            messagebox.showerror("Erreur", "Numéro et capacité sont requis.")
            return
        try:
            numero = int(numero_str)
            capacite = int(capacite_str)
        except ValueError:
            messagebox.showerror("Erreur", "Numéro et capacité doivent être des nombres.")
            return

        if any(s.numero == numero for s in self.salles):
            messagebox.showerror("Erreur", "Une salle avec ce numéro existe déjà.")
            return

        self.salles.append(Salle(numero, capacite))
        self.salle_num_entry.delete(0, tk.END)
        self.salle_cap_entry.delete(0, tk.END)
        self._sauvegarder()
        self.rafraichir_donnees()
        messagebox.showinfo("Succès", f"Salle {numero} créée.")

    def programmer_film(self):
        salle_label = self.combo_salles_prog.get()
        film_label = self.combo_films_prog.get()

        if not salle_label or not film_label:
            messagebox.showerror("Erreur", "Sélectionnez une salle et un film.")
            return

        salle = self._programmation_salles.get(salle_label)
        film = self._programmation_films.get(film_label)

        if not salle or not film:
            messagebox.showerror("Erreur", "Sélection invalide.")
            return

        salle.film = film
        self._sauvegarder()
        self.rafraichir_donnees()
        messagebox.showinfo("Succès", f"Film '{film.titre}' programmé en salle {salle.numero}.")

    # === CLIENT ===

    def _films_disponibles(self):
        salles_avec_films = [s for s in self.salles if s.film and (s.capacite - s.places_reservees) > 0]
        films_disponibles = {}
        for salle in salles_avec_films:
            film_titre = salle.film.titre
            if film_titre not in films_disponibles:
                film_obj = next(f for f in self.films if f.titre == film_titre)
                films_disponibles[film_titre] = {"film_obj": film_obj, "salles": []}
            places_restantes = salle.capacite - salle.places_reservees
            films_disponibles[film_titre]["salles"].append({"salle_obj": salle, "places_restantes": places_restantes})
        return films_disponibles

    def reserver_places(self):
        if not self.utilisateur_connecte or self.utilisateur_connecte.role != "client":
            messagebox.showerror("Erreur", "Connectez-vous en tant que client pour réserver.")
            return

        film_titre = self.combo_resa_films.get()
        salle_label = self.combo_resa_salles.get()
        nb_places_str = self.resa_places_entry.get().strip()

        if not film_titre or not salle_label or not nb_places_str:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        try:
            nb_places = int(nb_places_str)
        except ValueError:
            messagebox.showerror("Erreur", "Le nombre de places doit être un nombre.")
            return

        salle_selectionnee = self._salle_options.get(salle_label)
        films_dispo = self._films_disponibles()
        film_info = films_dispo.get(film_titre)
        if not salle_selectionnee or not film_info:
            messagebox.showerror("Erreur", "Sélection invalide.")
            return

        places_restantes = salle_selectionnee.capacite - salle_selectionnee.places_reservees
        if nb_places < 1 or nb_places > places_restantes:
            messagebox.showerror("Erreur", f"Nombre de places entre 1 et {places_restantes}.")
            return

        try:
            reservation = Reservation(
                self.utilisateur_connecte.username, salle_selectionnee.film, salle_selectionnee, nb_places
            )
            reservation.confirmer()
            self.reservations.append(reservation)
            self._sauvegarder()
            self.rafraichir_donnees()
            self.resa_places_entry.delete(0, tk.END)
            messagebox.showinfo("Succès", f"Réservation confirmée pour '{film_titre}'.")
        except SallePleineException as e:
            messagebox.showerror("Erreur", str(e))

    # === MISE À JOUR UI ===

    def rafraichir_donnees(self):
        self._rafraichir_listes_admin()
        self._rafraichir_reservation_fields()
        self._rafraichir_films_affiche()
        self._rafraichir_reservations_client()
        self._rafraichir_programmation_fields()
        self._rafraichir_stats()

    def _rafraichir_listes_admin(self):
        self.liste_films.delete(0, tk.END)
        for film in self.films:
            salles_count = len([s for s in self.salles if s.film and s.film.titre == film.titre])
            self.liste_films.insert(tk.END, f"{film.titre} ({film.duree} min) - {salles_count} salle(s)")

        self.liste_salles.delete(0, tk.END)
        for salle in self.salles:
            film_nom = salle.film.titre if salle.film else "Aucun film"
            places_restantes = salle.capacite - salle.places_reservees
            self.liste_salles.insert(
                tk.END, f"Salle {salle.numero} - {places_restantes}/{salle.capacite} places - Film: {film_nom}"
            )

    def _rafraichir_programmation_fields(self):
        self._programmation_salles = {}
        self._programmation_films = {}

        salles_labels = []
        for salle in sorted(self.salles, key=lambda s: s.numero):
            label = f"Salle {salle.numero}"
            salles_labels.append(label)
            self._programmation_salles[label] = salle
        self.combo_salles_prog["values"] = salles_labels
        self.combo_salles_prog.set(salles_labels[0] if salles_labels else "")

        films_labels = []
        for film in self.films:
            label = f"{film.titre} ({film.duree} min)"
            films_labels.append(label)
            self._programmation_films[label] = film
        self.combo_films_prog["values"] = films_labels
        self.combo_films_prog.set(films_labels[0] if films_labels else "")

    def _rafraichir_films_affiche(self):
        self.liste_films_affiche.delete(0, tk.END)
        films_info = {}
        for salle in [s for s in self.salles if s.film]:
            titre = salle.film.titre
            if titre not in films_info:
                films_info[titre] = {"duree": salle.film.duree, "salles": [], "places_total": 0}
            places_restantes = salle.capacite - salle.places_reservees
            films_info[titre]["salles"].append(salle.numero)
            films_info[titre]["places_total"] += places_restantes

        if not films_info:
            self.liste_films_affiche.insert(tk.END, "Aucun film programmé pour le moment.")
            return

        for titre, info in films_info.items():
            salles_str = ", ".join([f"Salle {n}" for n in info["salles"]])
            self.liste_films_affiche.insert(
                tk.END, f"{titre} ({info['duree']} min) - {salles_str} - Places dispo: {info['places_total']}"
            )

    def _rafraichir_reservation_fields(self):
        films_dispo = self._films_disponibles()
        films_labels = list(films_dispo.keys())
        self.combo_resa_films["values"] = films_labels
        if films_labels:
            current = self.combo_resa_films.get()
            if current not in films_labels:
                self.combo_resa_films.set(films_labels[0])
        else:
            self.combo_resa_films.set("")
        self._on_resa_film_change()

    def _on_resa_film_change(self, event=None):
        films_dispo = self._films_disponibles()
        film_titre = self.combo_resa_films.get()
        self._salle_options = {}

        if not film_titre or film_titre not in films_dispo:
            self.combo_resa_salles["values"] = []
            self.combo_resa_salles.set("")
            return

        salle_labels = []
        for s_info in films_dispo[film_titre]["salles"]:
            salle = s_info["salle_obj"]
            places = s_info["places_restantes"]
            label = f"Salle {salle.numero} ({places} places)"
            self._salle_options[label] = salle
            salle_labels.append(label)

        self.combo_resa_salles["values"] = salle_labels
        self.combo_resa_salles.set(salle_labels[0] if salle_labels else "")

    def _rafraichir_reservations_client(self):
        self.liste_reservations.delete(0, tk.END)
        if not self.utilisateur_connecte or self.utilisateur_connecte.role != "client":
            self.liste_reservations.insert(tk.END, "Connectez-vous en tant que client pour voir vos réservations.")
            return

        mes_res = [r for r in self.reservations if r.client_nom == self.utilisateur_connecte.username]
        if not mes_res:
            self.liste_reservations.insert(tk.END, "Aucune réservation.")
            return

        for res in mes_res:
            self.liste_reservations.insert(
                tk.END, f"{res.nb_places} place(s) - '{res.film.titre}' salle {res.salle.numero}"
            )

    def _rafraichir_stats(self):
        contenu = [
            f"Films : {len(self.films)}",
            f"Salles : {len(self.salles)}",
            f"Réservations : {len(self.reservations)}",
            f"Places vendues : {sum(r.nb_places for r in self.reservations)}",
        ]

        films_populaires = {}
        for res in self.reservations:
            films_populaires[res.film.titre] = films_populaires.get(res.film.titre, 0) + res.nb_places

        if films_populaires:
            contenu.append("")
            contenu.append("Films les plus populaires :")
            for film, places in sorted(films_populaires.items(), key=lambda x: x[1], reverse=True):
                contenu.append(f" - {film} : {places} places")

        self.stats_text.config(state="normal")
        self.stats_text.delete("1.0", tk.END)
        self.stats_text.insert("1.0", "\n".join(contenu))
        self.stats_text.config(state="disabled")

    # === UTILITAIRES ===

    def update_tabs(self):
        for key in ["admin", "client", "stats"]:
            frame = self.tabs[key]
            if str(frame) in self.notebook.tabs():
                self.notebook.forget(frame)

        if self.utilisateur_connecte:
            if self.utilisateur_connecte.role == "admin":
                self.notebook.add(self.tabs["admin"], text="Admin")
                self.notebook.add(self.tabs["stats"], text="Statistiques")
                self.notebook.select(self.tabs["admin"])
            else:
                self.notebook.add(self.tabs["client"], text="Client")
                self.notebook.select(self.tabs["client"])
        else:
            self.notebook.select(self.tabs["accueil"])

    def _sauvegarder(self):
        sauvegarder_donnees(self.films, self.salles, self.reservations)

    def fermer(self):
        self._sauvegarder()
        self.root.destroy()

    def run(self):
        self.rafraichir_donnees()
        self.root.mainloop()


if __name__ == "__main__":
    app = CinemaApp()
    sv_ttk.set_theme("dark")
    app.run()
