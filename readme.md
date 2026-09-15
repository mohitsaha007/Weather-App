

```markdown
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

```

### 2. Create a Virtual Environment

It is highly recommended to use a virtual environment to isolate dependencies.

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configuration

You need a free API key from [WeatherAPI](https://www.weatherapi.com/).

1. Create a file named `.env` in the root directory.
2. Add your API key to the file like this:

```text
WEATHER_API_KEY=your_actual_api_key_here

```

*(Note: Never commit your `.env` file to version control. It is already included in the `.gitignore`.)*

---

## 💻 Usage

To start the application, simply run the entry point file from the root directory:

```bash
python src/main.py

```

**Example Workflow:**

1. Type a city name (e.g., "London").
2. The app will fetch the current weather and display a sub-menu.
3. Choose `1` for current data, `2` for a forecast, `3` for history, or `4` to search a new city.
4. Type `q` at the main prompt or press `Ctrl+C` to safely exit the app.

---

## 📂 Project Structure

```text
weather_project/
├── .env                  # Secret API key (Not committed)
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── src/
    ├── config.py         # Environment configuration
    ├── main.py           # Application entry point
    ├── utility.py        # The View & Controller (UI and menus)
    └── weather_api.py    # The Model (External API requests)

```

```

```
