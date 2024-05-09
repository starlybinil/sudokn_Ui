import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Create a sample DataFrame
data = {
    'Latitude': [34.0522, 40.7128, 37.7749],
    'Longitude': [-118.2437, -74.0060, -122.4194]
}
df = pd.DataFrame(data)

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get state from latitude and longitude
def get_state(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), exactly_one=True)
        address = location.raw['address']
        state = address.get('state', '')
        return state
    except GeocoderTimedOut:
        return "Geocoder timed out"
    except Exception as e:
        return "Error: " + str(e)

# Apply the function to update the state column
df['State'] = df.apply(lambda row: get_state(row['Latitude'], row['Longitude']), axis=1)

# Print the updated DataFrame
print(df)