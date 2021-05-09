from django import forms 
from . import models


class CreateReviewForm(forms.ModelForm):
  class Meta:
    model = models.Review
    fields = ("text", "rating")
  
  def clean_rating(self):

    rating = self.cleaned_data.get("rating")
    
    if rating < 0 or rating > 5:
      raise forms.ValidationError("Rating should be 0 to 5!")
    
    return rating
  
