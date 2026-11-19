"""
Objets interactifs dans le monde du jeu
"""
import pygame
import math
from settings import *


class InteractiveObject(pygame.sprite.Sprite):
    """
    Objet cliquable ou interactif qui donne des informations
    """
    def __init__(self, x, y, obj_type, name, info_text, points=POINTS_OBJECT):
        super().__init__()
        # Sprite temporaire
        self.image = pygame.Surface((30, 30))
        
        # Couleur selon le type
        colors = {
            "pyramid": YELLOW,
            "sphinx": ORANGE,
            "scroll": CREAM,
            "artifact": PURPLE,
            "treasure": YELLOW,
            "sword": RED,
            "castle": DARK_BLUE
        }
        self.image.fill(colors.get(obj_type, GREEN))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Données de l'objet
        self.obj_type = obj_type
        self.name = name
        self.info_text = info_text
        self.points = points
        
        # État
        self.discovered = False
        self.pulsing = True  # Animation de pulsation pour attirer l'attention
        self.pulse_timer = 0
        self.original_size = self.rect.size
    
    def update(self, delta_time):
        """
        Animation de pulsation
        """
        if self.pulsing and not self.discovered:
            self.pulse_timer += delta_time
            scale = 1 + 0.1 * pygame.math.Vector2(1, 1).length() * abs(math.sin(self.pulse_timer * 3))
            new_size = (int(self.original_size[0] * scale), int(self.original_size[1] * scale))
            self.image = pygame.transform.scale(self.image, new_size)
            self.rect = self.image.get_rect(center=self.rect.center)
    
    def discover(self):
        """
        Marque l'objet comme découvert
        """
        if not self.discovered:
            self.discovered = True
            self.pulsing = False
            # Restaurer la taille originale
            self.image = pygame.Surface(self.original_size)
            colors = {
                "pyramid": YELLOW,
                "sphinx": ORANGE,
                "scroll": CREAM,
                "artifact": PURPLE,
                "treasure": YELLOW,
                "sword": RED,
                "castle": DARK_BLUE
            }
            self.image.fill(colors.get(self.obj_type, GREEN))
            # Rendre semi-transparent pour indiquer qu'il a été découvert
            self.image.set_alpha(150)
            return self.points
        return 0


class TemporalFragment(InteractiveObject):
    """
    Fragment temporel - objectif principal du niveau
    """
    def __init__(self, x, y, era_name):
        super().__init__(
            x, y, 
            "fragment", 
            f"Fragment {era_name}",
            f"Fragment temporel de l'époque {era_name}. Vous devez le collecter pour progresser!",
            points=500
        )
        self.image = pygame.Surface((40, 40))
        self.image.fill(PURPLE)
        self.locked = True  # Débloqué uniquement après avoir complété les objectifs
    
    def unlock(self):
        """
        Débloque le fragment après complétion des objectifs
        """
        self.locked = False
        self.image.fill(GREEN)  # Change de couleur quand débloqué
