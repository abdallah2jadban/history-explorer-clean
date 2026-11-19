"""
Configuration globale du jeu History Explorer
"""

# Dimensions de la fenêtre
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

# Taille des tuiles
TILE_SIZE = 64

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (52, 152, 219)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
YELLOW = (241, 196, 15)
PURPLE = (155, 89, 182)
ORANGE = (230, 126, 34)
LIGHT_BLUE = (174, 214, 241)
DARK_BLUE = (44, 62, 80)
CREAM = (245, 245, 220)

# Vitesse du joueur
PLAYER_SPEED = 5

# Points de score
POINTS_OBJECT = 50
POINTS_CORRECT_ANSWER = 100
POINTS_FIRST_TRY = 50

# Timer par niveau (en secondes)
LEVEL_TIME_LIMIT = 300

# Époques disponibles
ERAS = {
    "egypt": {
        "name": "Égypte Antique",
        "color": YELLOW,
        "unlocked": True
    },
    "medieval": {
        "name": "Moyen Âge",
        "color": PURPLE,
        "unlocked": False
    }
}

# Configuration des états du jeu
STATES = {
    "MENU": "menu",
    "PLAYING": "playing",
    "QUIZ": "quiz",
    "GAMEOVER": "gameover",
    "VICTORY": "victory"
}

# Répertoires
SAVE_FILE = "data/save.json"
DIALOGUES_FILE = "data/dialogues.json"
