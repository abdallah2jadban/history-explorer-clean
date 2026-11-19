# ⚡ DÉMARRAGE RAPIDE - HISTORY EXPLORER

## En 30 Secondes ⏱️

```bash
pip install pygame
cd history_explorer
python main.py
```

**C'est tout ! Le jeu se lance. 🎮**

---

## Commandes du Jeu 🎮

| Touche | Action |
|--------|--------|
| **⬆️ ⬇️ ⬅️ ➡️** ou **Z Q S D** | Se déplacer |
| **Espace** ou **Entrée** | Interagir / Parler |
| **Clic gauche** | Cliquer sur objets |
| **P** | Pause |
| **ESC** | Menu pause |

---

## Objectif 🎯

1. **Explorer** la carte de l'Égypte Antique
2. **Cliquer** sur les 5 objets historiques (pyramides, sphinx, etc.)
3. **Parler** aux 2 NPCs et réussir leurs quiz
4. **Collecter** le fragment temporel violet au centre
5. **Gagner** et débloquer l'époque suivante !

---

## Score Maximum 🏆

- 5 objets × 50 pts = **250**
- 2 quiz × 100 pts = **200**
- 2 bonus premier essai × 50 pts = **100**
- 1 fragment = **500**

**TOTAL : 1050 points**

---

## Temps Limite ⏰

**5 minutes** par niveau

Le timer est en haut à droite. Il devient rouge sous 1 minute !

---

## Indices 💡

### Trouver les Objets

Les objets **pulsent** (grossissent/rétrécissent) quand ils n'ont pas été découverts.

Cherchez dans toute la carte :
- Près des pyramides
- Autour du sphinx
- Dans les coins de la carte
- À côté des NPCs

### Réussir les Quiz

**Question Pharaon** : "Fonction des pyramides ?"
→ Réponse : **Tombeaux pour les pharaons**

**Question Scribe** : "Système d'écriture ?"
→ Réponse : **Hiéroglyphes**

---

## Astuces 🎓

1. **Parlez au guide en premier** (avatar bleu clair) pour comprendre les objectifs
   
2. **Explorez systématiquement** la carte pour ne rien manquer

3. **Lisez bien les questions** des quiz avant de répondre

4. **Le fragment est verrouillé** (violet) tant que tous les objectifs ne sont pas remplis

5. **Une fois vert**, vous pouvez le collecter et gagner !

---

## En Cas de Problème ⚠️

### Le jeu ne se lance pas

```bash
# Vérifier Python
python --version
# Doit être 3.7+

# Vérifier PyGame
python -c "import pygame"
# Si erreur → pip install pygame
```

### Fenêtre trop grande

Éditer `settings.py` :
```python
WINDOW_WIDTH = 1024  # Au lieu de 1280
WINDOW_HEIGHT = 576  # Au lieu de 720
```

### Jeu trop lent

1. Fermer les autres applications
2. Réduire la résolution (voir ci-dessus)

---

## Documentation Complète 📚

| Document | Contenu |
|----------|---------|
| **README.md** | Tout savoir sur le projet |
| **INSTALL.md** | Installation détaillée |
| **ARCHITECTURE.md** | Documentation technique |
| **TESTING.md** | Guide de test |
| **PRESENTATION.md** | Script de présentation |

---

## Structure Rapide 🗂️

```
history_explorer/
├── main.py          ← Lancer ça !
├── game.py          ← Moteur principal
├── settings.py      ← Config (couleurs, vitesse, etc.)
│
├── states/          ← Écrans du jeu
│   ├── menu.py
│   ├── playing.py
│   └── quiz.py
│
├── entities/        ← Personnages et objets
│   ├── player.py
│   ├── npc.py
│   └── interactive.py
│
└── data/            ← Données
    ├── dialogues.json
    └── save.json
```

---

## FAQ Express ❓

**Q : Combien de temps pour finir ?**  
A : 5-10 minutes pour un niveau complet

**Q : Combien d'époques ?**  
A : 1 complète (Égypte), 1 en dev (Moyen Âge)

**Q : Peut-on sauvegarder ?**  
A : Oui ! Auto-sauvegarde à la victoire

**Q : Multi-joueur ?**  
A : Pas encore (prévu v2.0)

**Q : En français uniquement ?**  
A : Oui pour l'instant

---

## Prochaines Étapes 🚀

Après avoir joué :

1. **Lire README.md** pour le contexte complet
2. **Consulter ARCHITECTURE.md** pour comprendre le code
3. **Essayer de modifier** settings.py
4. **Ajouter vos propres quiz** dans dialogues.json

---

## Bon Jeu ! 🎮

Amusez-vous bien et apprenez l'Histoire ! 📚✨

---

**Chaimae Berdij - 2026**
