subjects = ['Математика', 'Русский', 'Английский']
notes = [[], [], []]
subject = ''
while subject != '0':
    
    note = ''
    subject = input('По какому предмету будете вводить оценки?')
    if subject == '0':
        break
    subject = subjects.index(subject)
    current_notes = notes[subject]
    while note != 0:
        note = int(input('Введите свою оценку по математике. Когда захотите завершить ввод, напечатайте 0:'))
        current_notes.append(note)
    del current_notes[-1]
    notes[subject] = current_notes

print(notes)
subject = input('По какому предмету смотреть  оценки?')
subject = subjects.index(subject)
current_notes = notes[subject]
print(f'Средняя оценка по математике: {sum(current_notes)/len(current_notes)} ')
print(f'Минимальная оценка: {min(current_notes)}')
print(f'Максимальная оценка: {max(current_notes)}')
print('Количество оценок: ')
for i in range(1, 6):
    print(f'Количество оценки {i}: {current_notes.count(i)}')