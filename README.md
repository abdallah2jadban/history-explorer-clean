# HISTORY EXPLORER

**Jeu d'aventure et d'exploration ludo-éducatif en 2D**

---

## 📋 Informations du Projet

- **Titre du jeu** : History Explorer
- **Filière** : 5ème Année Génie Informatique
- **Encadrant** : Prof. HAJJI TARIK
- **Date** : Avril 2026
- **Type** : Jeu éducatif d'aventure / Point & Click

---

## 🎮 Concept du Jeu

Un jeu d'aventure éducatif où le joueur incarne un explorateur temporel qui voyage à travers différentes époques historiques. Guidé par un avatar interactif (hologramme IA), il doit :

- Explorer des cartes représentant différentes époques (Égypte antique, Moyen Âge)
- Cliquer sur des éléments du décor pour découvrir des faits historiques
- Résoudre des mini-énigmes et quiz pour progresser
- Collecter des fragments temporels pour débloquer les époques suivantes

---

## 🎯 Objectifs

### Objectif Pédagogique
Sensibiliser et enseigner l'histoire de manière ludique en ancrant les connaissances dans une mémoire visuelle et interactive.

### Objectif Technique
Maîtriser la bibliothèque PyGame :
- Gestion des collisions 2D
- Système de dialogue/UI complexe
- Gestion d'états (machine à états)
- Système de caméra avec scrolling

---

## 🎲 Gameplay

### Mécaniques Principales

1. **Exploration** : Déplacement libre en vue du dessus (Top-Down)
2. **Interaction** : Dialogue avec NPCs et objets interactifs
3. **Apprentissage** : Découverte de faits historiques
4. **Quiz** : Questions à choix multiples pour tester les connaissances
5. **Progression** : Système de score et déverrouillage d'époques

### Conditions de Victoire
- Explorer toutes les zones requises
- Découvrir tous les objets historiques
- Réussir tous les quiz des NPCs
- Récupérer le fragment temporel de l'époque

### Conditions de Défaite
- Épuisement du temps (timer de 5 minutes par époque)

---

## 🕹️ Commandes

| Touche | Action |
|--------|--------|
| **Flèches** ou **ZQSD** | Déplacement du joueur |
| **Espace** ou **Entrée** | Interaction principale (parler, valider) |
| **Clic gauche** | Interaction avec UI et objets |
| **P** | Pause |
| **ESC** | Menu pause / Quitter |

---

## 🏗️ Architecture du Projet

```
history_explorer/
│
├── main.py                 # Point d'entrée du jeu
├── game.py                 # Gestionnaire d'états (Machine à états)
├── settings.py             # Configuration globale
├── utils.py                # Fonctions utilitaires
│
├── core/                   # Moteur et logique globale
│   ├── state.py           # Classe mère pour les états
│   └── camera.py          # Gestion du scrolling
│
├── states/                 # Les différents écrans du jeu
│   ├── menu.py            # Écran d'accueil
│   ├── playing.py         # Phase d'exploration
│   ├── quiz.py            # Phase de questions
│   ├── gameover.py        # Écran de défaite
│   └── victory.py         # Écran de victoire
│
├── entities/               # Objets dynamiques du jeu
│   ├── player.py          # Personnage joueur
│   ├── npc.py             # NPCs et avatar guide
│   └── interactive.py     # Objets interactifs
│
├── world/                  # Gestion de la carte
│   ├── level.py           # Chargeur de niveau
│   └── tile.py            # Tuiles et obstacles
│
├── assets/                 # Ressources externes
│   ├── images/            # Sprites et décors
│   ├── sounds/            # Bruitages
│   ├── music/             # Musiques de fond
│   └── fonts/             # Polices de texte
│
└── data/                   # Données du jeu
    ├── save.json          # Sauvegarde
    └── dialogues.json     # Dialogues et quiz
```

---

## 📦 Installation et Lancement

### Prérequis

- Python 3.7 ou supérieur
- PyGame 2.0 ou supérieur

### Installation

```bash
# Installer PyGame
pip install pygame

# Ou avec le fichier requirements.txt
pip install -r requirements.txt
```

### Lancement du Jeu

```bash
# Se placer dans le dossier du jeu
cd history_explorer

# Lancer le jeu
python main.py
```

---

## 🌍 Époques Disponibles

### 1. Égypte Antique ✓
- **Thème** : Pyramides, Pharaons, Hiéroglyphes
- **NPCs** : Pharaon Khéops, Scribe Imhotep
- **Objets** : Grande Pyramide, Sphinx, Papyrus, Sarcophage, Trésor
- **Objectifs** : 5 objets à découvrir + 2 quiz à réussir

### 2. Moyen Âge 🔒
- **Thème** : Châteaux, Chevaliers, Royaume médiéval
- **NPCs** : Chevalier Roland
- **Objets** : Château Fort, Épée
- **Déverrouillage** : Terminer l'Égypte Antique

---

## 🎨 Fonctionnalités

### Implémentées ✓

- ✅ Système de déplacement et collisions
- ✅ Système de dialogue avec effet machine à écrire
- ✅ Système de quiz à choix multiples
- ✅ Système de score et progression
- ✅ Timer par niveau
- ✅ Caméra avec scrolling
- ✅ Menu principal interactif
- ✅ Écrans de victoire/défaite
- ✅ Sauvegarde de progression (JSON)
- ✅ Déverrouillage d'époques
- ✅ Objets interactifs avec animations
- ✅ Interface utilisateur (HUD)
- ✅ Système de pause

### Fonctionnalités Optionnelles (Futures Améliorations)

- ⬜ Graphismes avancés (sprites et animations)
- ⬜ Effets sonores et musiques
- ⬜ Événements aléatoires
- ⬜ Mini-jeu de puzzle
- ⬜ Plus d'époques (Renaissance, Antiquité Grecque, etc.)

---

## 💡 Conseils de Développement

### Pour Ajouter une Nouvelle Époque

1. Modifier `settings.py` pour ajouter l'époque dans `ERAS`
2. Créer une méthode `create_XXX_level()` dans `world/level.py`
3. Ajouter les données dans `data/dialogues.json`
4. Créer les graphismes dans `assets/images/`

### Pour Ajouter un Nouveau Type d'Objet

1. Ajouter le type dans `entities/interactive.py`
2. Définir sa couleur temporaire
3. Ajouter les données dans `dialogues.json`

### Pour Ajouter un Nouveau NPC

1. Créer l'instance dans la méthode de création du niveau
2. Définir ses dialogues et son quiz éventuel
3. L'ajouter au groupe `npcs`

---

## 🐛 Résolution de Problèmes

### Le jeu ne se lance pas
- Vérifier que PyGame est installé : `pip list | grep pygame`
- Vérifier la version de Python : `python --version`

### Erreur "Module not found"
- S'assurer d'être dans le bon dossier
- Vérifier que tous les fichiers sont présents

### Performance lente
- Réduire la résolution dans `settings.py`
- Limiter le nombre d'objets animés

---

## 📊 Système de Score

| Action | Points |
|--------|--------|
| Découverte d'objet | +50 |
| Bonne réponse au quiz | +100 |
| Bonne réponse au 1er essai | +50 bonus |
| Fragment temporel | +500 |

---

## 🎓 Compétences Techniques Démontrées

1. **Programmation Orientée Objet** : Architecture modulaire avec héritage
2. **Design Patterns** : Machine à états (State Pattern)
3. **Gestion des événements** : Clavier et souris
4. **Collision Detection** : AABB (Axis-Aligned Bounding Box)
5. **Gestion de données** : JSON pour sauvegarde et dialogues
6. **Interface utilisateur** : Menus, boutons, dialogues
7. **Game Loop** : Boucle de jeu avec delta time
8. **Caméra 2D** : Scrolling et suivi du joueur

---

## 📝 Notes de Développement

### Version 1.0 (Avril 2026)
- Première version fonctionnelle
- 1 époque complète (Égypte)
- Système de base complet
- Interface utilisateur minimale mais fonctionnelle

### Améliorations Futures
- Graphismes personnalisés
- Bande sonore originale
- Plus d'époques historiques
- Mode multijoueur coopératif

---

## 📄 Licence

Projet académique - 4ème Année Génie Informatique
© 2026 Chaimae Berdij

---

## 🙏 Remerciements

- **Prof. HAJJI TARIK** : Encadrement du projet
- **PyGame Community** : Documentation et tutoriels
- **Université Privée de Fès** : Cadre académique

---

## 📧 Contact

Pour toute question concernant ce projet :
- **Auteur** : Chaimae Berdij
- **Institution** : Université Privée de Fès
- **Filière** : 4ème Année Génie Informatique

---

**Bon voyage dans le temps ! 🕰️**
