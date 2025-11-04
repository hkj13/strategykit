"""
Company Data Loader - Ivy League Quality Analysis

Load pre-researched company data from our curated knowledge base.
All data sourced from authoritative sources (SEC filings, academic cases, etc.)
"""

import json
import os
from pathlib import Path
from typing import Optional, Dict, List
from business_frameworks import PortersFiveForces, SWOT, BCGMatrix, PESTEL


class CompanyDataLoader:
    """Load pre-researched company analysis from our knowledge base."""
    
    def __init__(self):
        # Find data directory
        current_dir = Path(__file__).parent.parent.parent
        self.data_dir = current_dir / "data" / "companies"
        
    def list_available_companies(self) -> List[str]:
        """Get list of companies with curated data available."""
        if not self.data_dir.exists():
            return []
        
        companies = []
        for file in self.data_dir.glob("*.json"):
            ticker = file.stem
            with open(file, 'r') as f:
                data = json.load(f)
                companies.append({
                    'ticker': ticker,
                    'name': data['meta']['company_name'],
                    'quality_score': data['meta']['data_quality_score'],
                    'last_updated': data['meta']['last_updated']
                })
        
        return companies
    
    def load_company(self, ticker: str) -> Dict:
        """Load all data for a specific company."""
        file_path = self.data_dir / f"{ticker.upper()}.json"
        
        if not file_path.exists():
            available = [c['ticker'] for c in self.list_available_companies()]
            raise ValueError(
                f"No data for {ticker}. Available companies: {available}"
            )
        
        with open(file_path, 'r') as f:
            return json.load(f)
    
    def get_porters(self, ticker: str) -> PortersFiveForces:
        """
        Get Porter's Five Forces analysis from curated data.
        
        Args:
            ticker: Stock ticker (e.g., 'AAPL', 'SBUX')
        
        Returns:
            PortersFiveForces object with all data pre-filled
        
        Example:
            >>> loader = CompanyDataLoader()
            >>> porters = loader.get_porters('AAPL')
            >>> porters.generate_report()
        """
        data = self.load_company(ticker)
        pf = data['porters_five_forces']
        
        # Create Porter's Five Forces
        porters = PortersFiveForces(
            industry=data['company_profile']['industry'],
            competitive_rivalry=pf['competitive_rivalry']['rating'],
            supplier_power=pf['supplier_power']['rating'],
            buyer_power=pf['buyer_power']['rating'],
            threat_of_substitutes=pf['threat_of_substitutes']['rating'],
            threat_of_new_entrants=pf['threat_of_new_entrants']['rating']
        )
        
        # Add detailed factors
        for force, details in pf.items():
            if force in ['competitive_rivalry', 'supplier_power', 'buyer_power', 
                        'threat_of_substitutes', 'threat_of_new_entrants']:
                force_name = force.replace('_', ' ').title()
                
                # Add key factors as details
                if 'factors' in details:
                    for factor in details['factors'][:3]:  # Top 3
                        porters.add_factor(force_name, factor)
        
        return porters
    
    def get_swot(self, ticker: str) -> SWOT:
        """
        Get SWOT analysis from curated data.
        
        Args:
            ticker: Stock ticker (e.g., 'AAPL', 'SBUX')
        
        Returns:
            SWOT object with all data pre-filled from authoritative sources
        
        Example:
            >>> loader = CompanyDataLoader()
            >>> swot = loader.get_swot('AAPL')
            >>> swot.plot()
        """
        data = self.load_company(ticker)
        swot_data = data['swot_analysis']
        
        # Extract just the factor text with evidence
        strengths = [
            f"{s['factor']} ({s['evidence']})" 
            for s in swot_data['strengths']
        ]
        
        weaknesses = [
            f"{w['factor']} ({w['evidence']})" 
            for w in swot_data['weaknesses']
        ]
        
        opportunities = [
            f"{o['factor']} - {o['potential']}" 
            for o in swot_data['opportunities']
        ]
        
        threats = [
            f"{t['factor']} (Impact: {t['impact']}/5, Likelihood: {t['likelihood']}/5)" 
            for t in swot_data['threats']
        ]
        
        return SWOT(
            company=data['meta']['company_name'],
            strengths=strengths,
            weaknesses=weaknesses,
            opportunities=opportunities,
            threats=threats
        )
    
    def get_company_report(self, ticker: str) -> str:
        """
        Generate comprehensive report with all frameworks and sources.
        
        Args:
            ticker: Stock ticker
        
        Returns:
            Formatted text report with citations
        """
        data = self.load_company(ticker)
        
        report = f"\n{'='*80}\n"
        report += f"COMPREHENSIVE STRATEGIC ANALYSIS: {data['meta']['company_name']}\n"
        report += f"{'='*80}\n\n"
        
        # Metadata
        report += f"Data Quality Score: {data['meta']['data_quality_score']}/10\n"
        report += f"Last Updated: {data['meta']['last_updated']}\n"
        report += f"Sources: {data['meta']['source_count']} authoritative sources\n"
        report += f"Review Status: {data['meta']['review_status']}\n\n"
        
        # Company Overview
        report += f"{'='*80}\n"
        report += f"COMPANY OVERVIEW\n"
        report += f"{'='*80}\n"
        profile = data['company_profile']
        report += f"Founded: {profile['founded']}\n"
        report += f"Headquarters: {profile['headquarters']}\n"
        report += f"CEO: {profile['ceo']}\n"
        report += f"Employees: {profile['employees']:,}\n"
        report += f"Industry: {profile['industry']}\n\n"
        
        # Financial Highlights
        report += f"{'='*80}\n"
        report += f"FINANCIAL HIGHLIGHTS (FY2023)\n"
        report += f"{'='*80}\n"
        fin = data['financial_overview']
        report += f"Revenue: ${fin['revenue_fy2023']/1e9:.1f}B\n"
        report += f"Net Income: ${fin['net_income_fy2023']/1e9:.1f}B\n"
        report += f"Market Cap: ${fin['market_cap']/1e9:.0f}B\n"
        report += f"Profit Margin: {fin['profit_margin']*100:.1f}%\n"
        report += f"Source: {fin['source']}\n\n"
        
        # Porter's Five Forces Summary
        report += f"{'='*80}\n"
        report += f"INDUSTRY ANALYSIS (Porter's Five Forces)\n"
        report += f"{'='*80}\n"
        pf = data['porters_five_forces']
        report += f"Overall Attractiveness: {pf['overall_attractiveness']}/5.0\n"
        report += f"Interpretation: {pf['interpretation']}\n\n"
        
        for force in ['competitive_rivalry', 'supplier_power', 'buyer_power', 
                     'threat_of_substitutes', 'threat_of_new_entrants']:
            force_data = pf[force]
            force_name = force.replace('_', ' ').title()
            report += f"{force_name}: {force_data['rating']}/5\n"
            report += f"  {force_data['justification']}\n"
        
        # SWOT Summary
        report += f"\n{'='*80}\n"
        report += f"SWOT ANALYSIS\n"
        report += f"{'='*80}\n\n"
        
        swot_data = data['swot_analysis']
        
        report += f"TOP STRENGTHS:\n"
        for s in swot_data['strengths'][:3]:
            report += f"• {s['factor']}\n"
            report += f"  Evidence: {s['evidence']}\n"
            report += f"  Source: {s['source']}\n"
        
        report += f"\nKEY WEAKNESSES:\n"
        for w in swot_data['weaknesses'][:3]:
            report += f"• {w['factor']}\n"
            report += f"  Evidence: {w['evidence']}\n"
            report += f"  Risk Level: {w['risk_level']}\n"
        
        report += f"\nMAJOR OPPORTUNITIES:\n"
        for o in swot_data['opportunities'][:3]:
            report += f"• {o['factor']}\n"
            report += f"  Potential: {o['potential']}\n"
            report += f"  Timeframe: {o['timeframe']}\n"
        
        report += f"\nTOP THREATS:\n"
        for t in swot_data['threats'][:3]:
            report += f"• {t['factor']}\n"
            report += f"  Impact: {t['impact']}/5, Likelihood: {t['likelihood']}/5\n"
        
        # Academic References
        report += f"\n{'='*80}\n"
        report += f"ACADEMIC REFERENCES\n"
        report += f"{'='*80}\n"
        for ref in data.get('academic_references', []):
            report += f"\n• {ref['title']}\n"
            source = ref.get('institution') or ref.get('journal')
            report += f"  {source}, {ref['year']}\n"
            if 'case_id' in ref:
                report += f"  Case ID: {ref['case_id']}\n"
        
        # Data Sources
        report += f"\n{'='*80}\n"
        report += f"DATA SOURCES ({data['meta']['source_count']} total)\n"
        report += f"{'='*80}\n"
        for source in data.get('data_sources', [])[:5]:  # Top 5
            report += f"• [{source['type']}] {source['name']}\n"
        
        report += f"\n{'='*80}\n"
        report += f"End of Report - All data from authoritative sources\n"
        report += f"{'='*80}\n"
        
        return report


# Convenience functions for easy access
def load_company_analysis(ticker: str):
    """
    Load complete company analysis in one line.
    
    Args:
        ticker: Stock ticker (e.g., 'AAPL')
    
    Returns:
        Dictionary with all framework objects
    
    Example:
        >>> analysis = load_company_analysis('AAPL')
        >>> analysis['swot'].plot()
        >>> analysis['porters'].generate_report()
    """
    loader = CompanyDataLoader()
    
    return {
        'porters': loader.get_porters(ticker),
        'swot': loader.get_swot(ticker),
        'report': loader.get_company_report(ticker),
        'raw_data': loader.load_company(ticker)
    }


def quick_analysis(ticker: str):
    """
    Print quick strategic analysis for a company.
    
    Args:
        ticker: Stock ticker (e.g., 'AAPL')
    
    Example:
        >>> quick_analysis('AAPL')
    """
    loader = CompanyDataLoader()
    print(loader.get_company_report(ticker))
