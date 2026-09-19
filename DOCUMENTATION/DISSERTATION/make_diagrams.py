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


def fig_3_2_verification_pattern():
    """The one pending -> verified/cleared -> released pattern reused for
    sale clearance, signup verification, movement permits and outbreak
    broadcast - confirmed by live testing in Chapter 4, not asserted."""
    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 4.2)
    ax.axis("off")

    stages = ["ACTION\nCREATED", "PENDING\nVERIFICATION", "AUTHORITY\nREVIEW"]
    x = 0.4
    for text in stages:
        box(ax, x, 2.4, 2.4, 1.1, text, ORANGE, fontsize=9)
        arrow(ax, x + 2.4, 2.95, x + 2.9, 2.95)
        x += 3.0

    box(ax, x, 2.4, 2.3, 1.1, "RELEASED\nvisible / effective", GREEN, fontsize=9)
    arrow(ax, x + 1.15, 2.4, x + 1.15, 1.3)
    box(ax, x - 3.0, 0.3, 2.3, 1.0, "REJECTED\nstays hidden", "#BE4141", fontsize=9)
    arrow(ax, x - 0.6, 1.3, x - 1.85, 1.3)

    ax.text(5.5, 3.85,
             "Reused for: sale clearance · new-account signup · movement permits · outbreak broadcast",
             ha="center", fontsize=9, style="italic")
    ax.set_title("Figure 3.2: The Shared Verification-Gate State Pattern", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig_3_2_verification_pattern.png"), dpi=200)
    plt.close(fig)


def fig_3_3_entity_relationship():
    """Simplified ERD - the entities and relationships already described in
    ch3.py's Table 3.2, drawn rather than only tabulated."""
    fig, ax = plt.subplots(figsize=(11, 7.8))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7.8)
    ax.axis("off")

    box(ax, 4.3, 6.5, 2.4, 0.8, "users\n(role column)", PURPLE, fontsize=9)

    entities = [
        (0.3, 5.0, "animals"), (0.3, 3.6, "health_events /\nweight_history"),
        (0.3, 2.2, "compliance_cases /\ncompliance_actions"),
        (3.0, 5.0, "marketplace_\nlistings"), (3.0, 3.6, "sale_clearances /\nmovement_permits"),
        (3.0, 2.2, "bids / orders"),
        (5.7, 5.0, "valuation_\ncertificates"), (5.7, 3.6, "certificate_\nlookups"),
        (5.7, 2.2, "outbreaks"),
        (8.4, 5.0, "cooperatives /\nmembers"), (8.4, 3.6, "feed_types /\nfeeding_plans"),
        (8.4, 2.2, "conversations /\nmessages"),
    ]
    for x, y, label in entities:
        box(ax, x, y, 2.2, 0.9, label, BLUE, fontsize=8)
        arrow(ax, x + 1.1, y + 0.9, 5.4, 6.5)

    ax.set_title("Figure 3.3: Simplified Entity-Relationship Diagram", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "fig_3_3_entity_relationship.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig_3_1_system_block()
    fig_3_2_verification_pattern()
    fig_3_3_entity_relationship()
    print("Saved diagrams to", OUT_DIR)
