# print('Здравствуйте, дорогие покупатели! Мы предлагаем вам оценить наш магазин. Введите свою оценку от 1 до 5')
# name = input('Как вас зовут, пользователь 1? ')
# mark1 = int(input(f'{name}, введите свою оценку: '))
# name = input('Как вас зовут, пользователь 2? ')
# mark2 = int(input(f'{name}, введите свою оценку: '))
# name = input('Как вас зовут, пользователь 3? ')
# mark3 = int(input(f'{name}, введите свою оценку: '))
# name = input('Как вас зовут, пользователь 4? ')
# mark4 = int(input(f'{name}, введите свою оценку: '))
# name = input('Как вас зовут, пользователь 5? ')
# mark5 = int(input(f'{name}, введите свою оценку: '))

# count_users = 5

# avg = (mark1 + mark2 + mark3 + mark4 + mark5)/count_users

# print(f'Пользователи оценили работу магазина в {avg} баллов из 5')



# comment = "Магазин супер! Фрукты - 5, овощи - 5, но лимонад - 4, слишком сладкий. Обязательно придем ещё!"

# mark_fruits = int(comment[24])
# mark_vegetables = int(comment[35])
# mark_soda = int(comment[51])

# print(f'Пользователь поставил фруктам оценку {mark_fruits}')
# print(f'Пользователь поставил овощам оценку {mark_vegetables}')
# print(f'Пользователь поставил лимонаду оценку {mark_soda}')

# print(f'Средняя оценка: {(mark_fruits + mark_vegetables + mark_soda)/3}')


# s = 'ieuhnreaqhh hhhp48q2i3\2uqdjn; skbr lwjher'
# print(len(s)) # считает длину строки
# print(s.count('h')) # считает количество определенных символов в строке
# s1 = s.split('h') # делит строку по символу
# print(s1)

# print('7'.isalpha())



# comment = "Магазин  супер!  Фрукты - 5,  овощи  -  5, но  лимонад  -  4,  слишком сладкий. Обязательно придем ещё!"

# comment = comment.replace('Фрукты', '')

# print(comment)


marks = "112334445512342324444123555555"

count_one = marks.count('1')
count_two = marks.count('2')
count_three = marks.count('3')
count_four = marks.count('4')
count_five = marks.count('5')

avg = (count_one + count_two * 2 + count_three * 3 + count_four * 4 + count_five * 5)/len(marks)

print(f'Средняя оценка магазина пользователями: {avg}')



