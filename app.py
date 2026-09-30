import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chennai Jobs Dashboard", layout="wide")

# DARK THEME CSS
st.markdown("""
<style>
   .stApp { background-color: #0E1117; color: white; }
    [data-testid="stSidebar"] { background-color: #1A1C24; }
    h1, h2, h3 { color: #00D4FF!important; }
    div[data-testid="metric-container"] {
        background-color: #262730;
        border: 1px solid #00D4FF;
        padding: 10px;
        border-radius: 10px;
    }
   .stDataFrame { background-color: #262730; }
</style>
""", unsafe_allow_html=True)

st.title("🌃 Chennai Jobs Live Dashboard - 300 Jobs")
st.markdown("---")

df = pd.read_csv("chennai_jobs.csv")

area_filter = st.sidebar.multiselect("Select Area", df['area'].unique(), default=df['area'].unique())
filtered_df = df[df['area'].isin(area_filter)]

col1, col2, col3 = st.columns(3)
col1.metric("Total Jobs", len(filtered_df))
col2.metric("Avg Salary", f"₹{int(filtered_df['salary_inr'].mean()):,}")
col3.metric("Top Area", filtered_df['area'].mode()[0])

col1, col2 = st.columns(2)
with col1:
    st.subheader("💰 Avg Salary by Area")
    st.bar_chart(filtered_df.groupby('area')['salary_inr'].mean(), color="#00D4FF")

with col2:
    st.subheader("📍 Jobs by Area")
    st.bar_chart(filtered_df['area'].value_counts(), color="#FF4B4B")

st.subheader("📋 Job Details")
st.dataframe(filtered_df, use_container_width=True)

st.success("💡 OMR & Sholinganallur = Highest Paying IT Corridor!")