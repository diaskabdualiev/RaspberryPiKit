Урок 18: NFC модуль MFRC522
==================================

.. code-block:: python

    import RPi.GPIO as GPIO
    from mfrc522 import SimpleMFRC522
    import time

    # Инициализация
    reader = SimpleMFRC522()

    try:
        while True:
            print("Поднесите карту к считывателю...")
            
            # Считывание ID карты и данных
            id, text = reader.read()
            
            print("ID карты: {}".format(id))
            print("Данные на карте: {}".format(text))
            
            # Задержка между считываниями
            time.sleep(2)
            
    except KeyboardInterrupt:
        # Выход по Ctrl+C
        print("Программа остановлена")
        
    finally:
        # Очистка GPIO
        GPIO.cleanup()