# 🌍 Live Air Quality Dashboard

💨 **Live Application:** [View the Live Air Quality Dashboard Here](https://air-quality-pipeline-agrdmw33wsnfbxf7vvs3zb.streamlit.app/)

## 📌 Project Overview
The **Live Air Quality Dashboard** is a real-time data visualization tool that monitors the Air Quality Index (AQI) and key pollutant levels (PM2.5, PM10, NO2, O3) across various global or regional locations. It connects to live environmental APIs to extract, process, and visualize critical atmospheric data.

This project demonstrates the ability to handle live JSON streams from REST APIs, perform environmental data transformations, and build an interactive user interface for public health monitoring.

## 🚀 Key Features
- **Real-Time AQI Extraction:** Fetches live air quality and pollutant metrics via the OpenWeather API.
- **Geospatial Visualization:** Maps station locations and visually scales markers based on AQI severity.
- **Dynamic Filtering:** Allows users to filter data by specific cities, regions, or pollutant types.
- **Cloud Deployment:** Fully deployed and continuously hosted on Streamlit Cloud.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Processing:** Pandas, Requests, JSON
- **Visualization/UI:** Streamlit, Plotly
- **External API:** OpenWeather API

**1. Clone the repository**
```bash
git clone [https://github.com/harshaey-555/air-quality-pipeline.git](https://github.com/harshaey-555/air-quality-pipeline.git)
cd air-quality-pipeline
```
**2. Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
**3. Install dependencies**

```bash
pip install -r requirements.txt
```
**4. Set up environment variables**
Create a .env file or use st.secrets to safely store your API key:

```text
AQI_API_KEY="your_api_key_here"
```
**5. Run the application**

```Bash
streamlit run app.py
```
## 📈 Future Scope
- Integrate a time-series forecasting model to predict tomorrow's AQI based on historical trends.
- Add automated email/SMS alerts when a user's local AQI enters the "Unhealthy" or "Hazardous" ranges.
