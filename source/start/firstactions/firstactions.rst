Первые действия для запуска
============================

**Сначала вытаскиваем Raspberry Pi из коробки**

.. figure:: images/raspberry.jpeg
   :width: 80%
   :align: center

   Рис. 1: Raspberry Pi в комплекте

**Устанавливаем SD карту с уже предустановленным образом в Raspberry**

.. figure:: images/raspberry-install-sd-card.jpeg
   :width: 80%
   :align: center

   Рис. 2: Установка microSD карты

**Берем коробку с кулером**

.. figure:: images/cooler-box.jpeg
   :width: 80%
   :align: center

   Рис. 3: Коробка с кулером

Вытаскиваем кулер
------------------

.. figure:: images/cooler-without-box.jpeg
   :width: 80%
   :align: center

   Рис. 4: Извлечение кулера

Переворачиваем
--------------

.. figure:: images/cooler-artynan.jpeg
   :width: 80%
   :align: center

   Рис. 5: Переворачиваем кулер

Убираем плёнку с термопрокладки
-------------------------------

.. figure:: images/cooler-bez-plenky.jpeg
   :width: 80%
   :align: center

   Рис. 6: Снятие защитной плёнки

Ставим на Raspberry
--------------------

.. figure:: images/cooler-install-raspberry-2.jpeg
   :width: 80%
   :align: center

   Рис. 7: Установка кулера на Raspberry Pi

Зажимаем до характерного щелчка в указанных местах
---------------------------------------------------

.. figure:: images/cooler-install-raspberry.jpeg
   :width: 80%
   :align: center

   Рис. 8: Фиксация кулера

С обратной стороны убеждаемся, что всё защёлкнуто
--------------------------------------------------

.. figure:: images/cooler-install-raspberry-3.jpeg
   :width: 80%
   :align: center

   Рис. 9: Проверка фиксации

Вставляем штекер кулера
------------------------

.. figure:: images/cooler-connector-install.jpeg
   :width: 80%
   :align: center

   Рис. 10: Подключение вентилятора

Штекер должен быть защёлкнут до конца
-------------------------------------

.. figure:: images/cooler-connector-install-2.jpeg
   :width: 80%
   :align: center

   Рис. 11: Штекер установлен

Берем основу
------------

.. figure:: images/main-body.jpeg
   :width: 80%
   :align: center

   Рис. 12: Основание

Снимаем скотч и вставляем в пазы
---------------------------------

.. figure:: images/main-install-breadboard.jpeg
   :width: 80%
   :align: center

   Рис. 13: Монтаж основания

Вставляем Raspberry на своё место
----------------------------------

.. figure:: images/main-install-raspberry.jpeg
   :width: 80%
   :align: center

   Рис. 14: Установка Raspberry в корпус

Прикручиваем винтами M2.5
--------------------------

.. figure:: images/main-install-raspberry-2-up.jpeg
   :width: 80%
   :align: center

   Рис. 15: Места крепления

В итоге должно получиться как на фото
--------------------------------------

.. figure:: images/main-install-raspberry-3-up.jpeg
   :width: 80%
   :align: center

   Рис. 16: Готовая сборка

Вставляем HDMI-MicroHDMI кабель в Raspberry
-------------------------------------------

.. figure:: images/main-raspberry-install-hdmi.jpeg
   :width: 80%
   :align: center

   Рис. 17: Подключение HDMI к Raspberry Pi

Один конец кабеля вставляем в разъём micro-HDMI на Raspberry Pi, другой — в монитор.

Вставляем кабель питания в разъём
----------------------------------

.. figure:: images/main-raspberry-install-typec.jpeg
   :width: 80%
   :align: center

   Рис. 18: Подключение блока питания

Используем блок питания USB-C, и подключаем его к соответствующему разъёму на Raspberry Pi.

Подключаем клавиатуру с тачпадом
---------------------------------

.. figure:: images/keyboard.jpeg
   :width: 80%
   :align: center

   Рис. 19: Клавиатура в комплекте

Вставляем USB свисток
----------------------

.. figure:: images/main-raspberry-keyboard-usb.jpeg
   :width: 80%
   :align: center

   Рис. 20: USB приёмник клавиатуры


Дальнейшая настройка
------------------------------------------------------------------------------------------------

После загрузки системы можно настроить удаленный доступ к Raspberry Pi:

- **VNC** — графический удаленный доступ к рабочему столу.
- **SSH** — подключение к терминалу Raspberry Pi через сеть.

Эти настройки выполняются после завершения первоначальной конфигурации системы.

.. note::

   Подключение через **SSH** по умолчанию может быть **отключено**. Чтобы его активировать,
   необходимо создать **пустой файл** с названием ``ssh`` (без расширения) в корневой директории
   карты памяти **перед первой загрузкой**.

