'''
写⼀个Bicycle(⾃⾏车)类,有run(骑⾏)⽅法, 调⽤时显⽰骑⾏⾥程km(骑⾏⾥程为传⼊的数字)，
再写⼀个电动⾃⾏车类EBicycle继承⾃Bicycle,添加电池电量valume属性通过，参数传⼊, 同时有两个⽅法：
1. fill_charge(vol) ⽤来充电, vol 为电量
2. run(km) ⽅法⽤于骑⾏,每骑⾏10km消耗电量1度,当电量消耗尽时调⽤Bicycle的run⽅法骑⾏，通过传⼊的骑⾏⾥程数，显⽰骑⾏结果
'''
class Bicycle():            #定义一个Bicycle类
    def run(self,km):       #定义一个run方法，并传入一个km参数
        print('骑行里程为{}'.format(km))     #打印骑行里程数

class Ebicycle(Bicycle):#定义一个Ebicycle类，继承Bicycle类的属性
    def __init__(self,volume):      #定义私有方法电量
        self.volume = volume
        print('当前电量为{}'.format(self.volume))    #打印当前电量

    def fill_charge(self,vol):              #定义电瓶车充电电量
        print('充电电量是{}'.format(vol))    #打印电瓶车充电电量

    def run(self,km):                   #定义电瓶车骑行方法
        e_miles = self.volume*10       #e_miles属性，电瓶车支持的最大里程
        miles = km - e_miles        #miles属性，用于判断电瓶能否支持骑完全程
        if miles <= 0:
            print('电瓶车骑了{}公里'.format(km))
        else:
            #子类中有一个run，把父类的run覆盖掉了。需要使用super()调用，并传入除了电瓶车骑行的里程数
            super().run(miles)

# b = Bicycle()
# b.run()

eb = Ebicycle(10)   #实例化类，只能传参给init方法
eb.run(200)
print()