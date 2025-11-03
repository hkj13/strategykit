"""
BCG Matrix (Growth-Share Matrix)

Analyzes business units or products based on market growth and market share.
"""

from typing import List, Optional, Dict, Tuple
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass


@dataclass
class BusinessUnit:
    """Represents a business unit or product in the BCG Matrix."""
    name: str
    market_share: float  # Relative market share (your share / leader's share)
    market_growth: float  # Annual market growth rate (%)
    revenue: float  # For bubble size
    
    def get_category(self) -> str:
        """Determine which quadrant the business unit falls into."""
        if self.market_growth >= 10:  # High growth
            if self.market_share >= 1.0:  # High share (market leader)
                return "Star"
            else:
                return "Question Mark"
        else:  # Low growth
            if self.market_share >= 1.0:  # High share
                return "Cash Cow"
            else:
                return "Dog"


class BCGMatrix:
    """
    BCG Matrix (Growth-Share Matrix) Analysis.
    
    Classifies business units into four categories:
    - Stars: High growth, high market share (invest to maintain)
    - Cash Cows: Low growth, high market share (milk for cash)
    - Question Marks: High growth, low market share (invest or divest)
    - Dogs: Low growth, low market share (consider divesting)
    
    Args:
        company: Name of the company being analyzed
    
    Example:
        >>> bcg = BCGMatrix("TechCorp")
        >>> bcg.add_business_unit("Cloud Services", market_share=1.5, 
        ...                       market_growth=25, revenue=500)
        >>> bcg.add_business_unit("Legacy Software", market_share=2.0,
        ...                       market_growth=2, revenue=300)
        >>> bcg.plot()
        >>> bcg.generate_recommendations()
    """
    
    def __init__(self, company: str):
        self.company = company
        self.business_units: List[BusinessUnit] = []
    
    def add_business_unit(self, name: str, market_share: float, 
                         market_growth: float, revenue: float) -> None:
        """
        Add a business unit to the analysis.
        
        Args:
            name: Business unit or product name
            market_share: Relative market share (your share / leader's share)
            market_growth: Annual market growth rate (%)
            revenue: Revenue in millions (used for bubble size)
        """
        bu = BusinessUnit(name, market_share, market_growth, revenue)
        self.business_units.append(bu)
    
    def get_portfolio_summary(self) -> Dict[str, List[str]]:
        """Get summary of portfolio by category."""
        summary = {
            "Star": [],
            "Cash Cow": [],
            "Question Mark": [],
            "Dog": []
        }
        
        for bu in self.business_units:
            category = bu.get_category()
            summary[category].append(bu.name)
        
        return summary
    
    def generate_recommendations(self) -> str:
        """Generate strategic recommendations based on portfolio."""
        report = f"\n{'='*70}\n"
        report += f"BCG MATRIX RECOMMENDATIONS: {self.company}\n"
        report += f"{'='*70}\n\n"
        
        summary = self.get_portfolio_summary()
        
        # Stars
        if summary["Star"]:
            report += "⭐ STARS - Invest to Maintain Leadership\n"
            report += "-" * 70 + "\n"
            for bu in summary["Star"]:
                report += f"  • {bu}: Continue heavy investment to maintain market position\n"
            report += "\n"
        
        # Cash Cows
        if summary["Cash Cow"]:
            report += "💰 CASH COWS - Harvest Cash Flow\n"
            report += "-" * 70 + "\n"
            for bu in summary["Cash Cow"]:
                report += f"  • {bu}: Milk for cash, minimal investment needed\n"
            report += "  Strategy: Use cash generated to fund Stars and Question Marks\n"
            report += "\n"
        
        # Question Marks
        if summary["Question Mark"]:
            report += "❓ QUESTION MARKS - Invest or Divest\n"
            report += "-" * 70 + "\n"
            for bu in summary["Question Mark"]:
                report += f"  • {bu}: Requires analysis - invest heavily or divest\n"
            report += "  Strategy: Pick winners and invest aggressively, exit losers\n"
            report += "\n"
        
        # Dogs
        if summary["Dog"]:
            report += "🐕 DOGS - Consider Divesting\n"
            report += "-" * 70 + "\n"
            for bu in summary["Dog"]:
                report += f"  • {bu}: Low priority, consider divestment\n"
            report += "  Strategy: Harvest or divest unless strategic reasons to keep\n"
            report += "\n"
        
        # Portfolio balance
        report += "PORTFOLIO BALANCE\n"
        report += "-" * 70 + "\n"
        total = len(self.business_units)
        report += f"  Stars: {len(summary['Star'])} ({len(summary['Star'])/total*100:.1f}%)\n"
        report += f"  Cash Cows: {len(summary['Cash Cow'])} ({len(summary['Cash Cow'])/total*100:.1f}%)\n"
        report += f"  Question Marks: {len(summary['Question Mark'])} ({len(summary['Question Mark'])/total*100:.1f}%)\n"
        report += f"  Dogs: {len(summary['Dog'])} ({len(summary['Dog'])/total*100:.1f}%)\n"
        
        print(report)
        return report
    
    def plot(self, figsize: Tuple[int, int] = (12, 10), 
             save_path: Optional[str] = None) -> None:
        """
        Create BCG Matrix visualization with bubble chart.
        
        Args:
            figsize: Figure size tuple
            save_path: Optional path to save figure
        """
        if not self.business_units:
            print("No business units to plot. Add units first.")
            return
        
        fig, ax = plt.subplots(figsize=figsize)
        
        # Define colors for each quadrant
        colors_map = {
            "Star": "#FFD700",           # Gold
            "Cash Cow": "#32CD32",       # Lime Green  
            "Question Mark": "#FF69B4",  # Hot Pink
            "Dog": "#808080"             # Gray
        }
        
        # Plot each business unit
        for bu in self.business_units:
            category = bu.get_category()
            color = colors_map[category]
            
            # Bubble size proportional to revenue
            size = bu.revenue * 5
            
            ax.scatter(bu.market_share, bu.market_growth, 
                      s=size, alpha=0.6, c=color, edgecolors='black', 
                      linewidth=2, label=category if category not in ax.get_legend_handles_labels()[1] else "")
            
            # Add labels
            ax.annotate(bu.name, (bu.market_share, bu.market_growth),
                       fontsize=9, ha='center', va='center', fontweight='bold')
        
        # Draw quadrant lines
        ax.axhline(y=10, color='black', linestyle='--', linewidth=2, alpha=0.7)
        ax.axvline(x=1.0, color='black', linestyle='--', linewidth=2, alpha=0.7)
        
        # Add quadrant labels
        ax.text(0.3, 25, 'QUESTION MARKS\n?', fontsize=14, 
               ha='center', va='center', alpha=0.3, fontweight='bold')
        ax.text(2.0, 25, 'STARS\n⭐', fontsize=14,
               ha='center', va='center', alpha=0.3, fontweight='bold')
        ax.text(0.3, 3, 'DOGS\n🐕', fontsize=14,
               ha='center', va='center', alpha=0.3, fontweight='bold')
        ax.text(2.0, 3, 'CASH COWS\n💰', fontsize=14,
               ha='center', va='center', alpha=0.3, fontweight='bold')
        
        # Styling
        ax.set_xlabel('Relative Market Share (vs. largest competitor)', 
                     fontsize=12, fontweight='bold')
        ax.set_ylabel('Market Growth Rate (%)', fontsize=12, fontweight='bold')
        ax.set_title(f'BCG Matrix (Growth-Share Matrix)\n{self.company}', 
                    fontsize=14, fontweight='bold', pad=20)
        
        # Set reasonable axis limits
        max_share = max(bu.market_share for bu in self.business_units) * 1.2
        max_growth = max(bu.market_growth for bu in self.business_units) * 1.2
        ax.set_xlim(0, max(max_share, 2.5))
        ax.set_ylim(0, max(max_growth, 30))
        
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper right', fontsize=10)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def to_dict(self) -> Dict:
        """Export analysis to dictionary."""
        return {
            "company": self.company,
            "business_units": [
                {
                    "name": bu.name,
                    "market_share": bu.market_share,
                    "market_growth": bu.market_growth,
                    "revenue": bu.revenue,
                    "category": bu.get_category()
                }
                for bu in self.business_units
            ],
            "portfolio_summary": self.get_portfolio_summary()
        }
