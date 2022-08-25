import json

FILE_NAME = 'data.json'

def get_data():
    '''
    for get list of data from json file
    '''
    with open(FILE_NAME) as file:
        return json.load(file)

id_ = 1
def id_up():
    '''
    incremention
    '''
    global id_
    list_id = [i['id'] for i in get_data()]
    # если ID уже есть в DATA, то будет выполняться инкременция до тех пор, пока ID не будет уникальным
    while id_ in list_id: 
        id_ += 1

    return id_

def listing():
    '''
    show data 
    '''
    [print(get_data()[i]) for i in range(len(get_data()))]
    return 'Список товаров'

def create():
    '''
    create the new product
    '''
    data = get_data()
    product = {
                'id': id_up(),
                'brand': input('Enter brand of laptop: '),
                'model': input('Enter model of laptop: '),
                'year': int(input('Enter the year of manufacture of the laptop: ')),
                'description': input('Enter description: '),
                'price': round(float(input('Enter price: ')), 2)
    }
    data.append(product)
    
    json.dump(data, open(FILE_NAME, 'w'))
    return 'CREATED!!!'

def retrieve():
    '''
    get one product from data
    '''
    data = get_data()
    id_ = int(input('Enter the ID of the product you want to VIEW: '))
    product = list(filter(lambda x: x['id']==id_, data))[0]
    if product: return product
    else: return 'The product not found'

def update():
    '''
    update one product in data
    '''
    data = get_data()
    message = 'data is incomplete\nNOT CHAGED'
    id_ = int(input('Enter the ID of the product you want to CHAGE: '))
    print('-'*50)

    product = list(filter(lambda x: x['id']==id_, data))[0]
    index_ = data.index(product)

    if not product: return 'The product not found'

    choice_ = input('Enter what you want to change?\n1-brand\t2-model\t3-year\t4-description\t5-price\nENTER: ')
    print('-'*50)

    if choice_ == '1': # brand
        data[index_]['brand'] = input('Enter new name of brand: ')
        if not choice_: return message

    elif choice_ == '2': # model
        data[index_]['model'] = input('Enter new name of brand: ')
        if not data[index_]['model']: return message

    elif choice_ == '3': # year
        data[index_]['year'] = int(input('Enter new year: '))
        if not data[index_]['year']: return message

    elif choice_ == '4': # description
        data[index_]['description'] = input('Enter new description: ')
        if not data[index_]['description']: return message

    elif choice_ == '5': # price
        data[index_]['price'] = round(float(input('Enter new price: ')), 2)
        if not data[index_]['price']: return message

    else: return 'The command not found\nNOT CHENGED'

    json.dump(data, open(FILE_NAME, 'w'))
    return 'CHANGED'



def delete():
    '''
    delete product in data
    '''
    data = get_data()
    id_ = int(input('Enter the ID of the product you want to DELETE: '))
    
    product = list(filter(lambda x: x['id']==id_, data))[0]
    if not product: return 'The product not found!'

    index_ = data.index(product)
    data.pop(index_)
    json.dump(data, open(FILE_NAME, 'w'))
    return 'DELETED'
