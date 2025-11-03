"""
Real-World Case Study: "CoffeeChain Inc." Strategy Analysis

A fictional but realistic coffee chain company facing strategic decisions.
This example demonstrates how to use all frameworks together for comprehensive analysis.
"""

from business_frameworks import (
    PortersFiveForces, 
    SWOT, 
    PESTEL, 
    BCGMatrix, 
    AnsoffMatrix
)

print("="*80)
print("COMPREHENSIVE STRATEGY ANALYSIS: CoffeeChain Inc.")
print("="*80)
print("\nScenario: CoffeeChain is a mid-sized coffee chain with 200 stores")
print("Planning expansion and evaluating their product portfolio.\n")

# ============================================================================
# 1. PORTER'S FIVE FORCES - Industry Attractiveness
# ============================================================================
print("\n" + "="*80)
print("1. INDUSTRY ANALYSIS - Porter's Five Forces")
print("="*80)

porters = PortersFiveForces(
    industry="Specialty Coffee Retail",
    competitive_rivalry=5,        # Very intense (Starbucks, Dunkin', local shops)
    supplier_power=3,             # Moderate (coffee bean suppliers)
    buyer_power=4,                # High (customers can easily switch)
    threat_of_substitutes=3,      # Moderate (tea, energy drinks, home brewing)
    threat_of_new_entrants=2      # Low (high capital requirements, brand loyalty)
)

porters.add_factor("Competitive Rivalry", 
                   "Dominated by Starbucks; many local independent shops")
porters.add_factor("Buyer Power", 
                   "Low switching costs; customers price-sensitive")
porters.add_factor("Supplier Power", 
                   "Global coffee supply but quality beans limited")

porters.generate_report()
# porters.plot()  # Uncomment to see visualization

# ============================================================================
# 2. PESTEL ANALYSIS - Macro Environment
# ============================================================================
print("\n" + "="*80)
print("2. MACRO-ENVIRONMENTAL ANALYSIS - PESTEL")
print("="*80)

pestel = PESTEL(industry="Specialty Coffee")

# Political
pestel.add_factor("Political", "Trade policies on coffee imports", impact=4, likelihood=3)
pestel.add_factor("Political", "Labor regulations and minimum wage", impact=5, likelihood=4)

# Economic
pestel.add_factor("Economic", "Economic recession risk", impact=5, likelihood=3)
pestel.add_factor("Economic", "Rising coffee bean prices", impact=4, likelihood=4)

# Social
pestel.add_factor("Social", "Health-conscious consumers", impact=4, likelihood=5)
pestel.add_factor("Social", "Work-from-home trend", impact=4, likelihood=4)

# Technological
pestel.add_factor("Technological", "Mobile ordering apps", impact=5, likelihood=5)
pestel.add_factor("Technological", "Automation in stores", impact=3, likelihood=3)

# Environmental
pestel.add_factor("Environmental", "Sustainability pressure", impact=4, likelihood=5)
pestel.add_factor("Environmental", "Climate change affecting coffee supply", impact=5, likelihood=4)

# Legal
pestel.add_factor("Legal", "Food safety regulations", impact=4, likelihood=4)

pestel.generate_report()
# pestel.plot_impact_matrix()  # Uncomment to see visualization

# ============================================================================
# 3. SWOT ANALYSIS - Internal & External Factors
# ============================================================================
print("\n" + "="*80)
print("3. COMPANY ANALYSIS - SWOT")
print("="*80)

swot = SWOT(
    company="CoffeeChain Inc.",
    strengths=[
        "Strong local brand recognition in 5 states",
        "High-quality ethically sourced coffee",
        "Loyal customer base with rewards program",
        "Experienced management team",
        "Efficient supply chain operations"
    ],
    weaknesses=[
        "Limited geographic presence (only 5 states)",
        "Smaller scale vs. Starbucks (higher costs)",
        "Outdated POS systems in some stores",
        "Limited brand awareness nationally",
        "Dependence on foot traffic"
    ],
    opportunities=[
        "Expand to 10 new cities",
        "Launch mobile app for ordering",
        "Introduce healthy food options",
        "Partner with offices for corporate accounts",
        "Develop premium coffee bean retail line"
    ],
    threats=[
        "Starbucks opening stores nearby",
        "Rising real estate costs",
        "Economic downturn reducing discretionary spending",
        "Coffee bean price volatility",
        "Changing consumer preferences"
    ]
)

swot.generate_report()
# swot.plot()  # Uncomment to see visualization

# ============================================================================
# 4. BCG MATRIX - Portfolio Analysis
# ============================================================================
print("\n" + "="*80)
print("4. PRODUCT PORTFOLIO ANALYSIS - BCG Matrix")
print("="*80)

bcg = BCGMatrix("CoffeeChain Inc.")

# Add business units/product lines
bcg.add_business_unit(
    name="Espresso Drinks",
    market_share=0.8,      # Below market leader
    market_growth=15,       # High growth
    revenue=120            # $120M revenue
)

bcg.add_business_unit(
    name="Drip Coffee",
    market_share=1.5,      # Market leader in segment
    market_growth=5,        # Low growth (mature)
    revenue=80             # $80M revenue
)

bcg.add_business_unit(
    name="Food Items",
    market_share=0.5,      # Low share
    market_growth=20,       # High growth
    revenue=40             # $40M revenue
)

bcg.add_business_unit(
    name="Packaged Coffee Beans",
    market_share=1.2,      # Market leader
    market_growth=8,        # Low growth
    revenue=30             # $30M revenue
)

bcg.add_business_unit(
    name="Merchandise",
    market_share=0.3,      # Low share
    market_growth=3,        # Low growth
    revenue=10             # $10M revenue
)

bcg.generate_recommendations()
# bcg.plot()  # Uncomment to see visualization

# ============================================================================
# 5. ANSOFF MATRIX - Growth Strategy
# ============================================================================
print("\n" + "="*80)
print("5. GROWTH STRATEGY ANALYSIS - Ansoff Matrix")
print("="*80)

ansoff = AnsoffMatrix("CoffeeChain Inc.", current_strategy="Market Penetration")

# Market Penetration (Current focus)
ansoff.add_strategy("Market Penetration", 
    initiatives=[
        "Launch loyalty app with personalized offers",
        "Increase marketing in existing cities",
        "Extend store hours to capture more traffic"
    ],
    priority=1
)

# Market Development
ansoff.add_strategy("Market Development",
    initiatives=[
        "Expand to 10 new cities in neighboring states",
        "Open airport and highway rest stop locations",
        "Target college campuses"
    ],
    priority=2
)

# Product Development
ansoff.add_strategy("Product Development",
    initiatives=[
        "Launch healthy food line (salads, protein bowls)",
        "Introduce premium cold brew line",
        "Develop coffee subscription service"
    ],
    priority=3
)

# Diversification
ansoff.add_strategy("Diversification",
    initiatives=[
        "Consider coffee roasting facility for B2B",
        "Explore franchising model",
        "Evaluate coffee equipment retail"
    ],
    priority=4
)

ansoff.generate_report()
# ansoff.plot()  # Uncomment to see visualization

# ============================================================================
# INTEGRATED RECOMMENDATIONS
# ============================================================================
print("\n" + "="*80)
print("INTEGRATED STRATEGIC RECOMMENDATIONS")
print("="*80)
print("""
Based on comprehensive analysis across all frameworks:

IMMEDIATE PRIORITIES (Next 6 months):
1. Market Penetration: Launch mobile ordering app (addresses SWOT weakness)
2. Invest in Espresso Drinks (BCG Question Mark → Star potential)
3. Milk Cash Cows: Use Drip Coffee profits to fund growth initiatives

SHORT-TERM (6-12 months):
1. Market Development: Expand to 5 new cities where competition is moderate
2. Product Development: Launch healthy food line (PESTEL opportunity)
3. Address SWOT weaknesses: Upgrade POS systems across all stores

MEDIUM-TERM (1-2 years):
1. Further Market Development: 10 additional cities
2. Divest or improve Merchandise (BCG Dog)
3. Build sustainability story (PESTEL environmental factor)

STRATEGIC FOCUS:
- Porter's analysis shows challenging industry → need differentiation
- SWOT shows quality is strength → maintain and promote
- BCG shows balanced portfolio → continue strategic investments
- Ansoff recommends Market Development → align with growth goals
- PESTEL highlights sustainability → incorporate into brand story

AVOID:
- Aggressive diversification (high risk, limited resources)
- Price wars with Starbucks (would hurt margins)
- Over-expansion (maintain quality control)
""")

print("\n" + "="*80)
print("Analysis Complete! Use these insights for board presentation.")
print("="*80)
