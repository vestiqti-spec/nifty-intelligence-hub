import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime
import pytz 

# Time Setup
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.datetime.now(IST)

st.set_page_config(page_title="VestIQ Intelligence", layout="wide")
analyzer = SentimentIntensityAnalyzer()

st.title("🚀 Nifty 500 Intelligence Hub")
st.caption(f"Analysis generated at: {datetime_ist.strftime('%Y-%m-%d %H:%M:%S')} IST")

# Sidebar for Ticker
ticker = st.sidebar.text_input("Stock Ticker", "RELIANCE")
st.sidebar.markdown("---")
st.sidebar.info("This tool scans management commentary for sentiment and high-leverage financial keywords.")

# Main Input
summary_text = st.text_area("Paste Management Summary / Result Snippets:", height=250)

if st.button("Extract Alpha"):
    if summary_text:
        score = analyzer.polarity_scores(summary_text)['compound']
        
        # Dashboard Style Columns
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("Verdict")
            label = "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"
            st.metric(label="Sentiment Score", value=label, delta=f"{score:.2f}")
            
        with col2:
            st.subheader("High-Leverage Insights")
            sentences = summary_text.split('.')
            for s in sentences:
                if any(word in s.lower() for word in ['growth', 'debt', 'revenue', 'margin', 'capex', 'guidance', 'profit']):
                    st.write(f"🎯 {s.strip()}.")
    else:
        st.warning("Input required to begin analysis.")

# Mandatory Disclaimer
st.markdown("---")
st.caption("Financial Disclaimer: Provided by VestIQ Tech Intelligence Pvt Ltd. For educational purposes only. Market investments are subject to risk.")
