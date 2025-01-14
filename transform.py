import pandas as pd

   
   # Rename columns in the dataset according to the provided dictionary.

   # Args:
        #df (pd.DataFrame): The DataFrame to rename columns for.

   # Returns:
        #pd.DataFrame: DataFrame with renamed columns.
    

def rename_column(df):
    new_cols_dict = {'timestamp': 'time',
        'cnt': 'count',
        't1': 'temp_real_c',
        't2': 'temp_feels_like_c',
        'hum': 'humidity_percent',
        'wind_speed': 'wind_speed_kph',
        'weather_code': 'weather',
        'is_holiday': 'is_holiday',
        'is_weekend': 'is_weekend',
        'season': 'season',
        }
    
    df = df.rename(new_cols_dict, axis=1)
    return df

def add_humidity_ratio(df):
    
    if 'humidity_percent' in df.columns:
        df['humidity_ratio'] = df['humidity_percent'] / 100
    else:
        raise KeyError("'humidity_percent' column not found in the dataframe")
    return df

def add_season_column(df):
    season_dict = {'0.0':'Spring',
                   '1.0':'Summer',
                   '2.0':'Autumn',
                   '3.0':'Winter'
    }
    
    df['season'] = df['season'].astype(str)
    df['season_name'] = df['season'].map(season_dict)
    return df
    
def add_weather_column(df):
    """
    Add a column for the weather's descriptive names.
    """
    weather_dict = {
        '1.0': 'Clear',
        '2.0': 'Scattered clouds',
        '3.0': 'Broken clouds',
        '4.0': 'Cloudy',
        '7.0': 'Rain',
        '10.0': 'Rain with thunderstorm',
        '26.0': 'Snowfall',
    }
    # Ensure the 'weather' column is treated as a string
    df['weather'] = df['weather'].astype(str)
    # Map descriptive names to the 'weather' column
    df['weather_name'] = df['weather'].map(weather_dict)
    return df

    

    
