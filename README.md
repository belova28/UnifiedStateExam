# Приложение для подготовки к ЕГЭ

Это приложение предназначено для помощи студентам в подготовке к Единому государственному экзамену (ЕГЭ) с помощью удобного интерфейса, который позволяет выбирать предметы, просматривать связанные темы и практиковаться с вопросами. Приложение использует PyQt6 для графического интерфейса и SQLite для управления данными.

## Функциональные возможности

- Выбор предметов: Выбор из различных предметов для изучения.
- Изучение тем: Просмотр подробной информации о выбранных темах.
- Практические вопросы: Возможность ответить на практические вопросы и получить мгновенную обратную связь.
- Управление пользовательскими задачами: Создание и управление собственными задачами для персонализированного обучения.

## Требования

- Python 3.x
- PyQt6
- SQLite3
- CSV файлы для первоначальной загрузки данных

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/belova28/UnifiedStateExam.git
cd unified-state-exam-app
2. Установите необходимые пакеты:
Вы можете установить необходимые пакеты Python с помощью pip:
pip install PyQt6
3. Подготовьте базу данных:
Убедитесь, что у вас есть база данных SQLite с именем UnifiedStateExam.db, содержащая соответствующие таблицы (topics, tasks, tasks_user) и CSV файл с именем items.csv, содержащий информацию о предметах.

4. Запустите приложение:
Выполните следующую команду, чтобы запустить приложение:
python main.py

## Структура кода

Приложение структурировано на несколько классов, каждый из которых представляет различные компоненты интерфейса:

- Main: Главное окно, где пользователи могут выбирать предметы.
- Topic: Отображает темы, связанные с выбранным предметом.
- Item: Позволяет пользователям выбрать между теорией и практикой для выбранной темы.
- Theory: Показывает теоретический контент для конкретной темы.
- Trainer: Предоставляет практические вопросы для ответов пользователей.
- User_tasks: Управляет задачами, созданными пользователями.
- New_task: Интерфейс для создания новых задач.
 
## Участники проекта:
- Белова Анна - [@belova28](https://github.com/belova28)
- Гаврилова Мария - [@Maria-125](https://github.com/Maria-125)
