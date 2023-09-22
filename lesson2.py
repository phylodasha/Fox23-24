# name_user = input('Введите ваше имя: ')
# name_adresat = input('Введите  имя адресата: ')

# first_wish = input('Введите первое пожелание: ')
# second_wish = input('Введите второе пожелание: ')
# third_wish = input('Введите третье пожелание (существительное в мужском роде): ')

# print(f'Дорогой {name_adresat}! От всей души поздравляю тебя с днем рождения! Хочется пожелать тебе {first_wish}, а также {second_wish} и, конечно,так необходимого всем {third_wish}. Пусть каждый твой день будет счастливым и радостным! С любовью и уважением, {name_user}')

count_packages_start = 100
price_packages = 1
count_sweets_start = 100
price_sweets = 67
count_pasta_start = 80
count_bread_start = 40
count_ice_cream_start = 55
count_cheasecacke_start = 1000

caschier_name = 'Александра'
price = 99
count_sweets = int(input('Введите количество купленных упаковок конфет: '))
count_pasta = int(input('Введите количество купленных упаковок макарон: '))
count_bread = int(input('Введите количество купленных буханок хлеба: '))
count_ice_cream = int(input('Введите количество купленного мороженого: '))
count_cheasecacke = int(input('Введите количество купленных сырков: '))
count_packages = int(input('Введите количество пакетов: '))

count_products = count_sweets + count_pasta + count_bread + count_ice_cream + count_cheasecacke

print('Магазин все по 99')

print('Продано товаров: ')
print(f'--пакетов: {count_packages} шт.')
print(f'--конфет: {count_sweets} шт.')
print(f'--макарон: {count_pasta} шт.')
print(f'--хлеба: {count_bread} шт.' )
print(f'--мороженого: {count_ice_cream} шт.')
print(f'--сырков: {count_cheasecacke} шт.')

print(f'Общее количество проданных товаров: {count_products}')

print('Количество оставшегося товара: ')
print(f'--пакетов: {count_packages_start - count_packages} шт.')
print(f'--конфет: {count_sweets_start - count_sweets} шт.')
print(f'--макарон: {count_pasta_start - count_pasta} шт.')
print(f'--хлеба: {count_bread_start - count_bread} шт.' )
print(f'--мороженого: {count_ice_cream_start - count_ice_cream} шт.')
print(f'--сырков: {count_cheasecacke_start - count_cheasecacke} шт.')

print('Кассовый чек')
print(f'Кассир: {caschier_name}')
print('=' * 20)
print(f'Количество товаров: {count_products}')
print(f'Количество пакетов: {count_packages}')
print(f'Сумма к оплате: {count_products * price + count_packages}')
print('Спасибо за покупку! Ждем вас снова!')