# Projet_Gestion_De_Cinema
(exécution du code tapper python 3 main.py)



# 🎬 Projet_Gestion_De_Cinema

Application de gestion de cinéma développée en **Python** avec **interface graphique Tkinter**.  
Le projet permet la gestion des films, des salles, des utilisateurs, des réservations et des statistiques.

> ▶️ Exécution du projet :

```bash
python main.py
````

---

## 🚀 Installation (Windows)

### ✅ Prérequis

* Python **3.8 ou plus**
* Tkinter (inclus par défaut)
* Thème graphique `sv-ttk`

Vérifier Python :

```bash
python --version
```

Installer la dépendance :

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
└── Data/              # Créé automatiquement (JSON)
```

---

## ▶️ Lancer l’application

1. Ouvre le dossier du projet
2. Shift + clic droit → **Ouvrir PowerShell ici**
3. Tape :

```bash
python main.py
```

✅ L’interface graphique s’ouvre.

---

## 👤 Comptes de démonstration

### Administrateur

* **Utilisateur** : `admin`
* **Mot de passe** : `admin123`

### Clients

* `jason / jason`
* `test / test`

💡 Utilise le compte **admin** pour accéder à toutes les fonctionnalités.



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


## 🎬 Données de test incluses

* **6 films** préchargés
* **8 salles** (capacités variables)
* Données sauvegardées automatiquement en **JSON**



## ⚙️ Fonctionnement technique

* Sauvegarde automatique
* Données persistantes (JSON)
* Mots de passe hachés (**SHA-256**)
* Vérification des entrées utilisateur
* Protection contre la surréservation
* Interface moderne (thème **Sun Valley**)



## 🧠 Ce qui a été fait

* Gestion dynamique des rôles (admin / client)
* Interface par onglets intuitive
* Mise à jour en temps réel
* Messages d’erreur clairs
* Architecture **MVC simplifiée**



## 🧪 Test rapide

1. Connexion admin (`admin / admin123`)
2. Ajouter un film
3. Créer une salle
4. Programmer le film
5. Inscrire un client
6. Réserver une place

 La réservation apparaît côté client et admin.



## 🧱 Technologies

* **Python**
* **Tkinter + sv-ttk**
* **JSON**
* **SHA-256**
* Compatible **Windows / Linux / macOS**



Dis-moi 👍
```
