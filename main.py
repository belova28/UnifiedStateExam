from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLineEdit, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
import sys
import sqlite3
import csv
import random

conn = sqlite3.connect('UnifiedStateExam.db')
cursor = conn.cursor()

class Main(QWidget):
    def __init__(self, *args):
        super().__init__()
        with open('items.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.items = {row['item']: row['item_information'] for row in reader}
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle('')
        self.items_buttons = {}
        main_layout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.label.setText(
            'Привет,эта программа поможет тебе в подготовке к ЕГЭ. Выбери предмет, который хочешь сдавать:     ')
        self.label.setFixedSize(700, 25)
        main_layout.addWidget(self.label)
        ma_layout = QGridLayout(self)
        for i, item in enumerate(self.items):
            x = i % 5
            y = i // 5
            self.items_buttons[i] = QPushButton(item, self)
            self.items_buttons[i].setDisabled(True)
            self.items_buttons[i].clicked.connect(self.clicked_item)
            ma_layout.addWidget(self.items_buttons[i], y, x)
        self.items_buttons[0].setDisabled(False)
        main_layout.addLayout(ma_layout)

    def clicked_item(self):
        self.it = self.sender().text()
        self.clicked_form = Topic(self, self.it, self.items)
        self.clicked_form.show()
        self.close()


class Topic(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.arg_item = args[2]
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle(str(args[1]))
        self.topics_buttons = {}
        topic_layout = QVBoxLayout(self)
        base_layout = QHBoxLayout(self)
        self.label = QLabel(self)
        self.label.setText(self.arg_item[str(args[1])])
        self.label.setWordWrap(True)
        self.label.setFixedSize(400, 150)
        self.last_button = QPushButton(self)
        base_layout.addWidget(self.label)
        self.last_button.setText('Главная')
        self.last_button.setFixedSize(70, 25)
        self.last_button.clicked.connect(self.last)
        base_layout.addWidget(self.last_button)
        topic_layout.addLayout(base_layout)
        button_layout = QVBoxLayout(self)
        res = cursor.execute("SELECT topic FROM topics").fetchall()
        for i, (topic,) in enumerate(res, start=1):
            self.topics_buttons[i] = QPushButton(topic, self)
            self.topics_buttons[i].clicked.connect(self.clicked_topic)
            button_layout.addWidget(self.topics_buttons[i])
        topic_layout.addLayout(button_layout)

    def clicked_topic(self):
        self.it = self.sender().text()
        self.clicked_form = Item(self, self.it)
        self.clicked_form.show()
        self.close()

    def last(self, arg):
        self.last_form = Main(self, arg)
        self.last_form.show()
        self.close()


class Item(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.arg = str(args[1])
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle(str(args[1]))
        item_layout = QVBoxLayout(self)
        base_layout = QHBoxLayout(self)
        self.label = QLabel(self)
        self.label.setText(
            'Выбери "Теория", для получения информации по выбранному ранее разделу, или "Тренажер/практика", для отработки своих знаний по по выбранной теме или создать свое задание')
        base_layout.addWidget(self.label)
        self.last_button = QPushButton(self)
        self.last_button.setText('Главная')
        self.last_button.setFixedSize(70, 25)
        self.last_button.clicked.connect(self.last)
        base_layout.addWidget(self.last_button)
        item_layout.addLayout(base_layout)
        button_layout = QHBoxLayout(self)
        self.theory = QPushButton(self)
        self.theory.setText('Теория')
        self.theory.clicked.connect(self.theory_form)
        button_layout.addWidget(self.theory)
        self.trainer = QPushButton(self)
        self.trainer.setText('Тренажер/практика')
        self.trainer.clicked.connect(self.trainer_form)
        button_layout.addWidget(self.trainer)
        item_layout.addLayout(button_layout)
        self.user_task = QPushButton(self)
        self.user_task.setText('Мои задачи')
        self.user_task.clicked.connect(self.user_task_form)
        button_layout.addWidget(self.user_task)

    def user_task_form(self):
        self.it = self.sender().text()
        self.clicked_form = User_tasks(self, self.it, self.arg)
        self.clicked_form.show()
        self.close()

    def theory_form(self):
        self.it = self.sender().text()
        self.clicked_form = Theory(self, self.it, self.arg)
        self.clicked_form.show()
        self.close()

    def trainer_form(self):
        self.it = self.sender().text()
        self.clicked_form = Trainer(self, self.it, self.arg)
        self.clicked_form.show()
        self.close()

    def last(self, arg):
        self.last_form = Main(self, arg)
        self.last_form.show()
        self.close()


class Theory(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.arg = str(args[2])
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle(str(args[1]))
        theory_layout = QVBoxLayout(self)
        base_layout = QHBoxLayout(self)
        self.label = QLabel(self)
        self.label.setText(str(args[2]))
        base_layout.addWidget(self.label)
        self.last_button = QPushButton(self)
        self.last_button.setText('Главная')
        self.last_button.setFixedSize(70, 25)
        self.last_button.clicked.connect(self.last)
        base_layout.addWidget(self.last_button)
        theory_layout.addLayout(base_layout)
        result = cursor.execute("SELECT theory FROM topics WHERE topic=?", (args[2],)).fetchall()
        self.label1 = QLineEdit(self)
        self.label1.setText(result[0][0])
        theory_layout.addWidget(self.label1)
        self.trainer_button = QPushButton(self)
        self.trainer_button.setText('Тренажер/практика')
        self.trainer_button.clicked.connect(self.trainer_form)
        theory_layout.addWidget(self.trainer_button)

    def trainer_form(self):
        self.it = self.sender().text()
        self.clicked_form = Trainer(self, self.it, self.arg)
        self.clicked_form.show()
        self.close()

    def last(self, arg):
        self.last_form = Main(self, arg)
        self.last_form.show()
        self.close()


class Trainer(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.arg = str(args[2])
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle(str(args[1]))
        trainer_layout = QVBoxLayout(self)
        base_layout = QHBoxLayout(self)
        self.label = QLabel(self)
        self.label.setText(str(args[2]))
        base_layout.addWidget(self.label)
        self.last_button = QPushButton(self)
        self.last_button.setText('Главная')
        self.last_button.setFixedSize(70, 25)
        self.last_button.clicked.connect(self.last)
        base_layout.addWidget(self.last_button)
        trainer_layout.addLayout(base_layout)
        result_id1 = cursor.execute("SELECT id_topic FROM topics WHERE topic=?", (self.arg,)).fetchall()
        result1 = cursor.execute("SELECT task FROM tasks WHERE id_topic=?", (str(result_id1[0][0]),)).fetchall()
        self.label1 = QLabel(self)
        i = int(random.randint(0, (len(result1) - 1)))
        self.label1.setText(result1[i][0])
        trainer_layout.addWidget(self.label1)
        result_id2 = cursor.execute("SELECT id_task FROM tasks WHERE task=?", (self.label1.text(),)).fetchall()
        result2 = cursor.execute("SELECT task_img FROM tasks WHERE id_task=?", (str(result_id2[0][0]),)).fetchall()
        self.picture = QPushButton("", self)
        self.picture.setFixedSize(150, 150)
        original_pixmap = QPixmap(str(result2[0][0]))
        scaled_pixmap = original_pixmap.scaled(self.picture.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        self.picture.setIcon(QIcon(scaled_pixmap))
        self.picture.setIconSize(self.picture.size())
        trainer_layout.addWidget(self.picture)
        if str(result2[0][0]) == 'None':
            self.picture.hide()
        answer_layout = QHBoxLayout(self)
        self.user_answer = QLineEdit(self)
        answer_layout.addWidget(self.user_answer)
        self.answer_button = QPushButton(self)
        self.answer_button.setText('Ответ')
        self.answer_button.clicked.connect(self.answer)
        answer_layout.addWidget(self.answer_button)
        trainer_layout.addLayout(answer_layout)
        result_id3 = cursor.execute("SELECT id_task FROM tasks WHERE task=?", (self.label1.text(),)).fetchall()
        result3 = cursor.execute("SELECT answer FROM tasks WHERE id_task=?", (str(result_id3[0][0]),)).fetchall()
        self.right_answer = QLabel(self)
        self.right_answer.setText(result3[0][0])
        self.right_answer.hide()
        trainer_layout.addWidget(self.right_answer)
        self.theory_button = QPushButton(self)
        self.theory_button.setText('Теория')
        self.theory_button.clicked.connect(self.theory_form)
        trainer_layout.addWidget(self.theory_button)

    def answer(self):
        self.right_answer.show()

    def theory_form(self):
        self.it = self.sender().text()
        self.clicked_form = Theory(self, self.it, self.arg)
        self.clicked_form.show()
        self.close()

    def last(self, arg):
        self.last_form = Main(self, arg)
        self.last_form.show()
        self.close()


class User_tasks(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.arg = str(args[2])
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle(str(args[1]))
        user_tasks_layout = QVBoxLayout(self)
        base_layout = QHBoxLayout(self)
        self.label = QLabel(self)
        self.label.setText(str(args[2]))
        base_layout.addWidget(self.label)
        self.last_button = QPushButton(self)
        self.last_button.setText('Главная')
        self.last_button.setFixedSize(70, 25)
        self.last_button.clicked.connect(self.last)
        base_layout.addWidget(self.last_button)
        user_tasks_layout.addLayout(base_layout)
        self.tasks_user = QTableWidget(self)
        self.tasks_user.setColumnCount(2)
        user_tasks_layout.addWidget(self.tasks_user)
        result_id = cursor.execute("SELECT id_topic FROM topics WHERE topic=?", (self.arg,)).fetchall()
        res = cursor.execute("SELECT task, answer FROM tasks_user WHERE id_topic=?", (str(result_id[0][0]))).fetchall()
        self.tasks_user.setRowCount(len(res))
        for row_index, (task, answer) in enumerate(res):
            self.tasks_user.setItem(row_index, 0, QTableWidgetItem(task))
            self.tasks_user.setItem(row_index, 1, QTableWidgetItem(answer))
        self.append_task = QPushButton(self)
        self.append_task.setText('Создать задачу')
        self.append_task.clicked.connect(self.append_task_form)
        user_tasks_layout.addWidget(self.append_task)

    def append_task_form(self):
        self.it = self.sender().text()
        self.clicked_form = New_task(self, self.it, self.arg)
        self.clicked_form.show()
        self.close()

    def last(self, arg):
        self.last_form = Main(self, arg)
        self.last_form.show()
        self.close()


class New_task(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.arg = str(args[2])
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(520, 100, 400, 150)
        self.setWindowTitle('Новая задача')
        task_layout = QVBoxLayout(self)
        base_layout = QHBoxLayout(self)
        self.label = QLabel(self)
        self.label.setText(str(args[2]))
        base_layout.addWidget(self.label)
        self.back_button = QPushButton(self)
        self.back_button.setText('Назад')
        self.back_button.setFixedSize(70, 25)
        self.back_button.clicked.connect(self.back_form)
        base_layout.addWidget(self.back_button)
        self.last_button = QPushButton(self)
        self.last_button.setText('Главная')
        self.last_button.setFixedSize(70, 25)
        self.last_button.clicked.connect(self.last)
        base_layout.addWidget(self.last_button)
        task_layout.addLayout(base_layout)
        self.label_task = QLabel(self)
        self.label_task.setText('Условие задачи:')
        task_layout.addWidget(self.label_task)
        self.user_task = QLineEdit(self)
        task_layout.addWidget(self.user_task)
        self.label_answer = QLabel(self)
        self.label_answer.setText('Правильный ответ на задачу:')
        task_layout.addWidget(self.label_answer)
        self.task_answer = QLineEdit(self)
        task_layout.addWidget(self.task_answer)
        self.append_task_button = QPushButton(self)
        self.append_task_button.setText('Добавить задачу')
        self.append_task_button.clicked.connect(self.append_task)
        task_layout.addWidget(self.append_task_button)
        self.confirmation = QLabel(self)
        self.confirmation.setText('')
        task_layout.addWidget(self.confirmation)

    def back_form(self):
        self.it = self.sender().text()
        self.clicked_form = User_tasks(self, self.it, self.arg)
        self.clicked_form.show()
        self.close()

    def append_task(self):
        user_task_text = self.user_task.text()
        task_answer_text = self.task_answer.text()
        result_id = cursor.execute("SELECT id_topic FROM topics WHERE topic=?", (self.arg,)).fetchall()
        if not user_task_text or not task_answer_text:
            self.confirmation.setText("Пожалуйста, заполните все поля.")
            return
        try:
            cursor.execute('INSERT INTO tasks_user (id_topic, task, answer) VALUES (?, ?, ?)',
                           (str(result_id[0][0]), user_task_text, task_answer_text))
            conn.commit()
            cursor.execute('INSERT INTO tasks (id_topic, task, answer) VALUES (?, ?, ?)',
                           (str(result_id[0][0]), user_task_text, task_answer_text))
            conn.commit()
            self.confirmation.setText("Задача добавлена.")
        except Exception as e:
            self.confirmation.setText(f"Ошибка при добавлении задачи: {e}")
        self.user_task.clear()
        self.task_answer.clear()

    def last(self, arg):
        self.last_form = Main(self, arg)
        self.last_form.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
conn.close()
