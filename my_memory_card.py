#создай приложение для запоминания информации
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])
main_win = QWidget()

RadioGroupBox = QGroupBox('Варианты ответов')
r_1 = QRadioButton('Энцы')
r_2 = QRadioButton('Смурфы')
r_3 = QRadioButton('Чулфымцы')
r_4 = QRadioButton('Алеуты')

l_1 = QHBoxLayout()
l_2 = QVBoxLayout()
l_3 = QVBoxLayout()

l_2.addWidget(r_1)
l_2.addWidget(r_2)
l_3.addWidget(r_3)
l_3.addWidget(r_4)
l_1.addLayout(l_2)
l_1.addLayout(l_3)
 
RadioGroupBox.setLayout(l_1)


q = QLabel('Какой национальности не существует?')
o = QPushButton ('Ответить')
o.setToolTip('Когда уверенны в своём ответе, нажмите сюда')



anss_box = QGroupBox('Результат теста')
anss = QLabel('Правильно/Неправильно')
anss_e = QLabel('Правильный ответ')
click = QPushButton('Следующий вопрос')

jake1 = QVBoxLayout()
jake1.addWidget(anss)
jake1.addWidget(anss_e)
anss_box.setLayout(jake1)
jake1.addWidget(click)
anss_box.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(r_1)
RadioGroup.addButton(r_2)
RadioGroup.addButton(r_3)
RadioGroup.addButton(r_4)

def  show_question():
    RadioGroupBox.hide()
    anss_box.show()
    o.hide()
    click.show()
    


o.clicked.connect(show_question)
RadioGroup.setExclusive(False)
r_1.setChecked(False)
r_2.setChecked(False)
r_3.setChecked(False)
r_4.setChecked(False)
RadioGroup.setExclusive(True)

class Question():
    def __init__ (self,question,right_answer,worn1,worn2,worn3):
        self.question = question
        self.right_answer = right_answer
        self.worn1 = worn1
        self.worn2 = worn2
        self.worn3 = worn3

q_1 = QVBoxLayout()
q_1.addWidget(q)
q_1.addWidget(RadioGroupBox)
q_1.addWidget(anss_box)
q_1.addWidget(o)

main_win.setLayout(q_1)

#main_win.setLayout(l_1)
main_win.show()
app.exec()
