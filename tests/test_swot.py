"""Tests for SWOT Analysis"""

from strategykit import SWOT


def test_swot_creation():
    swot = SWOT("TestCo", strengths=["S1", "S2"], weaknesses=["W1"])
    assert swot.company == "TestCo"
    assert len(swot.strengths) == 2
    assert len(swot.weaknesses) == 1


def test_add_methods():
    swot = SWOT("TestCo")
    swot.add_strength("Strong brand")
    swot.add_weakness("High costs")
    swot.add_opportunity("New market")
    swot.add_threat("Competition")
    
    assert len(swot.strengths) == 1
    assert len(swot.weaknesses) == 1
    assert len(swot.opportunities) == 1
    assert len(swot.threats) == 1
