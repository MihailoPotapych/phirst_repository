import random
from tkinter import *
window = Tk()
window.geometry("720x500")
window.title('Тест')

questions = [
    {
        'question': 'Мальчик-Который-Выжил - это...',
        'answers': ['Гарри Поттер', 'Рональд Уизли', 'Драко Малфой']},

    {
        'question': 'Кто из персонажей является оборотнем?',
        'answers': ['Римус Люпин', 'Сириус Блэк', 'Том Реддл']},

    {
        'question': 'Кто не предавал Волан-де-Морта?',
        'answers': ['Беллатриса Лестрейндж', 'Северус Снегг', 'Регулус Блэк']},

    {
        'question': 'Как зовут феникса Дамблдора?',
        'answers': ['Фоукс', 'Файрекс', 'Финикс']},

    {
        'question': 'Кто из перечисленных персонажей лучше играет в шахматы?',
        'answers': ['Рон', 'Гермиона', 'Гарри']},
    {
        'question': 'Кагого цвета глаза Гарри Поттера(в книге)?',
        'answers': ['Зелёного', 'Синего', 'Серого']},

    {
        'question': 'Какую форму имеет Патронус Гарри Поттера?',
        'answers': ['Олень', 'Выдра', 'Феникс']},

    {
        'question': 'Кто убил Беллатрису Лестрейндж?',
        'answers': ['Молли Уизли', 'Гарри Поттер', 'Джинни Уизли']},

    {
        'question': 'Как зовут кошку Филча?',
        'answers': ['Миссис Норрис', 'У Филча не было кошки', 'Мурка']},

    {
        'question': 'Настоящее имя Волан-де-Морта - это...',
        'answers': ['Том Реддл', 'Геллерт Гриндевальд', 'Квиринус Квиррелл']}

]

quest_num = 0
score = 0
entryVar = StringVar()
right_ans = 0

def closeWindow():
    window.destroy()

def showFinalScreen():
    title_label['text'] = 'Спасибо за прохождение!'
    label1['text'] = f'Ваш счет: {score}'
    entry.destroy()
    butt['text'] = 'Выход'
    butt['command'] = closeWindow


def getLabelText():
    global quest_num, right_ans # Надо ли?
    if quest_num == len(questions):
        showFinalScreen()
        return
    result = questions[quest_num]['question'] + '\n'*2
    elem_index_values = []

    for ans_num in range(1, len(questions[quest_num]['answers'])+1):
        elem_index = random.randint(0, len(questions[quest_num]['answers']) - 1)

        while True:
            if elem_index in elem_index_values:
                elem_index = random.randint(0, len(questions[quest_num]['answers']) - 1)
            else:
                break

        elem_index_values.append(elem_index)

        if elem_index == 0:
            right_ans = ans_num
        ans = questions[quest_num]['answers'][elem_index]

        result += str(ans_num) + '.' + ans + '\n'
    return result


def checkAnswer():
    global quest_num, score, right_ans
    user_ans = entry.get()#Сделать проверки------------------------------------------------------
    if int(user_ans) == right_ans:
        score += 1

    if quest_num < len(questions):
        quest_num += 1
        label1['text'] = getLabelText()
    else:
        points_label=Label(text='Вы получили' + str(score) + ' очков(а)', font=('Arial', 24), bg='red', fg='white')
        points_label.place(x=0, y=0, width=700, height=50)



#DEBUG:

Var1 = 10

def debCorr():
    global Var1
    Var1 += 10
    label1['width'] = Var1
    debLabel['text'] = str(Var1)
#890
def debCorr1():
    global Var1
    Var1 -= 10
    label1['width'] = Var1
    debLabel['text'] = str(Var1)

debButt = Button(text='Больше', command=debCorr)
debButt.place(x=400, y=300)

debButt1 = Button(text='Меньше', command=debCorr1)
debButt1.place(x=400, y=350)

debLabel = Label()
debLabel.place(x=400, y=400)

#END_OF_DEBUG


title_label = Label(text='Тестирование', font=('Arial', 24), bg='red', fg='white')
title_label.place(x=0, y=0, width=720, height=50)

label1 = Message(text=getLabelText(),font=('Arial', 18), width=690)
label1.place(x=10, y=50)

butt = Button(text='ОК', font=('Arial', 24), command=checkAnswer)
butt.place(x=200, y=250)


entry = Entry(font=('Arial', 18))
entry.place(x=400, y=230)

window.mainloop()


'''
Вариант для консоли:

print('*'*20 + ' Викторина на тему "Гарри Поттер" ' + '*'*20 + '\n')

ShowRightAns = input('Хотите ли вы, чтобы при вводе неверного ответа отображался верный?(да или нет)').lower()

while True:
    if (ShowRightAns == 'да') or (ShowRightAns == 'нет'):
        break
    else:
        ShowRightAns = input('Пожалуйста, введите корректное значение: ').lower()
print('\n')

for quest in questions:
    print('Вопрос №' + str(questions.index(quest) + 1) + '. ' + quest['question'])
    elem_index_values = []
    right_ans = 0
    for ans_num in range(1, len(quest['answers']) + 1):-------------------------
        elem_index = random.randint(0, len(quest['answers'])-1)
        
        while True:
            if elem_index in elem_index_values:
                elem_index = random.randint(0, len(quest['answers'])-1)
            else:
                break
        
        elem_index_values.append(elem_index)
        
        if elem_index == 0:
            right_ans = ans_num
        ans = quest['answers'][elem_index]
        
        print(str(ans_num) + '.', ans)
        
    user_ans = input('Введите номер ответа: ')
    while True:
        try:
            int(user_ans)
        except BaseException:
            user_ans = input('Пожалуйста, введите числовое значение: ')
        if int(user_ans) in range(1, len(quest['answers']) + 1):
            break
        else:
            user_ans = input('Пожалуйста, введите корректное значение: ')
                
    if int(user_ans) == right_ans:
        print('Верно!\n')
    else:
        if ShowRightAns == 'да':
            print('Неверно. Правильный ответ: ' + str(right_ans) + '.\n')
        else:
            print('Неверно.\n')
            
    if questions.index(quest) + 1 == len(questions):
        print('*'*20 + ' Спасибо за прохождение! ' + '*'*20)

'''