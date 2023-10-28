# season=int(input('Введите месяц:'))
# if season ==1 or season==2 or season==12:
#     print(season,'месяц принадлежит зиме')
# elif season ==3 or season==4 or season==5:
#     print(season,'месяц принадлежит весне')
# elif season ==6 or season==7 or season==8:
#     print(season,'месяц принадлежит лету')
# else:
#     print(season,'месяц принадлежит осени')


# bank=0
# money=int(input('Введите свой вклад:'))
# years=int(input('Введите количество лет:'))
# bank+=money
# for i in range(years):
#     bank+=money/10
# print(bank)


# list1=[]
# list2=[]
# count=0
# for i in range(5):
#     add1=int(input('Введите число для 1 списка:'))
#     add2=int(input('Введите число для 2 списка:'))
#     list1.append(add1)
#     list2.append(add2)
# list1.extend(list2)
# for i in range(len(list1)):
#     count+=list1[i]
# print(count)
# print(count/10)


# number=int(input('Введите число:'))
# for i in range(1,number):
#     print(0,i)
# i+=1
# print(0,i)


# list=[]
# for i in range(5):
#     add=input('Введите дополнение для списка:')
#     list.append(add)
#     for i in range(len(add)):
#         if add[i]=='A':
#             list.remove(add)
#         elif add[i]=='I':
#             list.remove(add)
#         elif add[i]=='a':
#             list.remove(add)
#         elif add[i]=='i':
#             list.remove(add)
# print(list)