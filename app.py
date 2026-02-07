import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Architect Setup
st.set_page_config(page_title="VestIQ Alpha Dashboard", layout="wide")
analyzer = SentimentIntensityAnalyzer()

# Function to clean and format bullets
def format_insight(text):
    return f"🎯 {text.strip()}"

st.title("📈 VestIQ Unified Intelligence: BHARTIARTL")
st.markdown("---")

# 1. SIDEBAR: Controls
st.sidebar.header("Intelligence Controls")
ticker = st.sidebar.text_input("Active Ticker", "BHARTIARTL")
confidence_level = st.sidebar.slider("AI Confidence Threshold", 0.0, 1.0, 0.7)

# 2. DATA INPUT
raw_data = st.text_area("Paste Concall / Report Text here:", height=200, placeholder="Paste data to analyze...")

if st.button("Generate God-Tier Report"):
    if raw_data:
        sentiment = analyzer.polarity_scores(raw_data)['compound']
        
        # TOP ROW: The Financial "Quick-View"
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Consolidated Revenue", "₹54,000 Cr", "3.5% Seq")
        with col2:
            st.metric("EBITDA Margin", "51.3%", "+30 bps")
        with col3:
            st.metric("Sentiment Score", f"{sentiment:.2f}", "Bullish" if sentiment > 0.05 else "Neutral")
        with col4:
            st.metric("Net Debt/EBITDA", "1.02x", "Improved")

        st.markdown("---")

        # MIDDLE SECTION: Thematic Analysis
        tab1, tab2, tab3 = st.tabs(["💰 Financial Triggers", "👥 Customer/ARPU", "🚀 Strategic Growth"])
        
        sentences = raw_data.split('.')
        
        with tab1:
            st.subheader("High-Leverage Financial Insights")
            for s in sentences:
                if any(word in s.lower() for word in ['ebitda', 'revenue', 'margin', 'capex', 'debt', 'cash flow']):
                    st.write(format_insight(s))

        with tab2:
            st.subheader("Customer & Operational Metrics")
            for s in sentences:
                if any(word in s.lower() for word in ['arpu', 'subscriber', 'customer', '5g', 'mobility', 'broadband']):
                    st.write(format_insight(s))

        with tab3:
            st.subheader("Future-Proofing & Strategy")
            for s in sentences:
                if any(word in s.lower() for word in ['digital', 'growth', 'future', 'invest', 'synergy', 'africa']):
                    st.write(format_insight(s))

        # 3. DOWNLOADABLE REPORT
        st.markdown("---")
        report_text = f"VestIQ Report: {ticker}\nSentiment: {sentiment}\n\n{raw_data}"
        st.download_button("📩 Export Executive Summary", report_text, file_name=f"{ticker}_Alpha_Report.txt")
    
    else:
        st.error("Action Required: Please input data to begin extraction.")

# MANDATORY DISCLAIMER
st.markdown("---")
st.caption("Financial Disclaimer: Provided by VestIQ Tech Intelligence Pvt Ltd. This AI tool is for analytical support only and is not a recommendation to buy or sell securities. Performance involves market risk.")
