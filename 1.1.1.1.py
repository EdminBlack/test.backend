# a=[]
# for i in range(100):
# print(a)
# users=['Nurbolot','Islam','Beksultan','Darika','MErgul']
# for i in users:
#     print('Hello',i)
#     a.append(i)

# for i in range(1,11):
#     print(i)
# n=9
# while True:
#     print(n)
#     n*=99999999999
users=[]
while True:
    name=input('Введите имя:')
    age=int(input('Введите возраст:'))
    if age>=18:
        print('Добро похаловать в наш клуб!!!')
        users.append(name)
        print(users)
    else:
        print('Вам нет 18 лет')