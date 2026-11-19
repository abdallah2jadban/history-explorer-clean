"""
Système de chargement et gestion des niveaux
"""
import pygame
from settings import *
from world.tile import Tile, Obstacle
from entities.player import Player
from entities.npc import NPC, Avatar
from entities.interactive import InteractiveObject, TemporalFragment


class Level:
    """
    Chargeur et gestionnaire de niveau
    """
    def __init__(self, era):
        self.era = era
        self.width = 0
        self.height = 0
        
        # Groupes de sprites
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.interactive_objects = pygame.sprite.Group()
        
        # Entités spéciales
        self.player = None
        self.avatar = None
        self.temporal_fragment = None
        
        # Créer le niveau selon l'époque
        if era == "egypt":
            self.create_egypt_level()
        elif era == "medieval":
            self.create_medieval_level()
    
    def create_egypt_level(self):
        """
        Crée le niveau Égypte Antique
        """
        # Dimensions de la carte
        map_width = 20
        map_height = 15
        self.width = map_width * TILE_SIZE
        self.height = map_height * TILE_SIZE
        
        # Créer le sol de sable
        for x in range(map_width):
            for y in range(map_height):
                tile = Tile(x, y, "sand")
                self.all_sprites.add(tile)
        
        # Créer des obstacles (murs du temple)
        # Bordures
        for x in range(map_width):
            wall_top = Obstacle(x * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE, "wall")
            wall_bottom = Obstacle(x * TILE_SIZE, (map_height - 1) * TILE_SIZE, TILE_SIZE, TILE_SIZE, "wall")
            self.obstacles.add(wall_top, wall_bottom)
            self.all_sprites.add(wall_top, wall_bottom)
        
        for y in range(1, map_height - 1):
            wall_left = Obstacle(0, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, "wall")
            wall_right = Obstacle((map_width - 1) * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, "wall")
            self.obstacles.add(wall_left, wall_right)
            self.all_sprites.add(wall_left, wall_right)
        
        # Quelques rochers dispersés
        rock_positions = [(5, 3), (8, 7), (12, 4), (15, 9), (6, 11)]
        for rx, ry in rock_positions:
            rock = Obstacle(rx * TILE_SIZE, ry * TILE_SIZE, TILE_SIZE, TILE_SIZE, "rock")
            self.obstacles.add(rock)
            self.all_sprites.add(rock)
        
        # Créer le joueur
        self.player = Player(TILE_SIZE * 2, TILE_SIZE * 2, self.obstacles)
        self.all_sprites.add(self.player)
        
        # Créer l'avatar guide
        avatar_dialogues = [
            "Bienvenue en Égypte Antique, jeune explorateur!",
            "Tu dois trouver les objets historiques et parler aux habitants.",
            "Explore la carte et clique sur les objets pour en apprendre plus!",
            "Une fois tous les objectifs complétés, tu pourras récupérer le fragment temporel."
        ]
        self.avatar = Avatar(TILE_SIZE * 3, TILE_SIZE * 2, avatar_dialogues)
        self.npcs.add(self.avatar)
        self.all_sprites.add(self.avatar)
        
        # Créer des NPCs
        pharaoh_quiz = {
            "question": "Quelle était la principale fonction des pyramides d'Égypte?",
            "answers": [
                "Temples religieux",
                "Tombeaux pour les pharaons",
                "Palais royaux",
                "Observatoires astronomiques"
            ],
            "correct": 1
        }
        pharaoh = NPC(
            TILE_SIZE * 10, TILE_SIZE * 5,
            "pharaoh", "Pharaon Khéops",
            ["Je suis le grand Pharaon! Réponds à ma question pour prouver ta sagesse."],
            pharaoh_quiz
        )
        self.npcs.add(pharaoh)
        self.all_sprites.add(pharaoh)
        
        scribe_quiz = {
            "question": "Quel système d'écriture utilisaient les Égyptiens?",
            "answers": [
                "Alphabet latin",
                "Hiéroglyphes",
                "Cunéiforme",
                "Idéogrammes chinois"
            ],
            "correct": 1
        }
        scribe = NPC(
            TILE_SIZE * 14, TILE_SIZE * 8,
            "scribe", "Scribe Imhotep",
            ["Je suis le gardien du savoir écrit. Montre-moi tes connaissances!"],
            scribe_quiz
        )
        self.npcs.add(scribe)
        self.all_sprites.add(scribe)
        
        # Créer des objets interactifs
        objects_data = [
            (7, 3, "pyramid", "Grande Pyramide", "La Grande Pyramide de Khéops est l'une des Sept Merveilles du monde antique."),
            (11, 10, "sphinx", "Le Sphinx", "Le Grand Sphinx de Gizeh est une statue monumentale à tête humaine et corps de lion."),
            (4, 8, "scroll", "Papyrus", "Les Égyptiens écrivaient sur du papyrus, fabriqué à partir de la plante du même nom."),
            (16, 5, "artifact", "Sarcophage", "Les pharaons étaient enterrés dans des sarcophages richement décorés."),
            (9, 12, "treasure", "Trésor", "Les tombeaux contenaient des trésors pour accompagner le pharaon dans l'au-delà.")
        ]
        
        for ox, oy, otype, oname, oinfo in objects_data:
            obj = InteractiveObject(ox * TILE_SIZE + 16, oy * TILE_SIZE + 16, otype, oname, oinfo)
            self.interactive_objects.add(obj)
            self.all_sprites.add(obj)
        
        # Créer le fragment temporel (verrouillé au départ)
        self.temporal_fragment = TemporalFragment(
            map_width // 2 * TILE_SIZE,
            map_height // 2 * TILE_SIZE,
            "Égypte Antique"
        )
        self.all_sprites.add(self.temporal_fragment)
    
    def create_medieval_level(self):
        """
        Crée le niveau Moyen Âge (similaire mais avec thème médiéval)
        """
        # Structure similaire à Egypt mais avec décor médiéval
        map_width = 20
        map_height = 15
        self.width = map_width * TILE_SIZE
        self.height = map_height * TILE_SIZE
        
        # Sol en herbe et pierre
        for x in range(map_width):
            for y in range(map_height):
                tile_type = "grass" if (x + y) % 3 != 0 else "stone"
                tile = Tile(x, y, tile_type)
                self.all_sprites.add(tile)
        
        # Créer le joueur
        self.player = Player(TILE_SIZE * 2, TILE_SIZE * 2, self.obstacles)
        self.all_sprites.add(self.player)
        
        # À compléter avec NPCs et objets médiévaux...
    
    def check_objectives_completed(self):
        """
        Vérifie si tous les objectifs sont complétés pour débloquer le fragment
        """
        # Tous les objets découverts?
        all_discovered = all(obj.discovered for obj in self.interactive_objects)
        
        # Tous les quiz complétés?
        all_quizzes_done = all(npc.quiz_completed or not npc.has_quiz() for npc in self.npcs)
        
        if all_discovered and all_quizzes_done:
            self.temporal_fragment.unlock()
            return True
        return False
    
    def update(self, delta_time):
        """
        Met à jour tous les éléments du niveau
        """
        # Mettre à jour tous les sprites selon leur type
        for sprite in self.all_sprites:
            if sprite == self.avatar:
                # L'avatar a besoin de la position du joueur
                sprite.update((self.player.rect.x, self.player.rect.y))
            elif isinstance(sprite, InteractiveObject):
                # Les objets interactifs ont besoin de delta_time
                sprite.update(delta_time)
            else:
                # Les autres sprites (player, etc.) ont des update() sans paramètres
                sprite.update()
        
        # Les objets interactifs sont déjà mis à jour ci-dessus
        
        # Vérifier si les objectifs sont complétés
        self.check_objectives_completed()
