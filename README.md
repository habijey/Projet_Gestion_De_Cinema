# 🎬 Projet_Gestion_De_Cinema

Application de gestion de cinéma développée en **Python** avec **interface graphique Tkinter**.
Elle permet de gérer les films, salles, utilisateurs, réservations et statistiques.

---

# 🚀 Installation & Préparation

## ✅ 1. Prérequis

Avant de lancer l’application, assure-toi d’avoir :

### 📝 Logiciels requis

* **Python 3.8 ou plus**
* **Tkinter** (inclus par défaut dans la plupart des installations Python)
* **pip** (gestionnaire de paquets Python)

### 🎨 Thème graphique requis

L’application utilise le thème moderne **Sun Valley Tkinter (sv-ttk)**.

📦 **Installer le thème :**

```bash
pip install sv-ttk
```

---

# ▶️ 2. Vérifier que Python est installé

```bash
python --version
```

Si cela ne fonctionne pas, utilise plutôt :

```bash
python3 --version
```

---

# ▶️ 3. Lancer l’application

Une fois les dépendances installées :

```bash
python main.py
```

ou (selon le système)

```bash
python3 main.py
```

---

# 📦 Structure du projet

```
cinema/
├── main.py            # Interface graphique
├── classe.py          # Films, salles, réservations
├── utilisateur.py     # Gestion des utilisateurs
├── sauvegarde.py      # Sauvegarde des données
├── utils.py           # Fonctions utilitaires
└── Data/              # Dossier créé automatiquement (JSON)
```

---

# 👤 Comptes de démonstration

### 👑 Administrateur

* **Utilisateur** : `admin`
* **Mot de passe** : `admin123`

### 👤 Clients

* `user1 / client123`
* `user2 / password123`
* `test / client123`

---

# 🧭 Fonctionnalités

### 👑 Administrateur

✔ Ajouter des films
✔ Créer des salles
✔ Programmer des films
✔ Consulter les statistiques

### 👤 Client

✔ Voir les films disponibles
✔ Réserver des places
✔ Consulter l’historique

---

# 🎬 Données de test incluses

* **6 films** prédéfinis
* **8 salles**
* Sauvegarde automatique **JSON**

---

# ⚙️ Fonctionnement technique

* Sauvegarde automatique
* Données persistantes (JSON)
* Mots de passe hachés (**SHA-256**)
* Validation des entrées
* Anti-surréservation
* Interface moderne avec **sv-ttk (Sun Valley Theme)**

---

# 🧪 Test rapide

1. Connexion admin (`admin / admin123`)
2. Ajouter un film
3. Créer une salle
4. Programmer un film
5. Connexion client
6. Faire une réservation

---

# 🧱 Technologies utilisées

* **Python**
* **Tkinter + sv-ttk**
* **JSON**
* **SHA-256**
* Compatible Windows / Linux / macOS
