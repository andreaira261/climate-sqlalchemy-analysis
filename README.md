# Climate SQLAlchemy Analysis

## Overview 
In this assignment, we used Python and SQLAlchemy to analyze and visualize climate data from a SQLite database. Aditionally, we designed a Flask API to make the climate data analysis accessible through various routes, enabling users to retrieve precipitation, stations, and temperature data as requested. 

## Languages/ Tools 
- SQLAlchemy
- SQLite
- Python
- Pandas
- Matplotlib
- Flask

## Part 1: Explore and Analyze the Climate Data
File: SurfsUp → [climate_code.ipynb](SurfsUp/climate_code.ipynb)

### Jupyter Notebook Database Connection
In this section, a connection to an SQLite database was established using SQLAlchemy. Tables were reflected into classes, and a SQLAlchemy session was created to link Python to the database.
![database-connect](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/abf6b424-7efb-457e-89e9-80ebf05daaf5)

### Precipitation Analysis 
For the precipitation analysis, SQL queries were used to find the most recent date in the dataset and to collect date-precipitation data for the last year. The results were saved to a Pandas DataFrame, sorted by date, and then plotted in a bar chart. Additionally, Pandas was used to print summary statistics for the precipitation data.
![prcp-1](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/ac8b55d7-2e67-4fd6-8aea-6f6308935de6)
![prcp-2](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/dd10e1c4-80c2-415d-a3d3-36ca2736001a)

### Station Analysis 
For the station analysis, SQL queries were used to determine the number of stations, list the stations with observation counts (identifying the most active station), find the minimum, maximum, and average temperatures for the most active station, and retrieve the previous 12 months of temperature observations (TOBS) for the station with the highest observation count. The results were then saved to a DataFrame, and a histogram was plotted.
![station-1](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/5b15ea67-812f-4f3e-b3ac-552325fbb1b4)
![station-2](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/62c7f888-0b39-44b4-8eff-040d5fc68fb5)

## Part 2: Design Your Climate App
File: SurfsUp → [app.py](SurfsUp/app.py)

### API SQLite Connection and Landing Page 
In this section, the engine was generated for the SQLite file, and `automap_base()` was employed to reflect the database schema. References to the tables in the SQLite file were saved, and subsequently, a session between the app and the database was created and bound.
![flask-code](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/e4923ed5-e741-46c4-97de-0897ce71ebdb)

The landing page is designed to display all the available routes. 
<img width="952" alt="landing-page" src="https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/c167e4fd-7853-4950-b962-ad5a96c07715">

### API Static Routes 
This precipitation landing route returns the JSON-ified precipitation data for the last year in the database.
![prcp-route](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/155c11d0-baf2-4146-b255-e450b3f6b260)
<br>
<br>

This stations landing route returns the JSON-ified data of all the stations in the database.
![stations-route](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/87954e9b-9bd2-4731-9731-703e0056a5a9)
<br>
<br>

This TOBS landing route returns the JSON-ified data for the most active station for the last year of data.
![tobs-route](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/65af7c3b-186f-4799-a68b-c15be8d41d12)

### API Dynamic Route 
This start route accepts the start date as a parameter from the URL and returns the minimum, maximum, and average temperature calculated from the given start date to the end of the dataset.
![start-route](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/0d6356c0-1b0d-49b1-931a-a23b373ba26a)
<br>
<br>

This start/end route accepts the start and end dates as parameters from the URL and returns the minimum, maximum, and average temperatures calculated from the given start date to the given end date.
![start-end-route](https://github.com/andreaira261/climate-sqlalchemy-analysis/assets/48165713/0a680e5a-6d6c-4678-bd3b-25aee5b48d9f)
