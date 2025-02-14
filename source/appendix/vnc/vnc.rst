Настройка VNC (Удаленный рабочий стол)
======================================

VNC позволяет удаленно управлять графическим интерфейсом Raspberry Pi.

.. note::
   Если устройства находятся в разных сетях, подключение может не работать.

Шаг 1: Установка VNC-сервера
-----------------------------

1. Откройте терминал на Raspberry Pi.
2. Введите команду:

   .. code-block:: bash

      sudo apt update && sudo apt install realvnc-vnc-server realvnc-vnc-viewer -y

3. Включите VNC в меню настроек Raspberry Pi:

   .. code-block:: bash

      sudo raspi-config

   - Перейдите в **Interface Options > VNC**
   - Выберите **Enable**

Шаг 2: Подключение к VNC
-------------------------

1. Установите VNC Viewer на компьютер.

   .. image:: https://raw.githubusercontent.com/diaskabdualiev/RaspberryPi-Kit/main/vnc_ssh_ftp/video1.gif
      :alt: Установка VNC Viewer
      :align: center

2. Запустите VNC Viewer и введите IP-адрес Raspberry Pi.

   .. image:: https://raw.githubusercontent.com/diaskabdualiev/RaspberryPi-Kit/main/vnc_ssh_ftp/vnc_raspi.gif
      :alt: Настройка VNC
      :align: center

3. Введите учетные данные:

   - Логин: ``dias``
   - Пароль: ``dias``

Скачать VNC Viewer:  
`RealVNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_
