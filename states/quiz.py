"""
État Quiz - questions à choix multiples
"""
import pygame
from core.state import State
from settings import *
from utils import *


class Quiz(State):
    """
    Écran de quiz avec questions à choix multiples
    """
    def __init__(self, game, playing_state, npc):
        super().__init__(game)
        self.playing_state = playing_state
        self.npc = npc
        self.quiz_data = npc.quiz_data
        
        # État du quiz
        self.selected_answer = 0
        self.answered = False
        self.correct = False
        self.first_try = True
        
        # Boutons de réponse
        self.answer_buttons = []
        self.create_answer_buttons()
    
    def create_answer_buttons(self):
        """
        Crée les boutons pour les réponses
        """
        button_width = 600
        button_height = 60
        button_spacing = 15
        start_y = 300
        
        for i, answer in enumerate(self.quiz_data["answers"]):
            x = (WINDOW_WIDTH - button_width) // 2
            y = start_y + i * (button_height + button_spacing)
            rect = pygame.Rect(x, y, button_width, button_height)
            self.answer_buttons.append({
                "rect": rect,
                "text": answer,
                "hover": False,
                "index": i
            })
    
    def update(self, delta_time, events):
        """
        Gère les interactions du quiz
        """
        if self.answered:
            # Attendre que le joueur continue
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.close_quiz()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.close_quiz()
            return
        
        mouse_pos = pygame.mouse.get_pos()
        
        # Mettre à jour l'état de survol des boutons
        for button in self.answer_buttons:
            button["hover"] = button["rect"].collidepoint(mouse_pos)
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_answer = (self.selected_answer - 1) % len(self.answer_buttons)
                elif event.key == pygame.K_DOWN:
                    self.selected_answer = (self.selected_answer + 1) % len(self.answer_buttons)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.submit_answer(self.selected_answer)
                elif event.key == pygame.K_ESCAPE:
                    # Annuler le quiz (sans points)
                    self.close_quiz()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in self.answer_buttons:
                        if button["rect"].collidepoint(mouse_pos):
                            self.submit_answer(button["index"])
    
    def submit_answer(self, answer_index):
        """
        Soumet une réponse et vérifie si elle est correcte
        """
        self.answered = True
        self.correct = answer_index == self.quiz_data["correct"]
        
        if self.correct:
            # Bonne réponse
            points = POINTS_CORRECT_ANSWER
            if self.first_try:
                points += POINTS_FIRST_TRY
            self.playing_state.score += points
            self.npc.complete_quiz()
        else:
            # Mauvaise réponse
            self.first_try = False
            # On peut permettre de réessayer ou non
            # Pour l'instant, on considère l'échec définitif
            pass
    
    def close_quiz(self):
        """
        Ferme le quiz et retourne à l'état de jeu
        """
        self.exit_state()
    
    def render(self, surface):
        """
        Affiche le quiz
        """
        # Afficher l'état de jeu en arrière-plan (flou)
        self.playing_state.render(surface)
        
        # Overlay semi-transparent
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        surface.blit(overlay, (0, 0))
        
        if not self.answered:
            # Afficher la question
            question_text = self.quiz_data["question"]
            
            # Boîte de question
            question_box = pygame.Rect(100, 100, WINDOW_WIDTH - 200, 150)
            draw_rounded_rect(surface, question_box, DARK_BLUE)
            pygame.draw.rect(surface, YELLOW, question_box, 3, border_radius=10)
            
            # Texte de la question
            text_rect = pygame.Rect(question_box.left + 20, question_box.top + 20, 
                                   question_box.width - 40, question_box.height - 40)
            draw_text_multiline(surface, question_text, 28, text_rect, WHITE)
            
            # Dessiner les boutons de réponse
            for i, button in enumerate(self.answer_buttons):
                is_selected = i == self.selected_answer
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
        
        else:
            # Afficher le résultat
            if self.correct:
                result_text = "BONNE RÉPONSE!"
                result_color = GREEN
                points_text = f"+{POINTS_CORRECT_ANSWER}"
                if self.first_try:
                    points_text += f" + {POINTS_FIRST_TRY} (premier essai!)"
            else:
                result_text = "MAUVAISE RÉPONSE"
                result_color = RED
                correct_answer = self.quiz_data["answers"][self.quiz_data["correct"]]
                points_text = f"La bonne réponse était : {correct_answer}"
            
            # Boîte de résultat
            result_box = pygame.Rect(200, 250, WINDOW_WIDTH - 400, 220)
            draw_rounded_rect(surface, result_box, DARK_BLUE)
            pygame.draw.rect(surface, result_color, result_box, 5, border_radius=10)
            
            # Texte du résultat
            draw_text(surface, result_text, 48, WINDOW_WIDTH // 2, result_box.top + 40, 
                     result_color, center=True)
            draw_text(surface, points_text, 32, WINDOW_WIDTH // 2, result_box.top + 100,
                     WHITE, center=True)
            
            # Instruction
            instruction = "[ESPACE ou CLIC pour continuer]"
            draw_text(surface, instruction, 24, WINDOW_WIDTH // 2, result_box.bottom - 40,
                     YELLOW, center=True)
