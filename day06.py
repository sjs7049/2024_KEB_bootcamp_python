class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')

class Pikachu(Pokemon): # is-a
    def __init__(self, name, type):
        super().__init__(name) # super(): 부모 클래스의 정의를 얻음 즉 부모 클래스의 init method 정의
        self.type = type
    def attack(self, target): # 부모 클래스의 attack을 override(재정의)
        print(f'{self.name}이(가) {target.name}을(를) {self.type} 공격!')
    def electric_info(self):
        print("전기 계열의 공격을 합니다.")

class Squirtle(Pokemon): # is-a
    pass

class Agumon:
    pass

p1 = Pikachu("피카츄", "전기")
p2 = Squirtle("꼬부기")
p1.electric_info()
# p2.electric_info() : error (electric_info()는 Pikachu에 정의된 method이기 때문
p1.attack(p2)
p2.attack(p1)
print(p1.name, p1.type)
print(p1.name)
print(issubclass(Pikachu, Pokemon))
print(issubclass(Agumon, Pokemon))
