from django.urls import path, include

from apps.users import views

urlpatterns = [
    path('', views.health_check),
]
