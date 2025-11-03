# Quick Start Guide - Business Frameworks

## Installation

```bash
# From your local directory (for now)
cd /Users/hk/CascadeProjects/strategykit
pip install -e .

# Once on PyPI (coming soon):
# pip install business-frameworks
```

## 5 Strategic Frameworks - Quick Examples

### 1. Porter's Five Forces 🏭

**When to use:** Analyze industry attractiveness before entering or investing

```python
from business_frameworks import PortersFiveForces

# Create analysis
porters = PortersFiveForces(
    industry="E-commerce",
    competitive_rivalry=4,      # 1-5 scale (5 = highest)
    supplier_power=2,
    buyer_power=5,
    threat_of_substitutes=3,
    threat_of_new_entrants=3
)

# Add details
porters.add_factor("Competitive Rivalry", "Amazon dominates market")

# Get insights
porters.generate_report()
porters.plot()  # Shows radar chart
```

**Real Example:** Use this before entering a new market or when considering mergers/acquisitions.

---

### 2. SWOT Analysis 📝

**When to use:** Internal strategy review, board presentations, business planning

```python
from business_frameworks import SWOT

swot = SWOT(
    company="Your Company",
    strengths=["Strong brand", "Loyal customers", "Good cash flow"],
    weaknesses=["High costs", "Limited presence"],
    opportunities=["New market", "Technology trends"],
    threats=["Competition", "Regulations"]
)

swot.generate_report()
swot.plot()  # Shows 2x2 matrix
```

**Real Example:** Quarterly strategic reviews, investor presentations, MBA case study prep.

---

### 3. PESTEL Analysis 🌍

**When to use:** Long-term planning, market entry decisions, risk assessment

```python
from business_frameworks import PESTEL

pestel = PESTEL(industry="Healthcare")

# Add factors with impact (1-5) and likelihood (1-5)
pestel.add_factor("Political", "Healthcare reform", impact=5, likelihood=4)
pestel.add_factor("Economic", "Recession risk", impact=4, likelihood=3)
pestel.add_factor("Social", "Aging population", impact=5, likelihood=5)
pestel.add_factor("Technological", "AI in diagnostics", impact=5, likelihood=4)
pestel.add_factor("Environmental", "Climate change", impact=3, likelihood=4)
pestel.add_factor("Legal", "Data privacy laws", impact=4, likelihood=5)

pestel.generate_report()
pestel.plot_impact_matrix()  # Shows scatter plot
```

**Real Example:** 5-year strategic planning, international expansion decisions.

---

### 4. BCG Matrix 💼

**When to use:** Product portfolio management, resource allocation decisions

```python
from business_frameworks import BCGMatrix

bcg = BCGMatrix("TechCorp")

# Add products/business units
bcg.add_business_unit(
    name="Cloud Services",
    market_share=1.5,   # Your share / leader's share (>1 = market leader)
    market_growth=20,    # Annual growth rate %
    revenue=500         # Revenue in millions (for bubble size)
)

bcg.add_business_unit("Legacy Software", market_share=2.0, market_growth=3, revenue=300)
bcg.add_business_unit("Mobile Apps", market_share=0.6, market_growth=25, revenue=100)
bcg.add_business_unit("Hardware", market_share=0.3, market_growth=2, revenue=50)

bcg.generate_recommendations()
bcg.plot()  # Shows bubble chart with quadrants
```

**Categories:**
- **Stars** (High growth, High share): Invest heavily
- **Cash Cows** (Low growth, High share): Milk for cash
- **Question Marks** (High growth, Low share): Invest or divest
- **Dogs** (Low growth, Low share): Consider divesting

**Real Example:** Annual budget allocation, deciding which products to invest in or kill.

---

### 5. Ansoff Matrix 🚀

**When to use:** Growth strategy planning, expansion decisions

```python
from business_frameworks import AnsoffMatrix

ansoff = AnsoffMatrix("RetailCo", current_strategy="Market Penetration")

# Add strategies with initiatives
ansoff.add_strategy("Market Penetration", 
    initiatives=[
        "Increase advertising",
        "Loyalty programs",
        "Competitive pricing"
    ],
    priority=1
)

ansoff.add_strategy("Market Development",
    initiatives=[
        "Expand to new cities",
        "Target new demographics",
        "Online sales channel"
    ],
    priority=2
)

ansoff.add_strategy("Product Development",
    initiatives=[
        "Launch new product line",
        "Add premium versions",
        "Bundle offerings"
    ],
    priority=3
)

ansoff.add_strategy("Diversification",
    initiatives=[
        "Enter related industry",
        "Acquire competitor",
        "New business model"
    ],
    priority=4
)

ansoff.generate_report()
ansoff.plot()  # Shows 2x2 matrix with risk levels
```

**Risk Levels:**
- Market Penetration: LOW risk
- Market/Product Development: MEDIUM risk
- Diversification: HIGH risk

**Real Example:** Strategic planning sessions, growth roadmap creation.

---

## Complete Real-World Example

See `examples/real_world_case_study.py` for a comprehensive analysis of "CoffeeChain Inc." using ALL 5 frameworks together!

```bash
python examples/real_world_case_study.py
```

This shows you how to:
1. Use multiple frameworks in sequence
2. Integrate insights across frameworks
3. Generate comprehensive recommendations

---

## Tips for MBA Case Studies

### Case Prep Workflow:

1. **Start with Porter's** - Understand industry dynamics
2. **Run PESTEL** - Identify external factors
3. **Do SWOT** - Analyze the specific company
4. **Use BCG** (if multi-product) - Prioritize investments
5. **End with Ansoff** - Recommend growth strategy

### For Presentations:

```python
# Save visualizations
porters.plot(save_path="porters.png")
swot.plot(save_path="swot.png")
bcg.plot(save_path="bcg.png")

# Copy images to PowerPoint
```

### For Reports:

```python
# Generate text reports
report = ""
report += porters.generate_report()
report += swot.generate_report()
report += bcg.generate_recommendations()

# Save to file
with open("analysis_report.txt", "w") as f:
    f.write(report)
```

---

## Common Use Cases

### Consulting Interview Prep
```python
# Quick framework for case interviews
porters = PortersFiveForces("Industry X", 4, 3, 4, 2, 3)
porters.generate_report()
```

### Startup Business Plan
```python
# Analyze your startup's position
swot = SWOT("MyStartup", 
    strengths=["Innovative tech", "Strong team"],
    weaknesses=["No revenue yet", "Limited funding"],
    opportunities=["Growing market", "No dominant player"],
    threats=["Established competitors", "Tech changes"])
swot.plot()
```

### Corporate Strategy Review
```python
# Full portfolio analysis
bcg = BCGMatrix("YourCorp")
# Add all business units...
bcg.generate_recommendations()
```

---

## Next Steps

1. **Try the examples** - Run `examples/quick_demo.py`
2. **Analyze your own company** - Pick one framework and start
3. **Prepare for case interviews** - Practice with Porter's and SWOT
4. **Create presentations** - Use `.plot()` to generate visuals

## Need Help?

- GitHub Issues: https://github.com/hkj13/strategykit/issues
- Read the code: All frameworks have detailed docstrings
- Check `examples/` folder for more examples

## What's Next?

Coming in future versions:
- Value Chain Analysis
- McKinsey 7S Framework
- Competitive Positioning Maps
- PDF report export
- PowerPoint generation

---

**Happy Analyzing! 📊**
