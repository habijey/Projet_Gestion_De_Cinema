# 🎬 Projet_Gestion_De_Cinema

Application de gestion de cinéma développée en **Python** avec **interface graphique Tkinter**.
Le projet permet la gestion des films, des salles, des utilisateurs, des réservations et des statistiques.

---

## ▶️ Lancer l’application

```bash
python main.py
```

✅ L’interface graphique s’ouvre.

💡 **Astuce** :
Si `python` ne fonctionne pas mais que `python3` oui, utilise :

```bash
python3 main.py
```

---

## 🚀 Installation

### ✅ Prérequis

* **Python 3.8 ou plus**
* Tkinter (inclus par défaut avec Python)
* Thème graphique `sv-ttk`

### 🔍 Vérification de la version de Python

```bash
python --version
```

---

## 📦 Installation des dépendances

Installer le thème graphique :

```bash
pip install sv-ttk
```

---

## 📁 Structure du projet

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

## 👤 Comptes de démonstration

### 👑 Administrateur

* **Utilisateur** : `admin`
* **Mot de passe** : `admin123`

### 👤 Clients

* `user1 / client123`
* `user2 / password123`
* `test / client123`

💡 Le compte **admin** donne accès à toutes les fonctionnalités.

---

## 🧭 Fonctionnalités

### 👑 Administrateur

* Ajouter des films
* Créer des salles
* Programmer des films
* Consulter les statistiques

### 👤 Client

* Consulter les films disponibles
* Réserver des places
* Voir l’historique des réservations

---

## 🎬 Données de test incluses

* **6 films** préchargés
* **8 salles** avec capacités variables
* Sauvegarde automatique des données en **JSON**

---

## ⚙️ Fonctionnement technique

* Sauvegarde automatique
* Données persistantes (JSON)
* Mots de passe hachés (**SHA-256**)
* Validation des entrées utilisateur
* Protection contre la surréservation
* Interface moderne (thème **Sun Valley**)

---

## 🧠 Ce qui a été implémenté

* Gestion dynamique des rôles (admin / client)
* Interface graphique par onglets
* Mise à jour en temps réel
* Messages d’erreur explicites
* Architecture **MVC simplifiée**

---

## 🧪 Test rapide

1. Connexion admin (`admin / admin123`)
2. Ajouter un film
3. Créer une salle
4. Programmer le film
5. Se connecter avec un client
6. Réserver une place

✅ La réservation est visible côté client et administrateur.

---

## 🧱 Technologies utilisées

* **Python**
* **Tkinter + sv-ttk**
* **JSON**
* **SHA-256**
* Compatible **Windows / Linux / macOS**

