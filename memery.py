from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QApplication, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QPushButton, QButtonGroup)    
from random import randint
from random import shuffle 

class Question():
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []
questions_list.append(Question('Какой город является столицей Австралии?', 'Канберра', 'Сидней', 'Брисбен', 'Мельбурн'))
questions_list.append(Question('Какой химический элемент обозначается символом O?', 'Кислород ', 'Железо', 'Золото', 'Водород'))
questions_list.append(Question('Какое млекопитающее является самым крупным на Земле?', 'Синий кит', 'Кашалот', 'Жираф', 'Слон'))
questions_list.append(Question('В каком году человек впервые полетел в космос?', '1961', '1969', '1975', '1957'))
questions_list.append(Question('Кто написал роман «Преступление и наказание»?', 'Фёдор Достоевский', 'Антон Чехов', 'Лев Толстой', 'Александр Пушкин'))
questions_list.append(Question('Какая планета Солнечной системы самая близкая к Солнцу?', 'Меркурий', 'Марс', 'Венера', 'Юпитер'))
questions_list.append(Question('Кто написал картину «Мона Лиза»?', 'Леонардо да Винчи ', 'Микеланджело', 'Рафаэль', 'Пабло Пикассо'))
questions_list.append(Question('Какой орган человеческого тела самый крупный?', 'Кожа ', 'Печень', 'Кишечник', 'Легкие'))
questions_list.append(Question('Как часто проводятся летние Олимпийские игры в обычных условиях?', 'Раз в четыре года', 'Раз в два года', 'Каждый год', 'Раз в пять лет'))
questions_list.append(Question('Какая река считается самой длинной в мире?', 'Нил', 'Янцзы', 'Миссисипи', 'Амазонка'))
questions_list.append(Question('Какая скорость является предельной во Вселенной согласно теории относительности?', 'Скорость света', 'Скорость звука', 'Скорость вращения Земли', 'Скорость солнечного ветра'))
questions_list.append(Question('Какому актеру принадлежит рекорд по числу премий «Оскар» за лучшую мужскую роль (три статуэтки)?', 'Дэниел Дэй-Льюис', 'Леонардо Ди Каприо', 'Брэд Питт', 'Том Хэнкс'))
questions_list.append(Question('Что из этого является «мозгом» компьютера, выполняющим основные вычисления?', 'Центральный процессор (CPU)', 'Видеокарта (GPU)', 'Жесткий диск (HDD)', 'Оперативная память (RAM)'))


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следущий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    GroupBox.setExclusive(False)
    radio_but1.setChecked(False)
    radio_but2.setChecked(False)
    radio_but3.setChecked(False)
    radio_but4.setChecked(False)
    GroupBox.setExclusive(True)


def ask(q):
    shuffle(answers)
    question.setText(q.question1)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()


def check_answers():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score  += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильный ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')


def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильный ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)

    q = questions_list[cur_question]
    ask(q)

def click_ok():
    if button.text() == 'Ответить':
        check_answers()
    else:
        next_question()



app = QApplication([])
window = QWidget()
window.setWindowTitle('Картачки для запиминания')
window.resize(600, 500)

question = QLabel('Вопрос')
button = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Вопрос-ответ')

radio_but1 = QRadioButton('Ответ1')
radio_but2 = QRadioButton('Ответ2')
radio_but3 = QRadioButton('Ответ3')
radio_but4 = QRadioButton('Ответ4')

answers = [radio_but1, radio_but2, radio_but3, radio_but4]

GroupBox = QButtonGroup()
GroupBox.addButton(radio_but1)
GroupBox.addButton(radio_but2)
GroupBox.addButton(radio_but3)
GroupBox.addButton(radio_but4)

main_group_line = QVBoxLayout()
group_line1 = QHBoxLayout()
group_line2 = QHBoxLayout()

group_line1.addWidget(radio_but1)
group_line1.addWidget(radio_but2)
group_line2.addWidget(radio_but3)
group_line2.addWidget(radio_but4)

main_group_line.addLayout(group_line1)
main_group_line.addLayout(group_line2)

RadioGroupBox.setLayout(main_group_line)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Правда/Неправда')
lb_correct = QLabel('Сам верный ответ')

ans_group_line = QVBoxLayout()
ans_group_line.addWidget(lb_result, alignment=(Qt.AlignTop | Qt.AlignLeft))
ans_group_line.addWidget(lb_correct, alignment=Qt.AlignHCenter)

AnsGroupBox.setLayout(ans_group_line)

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(question, alignment=Qt.AlignCenter)
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3.addStretch(2)
line3.addWidget(button, stretch=2)
line3.addStretch(2)
AnsGroupBox.hide()

main_line.addLayout(line1, stretch=2)
main_line.addLayout(line2, stretch=8)
main_line.addStretch(1)
main_line.addLayout(line3, stretch=2)
main_line.addStretch(1)
main_line.addSpacing(5)

window.setLayout(main_line)

button.clicked.connect(click_ok)



window.setStyleSheet("""background: qlineargradient(
            x1: 0, y1: 0, x2: 0, y2: 1,
            stop: 0 #dfe8ed, stop: 1 #0b2e42
        );
        font-size: 15px;
                  color:blak""")



window.score = 0
window.total = 0
next_question()
window.resize(600, 400)
window.show()
app.exec()
