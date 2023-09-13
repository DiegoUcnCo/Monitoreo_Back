from django.contrib import admin
from django.urls import path
from models.temperature import WokwiDataViewTemperature
from models.hidroponia import WokwiDataViewHidroponia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('temperature/', WokwiDataViewTemperature.as_view() ),
    path('hidroponia/', WokwiDataViewHidroponia.as_view() )
]
