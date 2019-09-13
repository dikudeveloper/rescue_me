from django.urls import path
from rescue_me.api import views

urlpatterns = [
    path('api/rescue_me/', views.RescueMeProfileList),
    path('api/rescue_me/<int:pk>/', views.RescueMeProfileDetail),
]