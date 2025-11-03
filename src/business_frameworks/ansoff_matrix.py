"""
Ansoff Matrix (Product/Market Expansion Grid)

Analyzes growth strategies based on products and markets.
"""

from typing import List, Optional, Dict
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class AnsoffMatrix:
    """
    Ansoff Matrix for Growth Strategy Analysis.
    
    Four growth strategies:
    1. Market Penetration: Existing products in existing markets (lowest risk)
    2. Market Development: Existing products in new markets
    3. Product Development: New products in existing markets
    4. Diversification: New products in new markets (highest risk)
    
    Args:
        company: Name of the company
        current_strategy: Current position (optional)
    
    Example:
        >>> ansoff = AnsoffMatrix("TechCorp")
        >>> ansoff.add_strategy("Market Penetration", 
        ...     initiatives=["Increase marketing", "Loyalty programs"],
        ...     risk_level="Low")
        >>> ansoff.plot()
    """
    
    def __init__(self, company: str, current_strategy: Optional[str] = None):
        self.company = company
        self.current_strategy = current_strategy
        self.strategies = {
            "Market Penetration": {"initiatives": [], "risk": "Low", "priority": None},
            "Market Development": {"initiatives": [], "risk": "Medium", "priority": None},
            "Product Development": {"initiatives": [], "risk": "Medium", "priority": None},
            "Diversification": {"initiatives": [], "risk": "High", "priority": None}
        }
    
    def add_strategy(self, strategy_name: str, initiatives: List[str], 
                    priority: Optional[int] = None) -> None:
        """
        Add initiatives for a specific growth strategy.
        
        Args:
            strategy_name: One of the four Ansoff strategies
            initiatives: List of specific actions/initiatives
            priority: Priority level (1=highest)
        """
        if strategy_name not in self.strategies:
            raise ValueError(f"Unknown strategy. Must be one of: {list(self.strategies.keys())}")
        
        self.strategies[strategy_name]["initiatives"] = initiatives
        self.strategies[strategy_name]["priority"] = priority
    
    def generate_report(self) -> str:
        """Generate strategic recommendations."""
        report = f"\n{'='*70}\n"
        report += f"ANSOFF MATRIX ANALYSIS: {self.company}\n"
        report += f"{'='*70}\n\n"
        
        if self.current_strategy:
            report += f"Current Focus: {self.current_strategy}\n\n"
        
        # Market Penetration
        report += "📊 MARKET PENETRATION (Existing Products, Existing Markets)\n"
        report += "-" * 70 + "\n"
        report += "Risk Level: LOW | Focus: Increase market share\n"
        if self.strategies["Market Penetration"]["initiatives"]:
            for init in self.strategies["Market Penetration"]["initiatives"]:
                report += f"  • {init}\n"
        else:
            report += "  • Increase marketing and promotional efforts\n"
            report += "  • Improve customer service and loyalty programs\n"
            report += "  • Competitive pricing strategies\n"
        report += "\n"
        
        # Market Development  
        report += "🌍 MARKET DEVELOPMENT (Existing Products, New Markets)\n"
        report += "-" * 70 + "\n"
        report += "Risk Level: MEDIUM | Focus: Enter new geographic or demographic markets\n"
        if self.strategies["Market Development"]["initiatives"]:
            for init in self.strategies["Market Development"]["initiatives"]:
                report += f"  • {init}\n"
        else:
            report += "  • Expand to new geographic regions\n"
            report += "  • Target new customer segments\n"
            report += "  • Explore new distribution channels\n"
        report += "\n"
        
        # Product Development
        report += "🔬 PRODUCT DEVELOPMENT (New Products, Existing Markets)\n"
        report += "-" * 70 + "\n"
        report += "Risk Level: MEDIUM | Focus: Innovate for current customers\n"
        if self.strategies["Product Development"]["initiatives"]:
            for init in self.strategies["Product Development"]["initiatives"]:
                report += f"  • {init}\n"
        else:
            report += "  • Develop new features or versions\n"
            report += "  • Create complementary products\n"
            report += "  • Innovate based on customer feedback\n"
        report += "\n"
        
        # Diversification
        report += "🚀 DIVERSIFICATION (New Products, New Markets)\n"
        report += "-" * 70 + "\n"
        report += "Risk Level: HIGH | Focus: Enter completely new areas\n"
        if self.strategies["Diversification"]["initiatives"]:
            for init in self.strategies["Diversification"]["initiatives"]:
                report += f"  • {init}\n"
        else:
            report += "  • Consider only if core business is strong\n"
            report += "  • Evaluate synergies carefully\n"
            report += "  • Start with related diversification\n"
        report += "\n"
        
        report += "RECOMMENDATION\n"
        report += "-" * 70 + "\n"
        report += "Start with Market Penetration (lowest risk), then consider\n"
        report += "Market Development or Product Development based on resources.\n"
        report += "Pursue Diversification only when other strategies are exhausted.\n"
        
        print(report)
        return report
    
    def plot(self, figsize=(12, 10), save_path: Optional[str] = None) -> None:
        """
        Create Ansoff Matrix visualization.
        
        Args:
            figsize: Figure size tuple
            save_path: Optional path to save figure
        """
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 2)
        ax.axis('off')
        
        # Define colors by risk level
        colors = {
            'Market Penetration': '#90EE90',      # Light green (low risk)
            'Market Development': '#FFD700',      # Gold (medium risk)
            'Product Development': '#FFA500',     # Orange (medium risk)
            'Diversification': '#FF6347'          # Tomato red (high risk)
        }
        
        # Define quadrants (strategy, x, y, color)
        quadrants = [
            ('Market Penetration', 0, 1, colors['Market Penetration']),
            ('Market Development', 1, 1, colors['Market Development']),
            ('Product Development', 0, 0, colors['Product Development']),
            ('Diversification', 1, 0, colors['Diversification']),
        ]
        
        for strategy, x, y, color in quadrants:
            # Draw rectangle
            rect = mpatches.Rectangle((x, y), 1, 1, linewidth=3,
                                     edgecolor='black', facecolor=color, alpha=0.3)
            ax.add_patch(rect)
            
            # Add title
            ax.text(x + 0.5, y + 0.92, strategy.upper(),
                   ha='center', va='top', fontsize=13, fontweight='bold')
            
            # Add risk level
            risk = self.strategies[strategy]["risk"]
            ax.text(x + 0.5, y + 0.82, f"Risk: {risk}",
                   ha='center', va='top', fontsize=10, style='italic',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
            
            # Add initiatives
            initiatives = self.strategies[strategy]["initiatives"]
            y_pos = y + 0.70
            if initiatives:
                for init in initiatives[:3]:  # Show max 3
                    text = init if len(init) <= 35 else init[:32] + "..."
                    ax.text(x + 0.05, y_pos, f"• {text}",
                           ha='left', va='top', fontsize=9)
                    y_pos -= 0.12
            
            # Highlight current strategy
            if self.current_strategy == strategy:
                highlight = mpatches.Rectangle((x, y), 1, 1, linewidth=5,
                                              edgecolor='blue', facecolor='none')
                ax.add_patch(highlight)
                ax.text(x + 0.5, y + 0.05, "★ CURRENT",
                       ha='center', va='bottom', fontsize=11,
                       fontweight='bold', color='blue')
        
        # Add axis labels
        fig.text(0.5, 0.95, 'PRODUCTS', ha='center', fontsize=14,
                fontweight='bold')
        fig.text(0.25, 0.93, 'EXISTING', ha='center', fontsize=11)
        fig.text(0.75, 0.93, 'NEW', ha='center', fontsize=11)
        
        fig.text(0.08, 0.5, 'MARKETS', va='center', rotation=90,
                fontsize=14, fontweight='bold')
        fig.text(0.06, 0.75, 'EXISTING', va='center', rotation=90, fontsize=11)
        fig.text(0.06, 0.25, 'NEW', va='center', rotation=90, fontsize=11)
        
        # Main title
        fig.suptitle(f'Ansoff Matrix: Growth Strategy Analysis\n{self.company}',
                    fontsize=16, fontweight='bold', y=0.98)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
