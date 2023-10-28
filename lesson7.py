# numbers=[1,2,3,4,5]
# result=list(map(lambda num:num*2,numbers))
# print(result)


# def result(numbers):
#     result_numbers=[]
#     for s:
#         result_numbers.append(num*2)
#         return(resulnum in numbert_numbers)



names=['Mergul','Beksultan','Islam','Vlad']

# result=list(map(lambda num:num.upper(),names))
# print(result)
# def a(names):
#     for i in range(len(names)):
#         print(names[i],len(names[i]),'Букв')
# a(names)




# for i in range(len(names)):
#     a=names[i]
#     print(a.upper())
# try:
#     n=0
#     n1=2
#     print(n1/n)
# except ZeroDivisionError:
#     print('НЕЛЬЗЯ ПИСАТЬ ТЕКСТ БЕЗ КОВЫЧЕК')


# while True:
#     try:
#         try:
#             num1=int(input('Введите первое число:'))
#             num2=int(input('Введите второе число:'))
#             print(num1/num2)
#         except:
#             print('На ноль делить нельзя, ид учи математику!!!')
#     except:
#         print('Не пиши буквы, иди учи русский') 

try:
    num1=6
    num2='6'
    print(num1+num2)
except TypeError:
    result_num2=int(num2)
    result_num1=int(num1)
    print('Результат:',result_num1+result_num2)