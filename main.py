print("hello")
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import *

app = QApplication([])
window = QWidget()
window.resize(500, 300)
words = QLabel('Задай вопрос оракулу.')
button = QPushButton('Получить ответ')
line = QVBoxLayout()
line.addWidget(words)
line.addWidget(button)
window.setLayout(line)
answer = ['да', 'нет', 'скорее нет', 'скорее да', 'возможно', ' вероятно', 'будущее туманно..']
def generate():
    words.setText(choice(answer))
button.clicked.connect(generate)
window.setStyleSheet('font-size: 28px;')
window.show()
app.exec()
