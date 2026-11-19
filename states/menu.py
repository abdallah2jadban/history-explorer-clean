"""
État du menu principal
"""
import pygame
from core.state import State
from settings import *
from utils import *


class Menu(State):
    """
    Écran d'accueil du jeu
    """
    def __init__(self, game):
        super().__init__(game)
        self.options = ["Jouer", "Continuer", "Quitter"]
        self.selected_option = 0
        self.buttons = []
        self.create_buttons()
    
    def create_buttons(self):
        """
        Crée les boutons du menu
        """
        button_width = 300
        button_height = 60
        button_spacing = 20
        start_y = WINDOW_HEIGHT // 2
        
        for i, option in enumerate(self.options):
            x = (WINDOW_WIDTH - button_width) // 2
            y = start_y + i * (button_height + button_spacing)
            rect = pygame.Rect(x, y, button_width, button_height)
            self.buttons.append({"rect": rect, "text": option, "hover": False})
    
    def update(self, delta_time, events):
        """
        Gère les interactions du menu
        """
        mouse_pos = pygame.mouse.get_pos()
        
        # Mettre à jour l'état de survol des boutons
        for button in self.buttons:
            button["hover"] = button["rect"].collidepoint(mouse_pos)
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.select_option(self.selected_option)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    for i, button in enumerate(self.buttons):
                        if button["rect"].collidepoint(mouse_pos):
                            self.select_option(i)
    
    def select_option(self, option_index):
        """
        Sélectionne une option du menu
        """
        if self.options[option_index] == "Jouer":
            # Charger l'écran de sélection d'époque puis lancer le jeu
            from states.playing import Playing
            new_state = Playing(self.game, "egypt")
            new_state.enter_state()
        
        elif self.options[option_index] == "Continuer":
            # Charger la sauvegarde
            save_data = load_json(SAVE_FILE)
            if save_data:
                from states.playing import Playing
                era = save_data.get("current_era", "egypt")
                new_state = Playing(self.game, era)
                new_state.score = save_data.get("score", 0)
                new_state.enter_state()
            else:
                # Pas de sauvegarde, lancer nouveau jeu
                from states.playing import Playing
                new_state = Playing(self.game, "egypt")
                new_state.enter_state()
        
        elif self.options[option_index] == "Quitter":
            self.game.running = False
    
    def render(self, surface):
        """
        Affiche le menu
        """
        # Fond dégradé
        surface.fill(DARK_BLUE)
        
        # Titre du jeu
        title_font = pygame.font.Font(None, 100)
        title_text = title_font.render("HISTORY EXPLORER", True, YELLOW)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 150))
        
        # Ombre du titre
        shadow = title_font.render("HISTORY EXPLORER", True, BLACK)
        shadow_rect = shadow.get_rect(center=(WINDOW_WIDTH // 2 + 3, 153))
        surface.blit(shadow, shadow_rect)
        surface.blit(title_text, title_rect)
        
        # Sous-titre
        subtitle_text = "4th Year Project by Chaimae Berdij"
        draw_text(surface, subtitle_text, 28, WINDOW_WIDTH // 2, 230, CREAM, center=True)
        
        # Dessiner les boutons
        for i, button in enumerate(self.buttons):
            is_selected = i == self.selected_option
            color = BLUE if not is_selected else GREEN
            draw_button(
                surface, 
                button["rect"], 
                button["text"],
                WHITE,
                color,
                YELLOW if is_selected else WHITE,
                border_width=3,
                hover=button["hover"]
            )
        
        # Instructions en bas
        instructions = "Utilisez les flèches ou la souris pour naviguer"
        draw_text(surface, instructions, 20, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50, CREAM, center=True)
