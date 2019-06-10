import urllib.request as req
import urllib.parse as prs
import requests
import json

class WeatherInfo:
    #API_URL = 'https://api.openweathermap.org/data/2.5/weather'
    API_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

    def getWeatherInfo(self, city_name, app_id):
        # param = {
        #     'q': city_id,
        #     'APPID': app_id,
        # }
        # r = req.Request('{}?{}'.format(WeatherInfo.API_URL, prs.urlencode(param)))
        # with req.urlopen(r) as res:
        #     body = res.read()
        #     return body
        url = WeatherInfo.API_URL.format(city=city_name, key=app_id)
        r = requests.get(url)
        data = json.loads(r.text)
        return data
