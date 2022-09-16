from views3 import CreateMixin, UpdateMixin, DestroyMixin, RetrieveMixin
import json 

class Product(CreateMixin, RetrieveMixin, DestroyMixin, UpdateMixin):
    def save(self):
        json.dump(self.objects, open('data2.json', 'w'))        
        return {'msg': 'Saved!'}

class Order:
    discount = 5
    def __init__(self) -> None:
        self.orders = []
        self.product = Product()
        self.product.post(title= 'Iphon 14 pro',
                        description= 'best best best',
                        qty = 3,
                        price = 800)

        self.product.post(title= 'Iphon 15 pro',
                        description= 'bestX20',
                        qty = 6,
                        price = 900)

    def create_order_(self, objects):
        ls = [] 
        for item in objects:
            for product in self.product.objects:
                if item['id'] == product['id']:
                    self.subtract_gty(item, product)
                    ls.append({'title': product['title'], 'qty': item['qty'], 'price': product['price']})
        self.orders.append(ls)
        money = self.total_count(ls)
        return {'order': ls, 'Total sum': money}



    def total_count(self, objects):
        total_count = 0
        for product in objects:
            price = product['price']
            total_count += self.make_discount(price, self.discount) * product['qty']
        return total_count

    def subtract_gty(self, item, product):
        result = product['qty'] - item['qty']
        if result < 0: raise Exception('Too many qty of product')
        product['qty'] = result

    def make_discount(self, price, percent):
        return price - (price / 100 * percent)

        
orders = Order()
print('\t\tBefore: ')
[print(i) for i in orders.product.objects]
print('\n'+ '='*100)
products = [{'id': 1, 'qty': 2}, {'id': 2, 'qty': 2}]
print(orders.create_order_(products))
print('\n'+ '='*100)
print('\t\tAfter: ')
[print(i) for i in orders.product.objects]
print('\n'+ '='*100)

# smartphons = Product()
# print('\n'+ '='*100 + '\n')
# print(smartphons.post(title= 'Iphone 14',
#                 description= ' The best',
#                 gty= 3,
#                 price= 700))
# print('\n'+ '='*100 + '\n')
# print(smartphons.post(title= 'Iphone 15',
#                 description= ' The best of the best',
#                 gty= 3,
#                 price= 700))

# print('\n'+ '='*100 + '\n')
# print(smartphons.get())
# print('\n'+ '='*100 + '\n')
# print(smartphons.patch(2, title= 'Redmi 100', 
#                           description='True hero',
#                           gty= 14,
#                           price=1200))
# print('\n'+ '='*100 + '\n')sudo apt install postgresql postgresql-contrib
# print(smartphons.delete(3))
# print('\n'+ '='*100 + '\n')
# print(smartphons.get())
# [print(i) for i in smartphons.get().['msg']]
# print('\n'+ '='*100 + '\n')
# print(smartphons.save())