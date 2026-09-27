"""
Generates all charts for the India Quick-Commerce market analysis.
Run from the project root: python scripts/build_charts.py
Outputs land in charts/
"""
import sys
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from data.market_data import (
    MARKET_SIZE_ESTIMATES,
    DARK_STORES_COMBINED,
    DARK_STORES_BY_PLAYER_MAR2026,
    MARKET_SHARE_GOV_JAN2026,
)

plt.rcParams["font.family"] = "DejaVu Sans"
NAVY, BLUE, LBLUE, GRAY = "#12234f", "#2b6cb0", "#63b3ed", "#8492a6"
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "charts")
os.makedirs(OUT_DIR, exist_ok=True)


def chart_market_size():
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=200)
    styles = {
        "consensus": (NAVY, "o", "Consensus (IMARC / R&M / Statista)"),
        "conservative": (GRAY, "s", "Conservative (Mordor Intelligence)"),
        "bull_case": (LBLUE, "^", "Bull-case (MarkNtel)"),
    }
    for key, (color, marker, label) in styles.items():
        d = MARKET_SIZE_ESTIMATES[key]["data"]
        years = sorted(d.keys())
        ax.plot(years, [d[y] for y in years], marker=marker, color=color,
                linewidth=2.2, markersize=6, label=label)

    ax.set_title("India Quick-Commerce Market Size: Analyst Estimates Diverge Sharply",
                 fontsize=13, fontweight="bold", color=NAVY, pad=14)
    ax.set_ylabel("Market size (US$ billions)", fontsize=10, color=NAVY)
    ax.set_xlabel("Year", fontsize=10, color=NAVY)
    ax.legend(loc="upper left", fontsize=8.5, frameon=False)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e2e8f0", linewidth=0.8)
    ax.tick_params(colors=NAVY, labelsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "chart1_market_size.png"), facecolor="white")
    plt.close()


def chart_market_share():
    players = list(MARKET_SHARE_GOV_JAN2026.keys())
    share = list(MARKET_SHARE_GOV_JAN2026.values())
    colors = [NAVY, BLUE, LBLUE, GRAY, "#cbd5e0"]

    fig, ax = plt.subplots(figsize=(9, 5), dpi=200)
    bars = ax.bar([p.replace(" ", "\n", 1) for p in players], share, color=colors, width=0.6)
    for b, s in zip(bars, share):
        ax.text(b.get_x() + b.get_width()/2, s + 1, f"{s}%", ha="center",
                 fontsize=11, fontweight="bold", color=NAVY)
    ax.set_title("Market Share by Gross Order Value - Jan 2026", fontsize=13,
                 fontweight="bold", color=NAVY, pad=14)
    ax.set_ylabel("Estimated market share (%)", fontsize=10, color=NAVY)
    ax.set_ylim(0, 55)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e2e8f0", linewidth=0.8)
    ax.tick_params(colors=NAVY, labelsize=9)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "chart2_market_share.png"), facecolor="white")
    plt.close()


def chart_dark_stores():
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.8), dpi=200,
                            gridspec_kw={"width_ratios": [1, 1.3]})

    dates = list(DARK_STORES_COMBINED.keys())
    counts = list(DARK_STORES_COMBINED.values())
    labels = ["May 2025", "May 2026"]
    ax[0].bar(labels, counts, color=[GRAY, NAVY], width=0.5)
    for i, c in enumerate(counts):
        ax[0].text(i, c + 60, f"{c:,}", ha="center", fontweight="bold", color=NAVY, fontsize=10)
    ax[0].set_title("Combined Dark Stores\n(Blinkit + Zepto + Instamart)", fontsize=11,
                     fontweight="bold", color=NAVY)
    ax[0].set_ylim(0, 6000)
    ax[0].spines[["top", "right"]].set_visible(False)
    ax[0].grid(axis="y", color="#e2e8f0", linewidth=0.8)
    ax[0].tick_params(colors=NAVY, labelsize=9)

    players = list(DARK_STORES_BY_PLAYER_MAR2026.keys())
    counts2 = list(DARK_STORES_BY_PLAYER_MAR2026.values())
    bars = ax[1].barh(players, counts2, color=[NAVY, BLUE, LBLUE])
    for b, s in zip(bars, counts2):
        ax[1].text(s + 30, b.get_y() + b.get_height()/2, f"{s:,}", va="center",
                    fontweight="bold", color=NAVY, fontsize=10)
    ax[1].set_title("Dark Store Count by Player\n(March 2026)", fontsize=11,
                     fontweight="bold", color=NAVY)
    ax[1].spines[["top", "right"]].set_visible(False)
    ax[1].grid(axis="x", color="#e2e8f0", linewidth=0.8)
    ax[1].tick_params(colors=NAVY, labelsize=9)
    ax[1].invert_yaxis()

    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, "chart3_dark_stores.png"), facecolor="white")
    plt.close()


if __name__ == "__main__":
    chart_market_size()
    chart_market_share()
    chart_dark_stores()
    print(f"Charts saved to {os.path.abspath(OUT_DIR)}/")