"""
Pre-built Templates and Real Company Examples

Makes it MUCH easier for users - they can start with real examples
and modify them instead of starting from scratch.
"""

from typing import Dict, List
from business_frameworks import PortersFiveForces, SWOT, BCGMatrix, PESTEL, AnsoffMatrix


class IndustryTemplates:
    """Pre-configured templates for common industries."""
    
    @staticmethod
    def get_industry_template(industry: str) -> Dict:
        """
        Get pre-configured Porter's Five Forces for common industries.
        
        Args:
            industry: One of 'tech', 'retail', 'food', 'healthcare', 'finance'
        
        Returns:
            Dictionary with typical ratings for that industry
        
        Example:
            >>> template = IndustryTemplates.get_industry_template('tech')
            >>> porters = PortersFiveForces(**template)
        """
        templates = {
            'tech': {
                'industry': 'Technology/Software',
                'competitive_rivalry': 5,
                'supplier_power': 2,
                'buyer_power': 4,
                'threat_of_substitutes': 4,
                'threat_of_new_entrants': 3
            },
            'retail': {
                'industry': 'Retail/E-commerce',
                'competitive_rivalry': 5,
                'supplier_power': 3,
                'buyer_power': 5,
                'threat_of_substitutes': 4,
                'threat_of_new_entrants': 3
            },
            'food': {
                'industry': 'Food & Beverage',
                'competitive_rivalry': 5,
                'supplier_power': 3,
                'buyer_power': 4,
                'threat_of_substitutes': 3,
                'threat_of_new_entrants': 2
            },
            'healthcare': {
                'industry': 'Healthcare/Pharma',
                'competitive_rivalry': 4,
                'supplier_power': 2,
                'buyer_power': 3,
                'threat_of_substitutes': 2,
                'threat_of_new_entrants': 1
            },
            'finance': {
                'industry': 'Financial Services',
                'competitive_rivalry': 4,
                'supplier_power': 2,
                'buyer_power': 4,
                'threat_of_substitutes': 3,
                'threat_of_new_entrants': 2
            }
        }
        
        if industry.lower() not in templates:
            raise ValueError(f"Unknown industry. Choose from: {list(templates.keys())}")
        
        return templates[industry.lower()]


class CompanyExamples:
    """Real company examples that users can use as starting points."""
    
    @staticmethod
    def starbucks_swot() -> SWOT:
        """Pre-built SWOT analysis for Starbucks (educational example)."""
        return SWOT(
            company="Starbucks",
            strengths=[
                "Strong global brand recognition",
                "Premium product positioning",
                "Extensive store network (30,000+ locations)",
                "Mobile app and loyalty program",
                "Ethical sourcing practices",
                "Innovation in products"
            ],
            weaknesses=[
                "High prices compared to competitors",
                "Dependence on US market",
                "Labor issues and unionization",
                "Limited product diversification",
                "Complex menu can slow service"
            ],
            opportunities=[
                "Expansion in emerging markets (China, India)",
                "Health-conscious product lines",
                "Digital ordering and delivery growth",
                "Coffee subscription services",
                "Strategic partnerships (Nestle)"
            ],
            threats=[
                "Intense competition (Dunkin', local shops)",
                "Coffee bean price volatility",
                "Economic downturns affecting discretionary spending",
                "Changing consumer preferences",
                "Negative publicity around labor practices"
            ]
        )
    
    @staticmethod
    def apple_swot() -> SWOT:
        """Pre-built SWOT analysis for Apple (educational example)."""
        return SWOT(
            company="Apple Inc.",
            strengths=[
                "World's most valuable brand",
                "Loyal customer ecosystem",
                "Premium pricing power",
                "Innovation leadership (iPhone, Mac, iPad)",
                "Strong financial position (cash reserves)",
                "Vertical integration and control"
            ],
            weaknesses=[
                "High product prices limit market share",
                "Dependence on iPhone (50%+ of revenue)",
                "Limited customization vs Android",
                "Closed ecosystem",
                "Manufacturing concentrated in China"
            ],
            opportunities=[
                "Services growth (Apple TV+, iCloud, Apple Pay)",
                "Wearables market expansion",
                "Autonomous vehicles",
                "Healthcare/medical devices",
                "Augmented reality products"
            ],
            threats=[
                "Intense smartphone competition (Samsung, Chinese brands)",
                "Regulatory pressure and antitrust",
                "Trade tensions US-China",
                "Maturing smartphone market",
                "Component supply shortages"
            ]
        )
    
    @staticmethod
    def netflix_bcg() -> BCGMatrix:
        """Pre-built BCG Matrix for Netflix (educational example)."""
        bcg = BCGMatrix("Netflix")
        
        bcg.add_business_unit(
            name="Streaming Subscription",
            market_share=1.5,     # Leader in streaming
            market_growth=12,     # Growing market
            revenue=28000         # $28B
        )
        
        bcg.add_business_unit(
            name="Original Content",
            market_share=0.8,     # Strong but not leader
            market_growth=20,     # High growth area
            revenue=17000         # $17B investment
        )
        
        bcg.add_business_unit(
            name="DVD Rental",
            market_share=2.0,     # Still market leader
            market_growth=-15,    # Declining market
            revenue=200           # $200M (tiny now)
        )
        
        bcg.add_business_unit(
            name="Gaming",
            market_share=0.1,     # Very small player
            market_growth=15,     # Growing market
            revenue=50            # $50M (new venture)
        )
        
        return bcg
    
    @staticmethod
    def tesla_pestel() -> PESTEL:
        """Pre-built PESTEL analysis for Tesla (educational example)."""
        pestel = PESTEL("Electric Vehicle Industry")
        
        # Political
        pestel.add_factor("Political", "EV subsidies and incentives", impact=5, likelihood=4)
        pestel.add_factor("Political", "Emissions regulations tightening", impact=5, likelihood=5)
        
        # Economic
        pestel.add_factor("Economic", "Rising gasoline prices", impact=4, likelihood=4)
        pestel.add_factor("Economic", "High interest rates affecting purchases", impact=4, likelihood=4)
        
        # Social
        pestel.add_factor("Social", "Climate change awareness", impact=5, likelihood=5)
        pestel.add_factor("Social", "Shift to sustainable transportation", impact=5, likelihood=4)
        
        # Technological
        pestel.add_factor("Technological", "Battery technology improvements", impact=5, likelihood=5)
        pestel.add_factor("Technological", "Autonomous driving development", impact=5, likelihood=4)
        pestel.add_factor("Technological", "Charging infrastructure expansion", impact=5, likelihood=4)
        
        # Environmental
        pestel.add_factor("Environmental", "Carbon emission targets", impact=5, likelihood=5)
        pestel.add_factor("Environmental", "Mining impact for batteries", impact=3, likelihood=4)
        
        # Legal
        pestel.add_factor("Legal", "Safety regulations for EVs", impact=4, likelihood=4)
        pestel.add_factor("Legal", "Direct-to-consumer sales restrictions", impact=3, likelihood=3)
        
        return pestel
    
    @staticmethod
    def amazon_porters() -> PortersFiveForces:
        """Pre-built Porter's Five Forces for Amazon's e-commerce business."""
        porters = PortersFiveForces(
            industry="E-commerce/Online Retail",
            competitive_rivalry=5,        # Extremely intense
            supplier_power=2,             # Amazon has power over suppliers
            buyer_power=5,                # Customers can switch easily
            threat_of_substitutes=4,      # Physical retail still exists
            threat_of_new_entrants=3      # Barriers exist but new players emerge
        )
        
        porters.add_factor("Competitive Rivalry", 
                          "Intense competition from Walmart, Alibaba, specialized retailers")
        porters.add_factor("Buyer Power", 
                          "Zero switching costs, price-sensitive customers, many alternatives")
        porters.add_factor("Supplier Power", 
                          "Amazon's scale gives it leverage, but key brands can resist")
        
        return porters


class QuickStart:
    """Convenience functions for instant analysis."""
    
    @staticmethod
    def analyze_company(company_name: str, industry: str = None):
        """
        Quick company analysis with sensible defaults.
        
        Args:
            company_name: Name of company to analyze
            industry: Industry type (optional, for better defaults)
        
        Example:
            >>> QuickStart.analyze_company("MyStartup", industry="tech")
        """
        print(f"\n{'='*70}")
        print(f"Quick Analysis Template for: {company_name}")
        print(f"{'='*70}\n")
        
        # Provide template SWOT with placeholders
        print("SWOT Analysis Template (Fill in your company specifics):")
        print("-" * 70)
        
        swot = SWOT(
            company=company_name,
            strengths=[
                "# Replace with YOUR company's strengths",
                "# Example: Strong technical team",
                "# Example: Unique product features"
            ],
            weaknesses=[
                "# Replace with YOUR company's weaknesses",
                "# Example: Limited marketing budget",
                "# Example: Small customer base"
            ],
            opportunities=[
                "# Replace with YOUR company's opportunities",
                "# Example: Growing market demand",
                "# Example: Partnership possibilities"
            ],
            threats=[
                "# Replace with YOUR company's threats",
                "# Example: Well-funded competitors",
                "# Example: Changing regulations"
            ]
        )
        
        swot.generate_report()
        
        # If industry provided, show Porter's template
        if industry:
            print(f"\n{'='*70}")
            print(f"Industry Analysis Template: {industry}")
            print(f"{'='*70}\n")
            
            try:
                template = IndustryTemplates.get_industry_template(industry)
                porters = PortersFiveForces(**template)
                porters.generate_report()
                print("\n💡 TIP: These are typical values for this industry.")
                print("   Adjust based on your specific market conditions.")
            except ValueError:
                print(f"No template for '{industry}'. Available: tech, retail, food, healthcare, finance")
        
        print(f"\n{'='*70}")
        print("Next Steps:")
        print("-" * 70)
        print("1. Replace the placeholder text with YOUR company's actual details")
        print("2. Adjust the ratings based on YOUR research")
        print("3. Call .plot() on each analysis to see visualizations")
        print("4. Use these insights for your presentation/report")
        print(f"{'='*70}\n")


# Convenience function for even easier access
def get_example(company: str) -> object:
    """
    Get a pre-built example for famous companies.
    
    Args:
        company: One of 'starbucks', 'apple', 'netflix', 'tesla', 'amazon'
    
    Returns:
        Pre-built framework analysis
    
    Example:
        >>> swot = get_example('starbucks')
        >>> swot.plot()
    """
    examples = {
        'starbucks': CompanyExamples.starbucks_swot,
        'apple': CompanyExamples.apple_swot,
        'netflix': CompanyExamples.netflix_bcg,
        'tesla': CompanyExamples.tesla_pestel,
        'amazon': CompanyExamples.amazon_porters
    }
    
    company_lower = company.lower()
    if company_lower not in examples:
        raise ValueError(f"Unknown company. Available examples: {list(examples.keys())}")
    
    return examples[company_lower]()
