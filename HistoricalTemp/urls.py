from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('histtemp', views.history),
    path('newpage/', views.new_page, name="my_function")
]
