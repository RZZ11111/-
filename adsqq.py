a = int(input('Введите первое число:'))
d = input('Введите знак:')

if d == '+':
    b = int(input('Введите второе число:')) 
    print('Сумма равна:', a + b)
elif d == '-':
     b = int(input('Введите второе число:')) 
     print('Разность равна:', a - b)
elif d == '*':
    b = int(input('Введите второе число:'))
    print('Произведение равно:', a * b)
elif d == '/':
    b = int(input('Введите второе число:'))
    print('Частное равно:', a / b)
elif d == '**':
    print('Квадрат равен:', a*a)
else:
    print('Такого тут нема:') 