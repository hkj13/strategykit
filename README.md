# Business Frameworks 📊

A comprehensive Python toolkit for strategic business analysis, built specifically for MBA students, consultants, and business analysts.

## Features

- **Porter's Five Forces**: Analyze competitive intensity and attractiveness of industries
- **SWOT Analysis**: Identify strengths, weaknesses, opportunities, and threats with visualization
- **PESTEL Analysis**: Evaluate macro-environmental factors
- **Business Model Canvas**: Design and visualize business models
- **Value Chain Analysis**: Identify sources of competitive advantage
- **Competitive Positioning Maps**: Visualize market positions

## Installation

```bash
pip install business-frameworks
```

## Quick Start

### Porter's Five Forces Analysis

```python
from business_frameworks import PortersFiveForces

analysis = PortersFiveForces(
    industry="Smartphone Manufacturing",
    competitive_rivalry=5,
    supplier_power=3,
    buyer_power=4,
    threat_of_substitutes=2,
    threat_of_new_entrants=2
)

# Generate report
analysis.generate_report()

# Visualize
analysis.plot()
```

### SWOT Analysis

```python
from business_frameworks import SWOT

swot = SWOT(
    company="TechCorp",
    strengths=["Strong brand", "Innovation culture", "High margins"],
    weaknesses=["Limited distribution", "High prices"],
    opportunities=["Emerging markets", "AI integration"],
    threats=["Intense competition", "Regulation"]
)

# Create visualization
swot.plot()

# Export to PDF
swot.export_pdf("swot_analysis.pdf")
```

### PESTEL Analysis

```python
from business_frameworks import PESTEL

pestel = PESTEL(industry="E-commerce")
pestel.add_factor("Political", "Trade policies", impact=4, likelihood=3)
pestel.add_factor("Economic", "GDP growth", impact=5, likelihood=4)
pestel.add_factor("Social", "Digital adoption", impact=5, likelihood=5)

pestel.generate_report()
pestel.plot_impact_matrix()
```

## Requirements

- Python 3.8+
- matplotlib
- pandas
- numpy

## Development

```bash
# Clone the repository
git clone https://github.com/hkj13/business-frameworks.git
cd business-frameworks

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src tests
ruff check src tests
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Roadmap

- [ ] Value Chain Analysis
- [ ] Competitive Positioning Maps
- [ ] BCG Matrix
- [ ] Ansoff Matrix
- [ ] McKinsey 7S Framework
- [ ] Export to PowerPoint
- [ ] Interactive dashboards

## Support

- Documentation: [https://strategykit.readthedocs.io](https://strategykit.readthedocs.io)
- Issues: [GitHub Issues](https://github.com/hkj13/business-frameworks/issues)
