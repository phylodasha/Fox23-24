# Задача 1. Клонировать список
s = list(range(1, 8))
new = s
new = list(s)
print(new is s)

# Задача 2. Вложенный список

numbers = [[15, 16, 17], [21, 22, 23], [45, 46, 47, 44, 78, 90]]

for number in numbers:
    for n in number:
        print(n)

# Задача 3. 
students = ['Виктория', 'Матвей', 'Алексей', 'Полина', 'Александр']

for student in students:
    print(student)
    for letter in student:
        print(letter)


