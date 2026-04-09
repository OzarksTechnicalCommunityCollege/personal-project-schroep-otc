from decimal import Decimal
from django.conf import settings
from food.models import FoodItem


class FoodCart:
 
# Inialize the cart
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        return len(self.cart)

    # Add a product to the cart or update quantity
    def add(self, food_item, quantity=1):
        item_id = str(food_item.id)

        if item_id not in self.cart:
            self.cart[item_id] = 0

        self.cart[item_id] += quantity
        self.save()

    # Remove a product from the cart
    def remove(self, food_item):
        item_id = str(food_item.id)

        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    #Remove cart from session
    def clear(self):
        self.cart = {}
        self.save()

    # Mark the session as modified to make sure its saved
    def save(self):
        self.session.modified = True