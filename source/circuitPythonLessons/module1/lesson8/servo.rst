============================================================
Урок 8: Сервопривод
============================================================

.. code-block:: python

    import time
    import board
    import pwmio
    from adafruit_motor import servo

    # Инициализация PWM на GPIO 18
    pwm = pwmio.PWMOut(board.D18, duty_cycle=2 ** 15, frequency=50)

    # Создание объекта сервопривода
    my_servo = servo.Servo(pwm)

    while True:
        print("Поворот на 0°")
        my_servo.angle = 0
        time.sleep(1)
        
        print("Поворот на 90°")
        my_servo.angle = 90
        time.sleep(1)
        
        print("Поворот на 180°")
        my_servo.angle = 180
        time.sleep(1)