import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_financial_data(num_quarters=12):
    """
    Generate synthetic quarterly financial data for demonstration
    """
    np.random.seed(42)
    
    # Generate quarters
    start_year = 2022
    quarters = []
    for i in range(num_quarters):
        year = start_year + (i // 4)
        quarter = (i % 4) + 1
        quarters.append(f"Q{quarter} {year}")
    
    # Base values with growth trend
    base_revenue = 1000000
    growth_rate = 0.05
    
    data = []
    
    for i, quarter in enumerate(quarters):
        # Revenue with growth and seasonality
        seasonal_factor = 1 + 0.1 * np.sin(i * np.pi / 2)
        revenue = base_revenue * (1 + growth_rate) ** i * seasonal_factor * np.random.uniform(0.95, 1.05)
        
        # Operating expenses (60-70% of revenue)
        operating_expenses = revenue * np.random.uniform(0.60, 0.70)
        
        # Net profit (after all expenses and taxes)
        gross_profit = revenue - operating_expenses
        net_profit = gross_profit * np.random.uniform(0.60, 0.75)
        
        # Assets (growing with business)
        total_assets = revenue * np.random.uniform(2.5, 3.5)
        current_assets = total_assets * np.random.uniform(0.35, 0.45)
        
        # Liabilities
        current_liabilities = current_assets * np.random.uniform(0.40, 0.60)
        total_liabilities = total_assets * np.random.uniform(0.45, 0.55)
        
        # Equity
        equity = total_assets - total_liabilities
        
        data.append({
            'Quarter': quarter,
            'Revenue': round(revenue, 2),
            'Operating_Expenses': round(operating_expenses, 2),
            'Net_Profit': round(net_profit, 2),
            'Total_Assets': round(total_assets, 2),
            'Current_Assets': round(current_assets, 2),
            'Current_Liabilities': round(current_liabilities, 2),
            'Equity': round(equity, 2)
        })
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Generate data
    df = generate_financial_data(num_quarters=12)
    
    # Save to Excel
    df.to_excel('financial_data.xlsx', index=False, sheet_name='Financial Data')
    
    print("✅ Financial data generated successfully!")
    print(f"📊 Created {len(df)} quarters of data")
    print(f"💾 Saved to: financial_data.xlsx")
    print("\nSample data:")
    print(df.head())
    print("\nFinancial metrics summary:")
    print(f"Average Revenue: ${df['Revenue'].mean():,.0f}")
    print(f"Average Net Profit: ${df['Net_Profit'].mean():,.0f}")
    print(f"Average Profit Margin: {(df['Net_Profit'] / df['Revenue'] * 100).mean():.1f}%")
