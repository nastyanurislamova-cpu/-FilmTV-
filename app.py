import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Financial Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Performance Analysis Dashboard")
st.markdown("### Analyze key financial metrics based on quarterly reports")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    data_source = st.radio(
        "Data Source",
        ["Upload File", "Use Sample Data"]
    )
    
    if data_source == "Upload File":
        uploaded_file = st.file_uploader("Upload Excel/CSV file", type=['xlsx', 'csv'])
    else:
        st.info("Using generated sample data")

# Load data
@st.cache_data
def load_sample_data():
    try:
        return pd.read_excel('financial_data.xlsx')
    except:
        st.warning("Sample data file not found. Please generate it first.")
        return None

if data_source == "Use Sample Data":
    df = load_sample_data()
else:
    if uploaded_file:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    else:
        df = None

if df is not None:
    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    
    latest_quarter = df.iloc[-1]
    prev_quarter = df.iloc[-2] if len(df) > 1 else latest_quarter
    
    with col1:
        revenue_change = ((latest_quarter['Revenue'] - prev_quarter['Revenue']) / prev_quarter['Revenue'] * 100)
        st.metric(
            "Latest Revenue",
            f"${latest_quarter['Revenue']:,.0f}",
            f"{revenue_change:+.1f}%"
        )
    
    with col2:
        profit_change = ((latest_quarter['Net_Profit'] - prev_quarter['Net_Profit']) / prev_quarter['Net_Profit'] * 100)
        st.metric(
            "Net Profit",
            f"${latest_quarter['Net_Profit']:,.0f}",
            f"{profit_change:+.1f}%"
        )
    
    with col3:
        st.metric(
            "Profit Margin",
            f"{(latest_quarter['Net_Profit'] / latest_quarter['Revenue'] * 100):.1f}%"
        )
    
    with col4:
        st.metric(
            "ROE",
            f"{(latest_quarter['Net_Profit'] / latest_quarter['Equity'] * 100):.1f}%"
        )
    
    # Tabs for different analyses
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Trends", "💰 Profitability", "💧 Liquidity", "📊 Ratios"])
    
    with tab1:
        st.subheader("Revenue and Profit Trends")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Quarter'], y=df['Revenue'], name='Revenue', line=dict(color='blue', width=3)))
        fig.add_trace(go.Scatter(x=df['Quarter'], y=df['Net_Profit'], name='Net Profit', line=dict(color='green', width=3)))
        fig.update_layout(height=400, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Operating Expenses")
        fig2 = px.bar(df, x='Quarter', y='Operating_Expenses', title='Quarterly Operating Expenses')
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        st.subheader("Profitability Analysis")
        
        df['Profit_Margin'] = (df['Net_Profit'] / df['Revenue'] * 100)
        df['ROA'] = (df['Net_Profit'] / df['Total_Assets'] * 100)
        df['ROE'] = (df['Net_Profit'] / df['Equity'] * 100)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.line(df, x='Quarter', y='Profit_Margin', title='Profit Margin (%)', markers=True)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df['Quarter'], y=df['ROA'], name='ROA', mode='lines+markers'))
            fig.add_trace(go.Scatter(x=df['Quarter'], y=df['ROE'], name='ROE', mode='lines+markers'))
            fig.update_layout(title='Return Ratios (%)', hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("Liquidity Indicators")
        
        df['Current_Ratio'] = df['Current_Assets'] / df['Current_Liabilities']
        df['Quick_Ratio'] = (df['Current_Assets'] - df['Current_Assets'] * 0.3) / df['Current_Liabilities']
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.line(df, x='Quarter', y='Current_Ratio', title='Current Ratio', markers=True)
            fig.add_hline(y=2.0, line_dash="dash", line_color="green", annotation_text="Healthy Level")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.line(df, x='Quarter', y='Quick_Ratio', title='Quick Ratio', markers=True)
            fig.add_hline(y=1.0, line_dash="dash", line_color="green", annotation_text="Healthy Level")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.subheader("Financial Ratios Summary")
        
        ratios_df = pd.DataFrame({
            'Quarter': df['Quarter'],
            'Profit Margin (%)': df['Profit_Margin'],
            'ROA (%)': df['ROA'],
            'ROE (%)': df['ROE'],
            'Current Ratio': df['Current_Ratio'],
            'Debt to Equity': df['Total_Assets'] / df['Equity'] - 1
        })
        
        st.dataframe(ratios_df.style.format({
            'Profit Margin (%)': '{:.2f}',
            'ROA (%)': '{:.2f}',
            'ROE (%)': '{:.2f}',
            'Current Ratio': '{:.2f}',
            'Debt to Equity': '{:.2f}'
        }), use_container_width=True)
        
        # Download button
        csv = ratios_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Analysis",
            data=csv,
            file_name=f"financial_analysis_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

else:
    st.info("👆 Please upload a file or select 'Use Sample Data' to begin analysis")
    
    with st.expander("📋 Expected Data Format"):
        st.markdown("""
        Your file should contain the following columns:
        - **Quarter**: Period identifier (e.g., Q1 2024)
        - **Revenue**: Total revenue
        - **Operating_Expenses**: Operating costs
        - **Net_Profit**: Net profit after taxes
        - **Total_Assets**: Total company assets
        - **Current_Assets**: Short-term assets
        - **Current_Liabilities**: Short-term liabilities
        - **Equity**: Shareholders' equity
        """)

st.markdown("---")
st.markdown("💡 **Tip**: Use the sidebar to switch between uploaded data and sample data")
