from django.urls import path
from . import views

app_name="favs"

urlpatterns = [
  path("toggle/<int:pk>", views.toggle_favs, name="toggle")
]

