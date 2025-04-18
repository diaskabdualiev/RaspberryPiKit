VNC-подключение
=======================

.. figure:: images/vnc/second.png
   :width: 80%
   :align: center

VNC (Virtual Network Computing) позволяет получить удаленный доступ к графическому рабочему столу Raspberry Pi с другого компьютера по сети. Это очень удобно, когда вы хотите работать с Raspberry Pi без необходимости подключать отдельный монитор, клавиатуру и мышь.

Преимущества VNC-подключения:
-----------------------------

- Доступ к полноценному рабочему столу Raspberry Pi с любого устройства
- Возможность работать с Raspberry Pi удаленно по сети
- Удобный интерфейс для копирования файлов между устройствами
- Не требуется дополнительный монитор и клавиатура для Raspberry Pi

Настройка VNC-подключения
-------------------------

На Raspberry Pi VNC-сервер уже активирован. Для подключения к нему вам необходимо установить VNC Viewer на ваш компьютер:

1. Скачайте и установите RealVNC Viewer с официального сайта
2. Запустите программу и введите IP-адрес вашего Raspberry Pi
3. Введите учетные данные для входа (логин: ``dias``, пароль: ``dias``)

Подробные инструкции по настройке и использованию VNC можно найти в разделе :doc:`/appendix/vnc/vnc`.

Запуск первого кода через VNC
-----------------------------

После успешного подключения через VNC вы получите доступ к рабочему столу Raspberry Pi. Теперь вы можете запустить VSCode и ваш первый проект точно так же, как если бы вы работали непосредственно на устройстве:

1. В окне VNC Viewer найдите и откройте VSCode через меню приложений
2. VSCode автоматически откроет папку с уроками
3. Перейдите к первому уроку в `lessons/module1/lesson1/`
4. Откройте файл `led.py`
5. Запустите код, нажав кнопку "Run" в правом верхнем углу

.. figure:: images/vnc/vnc.gif
   :width: 80%
   :align: center
   
   **Рис. 2:** Демонстрация запуска VSCode и первого примера кода через VNC

Вы увидите, как светодиод, подключенный к GPIO18, начнет мигать с интервалом в 1 секунду, хотя вы управляете Raspberry Pi с другого компьютера. Это демонстрирует гибкость работы с Raspberry Pi через удаленное подключение.

Примечание: При первом запуске кода через VNC может потребоваться немного больше времени из-за сетевой передачи данных. Это нормально и зависит от скорости вашей сети.