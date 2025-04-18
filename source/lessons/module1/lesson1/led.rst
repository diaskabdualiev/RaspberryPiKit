======================================================
Урок 1: Моргание светодиодом ✨
======================================================

Теоретическая часть
--------------------
GPIO (General Purpose Input/Output) – это универсальные цифровые входы и выходы на плате Raspberry Pi, которые позволяют взаимодействовать с различными электронными компонентами, такими как светодиоды, кнопки, реле и датчики.

В данном уроке мы будем управлять светодиодом, подключенным к Raspberry Pi, заставляя его моргать с интервалом в 1 секунду.

Необходимые компоненты
----------------------
- Raspberry Pi
- Светодиод (LED)
- Резистор 330 Ом
- Макетная плата (breadboard)
- Соединительные провода

Схема подключения
-----------------
.. figure:: images/lesson1.png
   :width: 80%
   :align: center

   **Рис. 1:** Схема подключения светодиода

Запуск кода
------------
1. Откройте **Thonny** на Raspberry Pi.
2. Создайте новый файл **blink.py** в папке `lessons/lesson1/`.
3. Вставьте в файл следующий код:

Код программы
-------------
Файл: `lessons/lesson1/blink.py`

.. code-block:: python

   from gpiozero import LED  # Импортируем класс LED из библиотеки gpiozero
   from time import sleep  # Импортируем sleep для задержек

   led = LED(18)  # Определяем светодиод, подключенный к GPIO18

   while True:  # Бесконечный цикл для мигания светодиода
      led.on()  # Включаем светодиод
      print("LED on")
      sleep(1)  # Ждём 1 секунду
      led.off()  # Выключаем светодиод
      print("LED off")
      sleep(1)  # Ждём 1 секунду

Разбор кода
------------
- `from gpiozero import LED` – импортируем класс LED для управления светодиодом.
- `from time import sleep` – импортируем функцию `sleep` для задержек.
- `led = LED(18)` – указываем, что светодиод подключён к GPIO 18.
- `led.on()` – включает светодиод, подавая на него 3.3В.
- `led.off()` – выключает светодиод.
- `sleep(1)` – задержка в 1 секунду между включением и выключением.
- `while True:` – бесконечный цикл для мигания светодиода.

Ожидаемый результат
-------------------
При запуске программы светодиод будет включаться и выключаться каждую секунду, создавая эффект мигания.

   **Рис. 2:** Ожидаемый результат работы кода

Завершение работы
-----------------
Для остановки программы нажмите **Ctrl + C** в терминале.

Поздравляем! 🎉 Вы успешно заставили светодиод мигать с помощью Raspberry Pi! В следующих уроках мы рассмотрим более сложные схемы и управляемые устройства.
