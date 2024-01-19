import random

# numbers = []
# for i in range(5):
#     numbers.append(random.randint(1,100))

numbers = [random.randint(1,100) for i in range(10)]
print(numbers)

try:
    pick = int(input(f"Input index (0 ~ {len(numbers) - 1}) : "))
    print(numbers[pick])

except IndexError as err: # as ~ 해주면 시스템이 던져주는 어떤 오류인지에 대한 문구도 출력
    print(f'Wrong index number\n {err}')
except ValueError as err:
    print(f'Input Only Number!\n{err}')
except Exception: # detail한 예외 위에 적은 뒤 마지막에 넣어야 함
    print("Error Occurs.")