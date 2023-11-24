words = {
    'Морковь': 'carrot',
    'Яблоко': 'apple',
    'Картофель': 'potato',
    'Банан': 'banana',
    'собака': 'dog'
}

while True:
    word = input('Какое слово нужно перевести на английский?')
    word = word.lower().capitalize()
    translation = words.get(word, 'Перевод не найден') 
    if translation == 'Перевод не найден':
        print('Такого слова пока нет в нашем словаре. Хотите добавить?')
        add = input().lower()
        if add == 'да':
            words[word] = input('Введите перевод слова на английский')
        else:
            print('Ладно, идем дальше')
    else:
        print(f'Перевод слова {word} на ангийский: {words[word]}')
    answr = input('Хотите завершить работу?')
    answr = answr.lower()
    if answr == 'да':
        break
