from django.urls import path

from .views import SimpleCandlestickWithPandas

urlpatterns = [

    path('', SimpleCandlestickWithPandas.as_view(), name='simple-candlestick'),

]