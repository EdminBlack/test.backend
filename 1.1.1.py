# listter=[1,2,3,4,5,6,7,8,9,10]
# print(type(listter))
# print(listter)
# users=['Geeks','Osh','Anton','Nurbolot',listter]
# print(users[4])
# type_data=[5,'Пять',5.5,True,[1,2,3,4,5]]
# print(type_data)
# users=['Geeks','Osh','Anton','Nurbolot']
# user=['Islam','Anton']
# print(users)
# users.append('Beksultan')
# print(users)
# users.insert(1,"123")#добавление индексом
# print(users)
# users.insert(0,'Islam')
# print(users)
# users.remove('Anton')
# print(users)
# users.pop(1)#удалеение с индексом
# print(users)
# users.remove('Islam')
# print(users)
# users.extend(user) #добавление другого списка
# print(users)
# print(users.index('Nurbolot'))#чтобы узнать индекс элемента
# print(users.count('Nurbolot'))#чтобы узнать количество элемента в списке
# users.pop(2)
# print(users)
# users.reverse()#перевернуть список
# print(users)
# users.sort()#сортировка по алфавиту
# print(users)
# users.clear()
# print(users)
# users.

# users=[]
# name=input('Введите свое имя:')
# age=int(input('Введите свой возраст:'))
# if age<=18:
#     users.append(name)
#     print(users)
# else:
#     print('Допуск запрещен')

# auto=['Mersedes','BMW','TAYOTA','Chevrale','Supra','Nissan','KIA','Hyundai','Tiko']
# name=input('Введите свое имя:')
# car=input('Введите название машины:')
# if car in auto:
#     print('Уважаемый',name,'ваш выбор есть у нас в наличии.')
# else:
#     print('Уважаемый',name,'ваш выбор у нас нет в наличии.',car)
a=[1]
b=2
a.remove(b)
print(a)