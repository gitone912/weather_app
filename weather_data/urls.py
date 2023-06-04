
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name='home'),
    path('climate/',views.climate_view,name='climate'),
]
