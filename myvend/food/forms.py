from django import forms
from .models import FoodItem, FoodType, Location

# Create FoodItemForm2
class FoodItemForm2(forms.Form):
    food_name = forms.CharField(max_length=50)
    food_type = forms.ChoiceField(FoodType.objects.All()) # want a dropdown menu
    location = forms.ChoiceField(Location.objects.All()) # want a dropdown menu
    quantity = forms.IntegerField(min_value=0)
    expiry_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )


# Make model form here
class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ["food_name", "food_type", "location", "quantity", "expiry_date"]



