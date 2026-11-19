"""
Gestionnaire principal du jeu - Machine à états
"""
import pygame
from settings import *


class Game:
    """
    Classe principale qui gère le jeu et les états
    """
    def __init__(self):
        pygame.init()
        
        # Fenêtre
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("History Explorer - 4th Year Project")
        
        # Horloge
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Pile d'états
        self.state_stack = []
        
        # Charger l'état initial (menu)
        from states.menu import Menu
        menu = Menu(self)
        menu.enter_state()
    
    def handle_events(self):
        """
        Gère les événements pygame
        """
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            events.append(event)
        return events
    
    def update(self, delta_time, events):
        """
        Met à jour l'état actuel
        """
        if self.state_stack:
            self.state_stack[-1].update(delta_time, events)
    
    def render(self):
        """
        Affiche l'état actuel
        """
        if self.state_stack:
            self.state_stack[-1].render(self.screen)
        pygame.display.flip()
    
    def run(self):
        """
        Boucle principale du jeu
        """
        while self.running:
            # Delta time en secondes
            delta_time = self.clock.tick(FPS) / 1000.0
            
            # Événements
            events = self.handle_events()
            
            # Mise à jour
            self.update(delta_time, events)
            
            # Rendu
            self.render()
        
        # Quitter proprement
        pygame.quit()
