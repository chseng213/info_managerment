import pickle
from prettytable import PrettyTable
from classes_module import *


class DB:
    '''
    将信息对象以二进制的形式写入文件中储存
    '''

    def __init__(self):
        '''
        初始化:连接数据库,加载出数据库中的内容
        '''
        # 异常处理,可能还未创建数据库
        try:
            with open('phone_info.data', 'rb') as f:
                info_bytes = f.read()
                self.info = pickle.loads(info_bytes)
        # 如未创建数据库,将空列表赋值给self.info
        except Exception as e:
            self.info = []

    def commit(self):
        '''
        提交内容,将内存中的self.info以二进制的形式覆盖写入文件中
        :return:None
        '''
        info_bytes = pickle.dumps(self.info)
        with open('phone_info.data', 'wb') as f:
            f.write(info_bytes)

    def insert(self, info):
        '''
        添加记录
        :return:None
        '''
        self.info.append(info)
        self.commit()


    def search_by_id(self, id):
        '''
        通过id查找记录
        :param id:
        :return:
        '''
        for info in self.info:
            if id == info.id.id:
                return info

    def fuzzy_search_by_brand(self,brand_str):
        '''
        通过品牌模糊查找
        :param brand_str:相关字符串
        :return:查找到返回True  未查找到返回False
        '''
        for brand_list in [info.brand.brand for info in self.info]:
            if brand_str in brand_list:
                return True


    def search_by_brand(self, brand_str):
        '''
        通过品牌查找记录
        :param brand_str: 相关字符串
        :return:
        '''
        if self.fuzzy_search_by_brand(brand_str):
            x = PrettyTable(['序号', '品牌', '型号', '价格', '数量', '版本'])
            x.align['序号'] = '1'
            x.padding_width = 1
            for info in [info for info in self.info]:
                if brand_str in info.brand.brand:
                    x.add_row(([info.id, info.brand, info.model, info.price, info.count, info.version]))
            print(x)

            return None
        print('对不起,您查询的手机不存在!')

    def del_by_id(self, id):
        '''
        通过id删除记录
        :param id: id
        :return:
        '''
        info = self.search_by_id(id)
        if info:
            self.info.remove(info)
            self.commit()

        else:
            print('对不起,您查询的手机不存在!')


    def update_by_id(self, id,price):
        '''
        通过id修改手机价格
        :param id: id
        :param price: 价格
        :return:
        '''
        info = self.search_by_id(id)
        if info:
            info.price.price=price
            self.commit()

        else:
            print('对不起,您查询的手机不存在!')

    def display_all(self):
        '''
        查询所有记录
        :return:
        '''
        x = PrettyTable(['序号', '品牌', '型号', '价格', '数量', '版本'])
        x.align['序号'] = '1'
        x.padding_width = 1
        for info in self.info:
            x.add_row(([info.id, info.brand, info.model, info.price, info.count, info.version]))
        print(x)



if __name__ == '__main__':
    info1=Info(ID(1),Brand('Apple'),Model('IPHone4S'),Price(4999),Count(22),Version('国行正货'))
    info2=Info(ID(1),Brand('Apple'),Model('IPHone4S'),Price(4999),Count(22),Version('国行正货'))
    info3=Info(ID(1),Brand('Apple'),Model('IPHone4S'),Price(4999),Count(22),Version('国行正货'))
    db=DB()
    # db.insert(info1)
    # db.insert(info2)
    # db.insert(info3)
    # db.commit()
    db.display_all()