import pandas as pd
import random
from geopy.distance import geodesic
import pickle

branch_details = pd.read_csv('branch_details.csv')

# simulate curfew data randomly
def simulate_curfew(branch_details):
    curfew_data = []
    for index, row in branch_details.iterrows():
        curfew = False
        curfew_data.append(curfew)
    return curfew_data

branch_details['Curfew'] = simulate_curfew(branch_details)

def simulate_weather(latitude, longitude, desired_time):
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy']
    weather = random.choice(weather_conditions)
    return weather


def weather_service(latitude, longitude, desired_time):
    weather = simulate_weather(latitude, longitude, desired_time)
    return weather

# Function to predict nearest branch based on weather, curfew, facility/
def predict_nearest_branch(customer_location, desired_time, facility):
     
     
    distances = branch_details.apply(
        lambda row: geodesic((row['Latitude'], row['Longitude']), customer_location).miles, axis=1
    )

    # Filter branches based on curfew and facility
    filtered_branches = branch_details.loc[(branch_details['Curfew'] == False) & branch_details['Facilities'].str.contains(facility, case=False)]

    
    if filtered_branches.empty:
        return "No suitable branches available.", pd.DataFrame()

   
    weather_conditions = []
    branch_names = []
    for index, row in filtered_branches.iterrows():
        weather = weather_service(row['Latitude'], row['Longitude'], desired_time)
        weather_conditions.append(weather)
        branch_names.append(row['Branch Name'])

    # Store the filtered branch data, weather conditions, distances, and branch names for future use
    branch_data = pd.DataFrame({
        'BranchName': branch_names,
        'WeatherCondition': weather_conditions,
        'Distance': distances.loc[filtered_branches.index]
    })

   
    return branch_data



