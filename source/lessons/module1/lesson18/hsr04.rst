==========================================================
Урок 7: Ультразвуковой радар 📡
==========================================================

Теоретическая часть
-------------------
Ультразвуковой датчик **HC-SR04** измеряет расстояние до объекта при помощи звуковых волн на частоте около 40 кГц. Датчик выдает два сигнала:
- **TRIG**: генерируем короткий импульс для отправки "ультразвукового пакета".
- **ECHO**: принимает отражённый сигнал, измеряя время между отправкой и приёмом.

Зная скорость звука (~343 м/с) и время полёта, можно вычислить расстояние:

.. .. math::
..    \text{Distance} = \frac{(\text{Time} * 34300)}{2} \text{ (см)}

В данном уроке мы дополним схему **активным зуммером**, который будет подавать звуковые сигналы в зависимости от дистанции. Такой принцип лежит в основе "парктроников".

Необходимые компоненты
----------------------
- Raspberry Pi
- HC-SR04 (ультразвуковой дальномер)
- Активный зуммер
- Макетная плата (breadboard)
- Соединительные провода

Схема подключения
-----------------
.. figure:: images/lesson7.png
   :width: 80%
   :align: center

Запуск кода
-----------
1. Создайте файл `hcsr04.py` в папке `lessons/lesson7/`:

   .. code-block:: bash

      nano lessons/lesson7/hcsr04.py

2. Скопируйте следующий код.
3. Запустите программу:

   .. code-block:: bash

      python3 lessons/lesson7/hcsr04.py

Код программы
-------------
Файл: `lessons/lesson7/hcsr04.py`

.. code-block:: python

   from gpiozero import DistanceSensor, Buzzer
   from time import sleep

   # Пины (BCM)
   TRIG = 23
   ECHO = 24
   BUZZER = 18

   # Инициализация датчика расстояния и буззера
   sensor = DistanceSensor(echo=ECHO, trigger=TRIG, max_distance=2.0)  # макс. дистанция ~2 м
   buzzer = Buzzer(BUZZER)

   def beep(duration_on, duration_off):
       """ Подать прерывистый сигнал буззера """
       buzzer.on()
       sleep(duration_on)
       buzzer.off()
       sleep(duration_off)

   try:
       print("Запуск парктроника (нажмите Ctrl+C для выхода)...")
       while True:
           dist = sensor.distance * 100  # Преобразуем метры -> сантиметры
           print(f"Текущее расстояние = {dist:.1f} см")

           if dist <= 5:
               # Почти непрерывный сигнал
               beep(0.1, 0.05)

           elif dist <= 10:
               # Быстрые сигналы
               beep(0.1, 0.1)

           elif dist <= 20:
               # Средние сигналы
               beep(0.2, 0.3)

           elif dist <= 30:
               # Медленные сигналы
               beep(0.3, 0.5)

           else:
               # Далеко — тишина
               buzzer.off()
               sleep(1)

   except KeyboardInterrupt:
       print("\nОстановка программы пользователем.")
       buzzer.off()
       print("Завершено.")

Разбор кода
-----------
- `DistanceSensor(echo=ECHO, trigger=TRIG, max_distance=2.0)` – объект датчика расстояния. Параметр `max_distance` задаёт максимальную дистанцию (в метрах) для калибровки.
- `buzzer = Buzzer(BUZZER)` – инициализация активного зуммера.
- `beep(duration_on, duration_off)` – функция для прерывистого сигнала.
  - `buzzer.on() / buzzer.off()` – включение и выключение зуммера.
  - `sleep(...)` – задержка между сигналами.
- `dist = sensor.distance * 100` – чтение дистанции в метрах, умножаем на 100 для перевода в сантиметры.
- В зависимости от `dist` варьируется интервал между сигналами зуммера.

Ожидаемый результат
-------------------
1. Если объект находится ближе 5 см, сигнал почти непрерывный.
2. 5–10 см – быстрые сигналы.
3. 10–20 см – средняя частота сигналов.
4. 20–30 см – медленные сигналы.
5. >30 см – зуммер не подаёт сигнал.

.. .. figure:: images/hcsr04_buzzer.gif
..    :width: 50%
..    :align: center

   **Рис. 2:** Пример "парктроника" с ультразвуковым датчиком

Завершение работы
-----------------
Нажмите **Ctrl + C** в терминале, чтобы остановить программу. Теперь вы умеете создавать простейшую систему "парктроника" или "дальномера", используя HC-SR04 и зуммер.
