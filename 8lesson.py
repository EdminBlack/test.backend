# file_write=open('Geeks.txt','w')
# file_write.write('Всем привет, меня зовут Ивангай, это прохождение майнкрафта')
# file_write.close()
# test=open('test.txt','w')
# test.write('This is test work!!!')
# test.close()
# a=1
# while True:
#     test=open(f'test{a}.txt','w')
#     test.write('This is test work!!!')



# name=input('Введие имя:')
# age=(input('Введите возраст'))
# phone=(input('Введите номер телефона:'))
# file=open('info.txt','w')
# file.write(f'Имя: {name}, Возвраст: {age}, Телефонный номер: {phone}')
# file.close()


# file_read=open('info.txt','r')
# result=file_read.read()
# print(result)



# users=['Beksultan','Myuha','Islam','Anton']
# with open('info.txt','w') as write_list:
#     write_list.write(f'Пользователи:{users}')

# with open('info.text','w') as user_list:
#     for i in users:
#         user_list.write(f'Пользователь:{i}, \n')
        
        
# with open('calculator.py','w') as calc:
#     calc.write('''num1=int(input('Введите первое число:'))
# num2=int(input('Введите второе число:'))
# print(f'Результат после сложения: {num1}+{num2}')
# print(f'Результат после вычитания: {num1}-{num2}')
# print(f'Результат после умножения: {num1}*{num2}')
# print(f'Результат после деления: {num1}/{num2}')
# ''')


with open ('text.txt','r') as read_file:
    result=read_file.read()
    print(result)