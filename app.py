import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. SETUP
analyzer = SentimentIntensityAnalyzer()

# Try to load your Watchlist from GitHub
try:
    df_watchlist = pd.read_csv("Stock_Intelligence_Hub - Watchlist.csv")
    watchlist = df_watchlist['Symbol'].tolist()
except:
    watchlist = ["BHARTIARTL", "RELIANCE", "TCS"]

st.title("🚀 VestIQ Intelligence Command Center")

# 2. SIDEBAR - Navigation & Input
st.sidebar.header("Navigation")
selected_stock = st.sidebar.selectbox("Choose Stock", ["Enter Manually"] + watchlist)
ticker = st.sidebar.text_input("Ticker Symbol", selected_stock) if selected_stock == "Enter Manually" else selected_stock

st.sidebar.markdown("---")
st.sidebar.info("System Status: Live & Optimized")

# 3. INPUT AREA
summary_input = st.text_area("Paste Management Summary / Result Data here:", height=300)

if st.button("Generate Intelligence Report"):
    if summary_input.strip() != "":
        # ANALYSIS LOGIC
        vs = analyzer.polarity_scores(summary_input)
        score = vs['compound']
        
        # --- THE REPORT OUTPUT ---
        st.markdown(f"## 📊 Analysis Report for {ticker}")
        
        # Visual Summary Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Sentiment Score", f"{score:.2f}")
        with col2:
            sentiment_label = "BULLISH" if score > 0.05 else "BEARISH" if score < -0.05 else "NEUTRAL"
            st.write(f"**Verdict:** {sentiment_label}")
        with col3:
            st.write(f"**Status:** Analysis Success")

        # FILTERED INSIGHTS (The "Analysis" Part)
        st.subheader("🎯 Key Financial Triggers")
        
        # We split the long text into sentences and only show the ones that matter
        sentences = summary_input.split('.')
        triggers = ['growth', 'capex', 'debt', 'revenue', 'margin', 'ebitda', 'profit', 'expansion']
        
        found_triggers = []
        for s in sentences:
            if any(t in s.lower() for t in triggers):
                found_triggers.append(s.strip())
        
        if found_triggers:
            for item in found_triggers:
                st.write(f"✅ {item}.")
        else:
            st.info("No major financial triggers detected. Content appears to be general narrative.")

        # --- EXPORT OPTION ---
        st.download_button(
            label="📩 Download Report",
            data=f"Ticker: {ticker}\nSentiment: {sentiment_label} ({score})\n\nInsights:\n" + "\n".join(found_triggers),
            file_name=f"{ticker}_Analysis.txt"
        )
    else:
        st.error("Error: No content found. Please paste data into the box above.")

# 4. COMPLIANCE
st.markdown("---")
st.caption("Financial Disclaimer: Provided by VestIQ Tech Intelligence Pvt Ltd. This AI analysis is for educational use only and does not constitute investment advice.")
