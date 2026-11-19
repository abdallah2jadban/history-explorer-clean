# GUIDE D'INSTALLATION RAPIDE - HISTORY EXPLORER

## 🚀 Installation en 3 Étapes

### Étape 1 : Vérifier Python

```bash
python --version
# ou
python3 --version
```

**Version requise** : Python 3.7 ou supérieur

Si Python n'est pas installé : [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

### Étape 2 : Installer PyGame

```bash
pip install pygame
# ou
pip3 install pygame
```

**Vérifier l'installation** :

```bash
python -c "import pygame; print(pygame.version.ver)"
```

---

### Étape 3 : Lancer le Jeu

```bash
cd history_explorer
python main.py
# ou
python3 main.py
```

---

## 🎮 C'est tout ! Le jeu devrait se lancer.

---

## 📝 Installation Détaillée

### Pour Windows

1. **Installer Python** :
   - Télécharger depuis [python.org](https://www.python.org/downloads/)
   - ⚠️ Cocher "Add Python to PATH"
   - Installer

2. **Ouvrir PowerShell ou CMD**

3. **Installer PyGame** :
   ```cmd
   pip install pygame
   ```

4. **Lancer le jeu** :
   ```cmd
   cd chemin\vers\history_explorer
   python main.py
   ```

---

### Pour macOS

1. **Installer Python** (si pas déjà installé) :
   ```bash
   # Avec Homebrew
   brew install python3
   ```

2. **Installer PyGame** :
   ```bash
   pip3 install pygame
   ```

3. **Lancer le jeu** :
   ```bash
   cd /chemin/vers/history_explorer
   python3 main.py
   ```

---

### Pour Linux (Ubuntu/Debian)

1. **Installer Python et pip** :
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Installer PyGame** :
   ```bash
   pip3 install pygame
   ```

3. **Lancer le jeu** :
   ```bash
   cd /chemin/vers/history_explorer
   python3 main.py
   ```

---

## 🔧 Script d'Installation Automatique

### Linux/macOS

```bash
chmod +x run.sh
./run.sh
```

Le script `run.sh` :
- Vérifie si PyGame est installé
- L'installe si nécessaire
- Lance le jeu

---

## ❌ Résolution de Problèmes

### Erreur : "pip n'est pas reconnu"

**Solution Windows** :
```cmd
python -m ensurepip --upgrade
python -m pip install pygame
```

**Solution macOS/Linux** :
```bash
python3 -m ensurepip --upgrade
python3 -m pip install pygame
```

---

### Erreur : "ModuleNotFoundError: No module named 'pygame'"

**Solution** :
```bash
pip install --user pygame
# ou
pip3 install --user pygame
```

---

### Erreur : "Permission denied"

**Linux/macOS** :
```bash
sudo pip3 install pygame
```

---

### Le jeu est lent / laggy

1. **Vérifier les specs minimales** :
   - CPU : Dual-core 1.5 GHz
   - RAM : 2 GB
   - GPU : Intégré (suffisant)

2. **Réduire la résolution** :
   - Éditer `settings.py`
   - Changer `WINDOW_WIDTH` et `WINDOW_HEIGHT`
   - Exemple : 800×600 pour machines anciennes

3. **Fermer les autres applications**

---

### Problème d'affichage / fenêtre trop grande

**Solution** :
- Éditer `settings.py`
- Ajuster `WINDOW_WIDTH` et `WINDOW_HEIGHT`
- Recommandé : 1280×720 (défaut) ou 1024×576

---

## 🖥️ Configuration Système

### Minimale

- **OS** : Windows 7+, macOS 10.12+, Linux
- **CPU** : 1.5 GHz Dual-Core
- **RAM** : 2 GB
- **Espace disque** : 50 MB
- **GPU** : Carte graphique intégrée

### Recommandée

- **OS** : Windows 10+, macOS 11+, Ubuntu 20.04+
- **CPU** : 2.0 GHz Quad-Core
- **RAM** : 4 GB
- **Espace disque** : 100 MB
- **GPU** : Carte graphique dédiée

---

## 📦 Installation via requirements.txt

```bash
cd history_explorer
pip install -r requirements.txt
python main.py
```

---

## 🧪 Vérifier l'Installation

### Test 1 : Python fonctionne

```bash
python --version
```

**Attendu** : `Python 3.7.x` ou supérieur

---

### Test 2 : PyGame fonctionne

```bash
python -c "import pygame; print('PyGame OK')"
```

**Attendu** : `PyGame OK`

---

### Test 3 : Lancer le jeu

```bash
cd history_explorer
python main.py
```

**Attendu** : Fenêtre de jeu avec menu

---

## 🌐 Installation sur Raspberry Pi

```bash
sudo apt update
sudo apt install python3-pygame
cd history_explorer
python3 main.py
```

**Note** : Le jeu tourne à 60 FPS sur Raspberry Pi 4

---

## 📱 Notes pour Développeurs

### Environnement Virtuel (Recommandé)

```bash
# Créer l'environnement
python3 -m venv venv

# Activer
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer le jeu
python main.py
```

---

### Mode Développement

```bash
# Clone le projet
git clone <repository>
cd history_explorer

# Créer l'environnement
python3 -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer en mode dev
python main.py
```

---

## ✅ Installation Réussie !

Si vous voyez le menu principal du jeu, l'installation est réussie ! 🎉

**Prochaines étapes** :
1. Lire le `README.md` pour comprendre le jeu
2. Consulter `TESTING.md` pour la checklist de test
3. Voir `PRESENTATION.md` pour une démo complète

---

## 💡 Astuces

### Lancer depuis n'importe où

**Créer un alias (Linux/macOS)** :

```bash
# Ajouter à ~/.bashrc ou ~/.zshrc
alias history_explorer="cd /chemin/vers/history_explorer && python3 main.py"

# Puis lancer avec:
history_explorer
```

**Créer un raccourci (Windows)** :

1. Clic droit sur le bureau → Nouveau → Raccourci
2. Emplacement : `python.exe C:\chemin\vers\history_explorer\main.py`
3. Nommer : "History Explorer"

---

### Mode Plein Écran (Modification)

Éditer `settings.py` :

```python
# Ajouter après les imports
import pygame
pygame.FULLSCREEN = True

# Dans main.py, modifier la création de la fenêtre
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
```

---

## 📞 Support

En cas de problème :

1. Vérifier cette page
2. Consulter `README.md`
3. Vérifier les logs d'erreur
4. Contacter : [votre email de support]

---

**Installation réussie ? Bon jeu ! 🎮**
