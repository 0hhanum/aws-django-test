from django.views.generic import ListView, DetailView, CreateView, UpdateView
from movies.models import Movie
from reviews.models import Review
from reviews.forms import CreateReviewForm as review_form

class MoviesView(ListView):

    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created_at"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Movies"
        return context


class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'
    
    def get_context_data(self, **kwargs):                
      
      form = review_form
      try:
        user_reviews = self.request.user.reviews.all()
        user_reviews = [review.movie for review in user_reviews]
      except:
        user_reviews = []
      reviewed = False
      context = super().get_context_data(**kwargs)        
      movie = context['movie']
      if movie in user_reviews:
        reviewed = True
      context['form']= form
      context['reviewed'] = reviewed
      return context

class CreateMovie(CreateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )


class UpdateMovie(UpdateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )
