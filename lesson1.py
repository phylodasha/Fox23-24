# Эта строка кода выводит на экран текст
# print('Привет, Фоксфорд!')
# print('1' + '2')
# print('Арсылан' + ' Топоев')
# print(1+2)

# print('1' * 1000)

# name = 'Даша'
# age = 57
# language = 'Русский'

# print('Мне ' , age, ' лет')

# age = input('Введите ваш возраст: ')
# age = int(age)
# print( age*2)


# Создай программу, которая запрашивает у 
# пользователя два числа и выводит их сумму, разность, 
# произведение и частное

a = int(input('Введите первое число: '))
b = int(input('введите второе число: '))

print('Сума: ', a+b)
print('Разность: ', a - b)
print('Произведение: ', a*b)
print('Частное: ', a / b)

# Создай программу, 
# которая вычисляет площадь прямоугольника, 
# квадрата и прямоугольного треугольника

a = int(input('введите длину стороны квадрата: '))
print('Площадь квадрата: ', a**2)


a = int(input('введите длину первой стороны прямоугольника: '))
b = int(input('введите длину второй стороны прямоугольника: '))

print('Площадь прямоугольника: ', a*b)


a = int(input('введите длину первого катета: '))
b = int(input('введите длину второго катета: '))

print('Площадь треугольника: ', (a*b)/2)