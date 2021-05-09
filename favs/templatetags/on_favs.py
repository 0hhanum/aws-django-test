from django import template
from favs import models as fav_models


register = template.Library()

@register.simple_tag(takes_context=True)
def on_favs(context, obj, type):
  user = context.request.user
  
  try:
    the_fav = fav_models.FavList.objects.get(created_by=user)
    if type == "movies":
      
      return obj in the_fav.movies.all()
    else:
      return obj in the_fav.books.all()

  except:
    the_fav = None
  pass


