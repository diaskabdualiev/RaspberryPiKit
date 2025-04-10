====================================================
Урок 3: Управление светодиодом через Flask
====================================================

В этом уроке мы создадим веб-приложение на базе **Flask**, позволяющее включать и выключать светодиод, подключённый к Raspberry Pi, через веб-интерфейс. Для управления GPIO используется библиотека **gpiozero**.

Структура проекта
-----------------
.. code-block:: bash

   lessons/
   └── lesson15/
       ├── app.py          # Flask-приложение
       └── templates/
           └── index.html  # HTML-файл для интерфейса

Полный код
----------
Ниже приведены файлы **app.py** и **index.html** целиком.

.. code-block:: python

   from flask import Flask, render_template, request
   from gpiozero import LED

   app = Flask(__name__)
   led = LED(18)  # Используем GPIO 18

   @app.route("/")
   def home():
       return render_template("index.html")

   @app.route("/led/<action>")
   def led_control(action):
       if action == "on":
           led.on()
           return "LED включён"
       elif action == "off":
           led.off()
           return "LED выключен"
       else:
           return "Неверная команда"

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)

.. code-block:: html

   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Управление светодиодом</title>
   </head>
   <body>
       <h1>Управление светодиодом</h1>
       <button onclick="fetch('/led/on')">Включить</button>
       <button onclick="fetch('/led/off')">Выключить</button>
   </body>
   </html>

Код приложения (app.py)
-----------------------
Ниже приведён код Flask-приложения, разбитый на несколько фрагментов с подробными пояснениями.

.. code-block:: python

   from flask import Flask, render_template, request
   from gpiozero import LED

Здесь:
- **Flask**, **render_template** и **request** импортируются из пакета flask, чтобы создать веб-приложение и рендерить шаблоны.
- **LED** из gpiozero позволяет включать/выключать светодиод на заданном GPIO.

.. code-block:: python

   app = Flask(__name__)
   led = LED(18)  # Используем GPIO 18

- Создаём объект Flask, передавая в него имя текущего модуля (__name__).
- Инициализируем **led = LED(18)**, что означает работу со светодиодом на GPIO 18.

.. code-block:: python

   @app.route("/")
   def home():
       return render_template("index.html")

- Декоратор **@app.route("/")** определяет маршрут для главной страницы. При переходе на http://<IP>:5000/ вызывается функция `home()`.
- Функция возвращает шаблон `index.html`, который лежит в папке `templates`.

.. code-block:: python

   @app.route("/led/<action>")
   def led_control(action):
       if action == "on":
           led.on()
           return "LED включён"
       elif action == "off":
           led.off()
           return "LED выключен"
       else:
           return "Неверная команда"

- Декоратор **@app.route("/led/<action>")** обрабатывает URL вида /led/on или /led/off.
- Если строка **action** равна "on", то вызывается **led.on()**, а при "off" — **led.off()**.
- Возвращается короткий текст о состоянии светодиода.

.. code-block:: python

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)

- При запуске файла напрямую, Flask-сервер стартует на **0.0.0.0:5000**, делая приложение доступным в локальной сети.

HTML-файл (index.html)
----------------------
Теперь рассмотрим саму HTML-страницу, расположенную по пути `templates/index.html`.

.. code-block:: html

   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Управление светодиодом</title>
   </head>
   <body>
       <h1>Управление светодиодом</h1>
       <button onclick="fetch('/led/on')">Включить</button>
       <button onclick="fetch('/led/off')">Выключить</button>
   </body>
   </html>

Здесь:
- Стандартные теги HTML: `<!DOCTYPE html>`, `<html>`, `<head>` (метаданные), `<body>` (контент).
- Две кнопки, при клике на которые отправляются GET-запросы `fetch('/led/on')` или `fetch('/led/off')`.
- Соответствующие маршруты в Flask-приложении вызывают включение или выключение светодиода.

Запуск проекта
--------------
1. Создайте папку `lesson15`, поместите туда `app.py` и папку `templates` с файлом `index.html`.
2. Убедитесь, что Flask и gpiozero установлены (например, `pip3 install flask gpiozero`).
3. Запустите приложение:

   .. code-block:: bash

      python3 lessons/lesson15/app.py

4. Откройте в браузере http://<RaspberryPi_IP>:5000

Ожидаемый результат
-------------------
В браузере отобразится страница с заголовком и двумя кнопками. При нажатии на «Включить» светодиод на GPIO18 загорается, при нажатии на «Выключить» — гаснет.

.. .. figure:: images/flask_gpio_led.png
..    :width: 50%
..    :align: center

   **Рис. 2:** Пример интерфейса управления LED

Завершение работы
-----------------
Нажмите **Ctrl + C** в терминале для остановки сервера. Теперь вы имеете простой веб-интерфейс для включения/выключения светодиода на Raspberry Pi!