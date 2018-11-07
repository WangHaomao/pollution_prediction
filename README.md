# Pollutions Prediction
A project in MS 5002 about pollution prediction in Beijing give data by Observed Weather Data and Grid Weather Data(Details in data folder).
## Goal
Predicting concentration levels of several pollutants over the coming 24*2 hours (two days) for 35 stations in Beijing, China
## Data Analysis
### stations
3 diff categories in Urban Stations, Suburban Stations, and Other Stations.

Each station has longitude and latitude

In **observedWeather** data, station info saved as region/district, e.g. 'zhaitang_meo' I need to find the station name from MAP(station_map)

In **gridWeather** data, station info saved as grad name, e.g. 'beijing_grid_645', I need to change the grid name to longitude and latitude in **Beijing_grid_weather_station.csv** and find the silimar longitude and latitude and get the station name in **Beijing_AirQuality_Stations_en.xlsx**

