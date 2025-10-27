from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('place/<slug:slug>/', views.place_detail, name='place_detail'),
]
