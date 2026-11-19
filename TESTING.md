# GUIDE DE TEST - HISTORY EXPLORER

## 📋 Checklist de Test Complète

### 1. Tests de Base ✓

#### Lancement du Jeu
- [ ] Le jeu se lance sans erreur
- [ ] La fenêtre s'affiche correctement (1280x720)
- [ ] Le titre "HISTORY EXPLORER" est visible
- [ ] Les boutons du menu sont affichés

#### Menu Principal
- [ ] Les 3 boutons sont visibles (Jouer, Continuer, Quitter)
- [ ] La navigation au clavier fonctionne (flèches)
- [ ] La navigation à la souris fonctionne (survol + clic)
- [ ] Le bouton "Jouer" lance une nouvelle partie
- [ ] Le bouton "Quitter" ferme le jeu

---

### 2. Tests de Gameplay 🎮

#### Déplacement du Joueur
- [ ] Le joueur se déplace avec les flèches directionnelles
- [ ] Le joueur se déplace avec ZQSD
- [ ] Le déplacement est fluide (pas de saccades)
- [ ] Les collisions avec les murs fonctionnent
- [ ] Les collisions avec les obstacles fonctionnent
- [ ] Le joueur ne peut pas sortir de la carte

#### Caméra
- [ ] La caméra suit le joueur
- [ ] La caméra ne dépasse pas les bords de la carte
- [ ] Le scrolling est fluide

---

### 3. Tests d'Interaction 🗣️

#### Dialogues avec NPCs
- [ ] Le joueur peut interagir avec l'avatar guide (Espace)
- [ ] Le dialogue s'affiche dans une boîte en bas de l'écran
- [ ] L'effet machine à écrire fonctionne
- [ ] Le nom du NPC s'affiche correctement
- [ ] On peut avancer dans les dialogues avec Espace
- [ ] Interaction avec le Pharaon fonctionne
- [ ] Interaction avec le Scribe fonctionne

#### Objets Interactifs
- [ ] Cliquer sur un objet affiche une popup d'information
- [ ] Le titre de l'objet s'affiche
- [ ] La description s'affiche correctement
- [ ] Les points sont ajoutés au score (+50)
- [ ] L'objet devient semi-transparent après découverte
- [ ] L'animation de pulsation fonctionne avant découverte
- [ ] La popup disparaît après 5 secondes

#### Tous les Objets (5 au total)
- [ ] Pyramide cliquable et fonctionnelle
- [ ] Sphinx cliquable et fonctionnel
- [ ] Papyrus cliquable et fonctionnel
- [ ] Sarcophage cliquable et fonctionnel
- [ ] Trésor cliquable et fonctionnel

---

### 4. Tests du Système de Quiz 📝

#### Déclenchement du Quiz
- [ ] Terminer le dialogue avec un NPC lance le quiz
- [ ] L'écran de quiz s'affiche avec overlay
- [ ] La question s'affiche clairement
- [ ] Les 4 réponses sont visibles

#### Navigation dans le Quiz
- [ ] On peut sélectionner une réponse avec les flèches
- [ ] On peut sélectionner une réponse à la souris
- [ ] Le survol des boutons fonctionne
- [ ] La réponse sélectionnée est mise en évidence

#### Réponses Correctes
- [ ] Une bonne réponse affiche "BONNE RÉPONSE!"
- [ ] +100 points sont ajoutés au score
- [ ] +50 points bonus pour le premier essai
- [ ] Le quiz est marqué comme complété
- [ ] On retourne au jeu après avoir cliqué

#### Réponses Incorrectes
- [ ] Une mauvaise réponse affiche "MAUVAISE RÉPONSE"
- [ ] La bonne réponse est indiquée
- [ ] Aucun point n'est ajouté
- [ ] Le quiz reste marqué comme non complété

#### Quiz Pharaon
- [ ] Question sur les pyramides affichée
- [ ] Réponse correcte : "Tombeaux pour les pharaons"
- [ ] Score mis à jour correctement

#### Quiz Scribe
- [ ] Question sur l'écriture affichée
- [ ] Réponse correcte : "Hiéroglyphes"
- [ ] Score mis à jour correctement

---

### 5. Tests du HUD 📊

#### Affichage du Score
- [ ] Le score s'affiche en haut à gauche
- [ ] Le score augmente quand on découvre des objets
- [ ] Le score augmente avec les bonnes réponses aux quiz

#### Timer
- [ ] Le timer s'affiche en haut à droite
- [ ] Le timer décrémente correctement
- [ ] Le timer devient rouge sous 1 minute
- [ ] Format MM:SS correct

#### Nom de l'Époque
- [ ] "Égypte Antique" s'affiche au centre
- [ ] La couleur correspond à l'époque

#### Barre de Progression
- [ ] La barre affiche "Objets: X/5"
- [ ] La barre se remplit quand on découvre des objets
- [ ] Elle devient verte quand complète

---

### 6. Tests de Progression 🎯

#### Objectifs du Niveau
- [ ] Tous les objets doivent être découverts (5/5)
- [ ] Tous les quiz doivent être réussis (2/2)
- [ ] Le fragment temporel est verrouillé au départ (violet)
- [ ] Le fragment se déverrouille quand objectifs complétés (vert)

#### Collecte du Fragment
- [ ] On peut interagir avec le fragment une fois déverrouillé
- [ ] +500 points sont ajoutés
- [ ] L'écran de victoire s'affiche

---

### 7. Tests des Écrans de Fin 🏆

#### Écran de Victoire
- [ ] "VICTOIRE!" s'affiche en grand
- [ ] Le score final est affiché
- [ ] "Fragment Temporel Collecté" est indiqué
- [ ] Message de déverrouillage du Moyen Âge
- [ ] Bouton "Époque Suivante" fonctionne
- [ ] Bouton "Menu Principal" fonctionne
- [ ] Bouton "Quitter" fonctionne

#### Écran de Game Over
- [ ] "GAME OVER" s'affiche si le temps est écoulé
- [ ] La raison est affichée ("Temps écoulé!")
- [ ] Le score final est affiché
- [ ] Bouton "Réessayer" relance le niveau
- [ ] Bouton "Menu Principal" retourne au menu
- [ ] Bouton "Quitter" ferme le jeu

---

### 8. Tests de Sauvegarde 💾

#### Système de Sauvegarde
- [ ] Le fichier save.json est créé
- [ ] Le score est sauvegardé
- [ ] L'époque actuelle est sauvegardée
- [ ] Les époques déverrouillées sont sauvegardées

#### Chargement de Sauvegarde
- [ ] Le bouton "Continuer" charge la sauvegarde
- [ ] Le score est restauré
- [ ] L'époque déverrouillée reste accessible

---

### 9. Tests de l'Interface 🎨

#### Boutons
- [ ] Tous les boutons ont un effet de survol
- [ ] Les boutons sont cliquables
- [ ] Les textes sont lisibles
- [ ] Les couleurs sont cohérentes

#### Boîtes de Dialogue
- [ ] Fond semi-transparent
- [ ] Bordures visibles
- [ ] Texte lisible
- [ ] Pas de débordement de texte

#### Popups
- [ ] Centrées à l'écran
- [ ] Fond opaque
- [ ] Fermeture automatique après timer

---

### 10. Tests de Performance ⚡

#### Fluidité
- [ ] Le jeu tourne à 60 FPS constant
- [ ] Pas de ralentissement visible
- [ ] Les animations sont fluides
- [ ] Le scrolling est sans saccades

#### Mémoire
- [ ] Pas de fuite mémoire après 10 minutes de jeu
- [ ] Le jeu reste réactif

---

### 11. Tests de Robustesse 🛡️

#### Gestion des Erreurs
- [ ] Le jeu ne crash pas si on spam les touches
- [ ] Le jeu ne crash pas si on clique partout rapidement
- [ ] Le jeu gère correctement les fichiers manquants

#### Cas Limites
- [ ] On peut mettre en pause pendant un dialogue
- [ ] On peut mettre en pause pendant un quiz
- [ ] ESC retourne bien au menu depuis la pause
- [ ] Impossible d'interagir 2 fois avec le même objet

---

### 12. Tests de Pause ⏸️

#### Fonctionnalité Pause
- [ ] P met le jeu en pause
- [ ] ESC met le jeu en pause
- [ ] L'écran s'assombrit
- [ ] "PAUSE" s'affiche
- [ ] Le timer s'arrête
- [ ] P reprend le jeu
- [ ] ESC reprend le jeu

---

## 🎯 Scénario de Test Complet

### Test End-to-End (E2E)

1. **Démarrage**
   - Lancer le jeu
   - Vérifier le menu principal
   
2. **Nouvelle Partie**
   - Cliquer sur "Jouer"
   - Vérifier le chargement du niveau Égypte
   
3. **Exploration**
   - Se déplacer dans toute la carte
   - Tester les collisions avec tous les obstacles
   
4. **Découverte des Objets**
   - Cliquer sur les 5 objets interactifs
   - Vérifier les popups et le score
   
5. **Dialogues**
   - Parler à l'avatar guide
   - Parler au Pharaon
   - Parler au Scribe
   
6. **Quiz**
   - Répondre au quiz du Pharaon (bonne réponse)
   - Répondre au quiz du Scribe (bonne réponse)
   
7. **Fragment Temporel**
   - Vérifier qu'il est déverrouillé
   - Le collecter
   
8. **Victoire**
   - Vérifier l'écran de victoire
   - Vérifier le score total
   - Vérifier le déverrouillage du Moyen Âge
   
9. **Retour Menu**
   - Cliquer sur "Menu Principal"
   - Vérifier qu'on est bien au menu
   
10. **Quitter**
    - Cliquer sur "Quitter"
    - Vérifier la fermeture propre

---

## 📊 Score Attendu (Partie Parfaite)

| Action | Points | Quantité | Total |
|--------|--------|----------|-------|
| Objets découverts | 50 | 5 | 250 |
| Quiz réussis | 100 | 2 | 200 |
| Bonus 1er essai | 50 | 2 | 100 |
| Fragment temporel | 500 | 1 | 500 |
| **TOTAL** | | | **1050** |

---

## 🐛 Bugs Connus

Aucun bug connu pour le moment.

---

## ✅ Critères de Validation

Le jeu est considéré comme validé si :

- ✅ Tous les tests de base passent
- ✅ Tous les tests de gameplay passent
- ✅ Le scénario E2E complet fonctionne
- ✅ Aucun crash durant 15 minutes de jeu
- ✅ Score de 1050 points atteignable

---

## 📝 Rapport de Test

**Date** : _________________

**Testeur** : _________________

**Version** : 1.0

**Résultat Global** : ☐ PASS  ☐ FAIL

**Commentaires** :
```
_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
```

**Bugs Trouvés** :
```
_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
```
