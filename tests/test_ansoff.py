"""Tests for Ansoff Matrix"""

import pytest
from business_frameworks import AnsoffMatrix


def test_ansoff_creation():
    ansoff = AnsoffMatrix("TestCorp")
    assert ansoff.company == "TestCorp"
    assert len(ansoff.strategies) == 4


def test_add_strategy():
    ansoff = AnsoffMatrix("TestCorp")
    ansoff.add_strategy("Market Penetration", 
                        initiatives=["Initiative 1", "Initiative 2"],
                        priority=1)
    assert len(ansoff.strategies["Market Penetration"]["initiatives"]) == 2
    assert ansoff.strategies["Market Penetration"]["priority"] == 1


def test_invalid_strategy():
    ansoff = AnsoffMatrix("TestCorp")
    with pytest.raises(ValueError):
        ansoff.add_strategy("Invalid Strategy", initiatives=["Test"])


def test_current_strategy():
    ansoff = AnsoffMatrix("TestCorp", current_strategy="Market Penetration")
    assert ansoff.current_strategy == "Market Penetration"
