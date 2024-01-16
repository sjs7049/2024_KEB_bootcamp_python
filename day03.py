# 3 입력할 때까지 반복문 돌아가도록 만들기 3 입력하면 프로그램 종료하도록
# 1 입력시: 화씨를 섭씨로 변경한 값 출력
# 2 입력시: 섭씨를 화씨로 변경한 값 출력
# 그 외 입력시: 프로그램 종료

while True:
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit    3) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}°F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}°C')
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}°C, Fahrenheit : {((celsius * 9.0 / 5.0) + 32.0):.4f}°F')
    elif menu == 3:
        print('Quit program.')
        break