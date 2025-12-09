# Projet_Gestion_De_Cinema
(exécution du code tapper python 3 main.py)
e demandé.

# 🎬 Système de Gestion de Cinéma – Interface Graphique Python

Projet étudiant en **ingénierie informatique** : application complète de gestion de cinéma avec **interface graphique Tkinter moderne**, gestion des utilisateurs, réservations, statistiques et persistance des données.

---

## 🚀 Installation et lancement (Windows)

### 🖥️ Étape 1 : Vérifier l’installation de Python

1. Appuie sur **Windows + R**
2. Tape `cmd` puis **Entrée**
3. Dans la fenêtre, tape :

```bash
python --version


✅ Si Python 3.8 ou plus est affiché, tout est bon.
❌ Sinon :

Télécharge Python depuis https://www.python.org

Pendant l’installation, coche ✅ Add Python to PATH

Redémarre ton PC

📁 Étape 2 : Préparer le projet

Crée un dossier nommé cinema

Place les fichiers suivants dans le même dossier :

cinema/
├── main.py
├── classe.py
├── utilisateur.py
├── sauvegarde.py
├── utils.py


📌 Le dossier Data/ sera créé automatiquement au premier lancement.

📦 Étape 3 : Installer les dépendances

Ce projet utilise un thème moderne pour Tkinter.

pip install sv-ttk


✅ Tkinter est inclus par défaut avec Python sur Windows.

▶️ Étape 4 : Lancer l’application
Méthode recommandée (ligne de commande)

Ouvre le dossier cinema

Shift + clic droit → Ouvrir PowerShell ici

Exécute :

python main.py


✅ L’interface graphique s’ouvre.

🛠️ Dépannage (Windows)
❌ Erreur : module non trouvé

Vérifie que tous les fichiers .py sont bien dans le même dossier

Vérifie les noms exacts des fichiers

❌ Tkinter non disponible

Réinstalle Python

Choisis Customize installation

Vérifie que tcl/tk and IDLE est bien coché

👤 Comptes de démonstration
Administrateur

Utilisateur : admin

Mot de passe : admin123

Clients

user1 / client123

user2 / password123

test / client123

💡 Commence par le compte admin pour explorer toutes les fonctionnalités.

🧭 Navigation dans l’application
Onglets disponibles

Accueil : Connexion & Inscription

Admin : Gestion complète (admin uniquement)

Client : Réservations & historique

Statistiques : Données globales du cinéma

🎟️ Fonctionnalités par rôle
👑 Administrateur

Ajouter des films (titre + durée)

Créer des salles (numéro + capacité)

Programmer des films dans les salles

Consulter les statistiques de fréquentation

👤 Client

Voir les films disponibles

Réserver des places

Consulter l’historique de réservations

🎬 Données initiales
Films disponibles au démarrage

Charlie et la Chocolaterie (115 min)

Avengers: Endgame (181 min)

Cars (117 min)

Le Roi Lion (88 min)

Harry Potter à l’école des sorciers (152 min)

Retour vers le Futur (116 min)

Salles

8 salles (140 à 250 places)

Salles 1 à 6 : déjà programmées

Salles 7 et 8 : libres pour tests

⚙️ Fonctionnement technique
Sauvegarde

Sauvegarde automatique

Données stockées en JSON

Persistance entre les sessions

Sécurité

Mots de passe hachés (SHA-256)

Validation des entrées utilisateur

Protection contre la surréservation

Interface

Thème moderne Sun Valley (sv-ttk)

Interface claire et intuitive

Mise à jour en temps réel

Messages d’erreur explicites

🧠 Ce qui a été implémenté (main.py)
✅ Gestion dynamique des rôles

Les onglets s’affichent selon le rôle (admin / client)

Interface sécurisée et adaptée

✅ Sauvegarde automatique

Sauvegarde des données à la fermeture

Aucun risque de perte

✅ Contrôles de saisie

Vérification des durées, capacités, réservations

Messages d’erreur clairs

✅ Logique intelligente

Affichage uniquement des films disponibles

Suivi en temps réel des places restantes

Empêche les conflits et doubles réservations

🧪 Test rapide conseillé

Connexion admin (admin / admin123)

Ajouter un film : Avatar – 180 min

Créer une salle : Salle 1 – 50 places

Programmer le film

Déconnexion

Inscrire un client

Réserver une place

✅ La réservation apparaît chez le client et dans les statistiques admin.

🧱 Architecture du projet

Langage : Python 3.8+

Interface : Tkinter + sv-ttk

Architecture : MVC simplifié

Stockage : JSON

Sécurité : SHA-256

OS : Windows / Linux / macOS

🔮 Améliorations possibles

Gestion des tarifs

Export PDF des statistiques

Gestion des séances par date

Système de billets numériques

✅ Projet prêt à être utilisé, testé et présenté.


---

Si tu veux, je peux aussi te faire :
- une **version plus académique** (pour rapport universitaire)
- une **version orientée recruteur**
- un **diagramme d’architecture**
- ou un **README anglais**

Dis-moi 👍
