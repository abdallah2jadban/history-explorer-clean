#!/bin/bash

echo "================================================"
echo "       HISTORY EXPLORER - Lancement"
echo "       4th Year Project by Chaimae Berdij"
echo "================================================"
echo ""

# Vérifier si pygame est installé
python3 -c "import pygame" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  PyGame n'est pas installé."
    echo "Installation de PyGame..."
    pip install pygame
    echo ""
fi

echo "🎮 Lancement du jeu..."
echo ""

# Lancer le jeu
python3 main.py

echo ""
echo "Merci d'avoir joué! 👋"
