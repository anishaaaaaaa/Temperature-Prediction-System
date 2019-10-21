from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import requests
import io
from pandas import read_csv
from matplotlib import pyplot as pp
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def history(request):
    return render(request, 'index.html')

@login_required(login_url="/login/")
def new_page(request):
    loc = request.GET['city']
    startdate = request.GET['sdate']
    enddate = request.GET['edate']
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&dateTimeFormat=yyyy-MM-dd'T'HH%3Amm%3Ass&startDateTime={x}T00%3A00%3A00&endDateTime={y}T00%3A00%3A00&dayStartTime=0%3A0%3A00&dayEndTime=0%3A0%3A00&aggregateHours=24&collectStationContribution=false&maxDistance=80467&maxStations=3&unitGroup=us&locations={z}&key=K8XLI0I46BOND6XXSFWKRU1TC".format(
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
    return render(request, 'plot.html', {'city': loc, 'startdate': startdate, 'enddate': enddate, 'data': data})