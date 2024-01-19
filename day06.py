class FlyingMixin:
    def fly(self):
        return f'{self.name}이(가) 하늘을 훨훨~'

class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 어푸~"

class Pokemon:
    def __init__(self, name):
        self.__name = name

    def attack(self):
        print("공격!!")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")

print(g1.name)
# print(g1.__name): error - direct access 불가
# g1.__name = "잉어킹" : 잉어킹으로 바꿔도 값이 바뀌지 않음
g1._Pokemon__name = "잉어킹"
print(g1._Pokemon__name) # 접근 방법

