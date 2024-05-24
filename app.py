import streamlit as st
import requests
import geopandas as gpd
import pandas as pd


st.markdown('''
# Taxi Fare Prediction Tool''')


query = None
response = None

with st.form('Insert the following Parameters'):
    pickup_datetime = st.text_input("Pickup Date and Time", '2013-07-06 17:18:00')
    pickup_longitude = st.text_input("Pickup Longitude", '-73.950655')
    pickup_latitude = st.text_input("Pickup Latitude", '40.783282')
    dropoff_longitude = st.text_input("Dropoff Longitude", '-73.984365')
    dropoff_latitude = st.text_input("Dropoff Latitude", '40.769802')
    passenger_count = st.text_input("Passenger Count", '1')
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # 2. Let's build a dictionary containing the parameters for our API...
        query = {
                    'pickup_datetime':pickup_datetime,
                    'pickup_longitude':float(pickup_longitude),
                    'pickup_latitude': float(pickup_latitude),
                    'dropoff_longitude':float(dropoff_longitude),
                    'dropoff_latitude': float(dropoff_latitude),
                    'passenger_count': int(passenger_count)
                }

# New York City map coordinates for display
nyc_map_data = pd.DataFrame({
    'lat': [float(pickup_lat), float(drop_lat)],
    'lon': [float(pickup_long), float(drop_long)]
})

# Display map of New York City
st.map(nyc_map_data)

# 3. Let's call our API using the `requests` package..

url = 'https://taxifare.lewagon.ai/predict'

if query != None:
    params = query

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

if query != None:
    response = requests.get(url=url, params=params).json()["fare"]

if response != None:
    st.write("Your estimated fare is", round(response,2), "dollars")
