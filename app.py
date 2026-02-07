import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. SETUP: The look of your app
st.set_page_config(page_title="VestIQ Intelligence Hub", layout="wide")
analyzer = SentimentIntensityAnalyzer()

st.title("📈 Nifty 500 AI Analyst")
st.write("Leapfrog the market with automated management sentiment analysis.")

# 2. INPUT: Where you put the data
ticker = st.text_input("Enter Stock Ticker (e.g., RELIANCE):", "RELIANCE")
summary_text = st.text_area("Paste Management Summary or Annual Report Snippet here:", height=300)

# 3. LOGIC: The 'Thinking' part
if st.button("Analyze Now"):
    if summary_text:
        # Calculate Sentiment
        vs = analyzer.polarity_scores(summary_text)
        score = vs['compound']
        
        # Display Results
        st.subheader(f"Analysis for {ticker}")
        
        if score >= 0.05:
            st.success(f"BULLISH Sentiment Detected (Score: {score})")
        elif score <= -0.05:
            st.error(f"BEARISH Sentiment Detected (Score: {score})")
        else:
            st.warning(f"NEUTRAL Sentiment (Score: {score})")

        # Basic Insight Extraction (finding lines with 'growth' or 'debt')
        st.info("Key Points Found:")
        sentences = summary_text.split('.')
        for s in sentences:
            if any(word in s.lower() for word in ['growth', 'debt', 'revenue', 'profit', 'capex']):
                st.write(f"- {s.strip()}")
    else:
        st.error("Please paste some text first!")

# 4. LEGAL: The mandatory protection
st.markdown("---")
st.caption("Financial Disclaimer: This tool is for educational purposes. Provided by VestIQ Tech Intelligence Pvt Ltd. We are not SEBI registered advisors.")
