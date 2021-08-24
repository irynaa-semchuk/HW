# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
from flask_restful import Resource, Api
import requests
from config import Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")

def query(q, cnt, mode, lon, lan, type, lat, units):
    return {"q": q, "cnt": cnt, "mode": mode, "lon": lon, "type": type, "lat": lat,
            "units": units}

def weather_headers():
    return {
        "x-rapidapi-key": Config.WEATHER_API_KEY,
        "x-rapidapi-host": Config.WEATHER_API_HOST
    }

def weather_request(headers, querystring):
    return requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    
@app.route('/search', methods=['POST'])
def search_weather():
    weather = []
    cities = request.form.get("cities")
    cities = cities.replace(" ", "")
    _list = cities.split(",")
    for city in _list:
        querystring = query(city, "1", "null", "0", "link, accurate", "0", "metric")
        headers = weather_headers()
        response = weather_request(headers, querystring)
        
        if response.status_code == 200:
            data = response.json()
            try:
                weather.append(data['list'][0])
            except(IndexError):
                return Response(status=404)
        else:
            return Response(status=404)
    return render_template("weather.html", weather=weather)

@app.route('/search_location', methods=['POST'])
def search_weather_location():
    weather = []
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    querystring = qsmake("", "1", "null", lon, "link, accurate", lat, "metric")
    headers = weather_headers()
    response = weather_request(headers, querystring)
    data = response.json()

    if response.status_code == 200:
        weather.append(data['list'][0])
        return render_template("weather.html", weather=weather)
    else:
        return Response(status=404)
        



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
