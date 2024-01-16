# prime number
number = int(input("Input number : "))
is_prime = True
i = 2
while i < number:
    if number % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(f'{number} is prime number.')
else:
    print(f'{number} is not prime number.')
