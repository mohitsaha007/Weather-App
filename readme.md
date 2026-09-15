# 🌤️ Python CLI Weather App

A robust, command-line interface (CLI) application that provides real-time weather, multi-day forecasts, and historical weather data. 

Built in Python, this project strictly adheres to the **Model-View-Controller (MVC)** architectural pattern, ensuring separation of concerns between data fetching, application logic, and user interface.

## ✨ Features
* **Real-Time Data:** Fetches current temperature, wind speed, conditions, and Air Quality Index (AQI).
* **Multi-Day Forecast:** Provides a 3-day outlook including max/min temperatures and rain probability.
* **Historical Weather:** Look up past weather conditions for any city on a specific date.
* **Interactive Menus:** A clean, nested CLI menu system that prevents redundant data fetching.
* **Graceful Error Handling:** Catches API errors, invalid inputs, and network timeouts without crashing.

## 🛠️ Technologies
* **Python 3.x**
* **[WeatherAPI.com](https://www.weatherapi.com/)** (Data provider)
* `requests` (HTTP client)
* `python-dotenv` (Environment variable management)

---

## 🚀 Setup & Installation

### 1. Clone or Create the Repository
Ensure you are in your project directory:
```bash
mkdir weather_project
cd weather_project