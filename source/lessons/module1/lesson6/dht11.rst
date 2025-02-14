==================================================
Урок 6: Датчик DHT11 (Кастомная реализация)
==================================================

Теоретическая часть
-------------------
Датчик **DHT11** передаёт данные о температуре и влажности в формате 40 бит. Разбивка:

- Первые 8 бит: целая часть влажности
- Следующие 8 бит: десятичная часть влажности
- Следующие 8 бит: целая часть температуры
- Следующие 8 бит: десятичная часть температуры
- Последние 8 бит: контрольная сумма (check bit)

При получении данных мы проверяем правильность с помощью суммы предыдущих 4 байт. Если контрольная сумма совпадает, значит данные корректны.

Необходимые компоненты
----------------------
- Raspberry Pi
- DHT11
- Резистор (обычно ~10 кОм)
- Соединительные провода

Схема подключения
-----------------
.. figure:: images/lesson6.png
   :width: 80%
   :align: center

Запуск кода
-----------
1. Создайте файл `dht11.py` в папке `lessons/lesson6/`:

   .. code-block:: bash

      nano lessons/lesson6/dht11.py

2. Вставьте следующий код и сохраните.
3. Запустите программу:

   .. code-block:: bash

      python3 lessons/lesson6/dht11.py

Код программы
-------------
Файл: `lessons/lesson6/dht11.py`

.. code-block:: python

   from gpiozero import OutputDevice, InputDevice
   import time

   class DHT11:
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
           time.sleep(0.02)  # Задержка ~20 мс

           gpio.close()
           gpio = InputDevice(self._pin, pull_up=self._pull_up)

           # -------------- wait response --------------
           while gpio.value == 1:
               pass

           # -------------- read data --------------
           while bit_count < self.BITS_LEN:
               # Ждём начала импульса
               while gpio.value == 0:
                   pass
               # Считаем, сколько времени вывод находится в HIGH
               while gpio.value == 1:
                   delay_count += 1
                   if delay_count > self.MAX_DELAY_COUINT:
                       break

               # Определяем, бит 1 или 0
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

           _sum = (humidity_integer + humidity_decimal + temperature_integer + temperature_decimal) & 0xFF

           # отладочная информация
           print(bits)
           print(humidity_integer, humidity_decimal, temperature_integer, temperature_decimal)
           print(f'sum:{_sum}, check_sum:{check_sum}')
           print()

           if check_sum != _sum:
               humidity = 0.0
               temperature = 0.0
           else:
               humidity = float(f'{humidity_integer}.{humidity_decimal}')
               temperature = float(f'{temperature_integer}.{temperature_decimal}')

           return humidity, temperature

   if __name__ == '__main__':
       dht11 = DHT11(18)
       while True:
           humidity, temperature = dht11.read_data()
           print(f"{time.time():.3f}  temperature: {temperature}°C  humidity: {humidity}%")
           time.sleep(5)

Разбор кода (Code Explanation)
------------------------------
Функция `read_data(self)` отвечает за инициацию и чтение 40-битного пакета данных от DHT11:

1. **Отправка старта**
   - Создаём объект `OutputDevice(self._pin)`.
   - Устанавливаем LOW (`off()`) на ~20 мс, чтобы сигнализировать датчику о начале чтения.
   - Закрываем `OutputDevice`, переводя пин в режим ввода `InputDevice` с опциональной подтяжкой.

2. **Ожидание отклика**
   - Ждём, пока уровень опустится с HIGH до LOW, означая, что датчик готов отправлять данные.

3. **Чтение данных**
   - Датчик передаёт 40 бит: каждый бит начинается, когда GPIO переходит в HIGH.
   - Время, в течение которого пин находится в HIGH, определяет, бит ли это "0" или "1" (чем дольше HIGH, тем больше вероятность "1").
   - Мы аккумулируем полученные биты в переменную `bits`.

4. **Парсинг результатов**
   - Раскладываем строку `bits` по 5 байтам:
   - Первые 8 бит: целая часть влажности.
   - Следующие 8 бит: десятичная часть влажности.
   - Следующие 8 бит: целая часть температуры.
   - Следующие 8 бит: десятичная часть температуры.
   - Последние 8 бит: контрольная сумма.

5. **Проверка контрольной суммы**
   - Вычисляем `_sum = humidity_integer + humidity_decimal + temperature_integer + temperature_decimal` и берём младший байт (`& 0xFF`).
   - Сравниваем с `check_sum`. Если они совпадают, данные верны.

6. **Возврат значений**
   - Если контрольная сумма не совпала, возвращаются нулевые значения.
   - Если всё корректно, возвращаем влажность (`humidity`) и температуру (`temperature`).

Пояснения по данным
~~~~~~~~~~~~~~~~~~~
- *Первые 16 бит* (Humidity High + Humidity Low) – влажность.
- *Следующие 16 бит* (Temperature High + Temperature Low) – температура.
- *Последние 8 бит* – проверочная сумма.

Если `check_sum != _sum`, значит данные, переданные датчиком, повреждены или считаны неверно. Функция вернёт 0.0/0.0.

Ожидаемый результат
-------------------
При корректном чтении в консоль выводится:

- Сырые двоичные данные, принятые от датчика.
- Разделённые значения влажности и температуры.
- Сравнение суммы и контрольной суммы.
- Итоговые значения влажности и температуры.

.. note::
   Если данные корректны, вы получите реальные показания `temperature` и `humidity`. В противном случае, функция вернёт 0.0/0.0, сигнализируя об ошибке чтения.

Завершение работы
-----------------
Нажмите **Ctrl + C** для остановки программы. Поздравляем! Теперь вы знаете, как вручную инициализировать и считывать данные от датчика DHT11 без сторонних библиотек (например, Adafruit_DHT).
