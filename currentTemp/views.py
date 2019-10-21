import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9c3f1af00ab7b14d1b7c0e29d374b63f'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []
    counter = 0
    for city in cities:
        counter += 1
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)
        # city.delete()
        # print(counter)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)
