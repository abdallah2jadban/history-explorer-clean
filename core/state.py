"""
Classe de base pour tous les états du jeu
"""
import pygame


class State:
    """
    Classe mère pour les différents états du jeu
    """
    def __init__(self, game):
        self.game = game
        self.previous_state = None
    
    def enter_state(self):
        """
        Appelé quand on entre dans cet état
        """
        if len(self.game.state_stack) > 1:
            self.previous_state = self.game.state_stack[-2]
        self.game.state_stack.append(self)
    
    def exit_state(self):
        """
        Appelé quand on quitte cet état
        """
        if self in self.game.state_stack:
            self.game.state_stack.pop()
    
    def update(self, delta_time, events):
        """
        Met à jour la logique de l'état
        À surcharger dans les classes enfants
        """
        pass
    
    def render(self, surface):
        """
        Affiche l'état à l'écran
        À surcharger dans les classes enfants
        """
        pass
