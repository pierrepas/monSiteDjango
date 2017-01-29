#!/bin/bash
clear
echo "Lancement du serveur..."
python manage.py runserver &
echo "Affichage dans le navigateur..."
sleep 1
firefox localhost:8000 &

