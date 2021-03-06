# Weather

# OpenWeatherMap

> OpenWeatherMap is an online service that provides a free API for weather data, including current weather data, forecasts, and historical data to the developers of web services and mobile applications. For data sources, it utilizes meteorological broadcast services, raw data from airport weather stations, raw data from radar stations, and raw data from other official weather stations. [OpenWeatherMap](http://openweathermap.org/current)

1. [Sign Up](https://home.openweathermap.org/users/sign_up)
2. 
   - Username
   - Email
   - Password
3. How and where will you use our API? 
   >  Hi! We are doing some housekeeping around thousands of our customers. Your impact will be much appreciated. All you need to do is to choose in which exact area you use our services.
   - Company: NuupXe
   - Purpose: Other
   - Your Answer: HAM Radio
4. NEW! Find your API keys in the special sheet [API keys](https://home.openweathermap.org/api_keys)
   -  Key: 3b6cda5c376c3eae4ec112682177c560
   -  Name: Default

# PyOWM

> PyOWM - A Python wrapper around the OpenWeatherMap Web API [Pip Page](https://github.com/csparpa/pyowm)

```
repeater@nuupxe:~$ sudo pip install pyowm
[sudo] password for xe1gyq: 
Collecting pyowm
  Downloading pyowm-2.3.2.tar.gz (1.3MB)
    100% |████████████████████████████████| 1.3MB 70kB/s 
Building wheels for collected packages: pyowm
  Running setup.py bdist_wheel for pyowm ... done
  Stored in directory: /root/.cache/pip/wheels/03/63/6a/79b3b59f86a973dcfb4cfc11c9613ac3e8ca866a5b4d073aa9
Successfully built pyowm
Installing collected packages: pyowm
Successfully installed pyowm-2.3.2
repeater@nuupxe:~$ 
```

```python
Python 2.7.9 (default, Mar  1 2015, 18:22:53) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyowm
>>> owm = pyowm.OWM('****************************')
>>> forecast = owm.daily_forecast("Guadalajara,MX")
>>> tomorrow = pyowm.timeutils.tomorrow()
>>> forecast.will_be_sunny_at(tomorrow)
False
>>> print forecast
<pyowm.webapi25.forecaster.Forecaster>
>>> 
```

```python
>>> observation = owm.weather_at_place('Guadalajara,MX')
>>> w = observation.get_weather()
>>> print(w)
<pyowm.webapi25.weather.Weather - reference time=2016-07-30 17:49:00+00, status=Clouds>
>>> w.get_wind()
{u'speed': 2.6, u'deg': 30}
>>> w.get_humidity()
60
>>> w.get_temperature('celsius')
{'temp_max': 23.0, 'temp_kf': None, 'temp': 23.0, 'temp_min': 23.0}
>>> 
```

# Forecast IO

- [Forecast.Io](https://github.com/ZeevG/python-forecast.io)
- [Forecast Io Developer](https://developer.forecast.io/)

## Register

1. [Register](https://developer.forecast.io/register)
   1 Email
   2 Password
   3 Confirm Password

