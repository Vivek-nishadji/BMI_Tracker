from django.urls import path
from . import views

urlpatterns = [
    path('', views.bmi_input, name='bmi_input'),
    path('result/<int:pk>/', views.bmi_result, name='bmi_result'),
]