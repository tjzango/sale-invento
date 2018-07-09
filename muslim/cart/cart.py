from decimal import Decimal
from django.conf import settings
from store.models import Stock


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        """
        Iterate over the items in the cart and get the stocks from the database.
        """
        stock_ids = self.cart.keys()
        # get the stock objects and add them to the cart
        stocks = Stock.objects.filter(id__in=stock_ids)
        for stock in stocks:
            self.cart[str(stock.id)]['stock'] = stock

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, stock, quantity=1, update_quantity=False):
        """
        Add a stock to the cart or update its quantity.
        """
        stock_id = str(stock.id)
        if stock_id not in self.cart:
            self.cart[stock_id] = {'quantity': 0,
                                   'price': str(stock.price)}
        if update_quantity:
            self.cart[stock_id]['quantity'] = quantity
        else:
            self.cart[stock_id]['quantity'] += quantity
        self.save()

    def remove(self, stock):
        """
        Remove a stock from the cart.
        """
        stock_id = str(stock.id)
        if stock_id in self.cart:
            del self.cart[stock_id]
            self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
