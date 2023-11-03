# # Задача 1 - Фибоначчи
# n = int(input())
# fib1 = 1
# fib2 = 1
# print(fib1)
# print(fib2)

# for i in range(2, n):
#     temp = fib1 + fib2
#     fib1 = fib2
#     fib2 = temp
#     print(fib2)


# # Задача 2 - сумма чисел от 1 до n

# n = int(input())
# sum_ = 0
# for number in range(1, n+1):
#     sum_ += number

# print(f"Сумма чисел от 1 до {number}: {sum_}")


## Задача 3. Таблица умножения

# for n in range(1, 11):
#     for i in range(1, 11):
#         print(f"{i}*{n}={n * i}")
#     print()
#     print()

tasks = []

task = input("Укажите задание, которое вы хотите выполнить (чтобы закончить список введите 0): ")
while task != "0":
    tasks.append(task)
    task = input("Укажите задание, которое вы хотите выполнить (чтобы закончить список введите 0): ")
    
print("Дела на сегодня:")
for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i]}")

