import tkinter as tk  # Importation du module Tkinter pour l’interface graphique
import math  # Importation du module math pour les calculs trigonométriques

# -----------------------------
# Configuration générale
# -----------------------------
WIDTH, HEIGHT = 800, 500  # Dimensions du canvas du thermomètre
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT - 40  # Coordonnées du centre du demi-cercle
RADIUS = 300  # Rayon du demi-cercle
MIN_TEMP = -20  # Température minimale
MAX_TEMP = 50   # Température maximale
STEP = 10       # Intervalle des graduations
RED_ZONE = 40   # Température critique (zone rouge)

# -----------------------------
# Fonction qui détermine la couleur du bargraphe
# -----------------------------
def temp_color(temp):
    if temp <= 0:
        return "#00BFFF"  # Bleu pour températures froides
    elif temp <= 25:
        return "#FFFF00"  # Jaune pour températures moyennes
    else:
        return "#FF4500"  # Rouge pour températures élevées

# -----------------------------
# Fonction qui convertit une température en angle du demi-cercle
# -----------------------------
def temp_to_angle(temp):
    # Retourne un angle compris entre 180° (MIN_TEMP) et 0° (MAX_TEMP)
    return 180 - 180 * (temp - MIN_TEMP) / (MAX_TEMP - MIN_TEMP)

# -----------------------------
# Fonction qui dessine l’aiguille du thermomètre
# -----------------------------
def draw_needle(canvas, temp):
    angle = math.radians(temp_to_angle(temp))  # Convertit l’angle en radians
    x = CENTER_X + RADIUS * math.cos(angle)    # Coordonnée X de la pointe de l’aiguille
    y = CENTER_Y - RADIUS * math.sin(angle)    # Coordonnée Y de la pointe de l’aiguille
    # Déplace l’aiguille aux nouvelles coordonnées
    canvas.coords(needle, CENTER_X, CENTER_Y, x, y)

# -----------------------------
# Fonction qui dessine le bargraphe
# -----------------------------
def draw_bar(bar_canvas, temp):
    bar_canvas.delete("all")  # Efface le contenu précédent du bargraphe

    BAR_TOP_MARGIN = 20       # Marge en haut du bargraphe
    BAR_BOTTOM_MARGIN = 20    # Marge en bas du bargraphe
    usable_height = HEIGHT - BAR_TOP_MARGIN - BAR_BOTTOM_MARGIN  # Hauteur utile du bargraphe

    # Calcule la hauteur du rectangle en fonction de la température
    bar_height = (temp - MIN_TEMP) / (MAX_TEMP - MIN_TEMP) * usable_height
    color = temp_color(temp)  # Détermine la couleur en fonction de la température

    # Dessine le rectangle coloré représentant la température
    bar_canvas.create_rectangle(
        20, HEIGHT-BAR_BOTTOM_MARGIN-bar_height,  # coin haut-gauche
        120, HEIGHT-BAR_BOTTOM_MARGIN,            # coin bas-droit
        fill=color, outline="black"
    )

    # Ajoute les graduations le long du bargraphe
    for t in range(MIN_TEMP, MAX_TEMP+1, STEP):
        y = HEIGHT - BAR_BOTTOM_MARGIN - (t - MIN_TEMP) / (MAX_TEMP - MIN_TEMP) * usable_height
        bar_canvas.create_line(120, y, 135, y, width=4)  # Petit trait de graduation
        bar_canvas.create_text(150, y, text=f"{t}°C", anchor="w", font=("Helvetica", 16))  # Texte des graduations

# -----------------------------
# Création de la fenêtre principale
# -----------------------------
root = tk.Tk()  # Initialise la fenêtre Tkinter
root.title("Thermomètre + Bargraphe (entrée directe)")  # Titre de la fenêtre
root.configure(bg="#2C2F33")  # Couleur de fond

# Frame principale qui contient tout
frame_main = tk.Frame(root, bg="#2C2F33")
frame_main.pack(padx=40, pady=40)

# -----------------------------
# Zone gauche : Thermomètre
# -----------------------------
frame_left = tk.Frame(frame_main, bg="#2C2F33")  # Frame pour le thermomètre
frame_left.pack(side="left", padx=20)

canvas = tk.Canvas(frame_left, width=WIDTH, height=HEIGHT, bg="#1C1E22", highlightthickness=0)  # Canvas du thermomètre
canvas.pack()

# Demi-cercle principal
canvas.create_arc(
    CENTER_X-RADIUS, CENTER_Y-RADIUS, CENTER_X+RADIUS, CENTER_Y+RADIUS,
    start=0, extent=180, style='arc', width=8, outline="white"
)

# Ajout des graduations sur le demi-cercle
for temp in range(MIN_TEMP, MAX_TEMP+1, STEP):
    angle = math.radians(temp_to_angle(temp))  # Angle de la graduation
    inner_x = CENTER_X + (RADIUS-20) * math.cos(angle)  # Coordonnée interne
    inner_y = CENTER_Y - (RADIUS-20) * math.sin(angle)
    outer_x = CENTER_X + RADIUS * math.cos(angle)  # Coordonnée externe
    outer_y = CENTER_Y - RADIUS * math.sin(angle)
    canvas.create_line(inner_x, inner_y, outer_x, outer_y, width=4, fill="white")  # Graduation blanche
    text_x = CENTER_X + (RADIUS-50) * math.cos(angle)  # Position du texte
    text_y = CENTER_Y - (RADIUS-50) * math.sin(angle)
    canvas.create_text(text_x, text_y, text=f"{temp}°C", font=("Helvetica", 18), fill="white")

# Zone rouge (températures critiques)
for temp in range(RED_ZONE, MAX_TEMP+1, 1):
    angle1 = math.radians(temp_to_angle(temp))
    angle2 = math.radians(temp_to_angle(temp+1))
    x1 = CENTER_X + RADIUS * math.cos(angle1)
    y1 = CENTER_Y - RADIUS * math.sin(angle1)
    x2 = CENTER_X + RADIUS * math.cos(angle2)
    y2 = CENTER_Y - RADIUS * math.sin(angle2)
    canvas.create_line(x1, y1, x2, y2, fill="red", width=8)

# Aiguille initiale (par défaut sur MIN_TEMP)
needle = canvas.create_line(CENTER_X, CENTER_Y, CENTER_X, CENTER_Y-RADIUS,
                            width=8, fill='red', capstyle='round')

# -----------------------------
# Zone de saisie pour entrer la température
# -----------------------------
entry_label = tk.Label(frame_left, text="Entrer la température :", font=("Helvetica", 16), bg="#2C2F33", fg="white")
entry_label.pack(pady=10)

entry = tk.Entry(frame_left, font=("Helvetica", 16))  # Zone de saisie
entry.pack(pady=10)

# Fonction appelée quand on clique sur "Valider"
def validate_entry():
    try:
        temp = float(entry.get())  # Récupère la valeur saisie et convertit en float
        if temp < MIN_TEMP: temp = MIN_TEMP  # Limite inférieure
        if temp > MAX_TEMP: temp = MAX_TEMP  # Limite supérieure
        draw_needle(canvas, temp)  # Met à jour l’aiguille
        draw_bar(bar_canvas, temp)  # Met à jour le bargraphe
    except ValueError:
        pass  # Ignore si l’utilisateur tape n’importe quoi

# Bouton pour valider la saisie
validate_button = tk.Button(frame_left, text="Valider", font=("Helvetica", 16),
                            command=validate_entry, bg="#444", fg="white")
validate_button.pack(pady=10)

# -----------------------------
# Zone droite : Bargraphe
# -----------------------------
frame_right = tk.Frame(frame_main, bg="#2C2F33")  # Frame pour le bargraphe
frame_right.pack(side="left", padx=50)

bar_canvas = tk.Canvas(frame_right, width=200, height=HEIGHT, bg="#1C1E22", highlightthickness=0)  # Canvas du bargraphe
bar_canvas.pack()

# Affiche bargraphe initial à MIN_TEMP
draw_bar(bar_canvas, MIN_TEMP)

# -----------------------------
# Boucle principale Tkinter
# -----------------------------
root.mainloop()
