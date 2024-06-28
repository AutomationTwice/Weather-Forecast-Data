# Weather Data Project

## Overview
This project fetches weather data from the OpenWeatherMap API for specified cities and stores it in a PostgreSQL database using SQLAlchemy. The data includes temperature, humidity, wind speed, and weather conditions. The project is containerized using Docker for easy setup and deployment.

## Prerequisites

- Docker
- Docker Compose
- Python 3.x
- `pytz` library
- `requests` library
- `SQLAlchemy` library

## Setup

1. **Clone the Repository**
   ```

2. Create a Python Virtual Environment
  ```
  python -m venv env
  source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
3.Install Python Dependencies
```
pip install -r requirements.txt
```
4. Setup Docker Compose
   Create a 'docker-compose.yml' file with the following content:
   
   ```
   version: '3.8'

   services:
    postgres:
      image: postgres:latest
      environment:
        POSTGRES_USER: user
        POSTGRES_PASSWORD: password
        POSTGRES_DB: weather_db
      volumes:
        - weather_data:/var/lib/postgresql/data
      networks:
        - weather_network
      ports:
        - "5432:5432"

   adminer:
    image: adminer:latest
    restart: always
    ports:
      - 8080:8080
    networks:
      - weather_network

    volumes:
      weather_data:

    networks:
      weather_network:

   ```
5. Run Docker Compose
   ```
   docker-compose up -d
   ```
   This will start a PostgreSQL container and an Adminer container for database management.

6. Configure the Database Connection

Update the db_config dictionary in weather_data.py with your database credentials if different from the defaults.

## Running the Script
1. Activate the Virtual Enviornmnet
   ```
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
2. Run the Weather Data Script
   ```
   python weather_data.py
   ```
   This script will fetch weather data for the specified cities and store it in the PostgreSQL database. It will also print a success message for each inserted record.

## Viewing the Data
1. Access Adminer

Open your web browser and go to http://localhost:8080.

2. Login to Adminer

Use the following credentials to log in:

System: PostgreSQL
Server: postgres
Username: username
Password: ypur_password
Database: database_name

3. View the Data

You can now view and manage your weather data in Adminer.

## Example Cities
The script fetches weather data for the city of Varanasi by default. You can add more cities to the cities list in weather_data.py.
```
cities = ['Varanasi', 'New York', 'London']

```
## License
This project is licensed under the MIT License.

## Acknowledgements
- OpenWeatherMap for providing the weather data API.
- Docker for containerization.
- SQLAlchemy for ORM.
## Contact
For any questions or suggestions, please open an issue on the GitHub repository.
```

Save this content as `README.md` in the root directory of your project. This file provides a comprehensive guide to setting up, running, and managing your weather data project.

```

