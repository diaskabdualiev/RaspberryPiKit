============================================================
Урок 9: Реле
============================================================

import time
import board
import digitalio

# Инициализация пина GPIO17 как выход
relay = digitalio.DigitalInOut(board.D18)
relay.direction = digitalio.Direction.OUTPUT

while True:
    print("Реле ВКЛ")
    relay.value = False  # активное низкое (LOW)
    time.sleep(2)
    
    print("Реле ВЫКЛ")
    relay.value = True   # неактивное (HIGH)
    time.sleep(2)