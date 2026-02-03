from django import forms

class FoodEnterForm(forms.Form):
    name = forms.CharField(max_length=50)
    calories = forms.PositiveIntegerField() # using PositiveIntegerField since I want it to be 0 or positive
    fat = forms.PositiveIntegerField()
    protein = forms.PositiveIntegerField()
    fiber = forms.PositiveIntegerField()
    purine = forms.PositiveIntegerField()
    location = forms.CharField(max_length=50)
    quantity = forms.PositiveIntegerField()