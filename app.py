import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import psycopg2
# Configure the webpage layout
st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

# --- Fetch Data ---
# @st.cache_data prevents Streamlit from querying the DB every time you click a button
@st.cache_data(ttl=600)
def load_data():
    
    DB_URL = st.secrets["NEON_DB_URL"]
    engine = create_engine(DB_URL)
    # SQL query to pull all data and sort by newest first
    query = "SELECT * FROM air_quality ORDER BY timestamp DESC"
    df = pd.read_sql(query, engine)
    return df

# Load the dataframe
df = load_data()

# --- Build the UI ---
st.title("🌬️ Real-Time Air Quality Monitor - Patna")
st.markdown("Live data extracted automatically via GitHub Actions.")

if df.empty:
    st.warning("No data found in the database. Wait for the pipeline to run!")
else:
    # 1. Top-Level Metric Cards
    latest_data = df.iloc[0] # Grab the most recent row
    col1, col2, col3 = st.columns(3)
    col1.metric("Current AQI Level", latest_data["aqi"])
    col2.metric("PM 2.5 Concentration", f'{latest_data["pm2_5"]} µg/m³')
    col3.metric("Last Updated", latest_data["timestamp"])

    st.divider()

    # 2. Interactive Line Chart
    st.subheader("Pollution Trends Over Time")
    fig = px.line(
        df, 
        x="timestamp", 
        y=["pm2_5", "pm10"], 
        markers=True,
        labels={"value": "Concentration (µg/m³)", "timestamp": "Time", "variable": "Pollutant"}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # 3. Raw Data Table
    with st.expander("View Raw Data Table"):
        st.dataframe(df)