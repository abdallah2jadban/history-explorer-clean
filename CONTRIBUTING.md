# GUIDE DE CONTRIBUTION - HISTORY EXPLORER

Merci de votre intérêt pour contribuer à History Explorer ! 🎮

---

## 🤝 Comment Contribuer

### Rapporter un Bug 🐛

1. **Vérifier** que le bug n'a pas déjà été signalé
2. **Créer** une issue avec :
   - Description claire du problème
   - Étapes pour reproduire
   - Comportement attendu vs réel
   - Screenshots si applicable
   - Version de Python et PyGame
   - Système d'exploitation

**Template de Bug Report :**

```markdown
**Description**
[Description claire du bug]

**Reproduction**
1. Lancer le jeu
2. Aller à [endroit]
3. Faire [action]
4. Voir erreur

**Attendu**
[Ce qui devrait se passer]

**Réel**
[Ce qui se passe vraiment]

**Environnement**
- OS: [Windows 10 / macOS 11 / Ubuntu 20.04]
- Python: [3.9]
- PyGame: [2.1.0]
```

---

### Proposer une Fonctionnalité ✨

1. **Vérifier** que la feature n'est pas déjà planifiée (voir CHANGELOG.md)
2. **Créer** une issue avec :
   - Description de la fonctionnalité
   - Cas d'usage
   - Exemples concrets
   - Impact sur le gameplay

---

### Soumettre du Code 💻

#### Workflow

1. **Fork** le projet
2. **Créer** une branche feature
   ```bash
   git checkout -b feature/nom-de-ma-feature
   ```
3. **Développer** votre fonctionnalité
4. **Tester** exhaustivement
5. **Commit** avec des messages clairs
   ```bash
   git commit -m "Ajout: Nouvelle époque Renaissance"
   ```
6. **Push** vers votre fork
   ```bash
   git push origin feature/nom-de-ma-feature
   ```
7. **Créer** une Pull Request

---

## 📝 Standards de Code

### Convention de Nommage

```python
# Classes : PascalCase
class PlayerCharacter:
    pass

# Fonctions et variables : snake_case
def calculate_score():
    total_points = 0
    
# Constantes : UPPER_SNAKE_CASE
MAX_HEALTH = 100
```

### Documentation

**Toujours** documenter les fonctions et classes :

```python
def calculate_distance(point1, point2):
    """
    Calcule la distance euclidienne entre deux points.
    
    Args:
        point1 (tuple): Coordonnées (x, y) du premier point
        point2 (tuple): Coordonnées (x, y) du second point
    
    Returns:
        float: Distance entre les deux points
    """
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return (dx**2 + dy**2)**0.5
```

### Style PEP 8

- **4 espaces** pour l'indentation (pas de tabs)
- **79 caractères** maximum par ligne
- **2 lignes vides** entre les classes
- **1 ligne vide** entre les méthodes

Vérifier avec :
```bash
pip install flake8
flake8 votre_fichier.py
```

---

## 🌍 Ajouter une Nouvelle Époque

### 1. Planifier l'Époque

Définir :
- **Nom** : Ex. "Renaissance Italienne"
- **Thème** : Couleur, ambiance
- **Objets** : 5 objets historiques
- **NPCs** : 2-3 personnages
- **Quiz** : 2 questions minimum

### 2. Ajouter les Données

**Dans `data/dialogues.json` :**

```json
{
  "renaissance": {
    "avatar": [
      "Bienvenue à la Renaissance!",
      "Explore Florence et découvre les secrets de cette époque."
    ],
    "npcs": {
      "leonardo": {
        "name": "Léonard de Vinci",
        "dialogues": ["Je suis artiste et inventeur..."],
        "quiz": {
          "question": "Quelle œuvre ai-je peinte?",
          "answers": ["La Joconde", "La Nuit Étoilée", "Les Tournesols", "Le Cri"],
          "correct": 0
        }
      }
    },
    "objects": [
      {
        "type": "painting",
        "name": "Mona Lisa",
        "info": "Chef-d'œuvre de Léonard de Vinci..."
      }
    ]
  }
}
```

### 3. Créer le Niveau

**Dans `world/level.py` :**

```python
def create_renaissance_level(self):
    """
    Crée le niveau Renaissance Italienne
    """
    map_width = 20
    map_height = 15
    self.width = map_width * TILE_SIZE
    self.height = map_height * TILE_SIZE
    
    # Créer le sol (pierre médiévale)
    for x in range(map_width):
        for y in range(map_height):
            tile = Tile(x, y, "stone")
            self.all_sprites.add(tile)
    
    # Ajouter obstacles, NPCs, objets...
    # (Suivre le modèle d'Égypte)
```

### 4. Configurer l'Époque

**Dans `settings.py` :**

```python
ERAS = {
    # ...
    "renaissance": {
        "name": "Renaissance",
        "color": PURPLE,
        "unlocked": False
    }
}
```

### 5. Tester

Utiliser `TESTING.md` comme checklist !

---

## 🎨 Ajouter des Assets Graphiques

### Structure

```
assets/
├── images/
│   ├── player/
│   │   ├── idle_down.png
│   │   ├── walk_down_1.png
│   │   └── ...
│   ├── npcs/
│   ├── objects/
│   └── tiles/
├── sounds/
└── music/
```

### Spécifications

**Sprites :**
- Format : PNG avec transparence
- Style : Pixel art 16×16 ou 32×32
- Animations : 4 frames minimum

**Sons :**
- Format : WAV ou OGG
- Qualité : 44.1 kHz, 16-bit

**Musiques :**
- Format : OGG (pour la taille)
- Durée : Loop de 2-3 minutes

### Intégration

```python
# Dans entities/player.py
def load_sprites(self):
    self.sprites = {
        'idle_down': pygame.image.load('assets/images/player/idle_down.png'),
        'walk_down_1': pygame.image.load('assets/images/player/walk_down_1.png'),
        # ...
    }
```

---

## 🧪 Tests

### Tests Manuels

Suivre la checklist dans `TESTING.md`

### Tests Automatiques (Futur)

```python
# tests/test_player.py
import unittest
from entities.player import Player

class TestPlayer(unittest.TestCase):
    def test_movement(self):
        player = Player(0, 0, [])
        player.vx = 5
        player.update()
        self.assertEqual(player.rect.x, 5)
```

---

## 📦 Types de Contributions Recherchées

### 🔥 Haute Priorité

- [ ] Graphismes pixel art professionnels
- [ ] Bande sonore et effets audio
- [ ] Complétion de l'époque Moyen Âge
- [ ] Animations pour personnages

### 💡 Améliorations

- [ ] Optimisation des performances
- [ ] Nouvelles époques historiques
- [ ] Mini-jeux (puzzles, etc.)
- [ ] Système d'achievements

### 📝 Documentation

- [ ] Traduction en anglais/arabe
- [ ] Tutoriels vidéo
- [ ] Guide de modding

---

## 🏅 Reconnaissance

Tous les contributeurs seront mentionnés dans :
- Le fichier `CONTRIBUTORS.md`
- Les notes de version `CHANGELOG.md`
- Les crédits du jeu

---

## ❓ Questions

Des questions ? Créez une issue avec le tag `question` !

---

## 📜 Licence

En contribuant, vous acceptez que votre code soit sous licence MIT.

---

## 🙏 Merci !

Chaque contribution, petite ou grande, fait avancer le projet ! 🚀

**Bon coding ! 💻✨**

---

**Chaimae Berdij - History Explorer Team**
