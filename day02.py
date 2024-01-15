letter = input("Input alphabet letter : ")
vowels = {'a','e','i','o','u'}
print(type(vowels))

if letter in vowels:
    print(f'{letter} is a vowel.')
else:
    print(f'{letter} is a consonant.')

vowels = 'aeiou'
print(type(vowels))