from django.shortcuts import render, reverse, redirect
from movies.models import Movie as movie_models
from books.models import Book as book_models
from . import models

# Create your views here.

def toggle_favs(request, pk):
  type = request.GET.get('type')
  action = request.GET.get('action')
  next_path = request.GET.get('next')
  if type == "movie":
    try:
      obj = movie_models.objects.get(pk=pk) 
      favs, _ = models.FavList.objects.get_or_create(
        created_by=request.user)  
      if obj is not None and action == 'add':
        favs.movies.add(obj)
      elif action == 'remove':
        favs.movies.remove(obj)
      return redirect(next_path)
    except movie_models.DoesNotExist:
      return redirect(reverse("core:home"))    
  elif type == "book":
    try:
      obj = book_models.objects.get(pk=pk)
      favs, _ = models.FavList.objects.get_or_create(
        created_by=request.user)
      if obj is not None and action == 'add':
        favs.books.add(obj)
      elif action == 'remove':
        favs.books.remove(obj)
      return redirect(next_path)   
    except book_models.DoesNotExist:
      return redirect(reverse("core:home"))
  else:
    return redirect(reverse("core:home"))

  return



