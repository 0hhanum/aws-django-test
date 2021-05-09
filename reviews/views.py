from django.shortcuts import redirect, reverse, render
from django.urls import reverse_lazy
from . import models, forms
from movies.models import Movie
from books.models import Book

# Create your views here.

def create_review(request, obj, pk):
  next_path = request.GET.get("next")

  try:
    
    if obj != 'movie' and obj != "book":
      raise Exception

    if request.method == "POST":
      form = forms.CreateReviewForm(request.POST)
      if form.is_valid():
        review = form.save(commit=False)
        review.created_by = request.user
        if obj == "movie":
          review.movie = Movie.objects.get(pk=pk)
        else:
          review.book = Book.objects.get(pk=pk)
        review.save()
        
        return redirect(next_path)
      elif obj == "movie":
        movie = Movie.objects.get(pk=pk)
        
        return render(request, "movies/movie_detail.html", {
          "movie": movie,
          "form": form
        })
      else:
        book = Book.objects.get(pk=pk)
        
        return render(request, "books/book_detail.html", {
          "book": book,
          "form": form
        })        
    

  except Exception as e:
    print(e)
    return redirect(reverse("core:home"))


def remove_reviews(request, pk):
  review = models.Review.objects.get(pk=pk)
  next_path = request.GET.get("next")
  review.delete()
  return redirect(next_path)

  