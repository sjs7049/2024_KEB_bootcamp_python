course = "2024 KEB Bootcamp"
print(course.replace('KEB','Inha'))
print(course)

course = "KEB 2024 KEB Bootcamp"
print(course.replace('KEB','Inha'))
print(course)

course = "KEB 2024 KEB Bootcamp KEB...*!#"
course = course.replace('KEB','Inha',2) # 앞에 두 개의 KEB만 Ihna로 대체됨
print(course)
print(course.strip())
print(course.strip("!#.*"))

course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
course = course.replace('KEB','Inha',2)
print(course)
print(course.strip())
print(course.strip("!#.*"))

course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.find('KEB'))
print(course.rfind('KEB')) # 역방향으로 탐색
print(course.index('KEB'))
print(course.rindex('KEB'))
print(course.find('Inha')) # result: -1 (찾는 값이 없을 때 -1 출력)
print(course.index('Inha')) # ValueError: substring not found (예외 던짐)
