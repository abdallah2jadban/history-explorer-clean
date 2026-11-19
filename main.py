"""
History Explorer
Jeu d'exploration et d'apprentissage historique

Projet de 4ème année Génie Informatique
Par : Chaimae Berdij
Encadrant : Prof. HAJJI TARIK
Date : Avril 2026
"""

from game import Game


def main():
    """
    Point d'entrée du jeu
    """
    print("=" * 60)
    print("HISTORY EXPLORER".center(60))
    print("4th Year Project by Chaimae Berdij".center(60))
    print("=" * 60)
    print()
    print("Chargement du jeu...")
    print()
    print("Commandes:")
    print("  - Flèches / ZQSD : Déplacement")
    print("  - Espace / Entrée : Interaction")
    print("  - Clic gauche : Interaction avec objets")
    print("  - P : Pause")
    print("  - ESC : Menu pause / Quitter")
    print()
    print("=" * 60)
    
    # Créer et lancer le jeu
    game = Game()
    game.run()
    
    print()
    print("Merci d'avoir joué à History Explorer!")


if __name__ == "__main__":
    main()
