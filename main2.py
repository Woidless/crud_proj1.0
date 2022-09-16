'''
CRUD
'''
from search_object import search_object
class CrudMixin:
    def _get_or_set_obj_and_id(self):
        try:
            if (self.objects or not self.objects) and (self.id or not self.id):
                pass
        except(NameError, AttributeError):
            self.objects = []
            self.id = 0

    def create(self, **kwargs):
        self._get_or_set_obj_and_id()
        self.id += 1
        object_ = dict(id = self.id, **kwargs)
        print('='*100)
        # print(object_)
        self.objects.append(object_)
        return {'status': 201, 'msg': object_}

    def list_api(self):
        result = []
        for obj in self.objects:
            result.append({'id':obj['id'],
                           'title': obj['title'],
                           'price':obj['price']})

        return {'status': 200, 'msg': result}

    @search_object
    def detail(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            return {'status': 200, 'msg': obj}
        return {'status': 404, 'msg': 'Not found!'}

    @search_object
    def update(self, id, **kwargs):
        obj = kwargs.pop('object_')

        if obj:
            obj.update(**kwargs)
            return {'status': 206, 'msg': obj}
        return {'status': 404, 'msg': 'Not found!'}

    @search_object
    def delete(self, id, **kwargs):
        obj = kwargs['object_']
        if obj:
            self.objects.remove(obj)
            return {'status': 204, 'msg': 'Successfully deleted!'}
        return {'status': 404, 'msg': 'Not found!'}

    def save(self):
        import json
        json.dump(self.objects, open('data2.json', 'w'))
        return 'Saved!'
    
# class Product(CrudMixin):
#     obj = [{}, {}, {}]

# class Post(CrudMixin):
#     pass

smartphons = CrudMixin()
print(smartphons.create(
                 title = 'Redmi Note 10',
                 description = 'The best',
                 qty= 10, 
                 price = 1000))

print(smartphons.create(
                 title = 'Redmi Note 20',
                 description = 'The smart',
                 qty= 13, 
                 price = 8000))

print(smartphons.create(
                 title = 'iPhone 13',
                 description = 'The rich',
                 qty= 3, 
                 price = 1200))

print('='*100)
print(smartphons.list_api())
print('='*100)
print(smartphons.detail(4))
print('='*100)
print(smartphons.update(1, title='Redmi Note 100 pro', qty=1))
print('='*100)
print(smartphons.detail(1))
print('='*100)
print(smartphons.list_api())
print('='*100)
print(smartphons.delete(3))
print('='*100)
print(smartphons.list_api())

print(smartphons.create(
                 title = 'iPhone 14',
                 description = 'The rich2',
                 qty= 3, 
                 price = 1300))
                 
print(smartphons.create(
                 title = 'iPhone 15',
                 description = 'The rich3',
                 qty= 3, 
                 price = 1400))
print('='*100)
print(smartphons.list_api())
print('='*100)
print(smartphons.save())