# factorial example
def factorial_repetition(n) -> int:
    '''
    반복문을 이용한 factorial 함수
    :param n: 정수, int
    :return: 팩토리얼 값, int
    '''
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_recursion(n):
    '''
    재귀함수를 이용한 factirial 함수
    :param n: 정수, int
    :return: function
    '''
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)

number = int(input("number: "))
print(factorial_repetition(number))
print(factorial_recursion(number))