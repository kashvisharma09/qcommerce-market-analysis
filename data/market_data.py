"""
India Quick-Commerce Market — Data Module
==========================================
All figures below are drawn from public analyst reports and news coverage
(sources cited inline). Where estimates diverge between sources, all
variants are kept rather than silently picking one, since the spread
itself is analytically interesting (see README).

Last verified: September 2026.
"""

# ---------------------------------------------------------------------------
# Market size estimates (US$ billions), by data provider.
# Providers disagree because they scope the market differently
# (pure quick-commerce grocery vs. broader "instant delivery" definitions).
# ---------------------------------------------------------------------------
MARKET_SIZE_ESTIMATES = {
    "consensus": {
        "source": "IMARC Group / ResearchAndMarkets / Statista",
        "url_notes": "imarcgroup.com; globenewswire.com (Apr 2026); statista.com",
        "data": {2020: 0.91, 2024: 5.48, 2025: 5.26, 2026: 6.5, 2029: 12.97, 2031: 10.20},
    },
    "conservative": {
        "source": "Mordor Intelligence",
        "url_notes": "mordorintelligence.com (Aug 2026)",
        "data": {2020: 0.91, 2024: 5.48, 2025: 3.65, 2026: 3.65, 2031: 6.64},
    },
    "bull_case": {
        "source": "MarkNtel Advisors",
        "url_notes": "marknteladvisors.com",
        "data": {2020: 0.91, 2024: 5.48, 2025: 5.6, 2026: 5.8, 2032: 87.5},
    },
}

CAGR_ESTIMATES = {
    "2020_2024_historical": 71.2,
    "2025_2029_researchandmarkets": 17.6,
    "2026_2034_imarc": 42.02,
    "2026_2031_statista": 12.82,
    "2026_2032_markntel": 56.9,
    "2026_yoy_equirus": 40.0,
}

DARK_STORES_COMBINED = {
    "2025-05": 3405,
    "2026-05": 5026,
}

DARK_STORES_BY_PLAYER_MAR2026 = {
    "Blinkit": 1954,
    "Zepto": 1089,
    "Swiggy Instamart": 1038,
}

MARKET_SHARE_GOV_JAN2026 = {
    "Blinkit": 46,
    "Swiggy Instamart": 24,
    "Zepto": 22,
    "BigBasket (BB Now)": 6,
    "Amazon Now / Flipkart Minutes": 2,
}

PLAYER_PROFILES = {
    "Blinkit": {
        "parent": "Eternal Ltd (formerly Zomato)",
        "model": "Inventory-led, company-operated and franchise dark stores",
        "positioning": "Scale leader; land-grab city expansion; first to reach adjusted EBITDA profitability",
        "target_demo": "Broad urban households",
        "2026_notes": "Q4 FY26 profitable on adjusted EBITDA; 2243 stores; pivoting toward private label to protect margins",
    },
    "Zepto": {
        "parent": "Kiranakart Technologies (independent, backed by Y Combinator, Lightspeed, CalPERS)",
        "model": "Consignment or COFO (company-owned, franchise-operated) inventory model",
        "positioning": "Youth-first brand; deep-not-wide city strategy; filed for IPO in 2026",
        "target_demo": "Gen Z and younger millennials, 18 to 34",
        "2026_notes": "1139 dark stores across 66 cities; about 48M annual transacting users; FY26 NRV Rs 24816 Cr",
    },
    "Swiggy Instamart": {
        "parent": "Swiggy Ltd (Bundl Technologies)",
        "model": "Leverages existing Swiggy delivery fleet and logistics network",
        "positioning": "Piggybacks on food-delivery infrastructure; contributes about 40 percent of Swiggy's revenue",
        "target_demo": "Meal-oriented families; cross-promoted from Swiggy food delivery base",
        "2026_notes": "Q4 FY25 GOV up 101 percent YoY to Rs 4670 Cr; adjusted EBITDA loss widened to Rs 840 Cr while adding 316 stores in one quarter",
    },
    "BigBasket (BB Now)": {
        "parent": "Tata Group",
        "model": "Hybrid, leans on Tata's grocery sourcing and supply chain",
        "positioning": "Trailing scale player; sourcing and supply-chain advantage via Tata ecosystem",
        "target_demo": "Value-conscious grocery shoppers, existing BigBasket user base",
        "2026_notes": "5 to 7 percent market share; scaling more cautiously than the top 3",
    },
    "Amazon Now / Flipkart Minutes": {
        "parent": "Amazon / Flipkart (Walmart)",
        "model": "New entrants leveraging existing e-commerce logistics and capital",
        "positioning": "Emerging challengers; 500 plus dark stores each as of mid-2026",
        "target_demo": "Existing Amazon and Flipkart customer base cross-sold into quick delivery",
        "2026_notes": "Scaling fast enough to squeeze pure-play startups; watch for consolidation pressure on smaller players",
    },
}

KEY_TRENDS = [
    {
        "trend": "Non-grocery category expansion",
        "detail": "Platforms are widening assortment beyond groceries into pharmacy, beauty, and electronics to raise average order value and improve store-level contribution margins.",
        "source": "marknteladvisors.com; founderpin.com",
    },
    {
        "trend": "Dark store consolidation and Tier-2/3 push",
        "detail": "Combined dark store count grew 48 percent in twelve months (3405 to 5026), with expansion increasingly targeting Tier-2/3 cities as metro density saturates.",
        "source": "Equirus report via newkerala.com",
    },
    {
        "trend": "Private label as margin strategy",
        "detail": "Blinkit is pivoting toward inventory-led operations specifically to support private-label expansion, since GOV growth alone has not translated into durable profitability for the sector.",
        "source": "founderpin.com",
    },
    {
        "trend": "Regulatory scrutiny intensifying",
        "detail": "India's government ordered Blinkit, Zepto, and Swiggy to stop marketing 10-minute delivery after rider-safety concerns; distributor associations have also petitioned antitrust regulators over alleged predatory pricing.",
        "source": "Reuters (Jan 2026), cited by quashbugs.com",
    },
    {
        "trend": "Profitability bifurcation",
        "detail": "Bernstein estimates roughly 3600 of the top 3800 metro dark stores are profitable, but Tier-2 stores still bleed cash, meaning aggregate sector growth masks a widening gap between winners and laggards at the unit-economics level.",
        "source": "Bernstein, cited by startupfeed.in",
    },
]

if __name__ == "__main__":
    print("Market data module loaded successfully.")
    print(f"Player profiles: {list(PLAYER_PROFILES.keys())}")