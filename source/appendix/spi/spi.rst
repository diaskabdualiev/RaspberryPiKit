.. _spi_configuration:

Настройка SPI
================================

.. note::

   Если вы установили готовый учебный образ набора, все необходимые настройки уже выполнены, и выполнение данных действий не требуется. Данная инструкция предназначена для пользователей, устанавливающих общедоступные образы Raspbian OS, где настройка SPI производится вручную.

Данная инструкция описывает пошаговую настройку интерфейса SPI на Raspberry Pi 5 с использованием утилиты ``raspi-config``. В ней также предусмотрены места для вставки фотографий.

Подготовка системы
------------------

Перед началом настройки убедитесь, что ваша система обновлена:

.. code-block:: bash

   sudo apt update
   sudo apt upgrade

Включение SPI через raspi-config
--------------------------------

1. **Запуск утилиты конфигурации**

   Откройте терминал и выполните команду:

   .. code-block:: bash

      sudo raspi-config

2. **Выбор настроек интерфейсов**

   В главном меню выберите пункт **"Interface Options"** (Настройки интерфейсов).

   .. image:: images/interface_options.png
      :alt: Меню "Interface Options"
      :width: 600px
      :align: center

3. **Активация SPI**

   Найдите пункт **"SPI"** и нажмите Enter. После этого выберите **"Yes"** для подтверждения включения интерфейса SPI.

   .. image:: images/spi_option.webp
      :alt: Опция "SPI" в raspi-config
      :width: 600px
      :align: center

4. **Перезагрузка системы**

   После включения SPI выйдите из утилиты и перезагрузите Raspberry Pi для применения настроек:

   .. code-block:: bash

      sudo reboot

Проверка работы SPI
--------------------

После перезагрузки можно проверить, что интерфейс SPI активирован. Для работы с устройствами через SPI рекомендуется установить библиотеку ``spidev``:

.. code-block:: bash

   sudo apt install -y python3-spidev

Для проверки работы SPI можно воспользоваться тестовым скриптом или обратиться к документации по использованию SPI устройств.

Заключение
----------

После выполнения всех шагов интерфейс SPI будет успешно активирован на вашем Raspberry Pi 5. Если у вас возникнут вопросы или проблемы, обратитесь к официальной документации Raspberry Pi или к сообществу пользователей.
