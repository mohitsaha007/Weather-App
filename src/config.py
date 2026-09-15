import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1"

if not API_KEY:
    raise RuntimeError(
        f"WEATHER_API_KEY is missing from {PROJECT_ROOT / '.env'}"
    )