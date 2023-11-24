a = [1, 2, 3, 4, 5]
try:
    print(a[7])
except IndexError:
    print('Такого индекса нет')


print('Привет мир')