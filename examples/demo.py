"""StrategyKit Demo Examples"""

from strategykit import PortersFiveForces, SWOT, PESTEL


def demo_porters():
    """Demo Porter's Five Forces"""
    print("\n" + "="*60)
    print("DEMO: Porter's Five Forces Analysis")
    print("="*60)
    
    pf = PortersFiveForces(
        industry="Smartphone Manufacturing",
        competitive_rivalry=5,
        supplier_power=3,
        buyer_power=4,
        threat_of_substitutes=2,
        threat_of_new_entrants=2
    )
    
    pf.add_factor("Competitive Rivalry", "Apple, Samsung, Google compete intensely")
    pf.add_factor("Supplier Power", "Limited chip suppliers (TSMC, Qualcomm)")
    
    pf.generate_report()
    pf.plot()


def demo_swot():
    """Demo SWOT Analysis"""
    print("\n" + "="*60)
    print("DEMO: SWOT Analysis")
    print("="*60)
    
    swot = SWOT(
        company="TechStartup Inc.",
        strengths=["Strong technical team", "Innovative product", "Low burn rate"],
        weaknesses=["Limited brand recognition", "Small market share"],
        opportunities=["Growing market demand", "Strategic partnerships"],
        threats=["Well-funded competitors", "Regulatory changes"]
    )
    
    swot.generate_report()
    swot.plot()


def demo_pestel():
    """Demo PESTEL Analysis"""
    print("\n" + "="*60)
    print("DEMO: PESTEL Analysis")
    print("="*60)
    
    pestel = PESTEL(industry="E-commerce")
    pestel.add_factor("Political", "Trade policy changes", 4, 3)
    pestel.add_factor("Economic", "GDP growth rate", 5, 4)
    pestel.add_factor("Social", "Digital adoption trend", 5, 5)
    pestel.add_factor("Technological", "AI advancements", 5, 4)
    pestel.add_factor("Environmental", "Sustainability pressure", 3, 4)
    pestel.add_factor("Legal", "Data privacy laws", 4, 5)
    
    pestel.generate_report()
    pestel.plot_impact_matrix()


if __name__ == "__main__":
    demo_porters()
    demo_swot()
    demo_pestel()
