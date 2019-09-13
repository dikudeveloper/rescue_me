from django.urls import path
from rescue_me.api import views

urlpatterns = [
    path('rescueme/', views.RescueMeProfileList),
    path('rescueme/<int:pk>/', views.RescueMeProfileDetail),
]