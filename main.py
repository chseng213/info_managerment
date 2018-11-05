from classes_module import *
from db import DB
import time


# todo 待完善
def main():
    db = DB()
    while True:
        print(
            '''
--------------------------------------------------            
            手机管理系统
            1.手机录入
            2.根据手机品牌查询手机信息
            3.查询全部收集信息
            4.根据手机编号修改手机价格
            5.根据手机编号删除记录
            6.退出
-------------------------------------------------- 
            '''
        )
        oper = input()
        if oper == '1':
            id = eval(input('请输入序号:'))
            if isinstance(id, int):

                brand = input('请输入品牌:')
                model = input('请输入型号:')
                price = eval(input('请输入价格:'))
                if isinstance(price, (int, float)):
                    count = input('请输入数量:')
                    if isinstance(count, int):
                        version = input('请输入版本:')
                        info = Info(ID(id), Brand(brand), Model(model), Price(price), Count(count), Version(version))
                        db.insert(info)
                        print('添加成功')
                        # db.commit()
                        db.display_all()
                        time.sleep(5)
                    else:
                        print('输入错误,请输入数字')
                        time.sleep(1)
                else:
                    print('输入错误,请输入数字')
                    time.sleep(1)
            else:
                print('输入错误,请输入数字')
                time.sleep(1)


        elif oper == '2':
            brand_str = input('请输入手机品牌:')
            db.search_by_brand(brand_str)
            time.sleep(5)

        elif oper == '3':
            db.display_all()
            time.sleep(5)

        elif oper == '4':
            id = eval(input('请输入编号'))
            if isinstance(id, int):
                price = eval(input('请输入修改的价格'))
                if isinstance(price, (int, float)):
                    db.update_by_id(id, price)
                    print('修改成功!')
                    db.display_all()
                    time.sleep(5)
                else:
                    print('输入错误,请输入数字')
                    time.sleep(1)
            else:
                print('输入错误,请输入数字')
                time.sleep(1)


        elif oper == '5':
            id = eval(input('请输入编号'))
            if isinstance(id, int):
                db.del_by_id(id)
                print('删除成功!')
                db.display_all()
                time.sleep(5)
            else:
                print('输入错误,请输入数字')
                time.sleep(1)
        elif oper == '6':
            print('程序退出,谢谢您的使用!')
            break
        else:
            print('对不起,您的输入有误,请重新输入!')
            time.sleep(1)


if __name__ == '__main__':
    main()
