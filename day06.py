# 포캣몬 게임 기획하기
import pokemon as p

# 1. 플레이어가 전투할 포켓몬 선택하기
print(p.pokemon_list) # 플레이어가 선택할 포켓몬 리스트

player = input("다음 중 전투할 포켓몬을 선택하세요. : ") # 포켓몬 리스트를 보고 포켓몬 이름을 직접 입력하여 선택
print(f'{player} 정보 = {p.pokemon_info[player]}') # 선택한 포켓몬 정보
p.pokemon_list.pop(p.pokemon_list.index(player)) # 게임 진행을 위한 부가적 코드

# 2. 랜덤으로 전투할 상대 포켓몬 뽑기
opponent = p.other_player(p.pokemon_list) # 전투할 상대 포켓몬 랜덤으로 지정
p.pokemon_list.pop(p.pokemon_list.index(opponent)) # 게임 진행을 위한 부가적 코드

# 3. 상대 포켓몬과 전투에 대한 선택
p.doyouWantToFight(opponent) # 지정된 상대 포켓몬과 전투할 것인지에 대한 물음
print("1. 전투    2. 도망    3. 포기") # 2번 물음에 대한 답 선택지

# 4. 각 선택지에 대한 코드
option = int(input("원하는 옵션의 번호를 입력하세요. : ")) # 원하는 답 번호로 입력
while True:
    if option == 1: # 1번 전투 입력 시
        # 위 내용을 두 포켓몬 중 한 명이라도 체력이 0이되면 종료
        pokemon1, pokemon2 = p.whoistheFirst(player, opponent)
        print(f'\n전투 시작 전 선공을 정합니다. 선공인 포켓몬은 {pokemon1}입니다.')
        print("----------전투를 시작합니다.----------")

        if pokemon1 == player: # 선공이 플레이어 포켓몬이면 먼저 공격
            cnt = 0
            first = p.Pokemon(pokemon1) # 플레이어 포켓몬
            second = p.Pokemon(pokemon2) # 상대 포켓몬
            while True:
                if cnt % 2 == 0: # 짝수면 플레이어 공격
                    first.attack(second) # 공격할 공격명 입력
                    if p.pokemon_info[pokemon1]["체력"] <= 0 or p.pokemon_info[pokemon2]["체력"] <= 0:
                        break # 두 포켓몬 중 누구든 체력이 없으면 전투 종료
                else: # 홀수면 상대 공격
                    second.random_attack(first)
                    if p.pokemon_info[pokemon1]["체력"] <= 0 or p.pokemon_info[pokemon2]["체력"] <= 0:
                        break
                cnt += 1
        else: # 선공이 상대 포켓몬이면 상대방이 공격한 후에 플레이어가 공격
            cnt = 1
            first = p.Pokemon(pokemon1) # 상대 포켓몬
            second = p.Pokemon(pokemon2) # 플레이어 포켓몬
            while True:
                if cnt % 2 == 0: # 짝수면 플레이어 공격
                    second.attack(first)
                    if p.pokemon_info[pokemon1]["체력"] <= 0 or p.pokemon_info[pokemon2]["체력"] <= 0:
                        break # 두 포켓몬 중 누구든 체력이 없으면 전투 종료
                else: # 홀수면 상대 공격
                    first.random_attack(second)
                    if p.pokemon_info[pokemon1]["체력"] <= 0 or p.pokemon_info[pokemon2]["체력"] <= 0:
                        break
                cnt += 1
        break
    elif option == 2: # 2번 도망 입력 시
        if not p.pokemon_list: # 더이상 전투할 포켓몬 없을 시 프로그램 종료
            print("더이상 전투할 포켓몬이 없습니다. 게임을 종료합니다.")
            break
        else:
            print("다른 전투 지역으로 이동합니다.") # 랜덤으로 지정된 상대 포켓몬과 전투하지 않을 시
            otherPokemon = p.other_player(p.pokemon_list) # 여태 나온 포켓몬 제외하고 랜덤으로 상대 포켓몬 다시 지정
            p.doyouWantToFight(otherPokemon) # 전투할 것인지에 대한 물음

            otherPokemon_list = p.pokemon_list.pop(p.pokemon_list.index(otherPokemon)) # 지정된 포켓몬 리스트에서 제외
            option = int(input("원하는 옵션의 번호를 입력하세요. : ")) # 다시 지정된 상대 포켓몬과 전투, 도망, 포기 중 고르기
            if option == 1: # 1번 전투 입력 시 위 1번 코드 실행
                opponent = otherPokemon
    elif option == 3: # 3번 포기 입력 시 프로그램 종료
        print("전투를 포기하셨습니다. 게임을 종료합니다.")
        break
    else: # 보기에 없는 번호 입력 시
        print("유효하지 않은 번호입니다.")
        option = int(input("\n원하는 옵션의 번호를 입력하세요. : "))