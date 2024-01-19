# Open Closed Principle
def test(f):
    '''
    decorator 함수, 함수 시작하면 start 출력, 함수 끝나면 end 출력
    :param f: function
    :return: closure function
    '''
    # def inner(*args, **kwargs)
    def inner(): # *args라 인수가 없어도 됨
        print('start')
        # result = f(*args, **kwargs)
        f()
        print('end')
        # return result
    return inner

@test
def greeting():
    print('안녕하세요~')

greeting()