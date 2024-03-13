# kali
Многофункциональный бот для ВКонтакте. В данный момент находится в стадии активной разработки.

## Установка
### Напрямую в системе
```sh
poetry env use python3.12
poetry install
poetry run python kali/main.py
```

### Docker Compose
Work in progress.

## Справка для разработчиков

### Установка Poetry
После того, как склонировал этот проект, [установи Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer), если ещё не сделал этого:

#### На Unix-системах:
```sh
curl -sSL https://install.python-poetry.org | python3 -

# Добавить следующую строку в ~/.zshrc или ~/.bashrc в зависимости от своего шелла:
export PATH="/home/vertex/.local/bin:$PATH"
```

#### На Windows:
При помощи pip:
```powershell
pip install poetry
```
Или вручную при помощи PowerShell:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Добавить в PATH следующую строку:
%APPDATA%\Python\Scripts
```

### Настройка виртуального окружения
```sh
poetry env use python3.12 
```
Советую также включить хранение venv в директории проекта, чтобы вдруг не потерять его и если вдруг IDE откажется резалвить импорты:
```sh
poetry config virtualenvs.in-project true
```
Для Visual Studio Code в репозитории лежит файл с настройками проекта, где указан путь к Python внутри venv и все модули должны адекватно отображаться, но если вдруг нет, то в настройках проекта укажи путь к Python, параметр `Python: Default Interpreter Path`, значение `.venv/bin/python`.

### Работа с зависимостями
Основные установленные зависимости описываются в `pyproject.toml`. Все зависимости проекта с конкретными версиями, в том числе дочерние основных, описываются внутри `poetry.lock` файла. Устанавливаются и удаляются очень просто:
```sh
poetry add vkbottle
poetry add vkbottle@^4.3 # конкретная версия
poetry add vkbottle --dev # как dev зависимость (не знаю зачем нам это нужно)
poetry add vkbottle --lock # добавить в poetry.lock, но не устанавливать в среду

poetry remove vkbottle
```
Посмотреть дерево зависимостей можно следующей командой:
```sh
poetry show --tree
```
Выполнение команд внутри виртуальной среды осуществляется так:
```sh
poetry run <команда>
poetry run python kali/main.py

# или можно войти в шелл используя текущий venv:
poetry shell
```

### Создание билда
Если вдруг будем публиковать релизы, то собрать проект можно при помощи следующей команды:
```sh
poetry build
```
Артефакты появятся в директории `dist` в корне проекта.

### Скрипты Poetry
С ними мы пока ещё не разобрались.