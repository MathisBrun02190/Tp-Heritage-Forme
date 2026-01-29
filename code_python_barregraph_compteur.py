import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Wedge
import numpy as np

class CombinedGaugeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compteur de vitesse + Barre de température")
        self.root.geometry("650x700")
        self.current_value = 0

        # Entrée utilisateur
        self.label = tk.Label(root, text="Entrez un entier entre -20 et 50 :", font=("Arial", 12))
        self.label.pack(pady=10)

        # Frame pour l'entrée et le bouton
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)

        self.entry = tk.Entry(input_frame, font=("Arial", 14), width=10, justify='center')
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind('<Return>', lambda e: self.update_displays())

        self.button = tk.Button(input_frame, text="Afficher", command=self.update_displays, 
                               font=("Arial", 12), bg="#4CAF50", fg="white", padx=20)
        self.button.pack(side=tk.LEFT, padx=5)

        # Bouton reset
        self.reset_button = tk.Button(root, text="Réinitialiser", command=self.reset_displays,
                                     font=("Arial", 10), bg="#f44336", fg="white")
        self.reset_button.pack(pady=5)

        # Figure matplotlib pour le compteur
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.fig.patch.set_facecolor('#f0f0f0')
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(pady=10)

        # Frame pour la barre de température
        self.temp_frame = tk.Frame(root, bg='black', padx=20, pady=15)
        self.temp_frame.pack(pady=10, padx=20, fill=tk.X)

        self.temp_label = tk.Label(self.temp_frame, text="", font=("Courier", 16, "bold"), 
                                   bg='black', fg='white', justify='left')
        self.temp_label.pack()

        # Valeur initiale
        self.draw_gauge(0)
        self.draw_temperature_bar(0)

    def get_temp_color_hex(self, temp):
        if -20 <= temp <= -1:
            return "#3498db"  # Bleu
        elif 0 <= temp <= 9:
            return "#2ecc71"  # Vert
        elif 10 <= temp <= 25:
            return "#f39c12"  # Jaune
        elif 26 <= temp <= 50:
            return "#e74c3c"  # Rouge
        return "#95a5a6"

    def draw_temperature_bar(self, temp):
        min_temp = -20
        max_temp = 50
        total_blocks = 8

        if temp < min_temp or temp > max_temp:
            bar_text = f"{temp:3d}°C : Température hors plage !"
            self.temp_label.config(text=bar_text, fg='red')
            return

        range_temp = max_temp - min_temp
        filled_blocks = (temp - min_temp) * total_blocks // range_temp
        if filled_blocks < 1:
            filled_blocks = 1
        if filled_blocks > total_blocks:
            filled_blocks = total_blocks

        color = self.get_temp_color_hex(temp)
        
        bar = ""
        for i in range(total_blocks):
            if i < filled_blocks:
                bar += "█"
            else:
                bar += "."

        bar_text = f"{temp:3d}°C : {bar}"
        self.temp_label.config(text=bar_text, fg=color)

    def draw_gauge(self, value):
        self.ax.clear()
        self.ax.set_facecolor('#f0f0f0')

        radius = 1.0

        # Zones colorées
        wedge1 = Wedge((0, 0), radius, 0, 114.3, facecolor='#4CAF50', alpha=0.3, edgecolor='none')
        self.ax.add_patch(wedge1)
        
        wedge2 = Wedge((0, 0), radius, 114.3, 154.3, facecolor='#FF9800', alpha=0.3, edgecolor='none')
        self.ax.add_patch(wedge2)
        
        wedge3 = Wedge((0, 0), radius, 154.3, 180, facecolor='#f44336', alpha=0.3, edgecolor='none')
        self.ax.add_patch(wedge3)

        # Contour
        theta = np.linspace(np.radians(180), np.radians(0), 300)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        self.ax.plot(x, y, 'k-', lw=4)

        # Graduations principales
        ticks = np.arange(-20, 51, 10)
        angles = np.linspace(np.pi, 0, len(ticks))
        
        for t, a in zip(ticks, angles):
            x_inner = 0.85 * np.cos(a)
            y_inner = 0.85 * np.sin(a)
            x_outer = 1.0 * np.cos(a)
            y_outer = 1.0 * np.sin(a)
            self.ax.plot([x_inner, x_outer], [y_inner, y_outer], 'k-', lw=2)
            
            xtick = 1.15 * np.cos(a)
            ytick = 1.15 * np.sin(a)
            self.ax.text(xtick, ytick, f"{int(t)}",
                        ha='center', va='center',
                        fontsize=11, fontweight='bold')

        # Graduations secondaires
        minor_ticks = np.arange(-20, 51, 5)
        minor_angles = np.linspace(np.pi, 0, len(minor_ticks))
        
        for t, a in zip(minor_ticks, minor_angles):
            if t % 10 != 0:
                x_inner = 0.92 * np.cos(a)
                y_inner = 0.92 * np.sin(a)
                x_outer = 1.0 * np.cos(a)
                y_outer = 1.0 * np.sin(a)
                self.ax.plot([x_inner, x_outer], [y_inner, y_outer], 'k-', lw=1)

        # Aiguille
        value_clamped = np.clip(value, -20, 50)
        angle = np.interp(value_clamped, [-20, 50], [np.pi, 0])

        if value_clamped < 20:
            needle_color = '#4CAF50'
        elif value_clamped < 35:
            needle_color = '#FF9800'
        else:
            needle_color = '#f44336'

        needle_length = 0.85
        needle_width = 0.03
        
        x_tip = needle_length * np.cos(angle)
        y_tip = needle_length * np.sin(angle)
        
        perp_angle = angle + np.pi/2
        x_base1 = needle_width * np.cos(perp_angle)
        y_base1 = needle_width * np.sin(perp_angle)
        x_base2 = needle_width * np.cos(perp_angle + np.pi)
        y_base2 = needle_width * np.sin(perp_angle + np.pi)
        
        needle_triangle = plt.Polygon(
            [(x_tip, y_tip), (x_base1, y_base1), (x_base2, y_base2)],
            color=needle_color, zorder=5
        )
        self.ax.add_patch(needle_triangle)

        # Centre
        centre_circle = plt.Circle((0, 0), 0.08, color='#333', zorder=6)
        self.ax.add_patch(centre_circle)

        # Valeur numérique
        self.ax.text(0, -0.35, f"{int(value_clamped)}", 
                    ha='center', va='center',
                    fontsize=24, fontweight='bold', color='#333')
        
        self.ax.text(0, -0.55, "unités", 
                    ha='center', va='center',
                    fontsize=12, color='#666')

        self.ax.set_xlim(-1.3, 1.3)
        self.ax.set_ylim(-0.7, 1.3)
        self.ax.axis('off')
        self.ax.set_aspect('equal')

        self.fig.tight_layout()
        self.canvas.draw()

    def update_displays(self):
        try:
            value = int(self.entry.get())
            if value < -20 or value > 50:
                messagebox.showwarning("Attention", 
                    f"La valeur {value} est hors limites.\nPlage valide: -20 à 50")
                return
            
            self.current_value = value
            self.draw_gauge(value)
            self.draw_temperature_bar(value)
            
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un entier valide entre -20 et 50.")

    def reset_displays(self):
        self.entry.delete(0, tk.END)
        self.current_value = 0
        self.draw_gauge(0)
        self.draw_temperature_bar(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = CombinedGaugeApp(root)
    root.mainloop()