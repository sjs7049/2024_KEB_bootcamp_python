# day2 homework에서 추가 수정
# 3번: 수 하나 입력 받아서 소수 판정
# 4번: 두 수 입력 받아서 해당 구간에서 소수인 거 모두 출력
# 5번: 종료

while True:
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit    3) Is prime?    "
                 "4) Prime output   5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}°F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}°C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}°C, Fahrenheit : {((celsius * 9.0 / 5.0) + 32.0):.4f}°F')
    elif menu == '3':
        number = int(input('Input number : '))
        is_prime = True

        if number < 2:
            print(f'{number} is not prime number.')
        else:
            for i in range(2,number):
                if number % i == 0:
                    is_prime = False
                    break

        if is_prime:
            print(f'{number} is prime number.')
        else:
            print(f'{number} is not prime number.')
    elif menu == '4':
        numbers = input('Input first & second number : ').split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2+1):
            is_prime = True

            if number < 2:
                pass
            else:
                for i in range(2,number):
                    if number % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(number, end=' ')
        print()
    elif menu == '5':
        print('Quit program.')
        break

# 6.1 Use a for loop to print the values of the list [3, 2, 1, 0].
numbers = [3,2,1,0]
for number in numbers:
    print(number)

# 6.2 Assign the value 7 to the variable guess_me, and the value 1 to the variable
# number. Write a while loop that compares number with guess_me.
# Print 'too low' if number is less than guess me.
# If number equals guess_me, print 'found it!' and then exit the loop.
# If number is greater than guess_me, print 'oops' and then exit the loop.
# Increment number at the end of the loop.
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
    number += 1

# 6.3 Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable
# called number over range(10). If number is less than guess_me, print 'too low'. If it
# equals guess_me, print found it! and then break out of the for loop. If number is
# greater than guess_me, print 'oops' and then exit the loop.
guess_me = 5
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break