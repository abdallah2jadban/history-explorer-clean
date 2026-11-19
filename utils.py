"""
Fonctions utilitaires pour le jeu History Explorer
"""
import pygame
import json
from settings import *


def draw_text(surface, text, size, x, y, color=WHITE, font_name=None, center=False):
    """
    Dessine du texte à l'écran
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    
    surface.blit(text_surface, text_rect)
    return text_rect


def draw_text_multiline(surface, text, size, rect, color=WHITE, font_name=None, line_spacing=5):
    """
    Dessine du texte multiligne dans un rectangle donné
    """
    font = pygame.font.Font(font_name, size)
    words = text.split(' ')
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        test_surface = font.render(test_line, True, color)
        
        if test_surface.get_width() <= rect.width - 20:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    y_offset = rect.top + 10
    for line in lines:
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (rect.left + 10, y_offset))
        y_offset += size + line_spacing
    
    return lines


def load_json(filepath):
    """
    Charge un fichier JSON
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def save_json(filepath, data):
    """
    Sauvegarde des données dans un fichier JSON
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def create_surface_with_text(text, size, color, bg_color, padding=10):
    """
    Crée une surface avec du texte centré et un fond
    """
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    
    surface = pygame.Surface((text_rect.width + padding * 2, text_rect.height + padding * 2))
    surface.fill(bg_color)
    surface.blit(text_surface, (padding, padding))
    
    return surface


def draw_rounded_rect(surface, rect, color, border_radius=10):
    """
    Dessine un rectangle avec coins arrondis
    """
    pygame.draw.rect(surface, color, rect, border_radius=border_radius)


def draw_button(surface, rect, text, text_color, bg_color, border_color=None, border_width=3, hover=False):
    """
    Dessine un bouton avec effet de survol
    """
    if hover:
        # Effet de survol : éclaircir la couleur
        bg_color = tuple(min(c + 30, 255) for c in bg_color)
    
    # Fond du bouton
    draw_rounded_rect(surface, rect, bg_color, border_radius=10)
    
    # Bordure
    if border_color:
        pygame.draw.rect(surface, border_color, rect, border_width, border_radius=10)
    
    # Texte
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)


def clamp(value, min_value, max_value):
    """
    Limite une valeur entre min et max
    """
    return max(min_value, min(value, max_value))


def typewriter_effect(text, char_index):
    """
    Retourne le texte jusqu'à l'index donné (effet machine à écrire)
    """
    return text[:char_index]
