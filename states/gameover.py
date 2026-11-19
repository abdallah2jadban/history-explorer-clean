"""
État Game Over - défaite
"""
import pygame
from core.state import State
from settings import *
from utils import *


class GameOver(State):
    """
    Écran de Game Over
    """
    def __init__(self, game, score, reason=""):
        super().__init__(game)
        self.score = score
        self.reason = reason
        
        # Boutons
        self.buttons = []
        self.create_buttons()
    
    def create_buttons(self):
        """
        Crée les boutons
        """
        button_width = 300
        button_height = 60
        button_spacing = 20
        start_y = WINDOW_HEIGHT // 2 + 100
        
        options = ["Réessayer", "Menu Principal", "Quitter"]
        
        for i, option in enumerate(options):
            x = (WINDOW_WIDTH - button_width) // 2
            y = start_y + i * (button_height + button_spacing)
            rect = pygame.Rect(x, y, button_width, button_height)
            self.buttons.append({"rect": rect, "text": option, "hover": False})
    
    def update(self, delta_time, events):
        """
        Gère les interactions
        """
        mouse_pos = pygame.mouse.get_pos()
        
        for button in self.buttons:
            button["hover"] = button["rect"].collidepoint(mouse_pos)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self.buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            self.handle_button_click(button["text"])
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.handle_button_click("Réessayer")
                elif event.key == pygame.K_ESCAPE:
                    self.handle_button_click("Menu Principal")
    
    def handle_button_click(self, button_text):
        """
        Gère les clics sur les boutons
        """
        if button_text == "Réessayer":
            # Retourner au menu puis relancer
            while len(self.game.state_stack) > 1:
                self.game.state_stack.pop()
            from states.playing import Playing
            new_state = Playing(self.game, "egypt")
            new_state.enter_state()
        
        elif button_text == "Menu Principal":
            # Retourner au menu
            while len(self.game.state_stack) > 1:
                self.game.state_stack.pop()
        
        elif button_text == "Quitter":
            self.game.running = False
    
    def render(self, surface):
        """
        Affiche l'écran Game Over
        """
        surface.fill(BLACK)
        
        # Titre GAME OVER
        title = "GAME OVER"
        draw_text(surface, title, 100, WINDOW_WIDTH // 2, 150, RED, center=True)
        
        # Raison
        if self.reason:
            draw_text(surface, self.reason, 32, WINDOW_WIDTH // 2, 250, WHITE, center=True)
        
        # Score final
        score_text = f"Score Final: {self.score}"
        draw_text(surface, score_text, 48, WINDOW_WIDTH // 2, 320, YELLOW, center=True)
        
        # Dessiner les boutons
        for button in self.buttons:
            draw_button(
                surface,
                button["rect"],
                button["text"],
                WHITE,
                DARK_BLUE,
                RED,
                border_width=3,
                hover=button["hover"]
            )
