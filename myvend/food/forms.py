from django import forms
from .models import FoodItem

# Create FoodItemForm
class FoodItemForm(forms.Form):
    food_name = forms.CharField(max_length=50)
    type_id = forms.IntegerField(min_value=0)       # allows 0 and up
    location_id = forms.IntegerField(min_value=0)   # allows 0 and up
    quantity = forms.IntegerField(min_value=0)
    expiry_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )


