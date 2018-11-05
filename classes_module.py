class ID:
    def __init__(self,id):
        self.id=id

    def __str__(self):
        return str(self.id)

class Brand:
    def __init__(self,brand):
        self.brand=brand

    def __str__(self):
        return self.brand

class Model:
    def __init__(self,model):
        self.model=model

    def __str__(self):
        return self.model

class Price:
    def __init__(self,price):
        self.price=price

    def __str__(self):
        return str(self.price)

class Count:
    def __init__(self,count):
        self.count=count

    def __str__(self):
        return str(self.count)

class Version:
    def __init__(self,version):
        self.version=version

    def __str__(self):
        return self.version

class Info:
    '''
    写入文件对象的类,用于储存一条记录
    '''
    def __init__(self,id,brand,model,price,count,version):
        '''

        :param id:id对象
        :param brand: brand对象
        :param model: model对象
        :param price: price对象
        :param count: count对象
        :param version: version对象
        '''
        self.id = id
        self.brand=brand
        self.count=count
        self.price=price
        self.model=model
        self.version=version
