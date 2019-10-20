from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import requests
import io
from pandas import read_csv
from matplotlib import pyplot as pp
import pycountry
import dateutil.parser



# Create your views here.
def prediction(request):
    return render(request, 'index1.html')


def new_pg(request):
    x = request.GET['city']
    y = request.GET['city']
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
    for i in li:
        dt = i['dt_txt']
        date = dateutil.parser.parse(dt).date()
        time = dateutil.parser.parse(dt).time()
        temp = i['main']['temp']
        desc = i['weather'][0]['description']
        print("Date Time: ", dt)
        print("Date: ", date)
        print("Time: ", time)
        print("Temperature: ", temp)
        print("Description: ", desc)
        print()
        print()
        #return render(request, 'plot1.html', {'data': json_data})

    '''
    loc = request.GET['city']
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&dateTimeFormat=yyyy-MM-dd'T'HH%3Amm%3Ass&startDateTime={x}T00%3A00%3A00&endDateTime={y}T00%3A00%3A00&dayStartTime=0%3A0%3A00&dayEndTime=0%3A0%3A00&aggregateHours=24&collectStationContribution=false&maxDistance=80467&maxStations=3&unitGroup=us&locations={z}&sessionId=6b588f0e2a5a521cb3ee675e3af1c4b3".format(
        x=startdate, y=enddate, z=loc)
    urlData = requests.get(url).content
    rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    print(rawData.head)
    # series = read_csv('/home/anisha/Downloads/data_1999.csv', header=0, index_col=0)
    # print(series.head())
    temp = rawData['Temperature']
    date = rawData['Date time']
    pp.plot(date, temp)
    pp.xticks(date, date, rotation='vertical')
    data = pp.show()
    return render(request, 'plot1.html', {'city': loc, 'startdate': startdate, 'enddate': enddate, 'data': data})
    '''