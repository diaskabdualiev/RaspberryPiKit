====================================================
Урок 4: Мониторинг DHT11 через Flask
====================================================

В данном уроке мы создадим Flask-приложение, которое будет считывать данные с датчика **DHT11** (температуру и влажность) и отображать их в реальном времени на веб-странице. Библиотека **gpiozero** тут не используется для датчика, поэтому для чтения данных мы реализуем собственный код через `OutputDevice` и `InputDevice`.

Структура проекта
-----------------
.. code-block:: bash

   lessons/
   └── lesson17/
       ├── app.py          # Flask-приложение
       └── templates/
           └── index.html  # HTML-файл для интерфейса

Полный код
----------
Ниже приведены файлы **app.py** и **index.html** целиком.

.. code-block:: python

   from flask import Flask, render_template, jsonify
   import time
   from gpiozero import OutputDevice, InputDevice

   app = Flask(__name__)

   class DHT11():
       MAX_DELAY_COUINT = 100
       BIT_1_DELAY_COUNT = 10
       BITS_LEN = 40

       def __init__(self, pin, pull_up=False):
           self._pin = pin
           self._pull_up = pull_up

       def read_data(self):
           bit_count = 0
           delay_count = 0
           bits = ""

           # -------------- send start --------------
           gpio = OutputDevice(self._pin)
           gpio.off()
           time.sleep(0.02)

           gpio.close()
           gpio = InputDevice(self._pin, pull_up=self._pull_up)

           # -------------- wait response --------------
           while gpio.value == 1:
               pass

           # -------------- read data --------------
           while bit_count < self.BITS_LEN:
               while gpio.value == 0:
                   pass

               while gpio.value == 1:
                   delay_count += 1
                   if delay_count > self.MAX_DELAY_COUINT:
                       break

               if delay_count > self.BIT_1_DELAY_COUNT:
                   bits += "1"
               else:
                   bits += "0"

               delay_count = 0
               bit_count += 1

           # -------------- verify --------------
           humidity_integer = int(bits[0:8], 2)
           humidity_decimal = int(bits[8:16], 2)
           temperature_integer = int(bits[16:24], 2)
           temperature_decimal = int(bits[24:32], 2)
           check_sum = int(bits[32:40], 2)

           _sum = humidity_integer + humidity_decimal + temperature_integer + temperature_decimal

           if check_sum != _sum:
               humidity = 0.0
               temperature = 0.0
           else:
               humidity = float(f'{humidity_integer}.{humidity_decimal}')
               temperature = float(f'{temperature_integer}.{temperature_decimal}')

           return humidity, temperature

   # Инициализируем датчик
   dht11 = DHT11(18)

   @app.route("/")
   def home():
       return render_template("index.html")

   @app.route("/data")
   def get_sensor_data():
       humidity, temperature = dht11.read_data()
       return jsonify({"temperature": temperature, "humidity": humidity})

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)

.. code-block:: html

   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Мониторинг Температуры и Влажности</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               background: linear-gradient(to right, #2980b9, #6dd5fa, #ffffff);
               text-align: center;
               padding: 20px;
           }
           .container {
               background: rgba(255, 255, 255, 0.9);
               padding: 20px;
               border-radius: 15px;
               box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
               display: inline-block;
               min-width: 300px;
           }
           h1 {
               color: #333;
           }
           .sensor-data {
               font-size: 24px;
               font-weight: bold;
               color: #27ae60;
               margin: 10px 0;
           }
           .refresh {
               margin-top: 20px;
               padding: 10px 20px;
               font-size: 16px;
               border: none;
               background: #3498db;
               color: white;
               cursor: pointer;
               border-radius: 5px;
               transition: 0.3s;
           }
           .refresh:hover {
               background: #2980b9;
           }
       </style>
       <script>
           function updateData() {
               fetch('/data')
               .then(response => response.json())
               .then(data => {
                   document.getElementById("temperature").innerText = data.temperature + "°C";
                   document.getElementById("humidity").innerText = data.humidity + "%";
               });
           }
           setInterval(updateData, 5000); // Автообновление каждые 5 секунд
           window.onload = updateData;
       </script>
   </head>
   <body>
       <div class="container">
           <h1>Мониторинг DHT11</h1>
           <p>Температура: <span class="sensor-data" id="temperature">--</span></p>
           <p>Влажность: <span class="sensor-data" id="humidity">--</span></p>
           <button class="refresh" onclick="updateData()">Обновить сейчас</button>
       </div>
   </body>
   </html>

Разбор кода (app.py)
---------------------
Ниже разделим Python-код на части для лучшего понимания.

.. code-block:: python

   from flask import Flask, render_template, jsonify
   import time
   from gpiozero import OutputDevice, InputDevice

- **Flask** для веб-сервера;
- **render_template** для рендеринга HTML;
- **jsonify** для отправки JSON-ответов;
- **OutputDevice** и **InputDevice** для низкоуровневого управления GPIO.

.. code-block:: python

   class DHT11():
       MAX_DELAY_COUINT = 100
       BIT_1_DELAY_COUNT = 10
       BITS_LEN = 40

       def __init__(self, pin, pull_up=False):
           self._pin = pin
           self._pull_up = pull_up

       def read_data(self):
           # ...

- Объявляем класс DHT11, в котором:
  - **MAX_DELAY_COUINT** – порог задержки,
  - **BIT_1_DELAY_COUNT** – число тактов, при котором считается бит = 1,
  - **BITS_LEN** = 40, так как DHT11 передаёт 5 байтов (температура, влажность и контрольная сумма).

.. code-block:: python

   # ... внутри read_data()

   gpio = OutputDevice(self._pin)
   gpio.off()
   time.sleep(0.02)  # Стартовый импульс ~20 мс

   gpio.close()
   gpio = InputDevice(self._pin, pull_up=self._pull_up)

- Сначала выставляем пин в режим **OutputDevice**, подаём LOW ~20 мс, чтобы сигнализировать датчику DHT11 о начале чтения.
- Затем закрываем **OutputDevice**, переключаемся в **InputDevice** (режим чтения). Если **pull_up=True**, то вход будет подтянут к VCC.

.. code-block:: python

   while gpio.value == 1:
       pass

   # Пока DHT11 не отдаст стартовый сигнал (GPIO=0), ждём.

.. code-block:: python

   # Считывание 40 бит
   while bit_count < self.BITS_LEN:
       # ...
       if delay_count > self.BIT_1_DELAY_COUNT:
           bits += "1"
       else:
           bits += "0"

- Каждый бит определяется длительностью сигнала HIGH.

.. code-block:: python

   humidity_integer = int(bits[0:8], 2)
   # ...
   check_sum = int(bits[32:40], 2)
   _sum = humidity_integer + humidity_decimal + temperature_integer + temperature_decimal

- Разбираем строку bits на 5 байтов.
- Если контрольная сумма совпадает, переводим в float (например, "25.0" для 25.0 °C).

Разбор HTML (index.html)
-------------------------

.. code-block:: html

   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <!-- ... -->
       <script>
           function updateData() {
               fetch('/data')
               .then(response => response.json())
               .then(data => {
                   document.getElementById("temperature").innerText = data.temperature + "°C";
                   document.getElementById("humidity").innerText = data.humidity + "%";
               });
           }
           setInterval(updateData, 5000);
           window.onload = updateData;
       </script>
   </head>
   <body>
       <!-- ... -->
       <button onclick="updateData()">Обновить сейчас</button>
   </body>
   </html>

- При загрузке страницы выполняется **window.onload = updateData**, чтобы сразу получить данные.
- Далее **setInterval(updateData, 5000)** автоматически обновляет данные каждые 5 секунд.
- **fetch('/data')** делает запрос к маршруту Flask, который возвращает JSON с температурой и влажностью.
- JS-код обновляет текстовые поля в документе.

Запуск
------
1. Создайте папку `lesson17`, поместите `app.py` и папку `templates/index.html`.
2. Убедитесь, что Flask установлен (`pip3 install flask`).
3. Запустите приложение:

   .. code-block:: bash

      python3 lessons/lesson17/app.py

4. Перейдите в браузере на http://<RaspberryPi_IP>:5000

Ожидаемый результат
-------------------
На странице будет отображаться текущая температура и влажность (обновляется каждые 5 секунд). При нажатии кнопки «Обновить сейчас» данные берутся немедленно.

.. figure:: images/dht11_flask_example.png
   :width: 50%
   :align: center

   **Рис. 2:** Пример интерфейса с DHT11

Завершение работы
-----------------
Нажмите **Ctrl + C** в терминале, чтобы остановить сервер. Теперь вы можете мониторить показания DHT11 через веб-интерфейс Flask!
