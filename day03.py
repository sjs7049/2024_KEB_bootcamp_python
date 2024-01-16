university = "Ihha\nUniversity"
# university = r"Ihha\nUniversity" # raw string
print(university)

number1 = input("First number : ")
number2 = input("Second number : ")
print(number1 + number2) # concatenation
print(number1 * 3) # duplicate
print(number1 + 3) # type error

university = "Ihha University!"
print(university[:4])
print(university[:-11]) # reverse index
print(university[:len(university)]) # print(university[:16])
print(university[::1]) # incresing 1
print(university[::2]) # incresing 2