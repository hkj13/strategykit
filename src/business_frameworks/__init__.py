"""
Business Frameworks - Strategic Framework Toolkit for MBA Students

A comprehensive Python library for business strategy analysis and visualization.
"""

__version__ = "0.1.0"

from business_frameworks.porters_five_forces import PortersFiveForces
from business_frameworks.swot import SWOT
from business_frameworks.pestel import PESTEL

__all__ = [
    "PortersFiveForces",
    "SWOT",
    "PESTEL",
]
