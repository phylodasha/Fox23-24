product = ''
product_list = []
while product != '0':
    product = input('Введите продукт, который нужно добавить в список. Если захотите закончить ввод, напишите 0: ')
    product = product.lower()
    product = product.capitalize()
    product_list.append(product)

del product_list[-1]
for i in range(len(product_list)):
    print(f'{i+1}. {product_list[i]}')

print('Добро пожаловать в магазин! Вводите те товары, которые вы уже купили!')

while len(product_list) > 0:
    product = input('Введите название продукта, который вы положили в корзину: ')
    product = product.lower()
    product = product.capitalize()
    if product in product_list:
        product_list.remove(product)
        print('Отлично! Удаляю продукт из списка. Вот что осталось купить:')
        for i in range(len(product_list)):
            print(f'{i+1}. {product_list[i]}')
    else:
        print('Такого продукта нет в списке')

print('Поздравляем! Вы купили все, что нужно! Счастливого пути домой!')