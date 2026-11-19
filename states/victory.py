"""
État Victory - victoire
"""
import pygame
from core.state import State
from settings import *
from utils import *


class Victory(State):
    """
    Écran de victoire
    """
    def __init__(self, game, score, era):
        super().__init__(game)
        self.score = score
        self.era = era
        
        # Déverrouiller la prochaine époque
        self.unlock_next_era()
        
        # Boutons
        self.buttons = []
        self.create_buttons()
        
        # Sauvegarder la progression
        self.save_progress()
    
    def unlock_next_era(self):
        """
        Déverrouille l'époque suivante
        """
        if self.era == "egypt":
            ERAS["medieval"]["unlocked"] = True
    
    def save_progress(self):
        """
        Sauvegarde la progression
        """
        save_data = {
            "score": self.score,
            "current_era": self.era,
            "eras_unlocked": {era: data["unlocked"] for era, data in ERAS.items()}
        }
        save_json(SAVE_FILE, save_data)
    
    def create_buttons(self):
        """
        Crée les boutons
        """
        button_width = 300
        button_height = 60
        button_spacing = 20
        start_y = WINDOW_HEIGHT // 2 + 100
        
        options = ["Époque Suivante", "Menu Principal", "Quitter"]
        
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
                    self.handle_button_click("Époque Suivante")
                elif event.key == pygame.K_ESCAPE:
                    self.handle_button_click("Menu Principal")
    
    def handle_button_click(self, button_text):
        """
        Gère les clics sur les boutons
        """
        if button_text == "Époque Suivante":
            # Charger l'époque suivante si déverrouillée
            next_era = "medieval" if self.era == "egypt" else None
            
            if next_era and ERAS[next_era]["unlocked"]:
                while len(self.game.state_stack) > 1:
                    self.game.state_stack.pop()
                from states.playing import Playing
                new_state = Playing(self.game, next_era)
                new_state.enter_state()
            else:
                # Pas d'autre époque, retour au menu
                while len(self.game.state_stack) > 1:
                    self.game.state_stack.pop()
        
        elif button_text == "Menu Principal":
            while len(self.game.state_stack) > 1:
                self.game.state_stack.pop()
        
        elif button_text == "Quitter":
            self.game.running = False
    
    def render(self, surface):
        """
        Affiche l'écran de victoire
        """
        surface.fill(DARK_BLUE)
        
        # Titre VICTOIRE
        title = "VICTOIRE!"
        draw_text(surface, title, 100, WINDOW_WIDTH // 2, 120, YELLOW, center=True)
        
        # Message de félicitations
        congrats = f"Vous avez terminé l'époque {ERAS[self.era]['name']}!"
        draw_text(surface, congrats, 36, WINDOW_WIDTH // 2, 230, WHITE, center=True)
        
        # Score final
        score_text = f"Score: {self.score}"
        draw_text(surface, score_text, 48, WINDOW_WIDTH // 2, 300, GREEN, center=True)
        
        # Fragment collecté
        fragment_text = "✓ Fragment Temporel Collecté"
        draw_text(surface, fragment_text, 32, WINDOW_WIDTH // 2, 370, LIGHT_BLUE, center=True)
        
        # Dessiner les boutons
        for button in self.buttons:
            draw_button(
                surface,
                button["rect"],
                button["text"],
                WHITE,
                GREEN,
                YELLOW,
                border_width=3,
                hover=button["hover"]
            )
        
        # Message de déverrouillage
        if self.era == "egypt":
            unlock_msg = "Nouvelle époque déverrouillée : Moyen Âge!"
            draw_text(surface, unlock_msg, 28, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50, 
                     PURPLE, center=True)
