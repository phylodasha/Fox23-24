cashier_name = "Людмила"
price = 99
count_products = int(input("Введите количество товаров: "))
count_packages = int(input("Введите количество пакетов: "))
summa = price*count_products + count_packages
discount = 0
print("ООО FoxPrice")
print("КАССОВЫЙ ЧЕК")
print(f"Кассир: {cashier_name}")
print("=====================")

if 500 <= summa < 1500:
    print('Вы получаете скидку 5%')
    discount = 0.05
if 1500 <= summa < 5000:
    print('Вы получаете скидку 10%')
    discount = 0.1
if 5000 <= summa < 10000:
    print('Вы получаете скидку 20%')
    discount = 0.2
if 10000 <= summa:
    print('Вы получаете скидку 50%')
    discount = 0.5

# print(f'Скидка 5%: {500 <= summa < 1500}')
# print(f'Скидка 10%: {1500 <= summa < 5000}')
# print(f'Скидка 20%: {5000 <= summa < 10000}')
# print(f'Скидка 50%: {10000 <= summa}')

print(f"Количество товаров: {count_products}")
print(f"Количество пакетов: {count_packages}")
to_pay = 1 - discount
print(f"ИТОГО без скидки: {(price*count_products + count_packages)}")

print(f"ИТОГО: {(price*count_products + count_packages) * to_pay}")




# name = 'Алексей'
# age = 18
# name_user = 'Денис'
# age_user = 15

# if (name == name_user) and (age_user < age):
#     print('Вы получаете скидку в Фоксфорде!')






