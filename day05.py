# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10).
# Use a for loop to find and print the third value returned.
def get_oods(first = 0, last = 10, step = 1):
    number = first
    while number < last:
        if number % 2 != 0:
            yield number
        number += 1

oods = get_oods()
ood = []
for x in oods:
    ood.append(x)
print(ood[2])

# 9.3 Define a decorator called test that prints 'start' when a function is called, and 'end' when it finishes.
def test():
    def func():
        print('start')
        print('end')
    return func

dec = test()
dec()

# 9.4 Define an exception called OopsException. Raise this exception to see what happens.
# Then, write the code to catch this exception and print 'Caught an oops'.
class OopsException(Exception):
    pass

try:
    raise OopsException('panic')
except OopsException as exp:
    print('Caught an oops')