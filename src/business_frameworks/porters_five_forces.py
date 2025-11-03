"""
Porter's Five Forces Analysis Framework

Analyzes the competitive intensity and attractiveness of an industry.
"""

from typing import Optional, Dict, List
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass


@dataclass
class Force:
    """Represents a single force in Porter's Five Forces framework."""
    name: str
    score: int  # 1-5 scale
    factors: List[str]
    
    def __post_init__(self) -> None:
        if not 1 <= self.score <= 5:
            raise ValueError(f"Score must be between 1 and 5, got {self.score}")


class PortersFiveForces:
    """
    Porter's Five Forces Analysis Framework.
    
    Analyzes five key competitive forces that shape every industry:
    1. Competitive Rivalry
    2. Supplier Power
    3. Buyer Power
    4. Threat of Substitutes
    5. Threat of New Entrants
    
    Args:
        industry: Name of the industry being analyzed
        competitive_rivalry: Score 1-5 (1=low, 5=high)
        supplier_power: Score 1-5
        buyer_power: Score 1-5
        threat_of_substitutes: Score 1-5
        threat_of_new_entrants: Score 1-5
    
    Example:
        >>> analysis = PortersFiveForces(
        ...     industry="Smartphone Manufacturing",
        ...     competitive_rivalry=5,
        ...     supplier_power=3,
        ...     buyer_power=4,
        ...     threat_of_substitutes=2,
        ...     threat_of_new_entrants=2
        ... )
        >>> analysis.generate_report()
        >>> analysis.plot()
    """
    
    def __init__(
        self,
        industry: str,
        competitive_rivalry: int,
        supplier_power: int,
        buyer_power: int,
        threat_of_substitutes: int,
        threat_of_new_entrants: int,
    ):
        self.industry = industry
        self.forces = {
            "Competitive Rivalry": Force("Competitive Rivalry", competitive_rivalry, []),
            "Supplier Power": Force("Supplier Power", supplier_power, []),
            "Buyer Power": Force("Buyer Power", buyer_power, []),
            "Threat of Substitutes": Force("Threat of Substitutes", threat_of_substitutes, []),
            "Threat of New Entrants": Force("Threat of New Entrants", threat_of_new_entrants, []),
        }
    
    def add_factor(self, force_name: str, factor: str) -> None:
        """Add a supporting factor for a specific force."""
        if force_name not in self.forces:
            raise ValueError(f"Unknown force: {force_name}")
        self.forces[force_name].factors.append(factor)
    
    def overall_attractiveness(self) -> float:
        """
        Calculate overall industry attractiveness.
        Lower scores indicate higher attractiveness (less competitive pressure).
        
        Returns:
            Average score across all five forces (1.0 to 5.0)
        """
        total = sum(force.score for force in self.forces.values())
        return total / len(self.forces)
    
    def get_interpretation(self) -> str:
        """Get interpretation of the overall attractiveness score."""
        score = self.overall_attractiveness()
        if score <= 2.0:
            return "Highly Attractive - Low competitive pressure"
        elif score <= 3.0:
            return "Moderately Attractive - Balanced competitive forces"
        elif score <= 4.0:
            return "Challenging - High competitive pressure"
        else:
            return "Unattractive - Intense competitive pressure"
    
    def generate_report(self) -> str:
        """Generate a text report of the analysis."""
        report = f"\n{'='*60}\n"
        report += f"PORTER'S FIVE FORCES ANALYSIS\n"
        report += f"Industry: {self.industry}\n"
        report += f"{'='*60}\n\n"
        
        for force_name, force in self.forces.items():
            report += f"{force_name}: {'★' * force.score}{'☆' * (5 - force.score)} ({force.score}/5)\n"
            if force.factors:
                for factor in force.factors:
                    report += f"  • {factor}\n"
            report += "\n"
        
        report += f"{'='*60}\n"
        report += f"Overall Industry Attractiveness: {self.overall_attractiveness():.2f}/5.0\n"
        report += f"Interpretation: {self.get_interpretation()}\n"
        report += f"{'='*60}\n"
        
        print(report)
        return report
    
    def plot(self, figsize: tuple = (10, 8), save_path: Optional[str] = None) -> None:
        """
        Create a radar chart visualization of the five forces.
        
        Args:
            figsize: Figure size tuple (width, height)
            save_path: Optional path to save the figure
        """
        force_names = list(self.forces.keys())
        scores = [self.forces[name].score for name in force_names]
        
        # Create radar chart
        angles = np.linspace(0, 2 * np.pi, len(force_names), endpoint=False).tolist()
        scores_plot = scores + [scores[0]]  # Complete the circle
        angles_plot = angles + [angles[0]]
        
        fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(projection='polar'))
        
        # Plot data
        ax.plot(angles_plot, scores_plot, 'o-', linewidth=2, color='#2E86AB', label='Current State')
        ax.fill(angles_plot, scores_plot, alpha=0.25, color='#2E86AB')
        
        # Customize
        ax.set_xticks(angles)
        ax.set_xticklabels(force_names, size=10)
        ax.set_ylim(0, 5)
        ax.set_yticks([1, 2, 3, 4, 5])
        ax.set_yticklabels(['1', '2', '3', '4', '5'], size=8)
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Add title
        plt.title(
            f"Porter's Five Forces Analysis\n{self.industry}\n"
            f"Overall Score: {self.overall_attractiveness():.2f}/5.0",
            size=14,
            weight='bold',
            pad=20
        )
        
        # Add legend
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()
    
    def to_dict(self) -> Dict:
        """Export analysis to dictionary format."""
        return {
            "industry": self.industry,
            "forces": {
                name: {
                    "score": force.score,
                    "factors": force.factors
                }
                for name, force in self.forces.items()
            },
            "overall_attractiveness": self.overall_attractiveness(),
            "interpretation": self.get_interpretation()
        }
