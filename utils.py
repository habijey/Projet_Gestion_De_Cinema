import os
import platform

def clear_ecran():
    """Efface l'écran de la console de manière cross-platform"""
    system = platform.system().lower()
    
    if system == "windows":
        os.system('cls')
    else:
        os.system('clear')

def pause_ecran(message="Appuyez sur Entrée pour continuer..."):
    """Met en pause l'exécution jusqu'à ce que l'utilisateur appuie sur Entrée"""
    input(f"\n{message}")