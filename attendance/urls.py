from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('time-in/', views.time_in_view, name='time_in'),
    path('time-out/', views.time_out_view, name='time_out'),
]

