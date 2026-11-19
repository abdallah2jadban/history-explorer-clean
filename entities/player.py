"""
Classe du joueur
"""
import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    """
    Le personnage joueur - explorateur temporel
    """
    def __init__(self, x, y, obstacles):
        super().__init__()
        # Sprite temporaire - forme colorée
        self.image = pygame.Surface((32, 48))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Mouvement
        self.vx = 0
        self.vy = 0
        self.speed = PLAYER_SPEED
        
        # Obstacles pour collisions
        self.obstacles = obstacles
        
        # Direction
        self.facing = "down"  # up, down, left, right
    
    def handle_input(self, keys):
        """
        Gère les entrées clavier pour le déplacement
        """
        self.vx = 0
        self.vy = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.vx = -self.speed
            self.facing = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = self.speed
            self.facing = "right"
        
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.vy = -self.speed
            self.facing = "up"
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = self.speed
            self.facing = "down"
    
    def update(self):
        """
        Met à jour la position du joueur avec détection de collisions
        """
        # Déplacement horizontal
        self.rect.x += self.vx
        self.check_collisions('x')
        
        # Déplacement vertical
        self.rect.y += self.vy
        self.check_collisions('y')
    
    def check_collisions(self, direction):
        """
        Vérifie et résout les collisions avec les obstacles
        """
        for obstacle in self.obstacles:
            if self.rect.colliderect(obstacle.rect):
                if direction == 'x':
                    if self.vx > 0:  # Déplacement vers la droite
                        self.rect.right = obstacle.rect.left
                    elif self.vx < 0:  # Déplacement vers la gauche
                        self.rect.left = obstacle.rect.right
                elif direction == 'y':
                    if self.vy > 0:  # Déplacement vers le bas
                        self.rect.bottom = obstacle.rect.top
                    elif self.vy < 0:  # Déplacement vers le haut
                        self.rect.top = obstacle.rect.bottom
    
    def get_interaction_rect(self):
        """
        Retourne un rectangle devant le joueur pour les interactions
        """
        interaction_rect = self.rect.copy()
        offset = 50
        
        if self.facing == "up":
            interaction_rect.y -= offset
        elif self.facing == "down":
            interaction_rect.y += offset
        elif self.facing == "left":
            interaction_rect.x -= offset
        elif self.facing == "right":
            interaction_rect.x += offset
        
        return interaction_rect
