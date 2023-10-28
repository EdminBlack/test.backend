# a=('Islam','Sanzar')
# print(type(a))
# a=list(a)
# print(type(a))
# student={'Name':'Beksultan','Age':20,'Height':160}
# dop_info={'hobby':'football'}
# print(student)
# print('Имя:',student['Name'])
# print('Возвраст:',student['Age'])
# print('Рост:',student['Height'])
# print(student)
# student['Job']='Developer'
# print(student)
# student['name']='Nurbolot'
# print(student)
# del student['Height']
# print(student)
# student.update(dop_info)
# print(student)

# print(student.keys())
# print(student.values())
# print(student.items())

# student.pop('Height')
# print(student)

# set,frozenset
# создается с помошью фигурных скобок
# не имеет структуры и определенного порядка
# не можем использовать индексы и срезы
# не имеет дупликаты
# set() неизменяемый тип данных
# frozenset не изменяемый тип данных
# users={'Nurbolot','Beksultan','Islambek','Geeks'}
# print(users)
# users.add('Anton')
# print(users)
# print(users[1]) не работает

# users=frozenset(['Nurbolot','Vlad','Georgia','Ilya'])
# users=set(users)
# users.remove('Vlad')
# users=frozenset(users)
# print(users)