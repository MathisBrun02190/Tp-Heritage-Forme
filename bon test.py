import tkinter as tk  # Importation du module Tkinter pour l'interface graphique
import math  # Importation du module math pour cos, sin et radians

# Configuration générale
WIDTH, HEIGHT = 400, 250  # Largeur et hauteur du canvas pour le thermomètre
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT - 20  # Coordonnées du centre du demi-cercle
RADIUS = 150  # Rayon du demi-cercle
MIN_TEMP = -20  # Température minimale affichée
MAX_TEMP = 50  # Température maximale affichée
STEP = 10  # Intervalle entre les graduations du thermomètre
RED_ZONE = 40  # Température critique où la zone rouge commence

# Fonction pour déterminer la couleur du bargraphe en fonction de la température
def temp_color(temp):
    """Retourne une couleur en fonction de la température"""
    if temp <= 0:
        return "#00BFFF"  # Bleu froid si temp <= 0
    elif temp <= 25:
        return "#FFFF00"  # Jaune si temp <= 25
    else:
        return "#FF4500"  # Rouge chaud si temp > 25

# Fonction pour convertir la température en angle sur le demi-cercle
def temp_to_angle(temp):
    return 180 - 180 * (temp - MIN_TEMP) / (MAX_TEMP - MIN_TEMP)  # Conversion proportionnelle en degrés

# Fonction pour dessiner l’aiguille sur le canvas
def draw_needle(canvas, temp):
    angle = math.radians(temp_to_angle(temp))  # Conversion de l'angle en radians
    x = CENTER_X + RADIUS * math.cos(angle)  # Coordonnée x de l'extrémité de l'aiguille
    y = CENTER_Y - RADIUS * math.sin(angle)  # Coordonnée y de l'extrémité de l'aiguille
    canvas.coords(needle, CENTER_X, CENTER_Y, x, y)  # Met à jour les coordonnées de l’aiguille

# Fonction pour dessiner le bargraphe
def draw_bar(bar_canvas, temp):
    bar_canvas.delete("all")  # Supprime l’ancien contenu du bargraphe
    BAR_TOP_MARGIN = 10  # Marge en haut du bargraphe
    BAR_BOTTOM_MARGIN = 10  # Marge en bas du bargraphe
    usable_height = HEIGHT - BAR_TOP_MARGIN - BAR_BOTTOM_MARGIN  # Hauteur utilisable du bargraphe

    # Hauteur proportionnelle de la barre
    bar_height = (temp - MIN_TEMP) / (MAX_TEMP - MIN_TEMP) * usable_height
    color = temp_color(temp)  # Détermine la couleur en fonction de la température

    # Rectangle du bargraphe
    bar_canvas.create_rectangle(10, HEIGHT-BAR_BOTTOM_MARGIN-bar_height, 60, HEIGHT-BAR_BOTTOM_MARGIN,
                                fill=color, outline="black")  # Dessine le rectangle

    # Graduations du bargraphe
    for t in range(MIN_TEMP, MAX_TEMP+1, STEP):  # Boucle sur toutes les graduations
        y = HEIGHT - BAR_BOTTOM_MARGIN - (t - MIN_TEMP) / (MAX_TEMP - MIN_TEMP) * usable_height  # Position verticale
        bar_canvas.create_line(60, y, 65, y, width=2)  # Ligne de graduation
        bar_canvas.create_text(75, y, text=f"{t}°C", anchor="w", font=("Helvetica", 9))  # Texte de la graduation

# Création de la fenêtre principale
root = tk.Tk()  # Crée la fenêtre Tkinter
root.title("Thermomètre + Bargraphe stylé")  # Titre de la fenêtre
root.configure(bg="#2C2F33")  # Couleur de fond de la fenêtre

# Frame principale pour contenir thermomètre et bargraphe
frame_main = tk.Frame(root, bg="#2C2F33")  # Création d'un conteneur principal
frame_main.pack(padx=20, pady=20)  # Positionnement avec padding

# ---- Thermomètre à gauche ----
frame_left = tk.Frame(frame_main, bg="#2C2F33")  # Frame pour le thermomètre
frame_left.pack(side="left", padx=10)  # Positionné à gauche

canvas = tk.Canvas(frame_left, width=WIDTH, height=HEIGHT, bg="#1C1E22", highlightthickness=0)  # Canvas pour dessiner le thermomètre
canvas.pack()  # Affichage du canvas

# Demi-cercle représentant le thermomètre
canvas.create_arc(CENTER_X-RADIUS, CENTER_Y-RADIUS, CENTER_X+RADIUS, CENTER_Y+RADIUS,
                  start=0, extent=180, style='arc', width=4, outline="white")  # Arc de 180° pour le thermomètre

# Graduations + zone rouge
for temp in range(MIN_TEMP, MAX_TEMP+1, STEP):  # Boucle sur toutes les graduations
    angle = math.radians(temp_to_angle(temp))  # Conversion en radians
    inner_x = CENTER_X + (RADIUS-10) * math.cos(angle)  # Coordonnée x interne de la graduation
    inner_y = CENTER_Y - (RADIUS-10) * math.sin(angle)  # Coordonnée y interne
    outer_x = CENTER_X + RADIUS * math.cos(angle)  # Coordonnée x externe
    outer_y = CENTER_Y - RADIUS * math.sin(angle)  # Coordonnée y externe
    canvas.create_line(inner_x, inner_y, outer_x, outer_y, width=2, fill="white")  # Dessine la graduation
    # Texte des graduations
    text_x = CENTER_X + (RADIUS-25) * math.cos(angle)  # Coordonnée x du texte
    text_y = CENTER_Y - (RADIUS-25) * math.sin(angle)  # Coordonnée y du texte
    canvas.create_text(text_x, text_y, text=f"{temp}°C", font=("Helvetica", 10), fill="white")  # Texte de la graduation

# Zone rouge pour températures élevées
for temp in range(RED_ZONE, MAX_TEMP+1, 1):  # Boucle sur zone rouge
    angle1 = math.radians(temp_to_angle(temp))  # Angle début segment
    angle2 = math.radians(temp_to_angle(temp+1))  # Angle fin segment
    x1 = CENTER_X + RADIUS * math.cos(angle1)  # Coordonnée x début
    y1 = CENTER_Y - RADIUS * math.sin(angle1)  # Coordonnée y début
    x2 = CENTER_X + RADIUS * math.cos(angle2)  # Coordonnée x fin
    y2 = CENTER_Y - RADIUS * math.sin(angle2)  # Coordonnée y fin
    canvas.create_line(x1, y1, x2, y2, fill="red", width=4)  # Dessine segment rouge

# Aiguille initiale
needle = canvas.create_line(CENTER_X, CENTER_Y, CENTER_X, CENTER_Y-RADIUS, width=4, fill='red', capstyle='round')  # Ligne rouge représentant l’aiguille

# Fonction appelée quand on change le slider
def on_slider(val):
    temp = float(val)  # Convertit la valeur du slider en float
    draw_needle(canvas, temp)  # Met à jour l’aiguille
    draw_bar(bar_canvas, temp)  # Met à jour le bargraphe

# Slider pour changer la température
slider = tk.Scale(frame_left, from_=MIN_TEMP, to=MAX_TEMP, orient='horizontal', length=350,
                  command=on_slider, bg="#2C2F33", fg="white", troughcolor="#555555")  # Slider horizontal
slider.pack(pady=10)  # Positionnement du slider

# ---- Bargraphe à droite ----
frame_right = tk.Frame(frame_main, bg="#2C2F33")  # Frame pour le bargraphe
frame_right.pack(side="left", padx=50)  # Positionné à droite du thermomètre

bar_canvas = tk.Canvas(frame_right, width=100, height=HEIGHT, bg="#1C1E22", highlightthickness=0)  # Canvas pour le bargraphe
bar_canvas.pack()  # Affichage du bargraphe

# Rectangle initial
draw_bar(bar_canvas, MIN_TEMP)  # Affiche le bargraphe initial à la température minimale

root.mainloop()  # Boucle principale Tkinter, ouvre la fenêtre et attend les événements
