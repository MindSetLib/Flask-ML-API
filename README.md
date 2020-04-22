# Flask-ML-API

## Пример вывода в продукцию модели машинного обучения

### Установка:
- создать виртуальное окружение с python 3.7

- установка зависимостей:
```sh
pip install -r requirements.txt
```

### Запуск сервера приложений

```sh
gunicorn -w 4 -b 127.0.0.1:5000 app:app
```

### Запуск тестов
```sh
python -m pytest -vv
```

### Для установки на Heroku
добавить buildpacks (java нужна для работы библиотеки h2o):
- heroku/python
- https://github.com/heroku/heroku-buildpack-jvm-common.git

### Презентация для лекции
[ссылка](https://hackmd.io/@AndreyPhys/flask-ml-api)
