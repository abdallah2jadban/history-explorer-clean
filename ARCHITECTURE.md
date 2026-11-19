# ARCHITECTURE TECHNIQUE - HISTORY EXPLORER

## 📐 Vue d'Ensemble

History Explorer utilise une architecture modulaire basée sur le **State Pattern** (patron de conception État) pour gérer les différentes phases du jeu.

---

## 🏗️ Diagramme d'Architecture

```
┌─────────────────────────────────────────────────────┐
│                    main.py                          │
│              (Point d'entrée)                       │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│                   game.py                           │
│            (Gestionnaire principal)                 │
│   - Boucle de jeu (Game Loop)                       │
│   - Pile d'états (State Stack)                      │
│   - Gestion des événements                          │
└──────────────────┬──────────────────────────────────┘
                   │
     ┌─────────────┴─────────────┐
     │                           │
     ▼                           ▼
┌─────────┐              ┌──────────────┐
│settings │              │    utils     │
│  .py    │              │    .py       │
└─────────┘              └──────────────┘
     │
     │  Configuration globale
     │
┌────┴────────────────────────────────────────────────┐
│              ÉTATS DU JEU                           │
│                                                     │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐            │
│  │  Menu   │─▶│ Playing │─▶│  Quiz   │            │
│  └─────────┘  └────┬────┘  └─────────┘            │
│                    │                               │
│                    ▼                               │
│       ┌──────────────────────────┐                │
│       │      ▼                   │                │
│  ┌─────────┐              ┌─────────┐            │
│  │GameOver │              │ Victory │            │
│  └─────────┘              └─────────┘            │
└─────────────────────────────────────────────────────┘
     │
     │  Utilise
     │
┌────┴────────────────────────────────────────────────┐
│            COMPOSANTS DU JEU                        │
│                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │  World   │  │ Entities │  │   Core   │         │
│  │          │  │          │  │          │         │
│  │ - Level  │  │ - Player │  │ - State  │         │
│  │ - Tile   │  │ - NPC    │  │ - Camera │         │
│  │          │  │ - Object │  │          │         │
│  └──────────┘  └──────────┘  └──────────┘         │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 Pattern de Conception : State Pattern

### Principe

Le jeu utilise une **pile d'états** (State Stack) pour gérer les différents écrans :

```python
state_stack = [Menu] → [Menu, Playing] → [Menu, Playing, Quiz]
                │              │                    │
              Menu        Exploration            Quiz actif
```

### Avantages

1. **Séparation des responsabilités** : Chaque état gère sa propre logique
2. **Navigation facile** : Push/Pop pour changer d'état
3. **États superposés** : Quiz par-dessus le jeu, pause par-dessus tout
4. **Maintenabilité** : Facile d'ajouter de nouveaux états

---

## 📦 Modules Principaux

### 1. **game.py** - Gestionnaire Principal

```python
class Game:
    - screen         # Surface PyGame principale
    - clock          # Horloge pour FPS
    - state_stack    # Pile d'états
    - running        # Booléen de boucle
    
    + run()          # Boucle principale
    + handle_events()
    + update()
    + render()
```

**Boucle de Jeu** :
```python
while running:
    delta_time = clock.tick(FPS)
    events = handle_events()
    update(delta_time, events)
    render()
```

---

### 2. **core/state.py** - Classe État de Base

```python
class State:
    + enter_state()    # Empiler l'état
    + exit_state()     # Dépiler l'état
    + update()         # Logique
    + render()         # Affichage
```

Tous les états héritent de cette classe :
- `Menu(State)`
- `Playing(State)`
- `Quiz(State)`
- `GameOver(State)`
- `Victory(State)`

---

### 3. **core/camera.py** - Système de Caméra

```python
class Camera:
    + apply(entity)      # Décale une entité
    + update(target)     # Suit le joueur
```

**Algorithme de Suivi** :
```python
x = -target.x + WINDOW_WIDTH / 2
y = -target.y + WINDOW_HEIGHT / 2

# Clamp aux bords de la carte
x = clamp(x, -(map_width - WINDOW_WIDTH), 0)
y = clamp(y, -(map_height - WINDOW_HEIGHT), 0)
```

---

### 4. **entities/** - Entités du Jeu

#### Player (entities/player.py)

```python
class Player(Sprite):
    + handle_input()        # Gère ZQSD/Flèches
    + update()              # Déplacement
    + check_collisions()    # AABB collision
    + get_interaction_rect()
```

**Collision AABB** :
```
┌──────────┐
│  Player  │
│  Rect    │
└──────────┘
     │
     │ colliderect()
     ▼
┌──────────┐
│ Obstacle │
│  Rect    │
└──────────┘
```

#### NPC (entities/npc.py)

```python
class NPC(Sprite):
    - dialogues[]
    - quiz_data
    - current_dialogue_index
    
    + get_current_dialogue()
    + advance_dialogue()
    + has_quiz()
```

#### InteractiveObject (entities/interactive.py)

```python
class InteractiveObject(Sprite):
    - discovered       # État de découverte
    - pulsing          # Animation
    
    + discover()       # Marque découvert, retourne points
    + update()         # Animation de pulsation
```

---

### 5. **world/** - Génération du Monde

#### Level (world/level.py)

```python
class Level:
    - all_sprites      # Tous les sprites
    - obstacles        # Obstacles pour collisions
    - npcs             # NPCs interactifs
    - interactive_objects
    
    + create_egypt_level()
    + create_medieval_level()
    + check_objectives_completed()
```

**Génération Procédurale** :
```python
for x in range(map_width):
    for y in range(map_height):
        tile = Tile(x, y, "sand")
        add_to_level(tile)
```

#### Tile (world/tile.py)

```python
class Tile(Sprite):
    - tile_type        # sand, grass, stone, wall...
    - is_obstacle      # Booléen collision
```

---

## 🔄 Flux de Données

### 1. Cycle de Jeu Complet

```
main.py
  │
  └─▶ Game.__init__()
        │
        ├─▶ Charger Menu (state)
        │
        └─▶ game.run()
              │
              └─▶ BOUCLE :
                    │
                    ├─▶ handle_events()
                    │     │
                    │     └─▶ pygame.event.get()
                    │
                    ├─▶ update(delta, events)
                    │     │
                    │     └─▶ state_stack[-1].update()
                    │
                    └─▶ render()
                          │
                          └─▶ state_stack[-1].render()
```

### 2. Flux d'Interaction Joueur

```
Joueur appuie sur ESPACE
  │
  ├─▶ Playing.handle_interaction()
  │     │
  │     ├─▶ Vérifie collision avec NPCs
  │     │     │
  │     │     └─▶ Si collision :
  │     │           │
  │     │           ├─▶ Afficher dialogue
  │     │           │
  │     │           └─▶ Si quiz disponible :
  │     │                 │
  │     │                 └─▶ Quiz(state).enter_state()
  │     │
  │     └─▶ Vérifie collision avec Fragment
  │           │
  │           └─▶ Si déverrouillé :
  │                 │
  │                 └─▶ Victory(state).enter_state()
  │
  └─▶ Update score et UI
```

### 3. Flux du Quiz

```
Quiz.enter_state()
  │
  ├─▶ Afficher question
  │
  ├─▶ Joueur sélectionne réponse
  │     │
  │     └─▶ submit_answer()
  │           │
  │           ├─▶ Si correct :
  │           │     │
  │           │     ├─▶ +100 points
  │           │     ├─▶ +50 bonus si 1er essai
  │           │     └─▶ npc.complete_quiz()
  │           │
  │           └─▶ Si incorrect :
  │                 │
  │                 └─▶ Afficher bonne réponse
  │
  └─▶ close_quiz()
        │
        └─▶ Quiz.exit_state()
```

---

## 💾 Gestion des Données

### Structure JSON - save.json

```json
{
  "score": 1050,
  "current_era": "egypt",
  "eras_unlocked": {
    "egypt": true,
    "medieval": true
  }
}
```

### Structure JSON - dialogues.json

```json
{
  "egypt": {
    "avatar": ["dialogue1", "dialogue2"],
    "npcs": {
      "pharaoh": {
        "dialogues": ["..."],
        "quiz": {
          "question": "...",
          "answers": ["A", "B", "C", "D"],
          "correct": 1
        }
      }
    },
    "objects": [...]
  }
}
```

---

## 🎨 Système de Rendu

### Ordre de Rendu (Layers)

```
Layer 0 : Fond (Tiles du sol)
Layer 1 : Obstacles (Murs, rochers)
Layer 2 : Objets interactifs
Layer 3 : NPCs
Layer 4 : Joueur
Layer 5 : UI / HUD
Layer 6 : Dialogues
Layer 7 : Popups
Layer 8 : Menus superposés
```

### Pipeline de Rendu

```python
1. Effacer écran (fill)
2. Pour chaque sprite dans all_sprites :
     screen.blit(sprite.image, camera.apply(sprite))
3. Render HUD (par-dessus)
4. Render dialogue (si actif)
5. Render popup (si actif)
6. pygame.display.flip()
```

---

## ⚙️ Détection de Collisions

### Algorithme AABB (Axis-Aligned Bounding Box)

```python
def colliderect(rect1, rect2):
    return (rect1.left < rect2.right and
            rect1.right > rect2.left and
            rect1.top < rect2.bottom and
            rect1.bottom > rect2.top)
```

### Résolution de Collision

```python
# Déplacement horizontal
player.x += velocity_x
if collision_detected('x'):
    if moving_right:
        player.right = obstacle.left
    else:
        player.left = obstacle.right

# Déplacement vertical  
player.y += velocity_y
if collision_detected('y'):
    if moving_down:
        player.bottom = obstacle.top
    else:
        player.top = obstacle.bottom
```

---

## 🕐 Gestion du Temps

### Delta Time

```python
delta_time = clock.tick(FPS) / 1000.0  # En secondes

# Utilisation pour animations indépendantes du framerate
animation_timer += delta_time
if animation_timer > animation_speed:
    next_frame()
    animation_timer = 0
```

### Timer de Niveau

```python
time_remaining = LEVEL_TIME_LIMIT - (current_time - start_time)

if time_remaining <= 0:
    GameOver()
```

---

## 🎯 Système de Score

### Calcul du Score

```python
class ScoreSystem:
    POINTS_OBJECT = 50
    POINTS_QUIZ = 100
    POINTS_FIRST_TRY = 50
    POINTS_FRAGMENT = 500
    
    def add_points(action_type, first_try=False):
        if action_type == "object":
            score += POINTS_OBJECT
        elif action_type == "quiz":
            score += POINTS_QUIZ
            if first_try:
                score += POINTS_FIRST_TRY
        elif action_type == "fragment":
            score += POINTS_FRAGMENT
```

---

## 🔧 Optimisations Implémentées

### 1. Spatial Partitioning

Les sprites sont regroupés par type pour éviter de tester toutes les collisions :

```python
obstacles_group      # Seulement pour collisions
interactive_group    # Seulement pour clics
npc_group           # Seulement pour interactions
```

### 2. Dirty Rectangles (Futur)

Actuellement, tout l'écran est redessiné. Optimisation future :

```python
# Ne redessiner que les zones qui ont changé
dirty_rects = []
for sprite in moved_sprites:
    dirty_rects.append(sprite.rect)
pygame.display.update(dirty_rects)
```

### 3. Sprite Sheets (Futur)

Charger toutes les images en une fois :

```python
sprite_sheet = load_image("all_sprites.png")
player_sprite = sprite_sheet.subsurface((0, 0, 32, 48))
```

---

## 📊 Complexité Algorithmique

| Opération | Complexité | Note |
|-----------|-----------|------|
| Collision joueur-obstacles | O(n) | n = nombre d'obstacles |
| Clic sur objet | O(m) | m = objets interactifs |
| Rendu | O(s) | s = tous les sprites |
| Update entités | O(s) | Tous les sprites |
| Pathfinding (futur) | O(n log n) | A* algorithm |

---

## 🚀 Extensions Futures

### 1. Système de Particules

```python
class ParticleSystem:
    def emit(position, count, color):
        for i in range(count):
            particle = Particle(position, random_velocity())
            particles.add(particle)
```

### 2. Animation de Sprites

```python
class AnimatedSprite(Sprite):
    def __init__(self, sprite_sheet):
        self.frames = load_frames(sprite_sheet)
        self.current_frame = 0
    
    def update(self, delta):
        self.frame_time += delta
        if self.frame_time > frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
```

### 3. Audio Manager

```python
class AudioManager:
    sounds = {}
    music = {}
    
    def play_sound(name):
        sounds[name].play()
    
    def play_music(name):
        pygame.mixer.music.load(music[name])
        pygame.mixer.music.play(-1)
```

---

## 📈 Métriques de Performance

### Objectifs

- **FPS** : 60 constant
- **Temps de chargement** : < 2 secondes
- **Mémoire** : < 200 MB
- **Sprites simultanés** : > 100

### Profiling

```python
import cProfile

cProfile.run('game.run()', 'profile_stats')
```

---

## 🔐 Sécurité et Validation

### Validation des Données JSON

```python
def validate_save_data(data):
    required_keys = ["score", "current_era", "eras_unlocked"]
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing key: {key}")
    
    if not isinstance(data["score"], int):
        raise TypeError("Score must be integer")
```

### Protection contre les Inputs Malveillants

```python
# Limiter les valeurs
score = clamp(score, 0, 999999)
player.x = clamp(player.x, 0, map_width)
```

---

## 📚 Ressources et Références

### Documentation PyGame
- [pygame.org](https://www.pygame.org/docs/)
- [PyGame Tutorials](https://www.pygame.org/wiki/tutorials)

### Patterns de Conception
- State Pattern
- Component Pattern (Entities)
- Observer Pattern (Events)

### Algorithmes
- AABB Collision Detection
- Camera Culling
- Spatial Hashing

---

## 👨‍💻 Guidelines de Développement

### Conventions de Code

1. **Nommage** :
   - Classes : `PascalCase`
   - Fonctions : `snake_case`
   - Constantes : `UPPER_SNAKE_CASE`

2. **Documentation** :
   - Docstrings pour toutes les classes et fonctions
   - Commentaires pour logique complexe

3. **Organisation** :
   - Un fichier par classe principale
   - Grouper les fonctions utilitaires dans `utils.py`

### Ajout de Fonctionnalités

1. Créer la branche feature
2. Implémenter et tester
3. Mettre à jour TESTING.md
4. Documenter dans ARCHITECTURE.md
5. Merger

---

**Dernière mise à jour** : Avril 2026
**Version** : 1.0
