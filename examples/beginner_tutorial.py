"""
BEGINNER TUTORIAL: How to Use Business Frameworks
For MBA students with no tech background

This tutorial shows EXACTLY what data you need and where it comes from.
"""

from business_frameworks import PortersFiveForces, SWOT, BCGMatrix

print("="*80)
print("BEGINNER TUTORIAL: Analyzing 'Joe's Coffee Shop'")
print("="*80)
print("\nScenario: You're consulting for a local coffee shop chain (5 locations)")
print("Let's analyze their business using strategic frameworks.\n")

# ===========================================================================
# STEP 1: PORTER'S FIVE FORCES
# ===========================================================================
print("\n" + "="*80)
print("STEP 1: PORTER'S FIVE FORCES - Understanding the Industry")
print("="*80)

print("""
What You Need to Know BEFORE Using the Library:
-----------------------------------------------
1. Who are the major competitors? (Starbucks, Dunkin', local shops)
2. How intense is competition? (Very intense in coffee industry)
3. Can customers easily switch? (Yes - low switching costs)
4. Are suppliers powerful? (Moderate - coffee bean suppliers)
5. Are there substitutes? (Tea, energy drinks, home brewing)

Based on Your Research:
- Competitive Rivalry: 5/5 (many competitors, price wars)
- Supplier Power: 3/5 (moderate - some dependency on suppliers)
- Buyer Power: 4/5 (customers can easily go elsewhere)
- Threat of Substitutes: 3/5 (tea, energy drinks available)
- Threat of New Entrants: 2/5 (hard to compete with Starbucks)
""")

# Now INPUT your analysis into the library:
porters = PortersFiveForces(
    industry="Local Coffee Shop Market",
    competitive_rivalry=5,      # ← From your judgment
    supplier_power=3,           # ← From your research
    buyer_power=4,              # ← From your analysis
    threat_of_substitutes=3,    # ← From market study
    threat_of_new_entrants=2    # ← From barrier analysis
)

# Add supporting details (optional but recommended):
porters.add_factor("Competitive Rivalry", "Starbucks on every corner, price-sensitive market")
porters.add_factor("Buyer Power", "Customers have many choices within 1 mile")

# Generate insights:
porters.generate_report()

print("\n📊 WHAT THE LIBRARY DID FOR YOU:")
print("   ✓ Calculated overall attractiveness (3.4/5 = Challenging)")
print("   ✓ Identified this as 'Challenging - High competitive pressure'")
print("   ✓ Would create a radar chart if you called .plot()")

# ===========================================================================
# STEP 2: SWOT ANALYSIS
# ===========================================================================
print("\n" + "="*80)
print("STEP 2: SWOT ANALYSIS - Analyzing Joe's Coffee Shop Specifically")
print("="*80)

print("""
What You Need to Find Out BEFORE Using the Library:
---------------------------------------------------
1. Visit the coffee shop or read case study
2. Interview the owner or analyze financials
3. Look at reviews and customer feedback
4. Research local market conditions

From Your Investigation, You Identified:

STRENGTHS (Internal, Positive):
- Great location near university
- Friendly staff with low turnover
- Unique locally-sourced beans

WEAKNESSES (Internal, Negative):
- Small menu compared to Starbucks
- No mobile app for ordering
- Limited seating space

OPPORTUNITIES (External, Positive):
- University enrollment growing 10%/year
- Trend toward local/sustainable products
- Potential catering to offices nearby

THREATS (External, Negative):
- New Starbucks opening next block
- Rising rent costs
- Coffee bean price inflation
""")

# Now INPUT your findings into the library:
swot = SWOT(
    company="Joe's Coffee Shop",
    strengths=[
        "Prime location near university campus",
        "Experienced, loyal staff",
        "Unique locally-sourced coffee beans",
        "Strong community reputation"
    ],
    weaknesses=[
        "Limited menu compared to chains",
        "No mobile ordering app",
        "Small seating capacity",
        "Lower marketing budget"
    ],
    opportunities=[
        "University enrollment growing 10%",
        "Consumer trend toward local businesses",
        "Office catering untapped",
        "Potential second location"
    ],
    threats=[
        "Starbucks opening nearby",
        "Rising commercial rent",
        "Coffee bean price volatility",
        "Economic recession risk"
    ]
)

swot.generate_report()

print("\n📊 WHAT THE LIBRARY DID FOR YOU:")
print("   ✓ Organized your findings into proper SWOT format")
print("   ✓ Would create a color-coded 2x2 matrix if you called .plot()")
print("   ✓ Ready for PowerPoint presentation")

# ===========================================================================
# STEP 3: BCG MATRIX - Product Portfolio
# ===========================================================================
print("\n" + "="*80)
print("STEP 3: BCG MATRIX - Which Products to Focus On?")
print("="*80)

print("""
What Data You Need to Collect:
------------------------------
For EACH product, you need 3 numbers:

1. MARKET SHARE: Your sales ÷ Competitor's sales
   Example: Joe's espresso drinks = $500k/year
           Starbucks (leader) = $2M/year in area
           Relative Share = 500k ÷ 2M = 0.25

2. MARKET GROWTH: How fast is this product category growing?
   Look up: Industry reports, news articles
   Example: Specialty coffee growing 15%/year

3. REVENUE: How much does this product make?
   Get from: Sales data, financial statements
   Example: Espresso drinks = $500k/year revenue

Your Research Findings:
----------------------
Product          Market Share  Market Growth  Revenue
Espresso Drinks     0.25          15%         $500k
Drip Coffee         0.40           3%         $300k
Pastries            0.20          10%         $150k
Merchandise         0.10           2%          $50k
""")

# Now INPUT your data into the library:
bcg = BCGMatrix("Joe's Coffee Shop")

bcg.add_business_unit(
    name="Espresso Drinks",
    market_share=0.25,    # ← From calculation: 500k ÷ 2M
    market_growth=15,     # ← From industry report
    revenue=500          # ← From sales data
)

bcg.add_business_unit(
    name="Drip Coffee",
    market_share=0.40,    # ← Higher share, mature product
    market_growth=3,      # ← Slow growth
    revenue=300
)

bcg.add_business_unit(
    name="Pastries",
    market_share=0.20,    # ← Lower share
    market_growth=10,     # ← Growing market
    revenue=150
)

bcg.add_business_unit(
    name="Merchandise",
    market_share=0.10,    # ← Low share
    market_growth=2,      # ← Low growth
    revenue=50
)

bcg.generate_recommendations()

print("\n📊 WHAT THE LIBRARY DID FOR YOU:")
print("   ✓ Categorized products into Stars/Cash Cows/Question Marks/Dogs")
print("   ✓ Recommended: Invest in Espresso Drinks, Milk Drip Coffee cash")
print("   ✓ Suggested: Consider dropping Merchandise (Dog)")
print("   ✓ Would create bubble chart if you called .plot()")

# ===========================================================================
# SUMMARY
# ===========================================================================
print("\n" + "="*80)
print("SUMMARY: What You Learned")
print("="*80)

print("""
KEY TAKEAWAY:
-------------
The library is a TOOL, not a magic answer generator!

YOU provide:        Library provides:
-------------       -----------------
✓ Research          ✓ Organization
✓ Data              ✓ Calculations  
✓ Judgment          ✓ Visualizations
✓ Analysis          ✓ Reports
✓ Industry knowledge ✓ Professional format

Think of it like Excel:
- Excel doesn't know your company's revenue
- YOU input the data, Excel creates charts
- Same concept here!

How to Use for Your MBA Project:
1. Pick a company (from case study or real life)
2. Do your research (read, interview, analyze)
3. Fill in the frameworks with YOUR findings
4. Generate professional reports and charts
5. Present to class/professors

Questions MBA Students Often Ask:
---------------------------------
Q: "Where do I get the numbers?"
A: Case studies, company reports, industry databases, your professor

Q: "What if I don't know the exact market share?"
A: Estimate! Use your best judgment. That's part of business analysis.

Q: "Do I need to use all 5 frameworks?"
A: No! Use what's relevant. Porter's and SWOT are most common.

Q: "Can I change numbers later?"
A: Yes! Just re-run the code with new inputs.

Next Steps:
-----------
1. Pick a company you're interested in
2. Read about them for 30 minutes
3. Try filling in ONE framework
4. See how easy it is!

Try it yourself:
python examples/beginner_tutorial.py
""")

print("\n" + "="*80)
print("End of Tutorial - Happy Analyzing! 📊")
print("="*80)
