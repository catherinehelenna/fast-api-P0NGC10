from fastapi import FastAPI, HTTPException, Header
import logging
# call FastAPI classs
app = FastAPI()

# API KEY

API_KEY = "weather_us_check_2024"

# weather data in different cities
weather = {
    "New York City":{
    "temperature":32, 
    "condition": 'Sunny'
    },
    "Los Angeles":{
    "temperature":25, 
    "condition": 'Cloudy'
    },
    "Chicago":{
    "temperature":20, 
    "condition": 'Rainy'
    }
}

# testing home url
# you must write this first!
@app.get('/')
def root():
    return {"message":"Hello World"}

# you have to define what is the value returned if you call /weather
# if you jump straight to '/weather/{location}, there'll be no output
# since the value of /weather is empty
@app.get('/weather')
def weather_info():
    return weather

# create feature get information from weather based on location typed on url
# location is a dynamic value: depends on user's input
@app.get('/weather/{location}')
def show_weather(location:str):
    if location in weather.keys():
        return weather[location]
    else:
        raise HTTPException(status_code = 404, detail = 'Data is unavailable')

# do authentification with API KEY
@app.post('/authenticate')
def api_authenticate(weatherData:dict,api_key:str=Header(None)):
    print('weather information: ', weatherData)
    print('api_key dari user: ', api_key)
    if api_key != API_KEY:
        raise HTTPException(status_code = 401, detail = 'The API is incorrect')
    
    cityName = weatherData['name']
    cityTemp = weatherData['temperature']
    cityCondition = weatherData['condition']

    weather[cityName] = {
        "temperature": cityTemp,
        "condition": cityCondition
    }
    return "New weather data is successfully added"
    