from django.views.generic import ListView, DetailView, CreateView, UpdateView
from books.models import Book
from reviews.forms import CreateReviewForm as review_form

class BooksView(ListView):
  
  model = Book
  paginate_by = 10
  paginate_orphans = 5
  ordering = "-created_at"
  context_object_name = "books"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_title'] = "All Books"
    return context


class BookDetail(DetailView):
  model = Book
  context_object_name = 'book'
    
  def get_context_data(self, **kwargs):                
    
    form = review_form

    try:
      user_reviews = self.request.user.reviews.all()
      user_reviews = [review.book for review in user_reviews]
    except:
      user_reviews = []
    reviewed = False    
    context = super().get_context_data(**kwargs)        
    book = context['book']
    if book in user_reviews:
      reviewed = True
    context['form']= form
    context['reviewed'] = reviewed
    return context  





class CreateBook(CreateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )


class UpdateBook(UpdateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )