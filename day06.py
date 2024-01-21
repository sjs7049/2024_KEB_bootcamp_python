# 포캣몬 게임 기획하기

# 1. 플레이어 선택하기
# 1-1. 플레이어 정보 알려주기(공격, hp, 속성 등)
pokemon_list = ["파이어", "리자몽", "갸라도스", "샤미드", "쉐이미스카이", "토대부기", "썬더", "라이코", "뮤츠", "한카리아스", "픽시", "맘모꾸리"]
print(pokemon_list)
pokemon_info = dict(파이어 = {"속성": "불꽃", "체력": 207, "공격": {"열풍": 95, "오버히트": 160}},
                    리자몽 = {"속성": "불꽃", "체력": 186, "공격": {"블라스트번": 110, "오버히트": 160}},
                    갸라도스 = {"속성": "물", "체력": 216, "공격": {"용의파동": 90, "하이드로펌프": 130}},
                    샤미드 = {"속성": "물", "체력": 277, "공격": {"아쿠아테일": 50, "하이드로펌프": 130}},
                    쉐이미스카이 = {"속성": "풀", "체력": 225, "공격": {"풀묶기": 90, "솔라빔": 180}},
                    토대부기 = {"속성": "풀", "체력": 216, "공격": {"하드플랜트": 100, "지진": 140}},
                    썬더 = {"속성": "전기", "체력": 207, "공격": {"번개": 100, "전자포": 140}},
                    라이코 = {"속성": "전기", "체력": 207, "공격": {"와일드볼트": 90, "번개": 100}},
                    뮤츠 = {"속성": "에스퍼", "체력": 214, "공격": {"사이코브레이크": 90, "파괴광선": 150}},
                    한카리아스 = {"속성": "드래곤, 땅", "체력": 239, "공격": {"역린": 110, "지진": 140}},
                    픽시 = {"속성": "페어리", "체력": 216, "공격": {"매지컬샤인": 100, "문포스": 130}},
                    맘모꾸리 = {"속성": "얼음, 땅", "체력": 242, "공격": {"눈사태": 90, "10만마력": 110}})

player = input("다음 중 전투할 포켓몬을 선택하세요. : ")
print(f'{player} 정보 = {pokemon_info[player]}')
pokemon_list.pop(pokemon_list.index(player))

# 2. 플레이어 고르면 랜덤으로 상대 플레이어 뽑기
# 2-1. 예를 들어, 꼬부기 고르면 ‘접근 포켓몬은 리자몽입니다’ 메세지 띄우고 상대 정보 알려주기
def other_player(pokemonlist):
    '''
    내 포켓몬과 상대할 포켓몬 랜덤으로 뽑기
    :param pokemonlist: 뽑을 포켓몬 리스트
    :return: 상대 포켓몬
    '''
    import random
    otherplayer = random.choice(pokemon_list)
    return otherplayer

def doyouWantToFight(player):
    print(f'\n전투할 상대 포켓몬은 {player}입니다. {player}이(가) 접근 중입니다. 전투하시겠습니까?')
    print(f'{player} 정보 = {pokemon_info[player]}')

opponent = other_player(pokemon_list)
pokemon_list.pop(pokemon_list.index(opponent))
doyouWantToFight(opponent)

# 3. 옵션 만들기 1) 전투, 2) 도망, 3) 포기
print("1. 전투    2. 도망    3. 포기")

# 4. 전투 누를 시 돌아가면서 한 번씩 공격하여 hp가 0이 되는 플레이어가 지도록 만들기
# 5. 도망 누를 시 '다른 전투 지역으로 이동합니다.' 메세지 띄우기 새로운 상대 포켓몬 랜덤하게 생성되도록
# 6. 포기 누를 시 프로그램 종료

def whoistheFirst(player1, player2):
    '''
    먼저 공격할 포켓몬 정하기
    :param player1: 내 포켓몬
    :param player2: 상대 포켓몬
    :return: 선공인 포켓몬
    '''
    import random
    battlePokemon = [player1, player2]
    n = random.randint(0, 1)

    first = battlePokemon[n]
    second = battlePokemon[1-n]

    return first, second

class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        '''
        원하는 공격 입력해서 내 포켓몬이 상대 포켓몬 공격
        :param target: 상대 포켓몬
        :return:
        '''
        attackName = input(f'원하는 공격을 입력하세요. {pokemon_info[self.name]["공격"]} : ')

        print(f'{self.name}이(가) {target.name}을(를) {attackName} 공격!')
        pokemon_info[target.name]["체력"] -= pokemon_info[self.name]["공격"][attackName]
        print(f'{target.name}의 Hp가 {pokemon_info[self.name]["공격"][attackName]}만큼 줄어들었습니다.')

        if pokemon_info[self.name]["체력"] <= 0:
            print(f'{target.name}이 승리했습니다.')
        elif pokemon_info[target.name]["체력"] <= 0:
            print(f'{self.name}이 승리했습니다.')
        else:
            print(f'{self.name} Hp = {pokemon_info[self.name]["체력"]}, {target.name} Hp = {pokemon_info[target.name]["체력"]}')
            print()

    def random_attack(self, target):
        '''
        상대 포켓몬이 내 포켓몬 공격
        :param target: 내 포켓몬
        :return:
        '''
        import random
        attack_dict = dict(pokemon_info[self.name]["공격"])
        attack_list = list(attack_dict.keys())
        attackName = random.choice(attack_list)

        print(f'{self.name}이(가) {target.name}을(를) {attackName} 공격!')
        pokemon_info[target.name]["체력"] -= pokemon_info[self.name]["공격"][attackName]
        print(f'{target.name}의 Hp가 {pokemon_info[self.name]["공격"][attackName]}만큼 줄어들었습니다.')

        if pokemon_info[self.name]["체력"] <= 0:
            print(f'{target.name}이 승리했습니다.')
        elif pokemon_info[target.name]["체력"] <= 0:
            print(f'{self.name}이 승리했습니다.')
        else:
            print(f'{target.name} Hp = {pokemon_info[target.name]["체력"]}, {self.name} Hp = {pokemon_info[self.name]["체력"]}')
            print()

option = int(input("원하는 옵션의 번호를 입력하세요. : "))
while True:
    if option == 1:
        # 선공이 내 포켓몬부터면 내 공격 먼저
        # 선공이 상대 포켓몬이면 상대방이 공격한 후에 내가 입력하도록 코드 구현
        # 위 내용을 두 포켓몬 중 한 명이라도 체력이 0이되면 종료
        pokemon1, pokemon2 = whoistheFirst(player, opponent)
        print(f'\n전투 시작 전 선공을 정합니다. 선공인 포켓몬은 {pokemon1}입니다.')
        print("전투를 시작합니다.")

        if pokemon1 == player:
            cnt = 0
            first = Pokemon(pokemon1)
            second = Pokemon(pokemon2)
            while True:
                if cnt % 2 == 0:
                    first.attack(second)
                    if pokemon_info[pokemon1]["체력"] <= 0 or pokemon_info[pokemon2]["체력"] <= 0:
                        break
                else:
                    second.random_attack(first)
                    if pokemon_info[pokemon1]["체력"] <= 0 or pokemon_info[pokemon2]["체력"] <= 0:
                        break
                cnt += 1
        else:
            cnt = 1
            first = Pokemon(pokemon1)
            second = Pokemon(pokemon2)
            while True:
                if cnt % 2 == 0:
                    second.attack(first)
                    if pokemon_info[pokemon1]["체력"] <= 0 or pokemon_info[pokemon2]["체력"] <= 0:
                        break
                else:
                    first.random_attack(second)
                    if pokemon_info[pokemon1]["체력"] <= 0 or pokemon_info[pokemon2]["체력"] <= 0:
                        break
                cnt += 1
        break
    elif option == 2:
        if not pokemon_list:
            print("더이상 전투할 포켓몬이 없습니다. 게임을 종료합니다.")
            break
        else:
            print("다른 전투 지역으로 이동합니다.")
            otherPokemon = other_player(pokemon_list)
            doyouWantToFight(otherPokemon)

            otherPokemon_list = pokemon_list.pop(pokemon_list.index(otherPokemon))
            option = int(input("원하는 옵션의 번호를 입력하세요. : "))
            if option == 1:
                opponent = otherPokemon
    elif option == 3:
        print("전투를 포기하셨습니다. 게임을 종료합니다.")
        break
    else:
        print("유효하지 않은 번호입니다.")
        option = int(input("\n원하는 옵션의 번호를 입력하세요. : "))