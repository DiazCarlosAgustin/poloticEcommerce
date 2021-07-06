
from .models import Cart
from decimal import Decimal
from products.models import Product

class carrito(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(request.user.id)

        if not cart:
            cart = self.session[request.user.id] = {}

        self.cart = cart

    def add(self,request,product):
        id = str(product["id"])
        if id not in  self.cart:
            self.cart[id] = {
                "precio": str(product["precio"]),
            }
        self.save(request)

    def save(self, request):
        self.session[request.user.id] = self.cart
        self.session.modified = True

    def __iter__(self):
        products_id = self.cart.keys()

        products = Product.objects.filter(id__in= products_id)
        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["precio"] = Decimal(item["precio"])
            yield item
