from flask import jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import requests

# Load the AC dataset
data = pd.read_csv("assets/flipkart_AC.csv")

# Convert cooling capacity to numeric and replace missing values with 0
data['Cooling Capacity'] = data['Cooling Capacity'].str.extract(
    r'([\d.]+)').astype(float)
data['Cooling Capacity'] = data['Cooling Capacity'].fillna(0)

# Convert capacity in tons to numeric and replace missing values with 0
data['Capacity in Tons'] = data['Capacity in Tons'].str.extract(
    r'([\d.]+)').astype(float)
data['Capacity in Tons'] = data['Capacity in Tons'].fillna(0)


def temparatue(lat, lon):
    WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=703f40c088b5d700ca7c56348da39650&units=imperial"
    response = requests.get(WEATHER_API_URL)
    data = response.json()

    # Extract relevant weather data (e.g., temperature, conditions)
    temp = data['main']["temp"]
    return int(temp)


def recommend(room_height, room_width, room_depth, lat, lon):
    volume = (room_height * room_width * room_depth)
    diff = temparatue(lat, lon) - 25
    cooling_load = volume * diff * 4.5
    cooling_capacity = cooling_load / 12000

    # Now find air conditioners with cooling capacities suitable for the room size
    recommended_acs = data[data['Capacity in Tons'] >= cooling_capacity]
    recommended_acs = recommended_acs.sort_values(by='Capacity in Tons')
    res = []
    for _, row in recommended_acs.head(3).iterrows():
        prod = {}
        prod["image_URL"] = row["image_URL"][2:-2]
        prod["Brand"] = row["Brand"]
        prod["URL"] = row["URL"]
        prod["Model Name"] = row["Model Name"]
        prod["Capacity in Tons"] = row["Capacity in Tons"]
        res.append(prod)

    if len(recommended_acs) == 0:
        recommended_acs = data[data['Capacity in Tons'] < cooling_capacity]
        recommended_acs = recommended_acs.sort_values(
            by='Capacity in Tons', ascending=False)

        res = []
        for _, row in recommended_acs.head(3).iterrows():
            prod = {}
            prod["image_URL"] = row["image_URL"][2:-2]
            prod["Brand"] = row["Brand"]
            prod["URL"] = row["URL"]
            prod["Model Name"] = row["Model Name"]
            prod["Capacity in Tons"] = row["Capacity in Tons"]
            res.append(prod)

        return jsonify({
            'product': res,
        })
    else:
        return jsonify({
            'product': res,
        })
