import json
import os
import time
import requests
from my_email import SendEmail
from interval_timer import IntervalTimer


LATITUDE = 43.01
LONGITUDE = -83.8
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": os.environ['OPENWEATHERMAP_API_KEY'],
    "units": "metric"
}

next_execution_time = 100
print(type(next_execution_time))
# TODO 1. Start the loop

for interval in IntervalTimer(3600):
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()

    msg_str = ""

    # weather id: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    weather_slice = data['list'][:3]

    for data_3h in weather_slice:
        condition_code = data_3h['weather'][0]['id']
        if int(condition_code) < 700:
            description = data_3h['weather'][0]['description']
            msg_time = data_3h['dt_txt']
            msg_str += f"{description} at {msg_time}\n"

    print(msg_str)

    # TODO 2. Send email
    EMAIL_RECIPIENT = "rezwanur.hussain@gmail.com"
    SUBJECT = "Weather alert"
    MESSAGE = msg_str

    if time.time() >= next_execution_time and len(MESSAGE) > 5:
        SendEmail(to_addr=EMAIL_RECIPIENT, subject=SUBJECT, body=MESSAGE)
        next_execution_time = time.time() + (12 * 3600)
