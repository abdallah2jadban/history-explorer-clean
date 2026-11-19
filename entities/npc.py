"""
Classe pour les NPCs (personnages non-joueurs)
"""
import pygame
from settings import *


class NPC(pygame.sprite.Sprite):
    """
    Personnage non-joueur avec dialogues et quiz
    """
    def __init__(self, x, y, npc_type, name, dialogues, quiz_data=None):
        super().__init__()
        # Sprite temporaire
        self.image = pygame.Surface((40, 50))
        
        # Couleur selon le type
        colors = {
            "guide": LIGHT_BLUE,
            "pharaoh": YELLOW,
            "scribe": ORANGE,
            "knight": PURPLE,
            "merchant": GREEN
        }
        self.image.fill(colors.get(npc_type, WHITE))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Données du NPC
        self.npc_type = npc_type
        self.name = name
        self.dialogues = dialogues  # Liste de dialogues
        self.current_dialogue_index = 0
        self.quiz_data = quiz_data  # None si pas de quiz
        
        # État
        self.has_been_talked_to = False
        self.quiz_completed = False
    
    def get_current_dialogue(self):
        """
        Retourne le dialogue actuel
        """
        if self.current_dialogue_index < len(self.dialogues):
            return self.dialogues[self.current_dialogue_index]
        return None
    
    def advance_dialogue(self):
        """
        Passe au dialogue suivant
        """
        self.current_dialogue_index += 1
        self.has_been_talked_to = True
    
    def has_quiz(self):
        """
        Vérifie si le NPC a un quiz
        """
        return self.quiz_data is not None and not self.quiz_completed
    
    def complete_quiz(self):
        """
        Marque le quiz comme complété
        """
        self.quiz_completed = True


class Avatar(NPC):
    """
    Avatar guide spécial (hologramme IA)
    """
    def __init__(self, x, y, dialogues):
        super().__init__(x, y, "guide", "Guide Temporel", dialogues)
        # L'avatar a une apparence différente
        self.image = pygame.Surface((35, 60))
        self.image.fill(LIGHT_BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, player_pos):
        """
        L'avatar peut suivre le joueur ou apparaître à certains moments
        """
        # Logique optionnelle : faire suivre l'avatar
        pass
