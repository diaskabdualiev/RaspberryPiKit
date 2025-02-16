==========================================
Урок 1: Первый веб-сайт на Flask
==========================================

Теоретическая часть
-------------------
**Flask** – это лёгкий фреймворк на Python, позволяющий быстро создавать веб-приложения и веб-сервисы. В данном уроке мы создадим простой веб-сайт, запустим локальный сервер на Raspberry Pi и выведем "Hello, World!".

Необходимые компоненты
----------------------
- Raspberry Pi с установленным Python 3
- Интернет-соединение или локальная сеть

Установка Flask
---------------
1. Обновите систему:

   .. code-block:: bash

      sudo apt-get update
      sudo apt-get upgrade

2. Установите Flask (через pip):

   .. code-block:: bash

      pip3 install flask

Запуск кода
-----------
1. Создайте файл `app.py` в папке `lessons/lesson13/`:

   .. code-block:: bash

      mkdir -p lessons/lesson13
      nano lessons/lesson13/app.py

2. Вставьте следующий код и сохраните.

3. Запустите Flask-приложение:

   .. code-block:: bash

      python3 lessons/lesson13/app.py

4. Откройте браузер и перейдите по адресу http://<RaspberryPi_IP>:5000/

   Например, если ваш Raspberry Pi имеет IP 192.168.0.100, то набирайте http://192.168.0.100:5000/

Код программы
-------------
Файл: `lessons/lesson13/app.py`

.. code-block:: python

   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)

Разбор кода
-----------


.. code-block:: python

   from flask import Flask

- Импортируем класс Flask из пакета `flask`.


.. code-block:: python

   app = Flask(__name__)

- Создаём объект приложения Flask и передаём в него имя модуля (`__name__`).


.. code-block:: python

   @app.route('/')
   def hello_world():
       return 'Hello, World!'

- Декоратор `@app.route('/')` связывает функцию `hello_world()` с корневым URL ("/").
- При обращении к http://<IP>:5000/ возвращается строка "Hello, World!".


.. code-block:: python

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)

- Запускаем веб-сервер на порту 5000.
- `host='0.0.0.0'` означает, что сервер доступен по любому IP-адресу, привязанному к Raspberry Pi.

Ожидаемый результат
-------------------
При переходе в браузере на адрес http://<IP_адрес_RaspberryPi>:5000 вы должны увидеть страницу с надписью:

::

   Hello, World!

.. figure:: images/flask_hello_world.png
   :width: 50%
   :align: center

   **Рис. 2:** Пример отображения "Hello, World!" в браузере

Завершение работы
-----------------
Чтобы остановить сервер, в терминале нажмите **Ctrl + C**. Поздравляем! Вы создали свой первый веб-сайт на Flask, используя Raspberry Pi.
