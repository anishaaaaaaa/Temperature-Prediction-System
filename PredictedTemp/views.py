from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import requests
import io
from pandas import read_csv
from matplotlib import pyplot as pp
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def prediction(request):
    return render(request, 'predictedindex.html')

@login_required(login_url="/login/")
def new_page(request): 
	loc = request.GET['city']
	print(loc)
	url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/forecast?&location={x}&aggregateHours=24&unitGroup=us&shortColumnNames=false&key=TIX7L5U729HEO5ZISDYPF3L7K".format(x=loc)
	urlData = requests.get(url).content
	rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
	rawData.dropna(inplace=True)
	print(rawData.head,type(rawData))

	temp = rawData['Temperature']
	date = rawData['Date time']
	pp.plot(date, temp)
	pp.xticks(date, date, rotation='vertical')
	data = pp.show()
	return render(request, 'plotpredicted.html', {'city': loc, 'data': data})
