"""TemperaturePrediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', user_views.login_user, name="login"),
    path('admin/', admin.site.urls),
    path('historicalTemp/', include('HistoricalTemp.urls')),
    path('predictedTemp/', include('PredictedTemp.urls')),
    path('currentTemp/', include('currentTemp.urls')),
    path('register/', user_views.register_user, name='register'),
    path('profile/',user_views.profile_user, name="profile"),
    path('login/', user_views.login_user, name="login"),
    url(r'^comment_app/', include('comment_app.urls')),
    path('weather/', include('weather.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
