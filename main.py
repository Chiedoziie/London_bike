import pandas as pd

from transform import rename_column, add_humidity_ratio, add_season_column, add_weather_column
from load import load_to_db

# Load dataset
bikes = pd.read_csv("datasets/london_bike_sharing/london_merged.csv")
print("Original DataFrame columns:", bikes.columns)

# Apply rename_column transformation
bikes = rename_column(bikes)
bikes = add_humidity_ratio(bikes)


# Debugging add_season_column
try:
    bikes = add_season_column(bikes)
    print("Sample data after add_season_column:")
    print(bikes[['season', 'season_name']].head())
except KeyError as e:
    print(f"KeyError in add_season_column: {e}")
except Exception as e:
    print(f"Unexpected error in add_season_column: {e}")

# Debugging add_weather_column
try:
    bikes = add_weather_column(bikes)
    print("Sample data after add_weather_column:")
    print(bikes[['weather', 'weather_name']].head())
except KeyError as e:
    print(f"KeyError in add_weather_column: {e}")
except Exception as e:
    print(f"Unexpected error in add_weather_column: {e}")

#print(bikes.head())


output_file = "london_bikes_final.xlsx"
bikes.to_excel(output_file, sheet_name='data', index=False)
print(f"Transformed data saved to london_bikes_final")

table_name = 'london_bike'
load_to_db(bikes, table_name)
