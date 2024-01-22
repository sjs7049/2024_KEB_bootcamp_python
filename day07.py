class FlyingBehavior:
    def fly(self):
        return f'하늘을 훨훨 날아갑니다~'

class Nofly(FlyingBehavior):
    def fly(self):
        return f'하늘을 날 수 업습니다.'

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f'날개로 하늘을 훨훨 날아갑니다~'

class SwimmingBehavior:
    def swim(self):
        return f'수영을 합니다.'

class Pokemon:
    def __init__(self, name, hp, fly):
        self.__name = name
        self.hp = hp
        self.fly_behavior = fly # aggregation (has-a)

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #name = property(get_name, set_name)
    # magic method 1
    def __str__(self):
        return self.__name + "입니다"

    # magic method 2
    def __add__(self, target):
        # return self.__name + " + " + target.__name
        return f'두 포켓몬 체력의 합은 {self.hp + target.hp}입니다.'

class Charizard(Pokemon):
    pass

class Pikachu(Pokemon):
    pass

nofly = Nofly()
p1 = Pikachu("피카츄", 35, nofly)
wings = FlyWithWings()
c1 = Charizard("리자몽", 120, wings)
print(c1.fly_behavior.fly())
print(p1.fly_behavior.fly())
print(p1)
print(c1)
print(p1+c1)