"""Tests for Porter's Five Forces"""

import pytest
from strategykit import PortersFiveForces


def test_porters_creation():
    pf = PortersFiveForces("Tech", 5, 3, 4, 2, 2)
    assert pf.industry == "Tech"
    assert pf.overall_attractiveness() == 3.2


def test_invalid_score():
    with pytest.raises(ValueError):
        PortersFiveForces("Tech", 6, 3, 4, 2, 2)


def test_add_factor():
    pf = PortersFiveForces("Tech", 5, 3, 4, 2, 2)
    pf.add_factor("Competitive Rivalry", "High competition")
    assert len(pf.forces["Competitive Rivalry"].factors) == 1
