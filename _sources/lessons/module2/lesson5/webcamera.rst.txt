====================================================
Урок 18: Онлайн-видеопоток с PiCamera2 через Flask
====================================================

В этом уроке мы научимся транслировать изображение с камеры Raspberry Pi в реальном времени на веб-страницу. Используем библиотеку **picamera2** для захвата кадров и **Flask** для организации веб-приложения.

Структура проекта
-----------------
.. code-block:: bash

   lessons/
   └── lesson18/
       ├── app.py          # Flask-приложение для видеопотока
       └── templates/
           └── index.html  # HTML-файл для отображения видеопотока

Полный код
----------
Ниже приведены файлы **app.py** и **index.html** целиком.

.. code-block:: python

   from flask import Flask, Response, render_template
   from picamera2 import Picamera2
   import cv2
   import io

   app = Flask(__name__)

   # Инициализация камеры
   camera = Picamera2()
   camera.configure(camera.create_video_configuration(main={"size": (640, 480)}))
   camera.start()

   def generate():
       while True:
           # Захватываем текущий кадр в формат numpy-массива
           frame = camera.capture_array()
           # Кодируем кадр в формат JPG (для веб-потока)
           _, buffer = cv2.imencode(".jpg", frame)
           frame_bytes = buffer.tobytes()

           # Отправляем кадр как часть потока
           yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

   @app.route("/")
   def index():
       return render_template("index.html")

   @app.route("/video_feed")
   def video_feed():
       # Возвращаем HTTP-ответ с типом multipart/x-mixed-replace
       return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000, debug=False)

.. code-block:: html

   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <meta charset="UTF-8">
       <title>Видеопоток с Raspberry Pi</title>
       <style>
           body {
               text-align: center;
               background: #f4f4f4;
               font-family: Arial, sans-serif;
           }
           .container {
               margin-top: 20px;
               background: white;
               padding: 15px;
               border-radius: 10px;
               box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
               display: inline-block;
           }
           h1 {
               color: #333;
           }
           img {
               border-radius: 10px;
               max-width: 100%;
               height: auto;
           }
       </style>
   </head>
   <body>
       <div class="container">
           <h1>Видеопоток с Raspberry Pi</h1>
           <img src="{{ url_for('video_feed') }}" alt="Видео с камеры">
       </div>
   </body>
   </html>

Разбор кода (app.py)
---------------------
Теперь рассмотрим код приложения подробнее.

.. code-block:: python

   from flask import Flask, Response, render_template
   from picamera2 import Picamera2
   import cv2

- **Flask** для создания веб-сервера.
- **Response** для возврата потоковых данных (multipart/x-mixed-replace).
- **render_template** для рендера HTML-файлов.
- **picamera2** для работы с новой камерой на Raspberry Pi.
- **cv2** (OpenCV) для кодирования кадров в JPG.

.. code-block:: python

   camera = Picamera2()
   camera.configure(camera.create_video_configuration(main={"size": (640, 480)}))
   camera.start()

- Инициализируем камеру, указываем разрешение 640×480.
- Вызываем **start()**, чтобы начать передачу.

.. code-block:: python

   def generate():
       while True:
           frame = camera.capture_array()
           _, buffer = cv2.imencode(".jpg", frame)
           frame_bytes = buffer.tobytes()

           yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

- Функция **generate()** — генератор, захватывающий кадры с камеры и кодирующий их в JPG.
- **yield** отправляет часть HTTP-ответа для технологии "multipart/x-mixed-replace".

.. code-block:: python

   @app.route("/")
   def index():
       return render_template("index.html")

- Корневой маршрут. Возвращаем шаблон `index.html`, где описан интерфейс.

.. code-block:: python

   @app.route("/video_feed")
   def video_feed():
       return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")

- Маршрут для видео потока.
- `Response(generate(), mimetype=...)` позволяет вернуть бесконечный поток JPEG-кадров.

.. code-block:: python

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000, debug=False)

- Запускаем Flask-сервер на порту 5000, доступном со всех интерфейсов.

HTML-файл (index.html)
----------------------

.. code-block:: html

   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <!-- ... -->
   </head>
   <body>
       <div class="container">
           <h1>Видеопоток с Raspberry Pi</h1>
           <img src="{{ url_for('video_feed') }}" alt="Видео с камеры">
       </div>
   </body>
   </html>

- Здесь мы отображаем изображение, загружая поток с адреса **/video_feed**.
- Каждое обновление кадра происходит автоматически, не требуя перезагрузки страницы.

Запуск
------
1. Создайте папку `lesson18`, положите `app.py` и шаблон `index.html`.
2. Установите зависимости (если нужно):

   .. code-block:: bash

      pip3 install picamera2 flask opencv-python

3. Запустите приложение:

   .. code-block:: bash

      python3 lessons/lesson18/app.py

4. Откройте в браузере http://<RaspberryPi_IP>:5000

Ожидаемый результат
-------------------
На веб-странице в реальном времени будет отображаться поток с камеры Raspberry Pi.

.. .. figure:: images/picamera2_flask_stream.png
..    :width: 50%
..    :align: center

   **Рис. 2:** Пример видео-трансляции

Завершение работы
-----------------
Нажмите **Ctrl + C** в терминале, чтобы остановить сервер и завершить работу. Теперь вы умеете раздавать видеопоток с Raspberry Pi в браузер, используя Flask и Picamera2.
