"""Quick demo without plots"""

from business_frameworks import PortersFiveForces, SWOT, PESTEL

print("\n" + "="*70)
print("BUSINESS FRAMEWORKS DEMO - Strategic Framework Toolkit for MBA Students")
print("="*70)

# Porter's Five Forces
print("\n1. PORTER'S FIVE FORCES ANALYSIS")
print("-"*70)
pf = PortersFiveForces(
    industry="Smartphone Manufacturing",
    competitive_rivalry=5,
    supplier_power=3,
    buyer_power=4,
    threat_of_substitutes=2,
    threat_of_new_entrants=2
)
pf.add_factor("Competitive Rivalry", "Apple vs Samsung vs Google")
pf.add_factor("Supplier Power", "Limited chip suppliers (TSMC)")
pf.generate_report()

# SWOT Analysis
print("\n2. SWOT ANALYSIS")
print("-"*70)
swot = SWOT(
    company="TechStartup Inc.",
    strengths=["Strong technical team", "Innovative AI product"],
    weaknesses=["Limited brand recognition", "Small marketing budget"],
    opportunities=["Growing AI market", "Enterprise partnerships"],
    threats=["Well-funded competitors", "Economic downturn"]
)
swot.generate_report()

# PESTEL Analysis
print("\n3. PESTEL ANALYSIS")
print("-"*70)
pestel = PESTEL(industry="E-commerce")
pestel.add_factor("Political", "Trade policy uncertainty", 4, 3)
pestel.add_factor("Economic", "GDP growth rate", 5, 4)
pestel.add_factor("Social", "Digital adoption surge", 5, 5)
pestel.add_factor("Technological", "AI/ML advancements", 5, 4)
pestel.add_factor("Environmental", "Sustainability pressure", 3, 4)
pestel.add_factor("Legal", "Data privacy regulations", 4, 5)
pestel.generate_report()

print("\n" + "="*70)
print("Demo complete! Check examples/demo.py for visualization examples.")
print("="*70)
