from django.urls import path
from . import views

app_name="reviews"

urlpatterns = [
  path("create/<str:obj>/<int:pk>/", views.create_review, name="create-review"),
  path("remove/<int:pk>", views.remove_reviews, name="remove")

]
