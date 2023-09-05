import requests    
import tkinter as tk
def get_weather():
    api_key = '38ae0e96895ba153e00f82bb193b2152'
    user_input = city_entry.get()
    weather_data =requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    if weather_data.json()['cod'] == '404':
        result_label.config(text="City name is not found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        description = weather_data.json()['weather'][0]['description']
        humidity = weather_data.json()['main']['humidity']
        wind_speed = weather_data.json()['wind']['speed']
        result_label.config(text=f"The weather in {user_input} is: {weather}")
        temp_label.config(text=f"The temperature in {user_input} is: {temp}°F")
        description_label.config(text=f"Description: {description}")
        humidity_label.config(text=f"Humidity: {humidity}%")    
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} mph")

root = tk.Tk()
root.title("Weather App By Atul")
# Create and configure a frame to organize widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)
# Create and configure input label and entry
city_label = tk.Label(frame, text="Enter City:")
city_label.grid(row=0, column=0, padx=10, pady=5)
city_entry = tk.Entry(frame)
city_entry.grid(row=0, column=1, padx=10, pady=5)
# Create and configure the "Get Weather" button
get_weather_button = tk.Button(frame, text="Get Weather",command=get_weather)
get_weather_button.grid(row=0, column=2, padx=10, pady=5)
# Create and configure labels for displaying results
result_label = tk.Label(frame, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
temp_label = tk.Label(frame, text="", font=("Helvetica", 12))
temp_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
description_label = tk.Label(frame, text="", font=("Helvetica", 12))
description_label.grid(row=3, column=0, columnspan=3, padx=10, 
pady=10)
humidity_label = tk.Label(frame, text="", font=("Helvetica", 12))
humidity_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
wind_speed_label = tk.Label(frame, text="", font=("Helvetica", 12))
wind_speed_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
# Start the Tkinter main loop
root.mainloop()

