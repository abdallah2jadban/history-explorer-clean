"""
Système de tuiles pour la construction de la carte
"""
import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    """
    Tuile de base pour le décor
    """
    def __init__(self, x, y, tile_type):
        super().__init__()
        self.tile_type = tile_type
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        
        # Couleurs selon le type de tuile
        colors = {
            "grass": (124, 185, 89),
            "sand": (237, 201, 175),
            "stone": (149, 165, 166),
            "water": (52, 152, 219),
            "wall": (127, 140, 141),
            "floor": (236, 240, 241),
            "dirt": (165, 105, 79)
        }
        
        self.image.fill(colors.get(tile_type, GREEN))
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        
        # Les murs et l'eau sont des obstacles
        self.is_obstacle = tile_type in ["wall", "water"]


class Obstacle(pygame.sprite.Sprite):
    """
    Obstacle spécifique (mur, rocher, etc.)
    """
    def __init__(self, x, y, width, height, obstacle_type="wall"):
        super().__init__()
        self.image = pygame.Surface((width, height))
        
        colors = {
            "wall": DARK_BLUE,
            "rock": (127, 140, 141),
            "tree": (39, 174, 96),
            "building": (189, 195, 199)
        }
        
        self.image.fill(colors.get(obstacle_type, DARK_BLUE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
