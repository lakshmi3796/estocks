from django.urls import path
from . import views
urlpatterns = [
	path('', views.homeindex, name="homeindex"),
    path('home', views.HomePage, name="homepage"),
]
