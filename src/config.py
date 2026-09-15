import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.get_env(WEATHER_API_KEY)
BASE_URL = "http://api.weatherapi.com/v1"