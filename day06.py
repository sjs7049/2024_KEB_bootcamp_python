# class Pokemon:
#     def __init__(self, name):
#         print(f'{name} 포켓몬스터 생성')
#
# pikachu = Pokemon('피카츄')
# squirtle = Pokemon('꼬부기')
# print(pikachu) # 메모리 주소 출력 <__main__.Pokemon object at 0x000001CDA13D56F0>
# print(squirtle)

# class Pokemon:
#     pass
#
# pikachu = Pokemon()
# squirtle = Pokemon()
# pikachu.name = "피카츄"
# pikachu.nemesis = squirtle
# print(pikachu.name)
# # print(pikachu.nemesis.name)
# pikachu.nemesis.name = "꼬부기" # squirtle.name = "꼬부기"
# print(pikachu.nemesis.name)
# print(squirtle.name)

class Pokemon:
    def __init__(self, name):
        self.name = name # error 1 해결 - 따라서 이 문구 넣어줘야 함
        print(f'{name} 포켓몬스터 생성')

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격')

pikachu = Pokemon('피카츄')
squirtle = Pokemon('꼬부기')
charizard = Pokemon("리자몽")
# 해당 시점에 수행하는 객체: self
charizard.attack(squirtle) # 주체(self)는 charizard임
# print(pikachu.name) # error: Pokemen 객체는 name이라는 속성이 없음 - 1
# print(squirtle.name)