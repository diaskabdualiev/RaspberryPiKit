============================================================
Урок 17: Камера
============================================================

В этом уроке мы рассмотрим, как управлять камерой Raspberry Pi (через библиотеку **picamera2**) с помощью кнопки и использовать светодиод для индикации. Когда нажимается кнопка, камера делает снимок и сохраняет его в домашней папке пользователя.

Структура проекта
-----------------
.. code-block:: bash

   lessons/
   └── lesson16/
       └── camera_button.py    # Основной скрипт

Полный код
----------
Ниже приведён файл **camera_button.py** целиком.

.. code-block:: python

   #!/usr/bin/env python3
   from picamera2 import Picamera2, Preview
   from gpiozero import LED, Button
   import time
   import os

   # Get the current user's login name and home directory
   user = os.getlogin()
   user_home = os.path.expanduser(f'~{user}')

   # Initialize the camera
   camera = Picamera2()
   camera.start()

   # Initialize a variable to track the camera's status
   global status
   status = False

   # Set up LED and button with their GPIO pin numbers
   led = LED(18)
   button = Button(23)

   def takePhotos(pin):
       """Function to set the camera's status to True when the button is pressed."""
       global status
       status = True

   try:
       # Assign the function to be called when the button is pressed
       button.when_pressed = takePhotos

       # Main loop
       while True:
           # Check if the button has been pressed
           if status:
               # Blink the LED five times
               for i in range(5):
                   led.on()
                   time.sleep(0.1)
                   led.off()
                   time.sleep(0.1)
               # Capture and save a photo
               camera.capture_file(f'{user_home}/my_photo.jpg')
               print('Take a photo!')
               # Reset the status
               status = False
           else:
               # Turn off the LED if not capturing
               led.off()

           # Wait for a short period before checking the button status again
           time.sleep(1)

   except KeyboardInterrupt:
       # Stop the camera and turn off the LED if a KeyboardInterrupt occurs
       camera.stop_preview()
       led.off()
       pass

Код программы
-------------
Давайте разберём скрипт по шагам.

.. code-block:: python

   from picamera2 import Picamera2, Preview
   from gpiozero import LED, Button
   import time
   import os

1. **picamera2** – библиотека для управления камерой на Raspberry Pi.
2. **gpiozero** – упрощает работу с GPIO (кнопкой, светодиодом).
3. **time**, **os** – стандартные модули Python для таймеров и операций с ОС.

.. code-block:: python

   user = os.getlogin()
   user_home = os.path.expanduser(f'~{user}')

- Получаем имя пользователя (логин) и путь к его домашней папке.
- В дальнейшем сохраняем снимок в файл `my_photo.jpg`, лежащий в директории `user_home`.

.. code-block:: python

   camera = Picamera2()
   camera.start()

- Создаём объект **Picamera2** и сразу его запускаем.

.. code-block:: python

   global status
   status = False

- Переменная `status` нужна, чтобы понять, была ли нажата кнопка.
- Когда она `True`, программа должна сделать снимок.

.. code-block:: python

   led = LED(18)
   button = Button(23)

- Инициализируем **LED(18)** и **Button(23)** (GPIO18 – для светодиода, GPIO23 – для кнопки).

.. code-block:: python

   def takePhotos(pin):
       global status
       status = True

- Функция **takePhotos** срабатывает при нажатии кнопки.
- Устанавливаем `status = True`, чтобы основной цикл сделал снимок.

.. code-block:: python

   button.when_pressed = takePhotos

- Связываем событие **when_pressed** кнопки с функцией **takePhotos**.

.. code-block:: python

   while True:
       if status:
           # Blink LED and take a photo
           # Reset status
       else:
           led.off()
       time.sleep(1)

- Основной цикл: если `status == True`, мигаем светодиодом 5 раз и делаем снимок.
- Потом `status` сбрасывается в `False`.
- Если `status == False`, просто выключаем светодиод.
- Спим 1 секунду, затем снова проверяем состояние.

.. code-block:: python

   camera.capture_file(f'{user_home}/my_photo.jpg')
   print('Take a photo!')

- Делаем снимок и выводим сообщение в консоль.
- Файл сохраняется в домашнюю директорию пользователя, как `my_photo.jpg`.

.. code-block:: python

   except KeyboardInterrupt:
       camera.stop_preview()
       led.off()

- При нажатии Ctrl+C или другом прерывании, останавливаем предпросмотр камеры и выключаем светодиод.

Запуск
------
1. Убедитесь, что камера Raspberry Pi корректно подключена и включена в настройках.
2. Установите библиотеку **picamera2** (если не установлена):

   .. code-block:: bash

      pip3 install picamera2

3. Запустите скрипт:

   .. code-block:: bash

      python3 camera_button.py

4. Нажмите кнопку на GPIO23, чтобы сделать снимок.

Ожидаемый результат
-------------------
- При каждом нажатии кнопки светодиод моргнёт 5 раз, а затем будет сделан снимок.
- Файл `my_photo.jpg` появится в домашней папке текущего пользователя.

Завершение работы
-----------------
Нажмите **Ctrl + C** в терминале, чтобы остановить программу. Поздравляем! Теперь вы умеете считывать нажатие кнопки, мигать светодиодом и управлять камерой с помощью **picamera2**.