import numpy as np
import matplotlib.pyplot as plt

temps = [1, 2, 3, 4, 6, 7, 9]
concentration = [5.5, 7.2, 11.8, 13.6, 19.1, 21.7, 29.4]

fig, ax = plt.subplots()
ax.scatter(temps, concentration, marker="o", color="blue", label="mesures")
ax.set_xlabel("Temps (h)")
ax.set_ylabel("Concentration (mg/L)")
ax.set_title("Concentration de produit en fonction du temps")

x = np.linspace(min(temps), max(temps), 50)
y = 2 + 3 * x

ax.plot(x, y, color="green", ls="--", label="modèle")

ax.grid()
ax.set_xlim(0, 10)
ax.set_ylim(0, 35)

ax.legend(loc="upper left")
fig.savefig("concentration.png", bbox_inches="tight", dpi=200)
