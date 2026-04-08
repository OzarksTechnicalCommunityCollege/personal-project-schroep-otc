class FoodCart:
    SESSION_KEY = "cart"

    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(self.SESSION_KEY, {})

    def __len__(self):
        return len(self.cart)

    def add(self, food_item, quantity=1):
        item_id = str(food_item.id)

        if item_id not in self.cart:
            self.cart[item_id] = 0

        self.cart[item_id] += quantity
        self.save()

    def remove(self, food_item):
        item_id = str(food_item.id)

        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def clear(self):
        self.cart = {}
        self.save()

    def save(self):
        self.session[self.SESSION_KEY] = self.cart
        self.session.modified = True