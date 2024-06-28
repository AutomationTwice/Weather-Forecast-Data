from sqlalchemy import create_engine, Column, Integer, String, Numeric, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import requests
from datetime import datetime
import pytz

db_config = {
    'user': 'username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432',
    'database': 'database_name'
}

# SQLAlchemy setup
engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")
Base = declarative_base()

# Define ORM class for weather data
class WeatherData(Base):
    __tablename__ = 'Table_name'

    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, nullable=False)  # Combined date and time column
    city = Column(String(255), nullable=False)
    country_code = Column(String(10), nullable=False)
    temperature = Column(Numeric)  # Current temperature
    humidity = Column(Numeric)
    wind_speed = Column(Numeric)
    conditions = Column(String(255))

# Create the database tables
Base.metadata.create_all(engine)

# Function to fetch weather data for a city from OpenWeatherMap API
def fetch_weather_data(city):
    api_key = 'your_api_key'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Extract relevant data from API response (iterate over the list to get multiple entries)
    for entry in data['list']:
        city_name = data['city']['name']
        country_code = data['city']['country']
        datetime_utc = datetime.fromtimestamp(entry['dt'], tz=pytz.UTC)
        temperature = entry['main']['temp']
        humidity = entry['main']['humidity']
        wind_speed = entry['wind']['speed']
        conditions = entry['weather'][0]['description']

        # Store data in PostgreSQL using SQLAlchemy ORM
        new_data = WeatherData(
            datetime=datetime_utc,
            city=city_name,
            country_code=country_code,
            temperature=temperature,
            humidity=humidity,
            wind_speed=wind_speed,
            conditions=conditions
        )
        session.add(new_data)
        # Print success message
        print(f"Inserted data for {city_name} at {datetime_utc}")

    session.commit()
    session.close()

# Function to fetch entire day's data for multiple cities
def fetch_entire_day_data(cities):
    # Iterate through each city and fetch weather data
    for city in cities:
        fetch_weather_data(city)

# Example cities to fetch data for
cities = ['City Name']

# Fetch entire day's data for the specified cities
fetch_entire_day_data(cities)
