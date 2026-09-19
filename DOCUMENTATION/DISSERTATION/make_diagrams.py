# -*- coding: utf-8 -*-
"""make_diagrams.py - generates Chapter 3's figures as PNGs via matplotlib.

Regeneratable and independent of thesis_builder.py: edit this file, rerun
`python make_diagrams.py`, then rerun `python thesis_builder.py` to pick up
the new images. Content mirrors the verified architecture already described
in chapters/ch3.py (roles, the combined web+mobile client, the Flask API's
nine modules, and the shared database) - not a fresh invention of the
system, a second rendering of the same facts.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

BLUE = "#5299D6"
GREEN = "#2FA05A"
ORANGE = "#E58226"
PURPLE = "#9141B4"
DARK = "#141414"


def box(ax, x, y, w, h, text, color, fontsize=9, textcolor="white"):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
        linewidth=0, facecolor=color,
    ))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
             fontsize=fontsize, color=textcolor, fontweight="bold", wrap=True)


def arrow(ax, x1, y1, x2, y2, color=DARK):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=12,
        linewidth=1.2, color=color,
    ))


def fig_3_1_system_block():
    fig, ax = plt.subplots(figsize=(11, 7.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    roles = ["Farmer", "Veterinarian", "Supplier", "Buyer", "Police", "Institution"]
    for i, r in enumerate(roles):
        y = 6.6 - i * 1.05
        box(ax, 0.3, y, 1.9, 0.7, r, BLUE, fontsize=9)
        arrow(ax, 2.2, y + 0.35, 3.0, 3.75)

    box(ax, 3.0, 3.15, 2.6, 1.2, "Web App  &  Mobile App\n(React/Vite + Expo/RN)\none tailored dashboard\nper role, on either client",
        GREEN, fontsize=8)
    arrow(ax, 5.6, 3.75, 6.4, 3.75)

    box(ax, 6.4, 2.3, 3.0, 2.9,
        "Flask API — 143 routes\n\n"
        "Registry & Compliance\nMarketplace & Clearance\n"
        "Certification & Ledger\nOutbreak Pipeline\n"
        "Cooperatives\nFeed & Trading Tools\nMessenger\nJinda Assistant",
        ORANGE, fontsize=8)
    arrow(ax, 9.4, 3.75, 10.1, 3.75)

    box(ax, 10.1, 3.15, 0.7, 1.2, "My\nSQL", PURPLE, fontsize=8)

    ax.set_title("Figure 3.1: Overall Platform System Block Diagram", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig_3_1_system_block.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig_3_1_system_block()
    print("Saved diagrams to", OUT_DIR)
