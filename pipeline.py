import requests
import pandas as pd
from datetime import datetime
import psycopg2
from sqlalchemy import create_engine
import os


API_KEY = os.environ.get("OPENWEATHER_API_KEY")
DB_URL = os.environ.get("NEON_DB_URL")
# Configuration
LAT = 25.5941 
LON = 85.1376 

def fetch_and_clean_data():
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # 1. Extract the nested data
        aqi = data['list'][0]['main']['aqi']
        components = data['list'][0]['components']
        
        # 2. Convert Unix timestamp to local readable time
        unix_time = data['list'][0]['dt']
        readable_time = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
        
        # 3. Create a clean, flat dictionary
        clean_record = {
            "timestamp": readable_time,
            "city": "Patna",
            "aqi": aqi, 
            "pm2_5": components.get("pm2_5"),
            "pm10": components.get("pm10"),
            "no2": components.get("no2"),
            "o3": components.get("o3")
        }
        return clean_record
    else:
        print(f"Failed with status code: {response.status_code}")
        return None

# Execute the function
record = fetch_and_clean_data()

if record:
    # 4. Load the dictionary into a Pandas DataFrame
    df = pd.DataFrame([record])
    print("\n--- Cleaned DataFrame ---")
    print("\nConnecting to database...")
engine = create_engine(DB_URL)

# Push the DataFrame to a table named 'air_quality'
df.to_sql("air_quality", engine, if_exists="append", index=False)

print("Success! Data loaded into PostgreSQL.")