"""PESTEL Analysis Framework"""

from typing import List, Dict, Optional
import matplotlib.pyplot as plt
import pandas as pd


class PESTEL:
    """PESTEL Analysis: Political, Economic, Social, Technological, Environmental, Legal"""
    
    def __init__(self, industry: str):
        self.industry = industry
        self.factors: List[Dict] = []
    
    def add_factor(self, category: str, description: str, 
                   impact: int, likelihood: int) -> None:
        """Add a PESTEL factor (impact & likelihood: 1-5)"""
        if category not in ['Political', 'Economic', 'Social', 'Technological', 
                           'Environmental', 'Legal']:
            raise ValueError(f"Invalid category: {category}")
        if not (1 <= impact <= 5 and 1 <= likelihood <= 5):
            raise ValueError("Impact and likelihood must be 1-5")
        
        self.factors.append({
            'category': category,
            'description': description,
            'impact': impact,
            'likelihood': likelihood,
            'score': impact * likelihood
        })
    
    def generate_report(self) -> str:
        """Generate text report"""
        report = f"\n{'='*60}\nPESTEL ANALYSIS: {self.industry}\n{'='*60}\n\n"
        
        for cat in ['Political', 'Economic', 'Social', 'Technological', 
                    'Environmental', 'Legal']:
            items = [f for f in self.factors if f['category'] == cat]
            if items:
                report += f"\n{cat.upper()}\n" + "-"*60 + "\n"
                for item in items:
                    report += f"• {item['description']} (Impact: {item['impact']}, "
                    report += f"Likelihood: {item['likelihood']})\n"
        
        print(report)
        return report
    
    def plot_impact_matrix(self, figsize: tuple = (10, 8), 
                          save_path: Optional[str] = None) -> None:
        """Plot impact vs likelihood matrix"""
        if not self.factors:
            print("No factors to plot")
            return
        
        df = pd.DataFrame(self.factors)
        fig, ax = plt.subplots(figsize=figsize)
        
        colors = {'Political': '#FF6B6B', 'Economic': '#4ECDC4', 
                 'Social': '#45B7D1', 'Technological': '#96CEB4',
                 'Environmental': '#FFEAA7', 'Legal': '#DFE6E9'}
        
        for cat in df['category'].unique():
            cat_df = df[df['category'] == cat]
            ax.scatter(cat_df['likelihood'], cat_df['impact'], 
                      s=200, alpha=0.6, c=colors.get(cat, '#000'),
                      label=cat, edgecolors='black', linewidth=1.5)
        
        ax.set_xlabel('Likelihood', fontsize=12, fontweight='bold')
        ax.set_ylabel('Impact', fontsize=12, fontweight='bold')
        ax.set_title(f'PESTEL Impact Matrix\n{self.industry}', 
                    fontsize=14, fontweight='bold')
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 6)
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper left')
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
