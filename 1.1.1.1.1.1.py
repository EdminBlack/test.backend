# def Heheheha():
#     print('Heheheha!')
# Heheheha()
# def грт(a,b):
#     print(a/b)
# грт(10,3)
import random
def game(num):
    ran=random.randint(1,5)
    if ran==num:
        print(f'Вы выиграли. Бот выбрал:{ran}')
    else:
        print(f'Вы проиграли. Бот выбрал:{ran}')


def menu():
    while True:
        print('1-играть или 2-узнать информацию')
        num=int(input('Введите свой выбор:'))
        if num==1:
            num1=int(input('Введите число от 1 до 5:'))
            game(num1)
        elif num==2:
            print('Вы аут')
def register(name,age,phone):
    if age>=18:
        print('Добро пожаловать')
        print(f'Имя:{name}, телефонный номер:{phone},возраст:{age}')
        menu()
    else:
        print('Вам нет 18 лет')
register('Islam',99,'0707007041')