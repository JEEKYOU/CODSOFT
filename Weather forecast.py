from tkinter import *
from tkinter import messagebox
import datetime as dt
import requests
 
window = Tk()

labelText=StringVar()
labelText.set("Enter city Name:")
label_entry=Label(window, 
                  textvariable=labelText,
                  height=2,
                  font=("Sans serif",10))
label_entry.grid(row=0, 
                 column = 0, 
                 columnspan= 4 )

e = Entry(window,
          width=20,
          borderwidth=5, 
          font=("Robota",20))
e.grid(row=1,
       column=0,
       columnspan=4,
       padx=10,
       pady=10)




base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = 'Enter the open weather API key'
city = ""



def temp_celsius_fah(kelvin):
    celsius = kelvin - 273.15
    fah = celsius*(9/5) + 32
    return celsius, fah



def submit():
    global temp_cel
    global temp_kelvin
    global humidity
    global description
    global sunrise_time
    global sunset_time

    global base_url
    global api_key 

    

    city = str(e.get())    
    url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_cel, temp_fah = temp_celsius_fah(temp_kelvin)
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response["timezone"])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response["timezone"])
    wind_speed = response['wind']['speed']

    forecast = (f"Temperature in {city}: {temp_cel:.2f}'C or {temp_fah:.2f}'F\n") + (f"Humidity in {city}:{humidity}%\n") + (f"Wind Speed in  {city}:{wind_speed}m/s\n") + (f"General Weather in {city} is :{description}\n") + (f"Sun rises at {sunrise_time} local time.\n") + (f"Sun rises at {sunrise_time} local time.\n") + (f"Sun sets at {sunset_time} local time.\n")

    
    messagebox.showinfo(title="Weather Forecast",message=forecast)

Submit = Button(window, 
                  text="Submit",
                  padx=20,
                  pady=10,
                  width = 30,
                  background="#b81616",
                  foreground="white",
                  font=("Sans serif",10), 
                  command=submit)
Submit.grid(row=2, column=0, columnspan=4)
window.mainloop()