"""Tests for PESTEL Analysis"""

import pytest
from strategykit import PESTEL


def test_pestel_creation():
    pestel = PESTEL("Tech Industry")
    assert pestel.industry == "Tech Industry"
    assert len(pestel.factors) == 0


def test_add_factor():
    pestel = PESTEL("Tech")
    pestel.add_factor("Political", "New regulations", 4, 3)
    assert len(pestel.factors) == 1
    assert pestel.factors[0]['score'] == 12


def test_invalid_category():
    pestel = PESTEL("Tech")
    with pytest.raises(ValueError):
        pestel.add_factor("Invalid", "Test", 3, 3)


def test_invalid_scores():
    pestel = PESTEL("Tech")
    with pytest.raises(ValueError):
        pestel.add_factor("Political", "Test", 6, 3)
