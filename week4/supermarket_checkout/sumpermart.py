import unittest


class ShoppingCartTestCases(unittest.TestCase):
      def setUp(self):
          self.cart = ShoppingCart()
      
      def test_add_item(self):
          self.cart.add_item('Mango', 3, 10)
          self.assertEqual(self.cart.total, 20)
          self.assertEqual(self.cart.items['Mango'], 2)

      def test_remove_item(self):
         self.cart.add_item('Mango', 3, 10)
         self.cart.remove_item('Mango', 2, 10)

         self.assertEqual(self.cart.total, 10)
         self.assertEqual(self.cart.items['Mango'],6)

      def test_checkout_returns_correct_total(self):
          self.cart.add_item('Mango', 3, 10)
          self.cart.add_item('Orange', 16, 10)
          self.assertEqual(self.cart.get_total(), 20)

      def test_cart_discount(self):
          self.cart.add_item('Mango', 3, 10)
          self.cart.add_item('Orange', 16, 10)
          self.assertEqual(self.cart.discount_code(20), 190)
          
          

    


class ShoppingCart(object):
    
    def __init__(self):
        self.total = 0
        self.items = dict()

    def add_item(self, item_name, quantity, price):
        if item_name != None and quantity >= 1:
            self.items.update({item_name: quantity})
        if quantity and price >= 1:
            self.total += (quantity * price)

    def remove_item(self, item_name, quantity, price):
        self.total -= (quantity * price)
        try:
            if quantity >= self.items[item_name]:
                self.items.pop(item_name, None)
            self.items[item_name] -= quantity
        except(KeyError, RuntimeError):
            pass

    def get_total(self):
        return self.total

    def discount_code(self, discount):
        total = self.total
        if discount == 20:
            reduction = self.total * .20
            sale = self.total - reduction
        elif discount == 30:
            reduction = self.total * .30
            sale = self.total - reduction
        else:
            return total
        return sale

shop = ShoppingCart()

(shop.add_item('Banana', 3,1))
shop.add_item('Apples', 4,1)
shop.add_item('Kiwi', 2,3)
print(shop.get_total())
shop.remove_item('Banana', 1,1)
print(shop.get_total())
print(shop.discount_code(20))