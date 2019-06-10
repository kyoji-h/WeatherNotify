from weather_info import WeatherInfo
from line_notify import LineNotifyBot

weather = WeatherInfo()

city_id_tokyo = 'Tokyo'
api_key = 'xxxx'
res_weather = weather.getWeatherInfo(city_id_tokyo, api_key)

lambda_k2c = lambda k: k - 273.15

weather = res_weather['weather'][0]['description']
temperature_max = round(lambda_k2c(res_weather['main']['temp_max']))
temperature_min = round(lambda_k2c(res_weather['main']['temp_min']))
humidity = res_weather['main']['humidity']
pressure = res_weather['main']['pressure']

print(weather,temperature_max,temperature_min,humidity,pressure)

access_token = 'xxxx'
notify = LineNotifyBot(access_token)

message = "\n天気：" + weather + "\n最高気温：" + str(temperature_max) + "\n最低気温：" + str(temperature_min) + "\n湿度：" + str(humidity) + "\n気圧：" + str(pressure)
print(message)
notify.send(message)
