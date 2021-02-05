from django.urls import path
from .import views
urlpatterns = [
    path('insert/', views.insertingData)
]