"""
Business Frameworks - Strategic Framework Toolkit for MBA Students

A comprehensive Python library for business strategy analysis and visualization.
"""

__version__ = "0.2.1"

from business_frameworks.porters_five_forces import PortersFiveForces
from business_frameworks.swot import SWOT
from business_frameworks.pestel import PESTEL
from business_frameworks.bcg_matrix import BCGMatrix
from business_frameworks.ansoff_matrix import AnsoffMatrix

# Convenience features
from business_frameworks import templates

__all__ = [
    "PortersFiveForces",
    "SWOT",
    "PESTEL",
    "BCGMatrix",
    "AnsoffMatrix",
    "templates",
]
