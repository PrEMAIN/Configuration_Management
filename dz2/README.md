# Генератор графа зависимостей Git

Этот проект генерирует граф зависимостей на основе истории коммитов Git-репозитория. Граф визуализирует отношения между коммитами и измененными файлами и выводит его в формате PDF.

## Функции

- Анализирует историю коммитов Git-репозитория.
- Строит граф зависимостей, показывающий отношения между коммитами и измененными файлами.
- Выводит граф в формате PDF с использованием Graphviz.

## Требования

- Python 3.x
- Библиотека `pygraphviz`
- Библиотека `gitpython`
- Graphviz (должен быть установлен на вашей системе)

### Зависимости Python

Чтобы установить необходимые Python-пакеты, создайте виртуальное окружение и установите зависимости с помощью файла `requirements.txt`:

```bash
# Создайте виртуальное окружение
python3 -m venv venv

# Активируйте виртуальное окружение
source venv/bin/activate  # На macOS/Linux
# .\venv\Scripts\activate  # На Windows

# Установите зависимости
pip install -r requirements.txt