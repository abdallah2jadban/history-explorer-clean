"""
État de jeu - phase d'exploration
"""
import pygame
from core.state import State
from core.camera import Camera
from world.level import Level
from settings import *
from utils import *
import time


class Playing(State):
    """
    Phase principale d'exploration du jeu
    """
    def __init__(self, game, era):
        super().__init__(game)
        self.era = era
        self.score = 0
        self.time_remaining = LEVEL_TIME_LIMIT
        self.start_time = time.time()
        
        # Charger le niveau
        self.level = Level(era)
        self.camera = Camera(self.level.width, self.level.height)
        
        # Dialogue actuel
        self.current_dialogue = None
        self.dialogue_npc = None
        self.dialogue_char_index = 0
        self.dialogue_speed = 2  # Caractères par frame
        
        # Info bulle pour objets
        self.info_popup = None
        self.info_popup_timer = 0
        
        # UI
        self.paused = False
    
    def update(self, delta_time, events):
        """
        Met à jour la logique du jeu
        """
        if self.paused:
            self.handle_pause_input(events)
            return
        
        # Mettre à jour le timer
        elapsed = time.time() - self.start_time
        self.time_remaining = max(0, LEVEL_TIME_LIMIT - elapsed)
        
        if self.time_remaining <= 0:
            # Game Over - temps écoulé
            from states.gameover import GameOver
            game_over_state = GameOver(self.game, self.score, "Temps écoulé!")
            game_over_state.enter_state()
            return
        
        # Input du joueur
        keys = pygame.key.get_pressed()
        self.level.player.handle_input(keys)
        
        # Gérer les événements
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                elif event.key == pygame.K_ESCAPE:
                    self.paused = True
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.handle_interaction()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    self.handle_click(pygame.mouse.get_pos())
        
        # Mettre à jour le niveau
        self.level.update(delta_time)
        
        # Mettre à jour la caméra
        self.camera.update(self.level.player)
        
        # Mettre à jour le dialogue (effet machine à écrire)
        if self.current_dialogue:
            self.dialogue_char_index += self.dialogue_speed
        
        # Mettre à jour le timer de popup
        if self.info_popup:
            self.info_popup_timer -= delta_time
            if self.info_popup_timer <= 0:
                self.info_popup = None
    
    def handle_interaction(self):
        """
        Gère l'interaction avec les NPCs
        """
        interaction_rect = self.level.player.get_interaction_rect()
        
        # Vérifier collision avec NPCs
        for npc in self.level.npcs:
            if interaction_rect.colliderect(npc.rect):
                if self.current_dialogue:
                    # Avancer le dialogue
                    self.dialogue_npc.advance_dialogue()
                    next_dialogue = self.dialogue_npc.get_current_dialogue()
                    
                    if next_dialogue:
                        self.current_dialogue = next_dialogue
                        self.dialogue_char_index = 0
                    else:
                        # Dialogue terminé, vérifier si quiz
                        if self.dialogue_npc.has_quiz():
                            from states.quiz import Quiz
                            quiz_state = Quiz(self.game, self, self.dialogue_npc)
                            quiz_state.enter_state()
                        self.current_dialogue = None
                        self.dialogue_npc = None
                else:
                    # Nouveau dialogue
                    self.dialogue_npc = npc
                    self.current_dialogue = npc.get_current_dialogue()
                    self.dialogue_char_index = 0
                return
        
        # Vérifier collision avec le fragment temporel
        if self.level.temporal_fragment and interaction_rect.colliderect(self.level.temporal_fragment.rect):
            if not self.level.temporal_fragment.locked:
                # Victoire!
                points = self.level.temporal_fragment.discover()
                self.score += points
                from states.victory import Victory
                victory_state = Victory(self.game, self.score, self.era)
                victory_state.enter_state()
    
    def handle_click(self, pos):
        """
        Gère les clics sur les objets interactifs
        """
        # Convertir la position de l'écran en position du monde
        world_pos = (pos[0] - self.camera.camera.x, pos[1] - self.camera.camera.y)
        
        for obj in self.level.interactive_objects:
            if obj.rect.collidepoint(world_pos):
                if not obj.discovered:
                    points = obj.discover()
                    self.score += points
                
                # Afficher la popup d'information
                self.info_popup = {
                    "title": obj.name,
                    "text": obj.info_text
                }
                self.info_popup_timer = 5  # 5 secondes
                break
    
    def handle_pause_input(self, events):
        """
        Gère les inputs pendant la pause
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    self.paused = False
    
    def render(self, surface):
        """
        Affiche le jeu
        """
        surface.fill(BLACK)
        
        # Afficher tous les sprites avec la caméra
        for sprite in self.level.all_sprites:
            surface.blit(sprite.image, self.camera.apply(sprite))
        
        # HUD (toujours affiché par-dessus)
        self.render_hud(surface)
        
        # Dialogue
        if self.current_dialogue:
            self.render_dialogue(surface)
        
        # Info popup
        if self.info_popup:
            self.render_info_popup(surface)
        
        # Pause
        if self.paused:
            self.render_pause(surface)
    
    def render_hud(self, surface):
        """
        Affiche l'interface utilisateur (score, temps, etc.)
        """
        # Fond semi-transparent pour le HUD
        hud_height = 80
        hud_surface = pygame.Surface((WINDOW_WIDTH, hud_height))
        hud_surface.set_alpha(200)
        hud_surface.fill(DARK_BLUE)
        surface.blit(hud_surface, (0, 0))
        
        # Score
        score_text = f"Score: {self.score}"
        draw_text(surface, score_text, 36, 20, 10, YELLOW)
        
        # Époque actuelle
        era_name = ERAS[self.era]["name"]
        draw_text(surface, era_name, 36, WINDOW_WIDTH // 2, 10, WHITE, center=True)
        
        # Temps restant
        minutes = int(self.time_remaining // 60)
        seconds = int(self.time_remaining % 60)
        time_text = f"Temps: {minutes:02d}:{seconds:02d}"
        time_color = RED if self.time_remaining < 60 else WHITE
        draw_text(surface, time_text, 36, WINDOW_WIDTH - 200, 10, time_color)
        
        # Barre de progression (objets découverts)
        total_objects = len(self.level.interactive_objects)
        discovered = sum(1 for obj in self.level.interactive_objects if obj.discovered)
        progress = discovered / total_objects if total_objects > 0 else 0
        
        bar_width = 200
        bar_height = 20
        bar_x = 20
        bar_y = 50
        
        # Fond de la barre
        pygame.draw.rect(surface, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
        # Remplissage
        fill_width = int(bar_width * progress)
        pygame.draw.rect(surface, GREEN, (bar_x + 2, bar_y + 2, fill_width - 4, bar_height - 4))
        
        # Texte de progression
        progress_text = f"Objets: {discovered}/{total_objects}"
        draw_text(surface, progress_text, 20, bar_x + bar_width + 10, bar_y + 2, WHITE)
    
    def render_dialogue(self, surface):
        """
        Affiche la boîte de dialogue
        """
        box_height = 150
        box_y = WINDOW_HEIGHT - box_height - 20
        box_rect = pygame.Rect(50, box_y, WINDOW_WIDTH - 100, box_height)
        
        # Fond de la boîte
        dialogue_surface = pygame.Surface((box_rect.width, box_rect.height))
        dialogue_surface.set_alpha(230)
        dialogue_surface.fill(DARK_BLUE)
        surface.blit(dialogue_surface, box_rect.topleft)
        
        # Bordure
        pygame.draw.rect(surface, LIGHT_BLUE, box_rect, 3, border_radius=10)
        
        # Nom du NPC
        if self.dialogue_npc:
            name_text = self.dialogue_npc.name
            draw_text(surface, name_text, 28, box_rect.left + 20, box_rect.top + 10, YELLOW)
        
        # Texte du dialogue avec effet machine à écrire
        displayed_text = typewriter_effect(self.current_dialogue, int(self.dialogue_char_index))
        text_rect = pygame.Rect(box_rect.left + 20, box_rect.top + 50, box_rect.width - 40, box_rect.height - 60)
        draw_text_multiline(surface, displayed_text, 24, text_rect, WHITE)
        
        # Indicateur pour continuer
        if self.dialogue_char_index >= len(self.current_dialogue):
            indicator = "▼ [ESPACE pour continuer]"
            draw_text(surface, indicator, 20, box_rect.right - 250, box_rect.bottom - 30, YELLOW)
    
    def render_info_popup(self, surface):
        """
        Affiche la popup d'information pour un objet
        """
        popup_width = 400
        popup_height = 200
        popup_x = (WINDOW_WIDTH - popup_width) // 2
        popup_y = (WINDOW_HEIGHT - popup_height) // 2
        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
        
        # Fond
        popup_surface = pygame.Surface((popup_width, popup_height))
        popup_surface.set_alpha(240)
        popup_surface.fill(CREAM)
        surface.blit(popup_surface, popup_rect.topleft)
        
        # Bordure
        pygame.draw.rect(surface, ORANGE, popup_rect, 4, border_radius=15)
        
        # Titre
        title = self.info_popup["title"]
        draw_text(surface, title, 32, popup_rect.centerx, popup_rect.top + 20, DARK_BLUE, center=True)
        
        # Texte
        text_rect = pygame.Rect(popup_rect.left + 20, popup_rect.top + 60, popup_rect.width - 40, popup_rect.height - 80)
        draw_text_multiline(surface, self.info_popup["text"], 20, text_rect, BLACK)
        
        # Points gagnés
        points_text = f"+{POINTS_OBJECT} points!"
        draw_text(surface, points_text, 24, popup_rect.centerx, popup_rect.bottom - 30, GREEN, center=True)
    
    def render_pause(self, surface):
        """
        Affiche l'écran de pause
        """
        # Overlay semi-transparent
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        surface.blit(overlay, (0, 0))
        
        # Texte PAUSE
        draw_text(surface, "PAUSE", 80, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50, WHITE, center=True)
        draw_text(surface, "Appuyez sur P ou ESC pour continuer", 30, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50, CREAM, center=True)
