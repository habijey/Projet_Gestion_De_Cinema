# 🎬 Projet_Gestion_De_Cinema

Application de gestion de cinéma développée en **Python** avec **interface graphique Tkinter**.
Le projet permet la gestion des films, des salles, des utilisateurs, des réservations et des statistiques.

> ▶️ Exécution du projet :

```bash
python main.py
```

---

## 🚀 Installation

### ✅ Prérequis

* **Python 3.8 ou plus**
* Tkinter (inclus par défaut avec Python)
* Thème graphique `sv-ttk`

Vérifier si Python est installé :

```bash
python --version
```

---

## 🐍 Installation de Python (si non installé)

Si la commande précédente **ne fonctionne pas** ou affiche une erreur, cela signifie que **Python n’est pas installé**.

### 🪟 Windows

1. Aller sur le site officiel :
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Télécharger **Python 3.8 ou plus récent**

3. Lancer l’installateur et **⚠️ cocher impérativement** :

   ```
   ✅ Add Python to PATH
   ```

4. Cliquer sur **Install Now**

5. Redémarrer PowerShell et vérifier :

   ```bash
   python --version
   ```

✅ Si une version s’affiche, Python est correctement installé.

---

### 🐧 Linux

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Vérification :

```bash
python3 --version
```

---

### 🍎 macOS

Via Homebrew :

```bash
brew install python
```

Ou téléchargement direct :
👉 [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)

---

💡 **Astuce** :
Si `python` ne fonctionne pas mais que `python3` oui, utilise :

```bash
python3 main.py
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

## ▶️ Lancer l’application

1. Ouvrir le dossier du projet
2. **Shift + clic droit → Ouvrir PowerShell ici**
3. Exécuter :

```bash
python main.py
```

✅ L’interface graphique s’ouvre.

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



