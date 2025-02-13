import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Simulated weather data generator
def generate_weather():
    temperature = round(random.uniform(-20, 40), 1)
    humidity = round(random.uniform(30, 90), 1)
    weather_conditions = {
        'Clear': '☀️',
        'Partly Cloudy': '⛅',
        'Cloudy': '☁️',
        'Rainy': '🌧️',
        'Stormy': '⛈️',
        'Snowy': '❄️'
    }
    condition = random.choice(list(weather_conditions.keys()))

    return {
        'temperature': temperature,
        'humidity': humidity,
        'condition': condition,
        'icon': weather_conditions[condition]
    }

# Function to display the weather
def display_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city.")
        return

    weather_data = generate_weather()
    messagebox.showinfo("Weather Information",
                        f"City: {city}\n"
                        f"Date: {date_entry.get()}\n"
                        f"Temperature: {weather_data['temperature']}°C\n"
                        f"Humidity: {weather_data['humidity']}%\n"
                        f"Condition: {weather_data['condition']} {weather_data['icon']}")

# Create the main application window
root = tk.Tk()
root.title("Simulated Weather App")

p1 = tk.PhotoImage(file = 'weather.png')
root.iconphoto(False, p1)

# Create GUI components
label = tk.Label(root, text="Simulated Weather App", font=("Helvetica", 16))
label.pack(pady=10)

city_label = tk.Label(root, text="Enter city:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

date_label = tk.Label(root, text="Enter date:")
date_label.pack(pady=5)

date_entry = tk.Entry(root)
date_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch Weather", command=display_weather)
fetch_button.pack(pady=10)

# Run the main event loop
root.mainloop()
