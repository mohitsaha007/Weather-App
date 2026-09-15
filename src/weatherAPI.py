import requests

from config import API_KEY, BASE_URL


class WeatherAPIClient:
    def _make_request(self, endpoint, params):
        request_params = {**params, "key": API_KEY}

        try:
            response = requests.get(
                f"{BASE_URL}/{endpoint}",
                params=request_params,
                timeout=10,
            )
            data = response.json()

            if response.status_code != 200 or "error" in data:
                error = data.get("error", {}).get(
                    "message",
                    f"HTTP error {response.status_code}",
                )
                return {"success": False, "error": error}

            return {"success": True, "data": data}

        except requests.exceptions.RequestException as error:
            return {"success": False, "error": f"Network error: {error}"}
        except ValueError:
            return {"success": False, "error": "Invalid response from weather API"}

    def fetch_current(self, city):
        return self._make_request(
            "current.json",
            {"q": city, "aqi": "yes"},
        )

    def fetch_forecast(self, city, days=3):
        return self._make_request(
            "forecast.json",
            {"q": city, "days": days, "aqi": "yes", "alerts": "yes"},
        )

    def fetch_history(self, city, date):
        return self._make_request(
            "history.json",
            {"q": city, "dt": date},
        )