a=input('Введите пароль:')
b=input('Введите пароль повторно:')
c=a.count('123')
if len(a)<=7:
    print('Короткий пароль!')
elif c==1 :
    print('Простой пароль!')
elif a!=b:
    print('Различаются')
else:
    print('OK','Пароль создан!')