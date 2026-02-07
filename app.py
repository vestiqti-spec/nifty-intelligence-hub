import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime
import pytz  # For India Time

# 1. SETUP: Local Time Logic
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.datetime.now(IST)

st.set_page_config(page_title="VestIQ Intelligence Hub", layout="wide")
analyzer = SentimentIntensityAnalyzer()

# Display Local Time
st.title("📈 Nifty 500 AI Analyst")
st.write(f"**Local Analysis Time:** {datetime_ist.strftime('%Y-%m-%d %H:%M:%S')} IST")
st.write("Leapfrog the market with automated management sentiment analysis.")

# 2. INPUT
ticker = st.text_input("Enter Stock Ticker (e.g., RELIANCE):", "RELIANCE")
summary_text = st.text_area("Paste Management Summary or Annual Report Snippet here:", height=300)

# 3. LOGIC
if st.button("Generate God-Tier Insights"):
    if summary_text:
        vs = analyzer.polarity_scores(summary_text)
        score = vs['compound']
        
        st.subheader(f"Analysis for {ticker}")
        
        # Professional Result Display
        col1, col2 = st.columns(2)
        with col1:
            if score >= 0.05:
                st.success(f"BULLISH Sentiment (Score: {score})")
            elif score <= -0.05:
                st.error(f"BEARISH Sentiment (Score: {score})")
            else:
                st.warning(f"NEUTRAL Sentiment (Score: {score})")

        with col2:
            st.info("Key Market Indicators Found:")
            sentences = summary_text.split('.')
            for s in sentences:
                # High-leverage keywords
                if any(word in s.lower() for word in ['growth', 'debt', 'revenue', 'margin', 'capex', 'guidance']):
                    st.write(f"✅ {s.strip()}")
    else:
        st.error("Please paste some text first!")

# 4. LEGAL
st.markdown("---")
st.caption("Financial Disclaimer: Provided by VestIQ Tech Intelligence Pvt Ltd. All rights reserved. Not SEBI registered.")
