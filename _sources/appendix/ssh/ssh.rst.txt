Настройка SSH (Командный доступ)
================================

SSH позволяет управлять Raspberry Pi через командную строку.

.. note::
   Если устройства находятся в разных сетях, подключение может не работать.

Шаг 1: Включение SSH
---------------------

1. Откройте терминал и введите:

   .. code-block:: bash

      sudo raspi-config

2. Перейдите в **Interface Options > SSH** и выберите **Enable**.

Шаг 2: Подключение к Raspberry Pi через SSH
--------------------------------------------

1. На Windows установите **PuTTY**, на Linux/macOS используйте терминал.

   .. image:: https://raw.githubusercontent.com/diaskabdualiev/RaspberryPi-Kit/main/vnc_ssh_ftp/putty.gif
      :alt: Установка SSH
      :align: center

2. Запустите PuTTY и введите IP-адрес Raspberry Pi.

   .. image:: https://raw.githubusercontent.com/diaskabdualiev/RaspberryPi-Kit/main/vnc_ssh_ftp/puttyssh.gif
      :alt: Соединение по SSH
      :align: center

3. Введите пароль.

Скачать PuTTY:  
`Официальный сайт PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_
