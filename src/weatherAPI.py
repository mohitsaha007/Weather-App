import requests
from config import API_KEY, BASE_URL

class WeatherAPIClient:
    def __make_request(self, endpoint, params):
        params["key"] = API_KEY
        
        try:
            response = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)
            data = response.json()
            
            if "error" in data:
                return {"success": False, "error": data["error"]["message"]}
                
            return {"success": True, "data": data}
            
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": f"Network error: {e}"}

    def fetch_current(self, city):
        return self._make_request("current.json", {"q": city, "aqi": "yes"})

    def fetch_forecast(self, city, days=3):
        return self._make_request("forecast.json", {"q": city, "days": days, "aqi": "yes", "alerts": "yes"})

    def fetch_history(self, city, date):
        return self._make_request("history.json", {"q": city, "dt": date})