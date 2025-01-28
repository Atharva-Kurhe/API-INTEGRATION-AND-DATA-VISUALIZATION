import requests
import matplotlib.pyplot as graph_plot

API_KEY = "2cc3b878753b01fc9bbe80cabd0a1be1"  
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
CITY1 = "Nagpur" 

def fetch_data_open_weather(city, api_key):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }
    respond = requests.get(BASE_URL, params=params)
    if respond.status_code == 200:
        return respond.json()
    else:
        print(f"Error: {respond.status_code}")
        return None

def visualize_data_open_weather(data):
    dates = [item["dt_txt"] for item in data["list"][:10]]  
    temperature = [item["main"]["temp"] for item in data["list"][:10]]

    graph_plot.figure(figsize=(10, 5))
    graph_plot.plot(dates, temperature, marker="o", label="Temperature (°C)")
    graph_plot.xlabel("Date and Time")
    graph_plot.ylabel("Temperature (°C)")
    graph_plot.title(f"Weather Forecast for {CITY1}")
    graph_plot.xticks(rotation=45)
    graph_plot.grid(True)
    graph_plot.legend()
    graph_plot.tight_layout()
    graph_plot.show()

if __name__ == "__main__":
    data_open_weather = fetch_data_open_weather(CITY1, API_KEY)
    if data_open_weather:
        visualize_data_open_weather(data_open_weather)
