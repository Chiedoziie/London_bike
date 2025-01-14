London Bike Data ETL Pipeline
Overview
This project is an ETL (Extract, Transform, Load) pipeline for London bike-sharing data. It demonstrates how to extract data, transform it by applying meaningful calculations, and load it into a PostgreSQL database for further analysis.

The pipeline is modular, consisting of three stages:

Extract: Loads raw bike data from a CSV file.
Transform: Renames columns, calculates new fields, and enriches the dataset.
Load: Saves the transformed dataset into a PostgreSQL database.
Features
Modularized ETL pipeline with separate files for extract.py, transform.py, and load.py.
Transformation tasks include:
Renaming columns for better readability.
Adding calculated columns (e.g., humidity ratio, weather names, season names).
Database integration using SQLAlchemy to store transformed data into a PostgreSQL database.
Technologies Used
Python: Core programming language.
Pandas: For data manipulation and transformation.
SQLAlchemy: For database connection and data loading.
PostgreSQL: Relational database for storing the final dataset.
Directory Structure
graphql
Copy code
London_Bike/
├── datasets/                  # Directory containing the raw CSV file
│   └── london_merged.csv      # Raw dataset used in the pipeline
├── config.py                  # Stores database credentials (excluded from Git)
├── extract.py                 # Handles data extraction
├── transform.py               # Handles data transformation
├── load.py                    # Handles data loading into the database
├── main.py                    # Orchestrates the ETL pipeline
├── london_bikes_final.xlsx    # Transformed data saved as an Excel file
├── .gitignore                 # Lists files to ignore in version control
└── README.md                  # Project documentation
Setup and Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/username/London_Bike.git
cd London_Bike
2. Create a Virtual Environment
bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. Install Required Dependencies
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
4. Configure Database
Create a PostgreSQL database (e.g., london_bike).

Update the config.py file with your database credentials:

python
Copy code
DB_TYPE = 'postgresql'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_NAME = 'london_bike'

Ensure config.py is added to .gitignore:



How to Run the Pipeline

1. Run the Pipeline
Run the main ETL pipeline:
python main.py

2. Output
Transformed data will be saved as london_bikes_final.xlsx.
Data will be loaded into the PostgreSQL database table london_bikes_data.

Sample Output
Transformed Data
time	count	temp_real_c	temp_feels_like_c	humidity_percent	wind_speed_kph	weather	season	weather_name	season_name
2015-01-04 01:00:00	182	2.7	0.8	93.0	6.0	3.0	3.0	Broken clouds	Winter
2015-01-04 02:00:00	138	2.7	0.8	93.0	5.0	1.0	3.0	Clear	Winter

Database Table
Verify the data in PostgreSQL:
SELECT * FROM london_bikes_data LIMIT 5;

Customization
You can easily extend the pipeline:

Add more transformation logic in transform.py.
Integrate other databases (e.g., MySQL, SQLite) by updating config.py and load.py.


Known Issues
The password in config.py should not contain special characters like @. Use URL-encoding (e.g., %40) if necessary.
Ensure your PostgreSQL server is running and accessible.


Future Enhancements
Use .env files for sensitive credentials.
Add a unit testing suite for the ETL pipeline.
Create a web dashboard for visualizing the bike data.


Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Contact
For any questions or issues, please contact:

Name: Fortune Ehienulo
Email: ehienulofortune@gmail.com
GitHub: [Your GitHub Profile](https://github.com/Chiedoziie)
# London_bike
