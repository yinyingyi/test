'''
⼀个回合制游戏，每个⾓⾊都有hp 和power，hp代表⾎量，power代表攻击⼒，hp的初始值为1000，power的初始值为200。
定义⼀个fight⽅法：final_hp = hp-enemy_power
enemy_final_hp = enemy_hp - power
两个hp进⾏对⽐，⾎量剩余多的⼈获胜
'''
class Game():       #定义一个Game类
    def role(self,hp,power):    #定义role方法
        self.hp = hp            #定义hp属性，使用self后才能被其他方法调用
        self.power = power      #定义power属性

    def fight(self,enemy_power,enemy_hp):       #定义fight方法，敌人属性
        final_hp = self.hp - enemy_power        #定义final_hp计算方法
        enemy_final_hp = enemy_hp - self.power      #定义敌人final_hp计算方法
        if final_hp > enemy_final_hp:
            print('我赢啦！！')
        elif final_hp == enemy_final_hp:
            print('打了个平手！')
        else:
            print('很遗憾！我输了！')

g = Game()          #对Game()类进行实例化
g.role(1000,100)    #给role方法传参
g.fight(1200,200)   #给fight方法传参