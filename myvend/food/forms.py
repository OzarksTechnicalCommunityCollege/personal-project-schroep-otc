from django import forms
from .models import FoodItem, FoodType, Location


# Make model form here
class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ["food_name", "food_type", "location", "quantity", "expiry_date"]
        widgets = {
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
        }

# Make search form here
class SearchForm(forms.Form):
    query = forms.CharField()

# Make login form here
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
