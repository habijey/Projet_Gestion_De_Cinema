import hashlib
import json
import os

class Utilisateur:
    def __init__(self, username, password, role):
        self.username = username
        self.password_hash = self._hash_password(password)
        self.role = role  # "admin" ou "client"
    
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verifier_password(self, password):
        return self.password_hash == self._hash_password(password)
    
    def to_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role
        }
    
    @staticmethod
    def from_dict(data):
        user = Utilisateur(data["username"], "temp", data["role"])
        user.password_hash = data["password_hash"]
        return user

class GestionUtilisateurs:
    def __init__(self):
        self.fichier_utilisateurs = "Data/utilisateurs.json"
        os.makedirs("Data", exist_ok=True)
        self.utilisateurs = self.charger_utilisateurs()
        self._creer_admin_par_defaut()
    
    def charger_utilisateurs(self):
        try:
            with open(self.fichier_utilisateurs, "r") as f:
                data = json.load(f)
                return [Utilisateur.from_dict(u) for u in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def sauvegarder_utilisateurs(self):
        with open(self.fichier_utilisateurs, "w") as f:
            json.dump([u.to_dict() for u in self.utilisateurs], f, indent=4)
    
    def _creer_admin_par_defaut(self):
        if not any(u.username == "admin" for u in self.utilisateurs):
            admin = Utilisateur("admin", "admin123", "admin")
            self.utilisateurs.append(admin)
            self.sauvegarder_utilisateurs()
            print("✅ Compte admin créé par défaut (admin/admin123)")
    
    def inscrire(self, username, password, role="client"):
        if any(u.username == username for u in self.utilisateurs):
            return False, "❌ Nom d'utilisateur déjà pris"
        
        nouvel_utilisateur = Utilisateur(username, password, role)
        self.utilisateurs.append(nouvel_utilisateur)
        self.sauvegarder_utilisateurs()
        return True, "✅ Inscription réussie !"
    
    def connecter(self, username, password):
        utilisateur = next((u for u in self.utilisateurs if u.username == username), None)
        if utilisateur and utilisateur.verifier_password(password):
            return True, utilisateur
        return False, "❌ Identifiants incorrects"