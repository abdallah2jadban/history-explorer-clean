"""
Système de caméra pour le scrolling de la carte
"""
import pygame
from settings import *


class Camera:
    """
    Gestion du défilement de l'écran
    """
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        """
        Applique le décalage de la caméra à une entité
        """
        return entity.rect.move(self.camera.topleft)
    
    def apply_rect(self, rect):
        """
        Applique le décalage de la caméra à un rectangle
        """
        return rect.move(self.camera.topleft)
    
    def update(self, target):
        """
        Centre la caméra sur la cible (généralement le joueur)
        """
        x = -target.rect.centerx + WINDOW_WIDTH // 2
        y = -target.rect.centery + WINDOW_HEIGHT // 2
        
        # Limiter le défilement aux bords de la carte
        x = min(0, x)  # Gauche
        y = min(0, y)  # Haut
        x = max(-(self.width - WINDOW_WIDTH), x)  # Droite
        y = max(-(self.height - WINDOW_HEIGHT), y)  # Bas
        
        self.camera = pygame.Rect(x, y, self.width, self.height)
