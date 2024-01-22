# 포켓몬 게임 7일차에 배웠던 것들 활용해서 업그레이드 시키기

# 포켓몬 10마리 정보
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

pokemon_list = ["파이어", "리자몽", "갸라도스", "샤미드", "쉐이미스카이", "토대부기", "썬더", "라이코", "뮤츠", "한카리아스", "픽시", "맘모꾸리"]
def other_player(pokemonlist):
    '''
    내 포켓몬과 상대할 포켓몬 랜덤으로 뽑는 함수
    :param pokemonlist: 뽑을 포켓몬 리스트
    :return: 상대 포켓몬
    '''
    import random
    otherplayer = random.choice(pokemon_list)
    return otherplayer

def doyouWantToFight(opponent):
    '''
    상대 포켓몬과 전투할 여부 묻고 상대 포켓몬 정보 알려주는 함수
    :param opponent: 상대 포켓몬
    '''
    print(f'\n전투할 상대 포켓몬은 {opponent}입니다. {opponent}이(가) 접근 중입니다. 전투하시겠습니까?')
    print(f'{opponent} 정보 = {pokemon_info[opponent]}')

def whoistheFirst(player1, player2):
    '''
    먼저 공격할 포켓몬 정하기
    :param player1: 내 포켓몬
    :param player2: 상대 포켓몬
    :return: 선공, 후공
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