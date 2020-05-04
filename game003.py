'''
代码优化——继承
使⽤传参的⽅式传⼊hp和⾎量,第⼆个⾓⾊，他叫后裔，后裔继承了⾓⾊的hp 和power。并多了护甲属性。
重新定义另外⼀个defense⽅法：final_hp = hp+defense-enemy_power
enemy_final_hp = enemy_hp - power
两个hp进⾏对⽐，⾎量剩余多的⼈获胜
'''
class Game():       #定义一个Game类
    def __init__(self,hp=1000,power=200):    #定义role方法,并给定属性赋默认值
        self.hp = hp            #定义hp属性，使用self后才能被其他方法调用
        self.power = power      #定义power属性

    def fight(self,enemy_power,enemy_hp):       #定义fight方法，敌人属性
        final_hp = self.hp - enemy_power        #定义final_hp计算方法
        enemy_final_hp = enemy_hp - self.power      #定义敌人final_hp计算方法
        if final_hp > enemy_final_hp:           #判断条件
            print('我赢啦！！')
        elif final_hp == enemy_final_hp:
            print('打了个平手！')
        else:
            print('很遗憾！我输了！')

class Houyi(Game):      #定义Houyi类，继承Game的属性
    def __init__(self,defense1):        #定义私有方法
        super().__init__()              #使用super()继承父类init()方法的属性
        self.defense1 = defense1        #定义defense1属性

    def defense(self,enemy_power,enemy_hp):     #定义defense方法
        final_hp = self.hp + self.defense1 - enemy_power    #后裔的最终血量计算方法
        enemy_final_hp = enemy_hp - self.power      #敌人的最终血量计算方法
        if final_hp > enemy_final_hp:
            print('h我赢啦！！')
        elif final_hp == enemy_final_hp:
            print('h打了个平手！')
        else:
            print('h很遗憾！我输了！')

h = Houyi(300)     #对Houyi()类进行实例化,并给defense1传参
h.defense(1200,300)     #给Houyi()类中defense方法传参
