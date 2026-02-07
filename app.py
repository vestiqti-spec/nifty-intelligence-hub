import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize tools
analyzer = SentimentIntensityAnalyzer()

# Load Watchlist from your uploaded CSV
try:
    df_watchlist = pd.read_csv("Stock_Intelligence_Hub - Watchlist.csv")
    watchlist = df_watchlist['Symbol'].tolist()
except:
    watchlist = ["BHARTIARTL", "RELIANCE", "TCS"]

st.title("🚀 VestIQ Stock Intelligence Hub")

# Sidebar
selected_stock = st.sidebar.selectbox("Watchlist", ["Enter Manually"] + watchlist)
ticker = st.sidebar.text_input("Ticker", selected_stock) if selected_stock == "Enter Manually" else selected_stock

# Input Section
summary_text = st.text_area("Paste Management Summary / Concall Text here:", height=300)

if st.button("Generate Intelligence Report"):
    if summary_text:
        # 1. Sentiment Calculation
        score = analyzer.polarity_scores(summary_text)['compound']
        
        # 2. THE REPORT SECTION (This is what was missing)
        st.markdown(f"## 📊 Intelligence Report: {ticker}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Sentiment Score", f"{score:.2f}")
            if score > 0.05:
                st.success("✅ BULLISH BIAS")
            elif score < -0.05:
                st.error("⚠️ BEARISH BIAS")
            else:
                st.warning("⚖️ NEUTRAL")

        with col2:
            st.subheader("Key Financial Triggers")
            sentences = summary_text.split('.')
            found = False
            for s in sentences:
                if any(word in s.lower() for word in ['growth', 'capex', 'debt', 'revenue', 'margin', 'profit']):
                    st.write(f"🎯 {s.strip()}")
                    found = True
            if not found:
                st.write("No specific financial triggers detected in text.")
        
        # 3. Add a Download Button for your records
        report_data = f"Report for {ticker}\nSentiment: {score}\n\nText: {summary_text}"
        st.download_button("📩 Download Analysis Report", report_data, file_name=f"{ticker}_report.txt")
        
    else:
        st.error("Please paste text to analyze!")

# Legal Protection
st.markdown("---")
st.caption("Financial Disclaimer: Provided by VestIQ Tech Intelligence Pvt Ltd. This is an AI-generated analysis and not investment advice.")
