from tests.conftest import client
from config import Config


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

def test_search_weather(client):
    Config.WEATHER_API_KEY = "eb693de49dmsh5020a2f638740f4p1f0889jsnf4b5bc7fbd2f"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"city": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data
    
def test_search_weather_mock(client, mocker):
Config.WEATHER_API_KEY = "eb693de49dmsh5020a2f638740f4p1f0889jsnf4b5bc7fbd2f"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    mocker.patch('requests.request', side_effect=MockApi)
    response = client.post("/search", data={"cities": "london"})
    print(response)
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data
    
class MockApi:
    def __init__(self, *args, **kwargs):
        self.data_json = {'message': 'accurate', 'cod': '200', 'count': 1, 'list': [
            {'id': 2643743, 'name': 'London', 'coord': {'lat': 51.5085, 'lon': -0.1257},
             'main': {'temp': 295.81, 'feels_like': 294.33, 'temp_min': 294.26, 'temp_max': 296.15, 'pressure': 1023,
                      'humidity': 34}, 'dt': 1623258571, 'wind': {'speed': 3.09, 'deg': 240}, 'sys': {'country': 'GB'},
             'rain': None, 'snow': None, 'clouds': {'all': 88},
             'weather': [{'id': 801, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}]}]}
        self.status_code = 200
        
        
    def json(self):
        return self.data_json
