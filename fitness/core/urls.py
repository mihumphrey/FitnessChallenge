from django.urls import path

from core.views import home
#from . import views

urlpatterns = [
    path('', home.HomeView.as_view(), name="home"),
    

]