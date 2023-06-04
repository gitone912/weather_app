from django.shortcuts import render
import requests
# Create your views here.

def home_view(request):
    return render(request,'index.html')

"""write a view function that will take city as data and render the climate data of that city using openweather api https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"""

def climate_view(request):
    city=request.GET.get('city')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7f5c68079c6516e6425b3f5305f06fdd'
    data=requests.get(url).json()
    temp=data['main']['temp']
    temp=temp-273.15
    humidity=data['main']['humidity']
    weather=data['weather'][0]['main']
    context={
        'city':city,
        'temp':round(temp,2),
        'humidity':humidity,
        'weather':weather,
    }
    return render(request,'climate.html',context)