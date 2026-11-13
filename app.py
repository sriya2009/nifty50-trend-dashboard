
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NIFTY AI | Trend Insights",
    page_icon="📈",
    layout="wide"
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #10152f, #211b48);
    color: #f4f6ff;
}
h1, h2, h3 {
    color: #f4f6ff;
}
[data-testid="stMetric"] {
    background: #20294d;
    border: 1px solid #52618e;
    padding: 18px;
    border-radius: 12px;
}
div.stButton > button {
    background: #24c9d8;
    color: #10152f;
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("📈 NIFTY AI")
st.subheader("AI-Powered Nifty 50 Trend Prediction")
st.caption("Technical Indicator-Based Random Forest Classification")

st.divider()

# ---------- PROJECT STATUS ----------
st.markdown("### Market Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Predicted Trend", "Awaiting Model")
col2.metric("Trading Signal", "Pending")
col3.metric("Model", "Random Forest")

st.info(
    "The prediction model is under development. "
    "Actual market predictions will appear after model integration."
)

# ---------- DATASET UPLOAD ----------
st.markdown("### Historical Market Data")

uploaded_file = st.file_uploader(
    "Upload processed Nifty 50 CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.markdown("#### Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.markdown("#### Dataset Information")

    c1, c2 = st.columns(2)
    c1.metric("Total Rows", len(df))
    c2.metric("Total Columns", len(df.columns))

    st.markdown("#### Available Features")
    st.write(list(df.columns))

    indicators = [
        col for col in ["RSI", "EMA", "MACD"]
        if col in df.columns
    ]

    if indicators:
        st.markdown("#### Technical Indicators")
        st.dataframe(
            df[indicators].tail(10),
            use_container_width=True
        )
    else:
        st.warning(
            "RSI, EMA or MACD columns are not available yet."
        )

else:
    st.warning(
        "Upload the processed Nifty 50 dataset to view market information."
    )

# ---------- MODEL SECTION ----------
st.divider()
st.markdown("### Random Forest Prediction")

st.write(
    "Our proposed model will classify the next trading-day trend "
    "into Bullish, Bearish or Sideways."
)

st.markdown("""
- 🟢 Bullish → BUY
- 🔴 Bearish → SELL
- 🟡 Sideways → HOLD
""")

st.warning(
    "Predictions and performance metrics will be displayed "
    "after the actual model has been trained and integrated."
)

# ---------- FOOTER ----------
st.divider()
st.caption(
    "ASTRAQUANT X 2026 | KL University | Team Project"
)
