import pandas as pd
from sqlalchemy import create_engine

import config


def load_to_db(df, london_bike):
    engine = create_engine(
    f"{config.DB_TYPE}://{config.DB_USER}:{config.DB_PASSWORD}"
    f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    )



    try: 
        df.to_sql(london_bike, engine, if_exists='replace', index=False)
        print(f"Data loaded successfully into the 'london_bike' table.")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")


