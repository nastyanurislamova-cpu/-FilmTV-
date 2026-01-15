# Financial Performance Analysis Dashboard

Interactive dashboard for analyzing key financial metrics of a company based on quarterly accounting reports.

## 📊 Overview

This application provides comprehensive analysis of financial performance indicators including:
- Revenue and profit dynamics
- Profitability ratios (ROA, ROE, profit margins)
- Liquidity indicators (current ratio, quick ratio)
- Financial leverage metrics
- Trend analysis and forecasting

## 🚀 Features

- **Interactive Visualizations**: Dynamic charts showing quarterly trends
- **Comparative Analysis**: Period-over-period comparison of key metrics
- **Financial Ratios**: Automatic calculation of important financial indicators
- **Data Export**: Download analysis results in various formats
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Technology Stack 

- **Python 3.11+**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive visualizations
- **Docker** - Containerization

## 📦 Installation

### Using Docker (Recommended)

Pull from Docker Hub:
```bash
docker pull nastyanurislamova/financial-analysis:latest
docker run -p 8501:8501 nastyanurislamova/financial-analysis:latest
```

Or build locally:
```bash
docker build -t financial-analysis .
docker run -p 8501:8501 financial-analysis
```

### Local Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📈 Usage

1. Launch the application
2. Upload your financial data (Excel/CSV format) or use generated sample data
3. Select the metrics you want to analyze
4. Explore interactive charts and insights

## 📄 Data Format

The application expects quarterly financial data with the following structure:
- Quarter/Period
- Revenue
- Operating Expenses
- Net Profit
- Total Assets
- Current Assets
- Current Liabilities
- Equity

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Live Demo](https://nastyanurislamova.streamlit.app/)
- [Docker Hub](https://hub.docker.com/r/nastyanurislamova/financial-analysis)
- [Documentation](https://github.com/yourusername/financial-analysis)

---

**Note**: This application uses synthetic data for demonstration purposes. For production use, please provide actual financial statements.
