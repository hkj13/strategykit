"""Tests for BCG Matrix"""

from business_frameworks import BCGMatrix


def test_bcg_creation():
    bcg = BCGMatrix("TestCorp")
    assert bcg.company == "TestCorp"
    assert len(bcg.business_units) == 0


def test_add_business_unit():
    bcg = BCGMatrix("TestCorp")
    bcg.add_business_unit("Product A", market_share=1.5, market_growth=20, revenue=100)
    assert len(bcg.business_units) == 1
    assert bcg.business_units[0].name == "Product A"


def test_business_unit_category():
    bcg = BCGMatrix("TestCorp")
    bcg.add_business_unit("Star", market_share=2.0, market_growth=15, revenue=100)
    bcg.add_business_unit("Cash Cow", market_share=1.5, market_growth=3, revenue=80)
    bcg.add_business_unit("Question Mark", market_share=0.5, market_growth=25, revenue=50)
    bcg.add_business_unit("Dog", market_share=0.3, market_growth=2, revenue=20)
    
    assert bcg.business_units[0].get_category() == "Star"
    assert bcg.business_units[1].get_category() == "Cash Cow"
    assert bcg.business_units[2].get_category() == "Question Mark"
    assert bcg.business_units[3].get_category() == "Dog"


def test_portfolio_summary():
    bcg = BCGMatrix("TestCorp")
    bcg.add_business_unit("Star1", market_share=2.0, market_growth=15, revenue=100)
    bcg.add_business_unit("Dog1", market_share=0.3, market_growth=2, revenue=20)
    
    summary = bcg.get_portfolio_summary()
    assert len(summary["Star"]) == 1
    assert len(summary["Dog"]) == 1
    assert "Star1" in summary["Star"]
