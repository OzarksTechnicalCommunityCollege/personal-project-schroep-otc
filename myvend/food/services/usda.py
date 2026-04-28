import requests
from django.conf import settings

BASE_URL = "https://api.nal.usda.gov/fdc/v1"


def search_food(query):
    url = f"{BASE_URL}/foods/search"
    params = {
        "api_key": settings.USDA_API_KEY,
        "query": query,
        "pageSize": 1,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json().get("foods", [])


def get_nutrient(food, nutrient_name):
    for nutrient in food.get("foodNutrients", []):
        if nutrient.get("nutrientName") == nutrient_name:
            return nutrient.get("value")
    return None


def get_nutrition_from_food(food):
    return {
        "fdc_id": food.get("fdcId"),
        "calories": get_nutrient(food, "Energy"),
        "protein_g": get_nutrient(food, "Protein"),
        "carbs_g": get_nutrient(food, "Carbohydrate, by difference"),
        "fat_g": get_nutrient(food, "Total lipid (fat)"),
        "fiber_g": get_nutrient(food, "Fiber, total dietary"),
        "sugar_g": get_nutrient(food, "Sugars, total including NLEA"),
        "sodium_mg": get_nutrient(food, "Sodium, Na"),
        "serving_size": food.get("servingSize"),
        "serving_unit": food.get("servingSizeUnit", ""),
    }