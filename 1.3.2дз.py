a=int(input('Введите число:'))
b=int(input('Введите число:'))
c=int(input('Введите число:'))
if a<b and a<c:
    print(a)
elif b<c and b<a:
    print(b)
else:
    print(c)