from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('predicttemp', views.prediction),
    path('newpg/', views.new_pg, name="my_func")
]
