from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import requests
import io
from pandas import read_csv
from matplotlib import pyplot as pp
import pycountry
import dateutil.parser
import pytemperature
from pandas.io.json import json_normalize

from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def prediction(request):
    return render(request, 'index1.html')

@login_required(login_url="/login/")
def new_pg(request):
    x = request.GET['city']
    y = request.GET['country']
    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2
    code = countries.get(y, 'Unknown code')
    cc = code.lower()
    api_address = 'http://api.openweathermap.org/data/2.5/forecast?q={x},{code}&appid=0c42f7f6b53b244c78a418f4f181282a'.format(
        x=x, code=cc)
    print(api_address)
    json_data = requests.get(api_address).json()
    li = json_data['list']
    data = pd.DataFrame(columns=['date_time', 'Temperature'])
    for i in li:
        dt = i['dt_txt']
        date = dateutil.parser.parse(dt).date()
        time = dateutil.parser.parse(dt).time()
        tem = i['main']['temp']
        temp = pytemperature.k2f(tem)
        desc = i['weather'][0]['description']
        print("Date Time: ", dt)
        print("Date: ", date)
        print("Time: ", time)
        print("Temperature: ", temp)
        print("Description: ", desc)
        print()
        print()
        data = data.append({'date_time': dt, 'Temperature':temp}, ignore_index=True)
    # print(json_data.keys)
    # print((json_normalize(json_data)).columns)
        print(data)
        data.to_csv('file1.csv')
        temp = data['Temperature']
    date = data['date_time']
    pp.plot(date, temp)
    pp.xticks(date, date, rotation='vertical')
    data = pp.show()
    return render(request, 'plot1.html')

'''
@login_required(login_url="/login/")
def new_pg(request):
    l1 = []
    l2 = []
    x = request.GET['city']
    y = request.GET['country']
    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2
    code = countries.get(y, 'Unknown code')
    cc = code.lower()
    api_address = 'http://api.openweathermap.org/data/2.5/forecast?q={x},{code}&appid=0c42f7f6b53b244c78a418f4f181282a'.format(
        x=x, code=cc)
    #print(api_address)
    json_data = requests.get(api_address).json()
    li = json_data['list']
    for i in li:
        dt = i['dt_txt']
        date = dateutil.parser.parse(dt).date()
        time = dateutil.parser.parse(dt).time()
        tem = i['main']['temp']
        temp = pytemperature.k2f(tem)
        desc = i['weather'][0]['description']
        print("Date Time: ", dt)
        print("Date: ", date)
        print("Time: ", time)
        print("Temperature: ", temp)
        print("Description: ", desc)
        print()
        print()
        l1.append(date)
        l2.append(temp)
    pp.plot(l1, l2)
    pp.xticks(l1, l1, rotation='vertical')
    data = pp.show()
    return render(request, 'plot1.html',{'graph': data})

'''