# Поле чудес

print('Приветствуем нового игрока')
print('Мы сыграем в игру Поле чудес')

word = 'рюкзак'
task = 'Вид сумки'
# номер последней угаданной буквы
letter_number = 1
print(f'Задание этого раунда: {task}')
print(f'Слово состоит из {len(word)} букв')

count_try = 3
print(f'{word[0:letter_number]}{(len(word) - letter_number)*" _"}')

while count_try >=0 and letter_number < len(word)-1:
    letter = input(f'Введите {letter_number + 1}-ю букву:')
    if letter == word[letter_number]:
        letter_number += 1
    else:
        count_try -= 1
    print(f'{word[0:letter_number]}{(len(word) - letter_number)*" _"}')

if count_try <= 0:
    print('Не переживайте, вы сможете попробовать еще раз')
else:
    print('Поздравляю с победой!')