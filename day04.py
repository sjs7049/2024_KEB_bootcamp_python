# prime 2
numbers = input('Input first & second number : ').split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

for number in range(n1, n2 + 1):
    is_prime = True

    if number < 2:
        pass
    else:
        i = 2
        while i*i <= number:
            if number % i == 0:
                is_prime = False
                break
            i += 1
            # print(i, end=' ') # count check
        if is_prime:
            print(number, end=' ')