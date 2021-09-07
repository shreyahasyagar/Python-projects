import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textfield.get()
    api="http://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=b1378f75c56038ea66471b608cb4e500"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    min_temp=int(json_data['main']['temp_min']-273.15)
    max_temp=int(json_data['main']['temp_max']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-19800))
    sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-19800))
    

    final_info= condition +"\n"+ str(temp)+"°C"

    final_data="\n" + "Max Temp:" + str(max_temp)+"\n"+"\n" + "Min Temp:" + str(min_temp) +"\n"+"\n"+ "Pressure:"+str(pressure)+"\n"+"\n"+"Humidity"+str(humidity)+"\n"+"\n"+"Wind Speed:"+str(wind)+ "\n"+"\n"+"Sunrise:"+str(sunrise)+"\n"+"\n"+"Sunset:"+str(sunset)

    label1.config(text=final_info)
    label2.config(text=final_data)
    


canvas=tk.Tk()
canvas.geometry("600x500")

canvas.title("Weather App")

f=("Constania",10,"normal")
t=("Constania",35,"bold")

textfield=tk.Entry(canvas,justify="center",font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1=tk.Label(canvas,font=t)
label1.pack()
label2=tk.Label(canvas,font=f)
label2.pack()

canvas.mainloop()