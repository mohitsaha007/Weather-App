import sys
from weather_api import WeatherAPIClient

class CLIInterface:
    
    def display_message(self, message):
        print(message)

    def display_error(self, error_message):
        print(f"❌ Error: {error_message}")
        
    def get_input(self, prompt_text):
        return input(prompt_text).strip()

    def display_current(self, data):
        loc, curr = data["location"], data["current"]
        aqi = curr.get("air_quality", {}).get("us-epa-index", "N/A")
        
        print(f"\n{'='*50}")
        print(f"📍 Current Weather: {loc['name']}, {loc['country']}")
        print(f"{'='*50}")
        print(f"Condition:   {curr['condition']['text']}")
        print(f"Temperature: {curr['temp_c']}°C (Feels like {curr['feelslike_c']}°C)")
        print(f"Wind:        {curr['wind_kph']} km/h {curr['wind_dir']}")
        print(f"Air Quality: {aqi} (US EPA Index)")
        print(f"{'='*50}")

    def display_forecast(self, data):
        loc = data["location"]
        print(f"\n--- Forecast for {loc['name']} ---")
        for day in data["forecast"]["forecastday"]:
            date, d_data = day["date"], day["day"]
            print(f"[{date}] {d_data['condition']['text']:<20} | Max: {d_data['maxtemp_c']}°C | Min: {d_data['mintemp_c']}°C | Rain: {d_data['daily_chance_of_rain']}%")
        print("-" * 50)

    def display_history(self, data):
        loc = data["location"]
        day = data["forecast"]["forecastday"][0]
        d_data = day["day"]
        print(f"\n--- Past Weather on {day['date']} in {loc['name']} ---")
        print(f"Condition: {d_data['condition']['text']}")
        print(f"Avg Temp:  {d_data['avgtemp_c']}°C")
        print(f"Rainfall:  {d_data['totalprecip_mm']} mm")
        print("-" * 50)

    def display_submenu(self, city):
        print(f"\nWhat would you like to see for {city.title()}?")
        print("1. Current weather")
        print("2. 3-day forecast")
        print("3. Past weather")
        print("4. Search a different city")
        print("5. Quit app")


class AppRunner:
    
    def __init__(self):
        self.api = WeatherAPIClient()
        self.ui = CLIInterface()

    def run(self):
        self.ui.display_message("\n🌤️  Welcome to the Python Weather App!")
        
        while True:
            city = self.ui.get_input("\n🌍 Enter a city name (or 'q' to quit): ")
            
            if city.lower() == 'q':
                self.ui.display_message("Goodbye!")
                break
            if not city:
                continue
            
            self._handle_city_menu(city)

    def _handle_city_menu(self, city):
        while True:
            self.ui.display_submenu(city)
            choice = self.ui.get_input("Select (1-5): ")
            try:
                choice = int(choice)
            except ValueError:
                self.ui.display_message("Invalid choice. Please select 1-5.")
                continue
            
            match choice:
                case 1:
                    self.ui.display_message(f"Fetching current weather for {city}...")
                    res = self.api.fetch_current(city)
                    if res["success"]: 
                        self.ui.display_current(res["data"])
                    else: 
                        self.ui.display_error(res['error'])
            
                case 2:
                    self.ui.display_message(f"Fetching forecast for {city}...")
                    res = self.api.fetch_forecast(city, days=3)
                    if res["success"]: 
                        self.ui.display_forecast(res["data"])
                    else: 
                        self.ui.display_error(res['error'])
                
                case 3:
                    date = self.ui.get_input("Enter date (YYYY-MM-DD): ")
                    self.ui.display_message(f"Fetching history for {city} on {date}...")
                    res = self.api.fetch_history(city, date)
                    if res["success"]: 
                        self.ui.display_history(res["data"])
                    else: 
                        self.ui.display_error(res['error'])
                
                case 4:
                    break
                
                case 5:
                    self.ui.display_message("Goodbye!")
                    sys.exit(0)
                
                case _:
                    self.ui.display_message("Invalid choice. Please select 1-5.")