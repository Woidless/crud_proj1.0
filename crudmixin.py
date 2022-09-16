 product_ = dict(id=id, 
                        brand= input('Введите бренд: '),
                        model = input('Введите модель: '),
                        release = int(input('Введите дату релиза: ')),
                        volume = int(input('Введите объем: ')),
                        color = input('Введите цвет: '),
                        body = input('Выберите тип кузова:\n1-седан\t2-универсал\t3-купе\n4-минивен\t5-внедорожник\t6-пикап'),
                        mileage = int(input('Введите пробег: ')),
                        price = round(float(input('Введите цену: ')), 1))
