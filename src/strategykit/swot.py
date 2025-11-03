"""SWOT Analysis Framework"""

from typing import List, Optional
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class SWOT:
    """SWOT Analysis: Strengths, Weaknesses, Opportunities, Threats"""
    
    def __init__(self, company: str, strengths: Optional[List[str]] = None,
                 weaknesses: Optional[List[str]] = None, opportunities: Optional[List[str]] = None,
                 threats: Optional[List[str]] = None):
        self.company = company
        self.strengths = strengths or []
        self.weaknesses = weaknesses or []
        self.opportunities = opportunities or []
        self.threats = threats or []
    
    def add_strength(self, strength: str) -> None:
        self.strengths.append(strength)
    
    def add_weakness(self, weakness: str) -> None:
        self.weaknesses.append(weakness)
    
    def add_opportunity(self, opportunity: str) -> None:
        self.opportunities.append(opportunity)
    
    def add_threat(self, threat: str) -> None:
        self.threats.append(threat)
    
    def generate_report(self) -> str:
        """Generate text report"""
        report = f"\n{'='*60}\nSWOT ANALYSIS: {self.company}\n{'='*60}\n\n"
        report += "STRENGTHS\n" + "\n".join(f"  • {s}" for s in self.strengths) + "\n\n"
        report += "WEAKNESSES\n" + "\n".join(f"  • {w}" for w in self.weaknesses) + "\n\n"
        report += "OPPORTUNITIES\n" + "\n".join(f"  • {o}" for o in self.opportunities) + "\n\n"
        report += "THREATS\n" + "\n".join(f"  • {t}" for t in self.threats) + "\n"
        print(report)
        return report
    
    def plot(self, figsize: tuple = (12, 10), save_path: Optional[str] = None) -> None:
        """Create SWOT matrix visualization"""
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim(0, 2)
        ax.set_ylim(0, 2)
        ax.axis('off')
        
        colors = {'s': '#4CAF50', 'w': '#FF9800', 'o': '#2196F3', 't': '#F44336'}
        quadrants = [
            ('STRENGTHS', self.strengths, 1, 1, colors['s']),
            ('WEAKNESSES', self.weaknesses, 0, 1, colors['w']),
            ('OPPORTUNITIES', self.opportunities, 1, 0, colors['o']),
            ('THREATS', self.threats, 0, 0, colors['t']),
        ]
        
        for title, items, x, y, color in quadrants:
            rect = mpatches.Rectangle((x, y), 1, 1, linewidth=2, edgecolor='black',
                                     facecolor=color, alpha=0.2)
            ax.add_patch(rect)
            ax.text(x + 0.5, y + 0.95, title, ha='center', va='top',
                   fontsize=14, fontweight='bold')
            
            y_pos = y + 0.85
            for item in items:
                ax.text(x + 0.05, y_pos, f"• {item[:50]}", ha='left', va='top', fontsize=9)
                y_pos -= 0.08
        
        fig.suptitle(f'SWOT Analysis: {self.company}', fontsize=16, fontweight='bold')
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
