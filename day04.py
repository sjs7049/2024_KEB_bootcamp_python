t1 = (5) # type: int
t2 = 5, # type: tuple
t3 = (5,) # type: tuple
t4 = (5,7) # type: tuple
t5 = 5,7 # type: tuple
print(type(t1),type(t2),type(t3),type(t4),type(t5))

t6 = "python", "kim" # packing
print(type(t6), t6[1])

subject, prof = t6 # unpacking
print(prof)
print(subject)

# packing 개수와 받는 변수 개수 같아야 함
# a,b,c = t6 # ValueError

t7 = () # type: tuple
t8 = tuple() # type: tuple
print(type(t7),type(t8))
print(type(9,),type((9,))) # type: int, tuple

t9 = 1, 2, 3
t10 = 1, 2
print(t9 == t10)
print(t9 <= t10)
print(t9 > t10)

t11 = 4.43,
t12 = 3.97, 4.1, 3.27
# print(t11 + t12)
print(id(t11))
t11 += t12
print(id(t11))
print(t11)