"""
Optional module: demonstrates SQL skills on top of the same dataset.
Uses Python's built-in sqlite3 - no separate database install needed.

Run from the project root: python scripts/sql_analysis.py
"""
import sqlite3
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from data.market_data import (
    PLAYER_PROFILES,
    MARKET_SHARE_GOV_JAN2026,
    DARK_STORES_BY_PLAYER_MAR2026,
)

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "qcommerce.db")


def build_database():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE players (
            name TEXT PRIMARY KEY,
            parent TEXT,
            model TEXT,
            positioning TEXT,
            target_demo TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE market_share (
            player TEXT,
            share_pct REAL,
            snapshot_date TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE dark_stores (
            player TEXT,
            store_count INTEGER,
            snapshot_date TEXT
        )
    """)

    for name, profile in PLAYER_PROFILES.items():
        cur.execute(
            "INSERT INTO players VALUES (?, ?, ?, ?, ?)",
            (name, profile["parent"], profile["model"], profile["positioning"], profile["target_demo"]),
        )

    for player, share in MARKET_SHARE_GOV_JAN2026.items():
        cur.execute("INSERT INTO market_share VALUES (?, ?, ?)", (player, share, "2026-01"))

    for player, count in DARK_STORES_BY_PLAYER_MAR2026.items():
        cur.execute("INSERT INTO dark_stores VALUES (?, ?, ?)", (player, count, "2026-03"))

    conn.commit()
    return conn


def run_example_queries(conn):
    print("\n--- Market share ranked ---")
    for row in conn.execute("SELECT player, share_pct FROM market_share ORDER BY share_pct DESC"):
        print(f"  {row[0]:<32} {row[1]:>5.1f}%")

    print("\n--- Dark stores per player, with GOV share for context ---")
    query = """
        SELECT d.player, d.store_count, m.share_pct
        FROM dark_stores d
        LEFT JOIN market_share m ON d.player = m.player
        ORDER BY d.store_count DESC
    """
    for row in conn.execute(query):
        share = f"{row[2]:.0f}%" if row[2] is not None else "n/a"
        print(f"  {row[0]:<20} {row[1]:>6,} stores   GOV share: {share}")

    print("\n--- Revenue-per-store proxy (share% / store_count), highest first ---")
    query = """
        SELECT d.player,
               d.store_count,
               m.share_pct,
               ROUND(m.share_pct * 1.0 / d.store_count, 4) AS share_per_store
        FROM dark_stores d
        JOIN market_share m ON d.player = m.player
        ORDER BY share_per_store DESC
    """
    for row in conn.execute(query):
        print(f"  {row[0]:<20} share/store index: {row[3]}")


if __name__ == "__main__":
    conn = build_database()
    run_example_queries(conn)
    conn.close()
    print(f"\nSQLite DB written to {os.path.abspath(DB_PATH)}")