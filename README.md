# Raspberry Pi Wiki Platform

Это образ для Raspberry Pi 5, предназначенный для Wiki платформы по изучению Raspberry Pi. Файл содержит инструкции по настройке окружения и установке необходимого программного обеспечения.

Доменное имя pialash.local
Логин alash
пороль alash

Wifi ssid AlashElectronics
wifi password 28071917

Обои находиться по пути
data/Alash Raspberry Pi Kit.png

sudo apt update
sudo apt upgrade

для создания venv
sudo apt install python3-venv python3-full

создание вирутального окружения и его запуск
python3 -m venv venv
source venv/bin/activate
pip install adafruit-blinka

нужно установить зависмости так как в raspberry pi5  другой подход работы с пинами
sudo apt install -y liblgpio-dev
pip install lgpio

до 5 урока этого хватает но для 6 урока dht нужно установить pip модуль для работы с dht
pip install adafruit-circuitpython-dht

для 7 урока где используется ультравзуковой датчик нужно установить
pip install adafruit-circuitpython-hcsr04

для работы с сервоприоводом напрямую нужно установить
pip install adafruit-circuitpython-servokit

для 10 урока 
pip install adafruit-circuitpython-matrixkeypad

для 11 урока 
pip install adafruit-circuitpython-rotaryio

для 12 урока
pip install adafruit-circuitpython-max7219

для 13 урока
pip install adafruit-circuitpython-ads1x15

для 15 урока 
pip install adafruit-circuitpython-mpu6050

для 16 урока
pip install adafruit-circuitpython-pca9685

17 урок для работы с lcd1602
pip install RPLCD
pip install adafruit-circuitpython-charlcd

18 урок для работы с pn532
pip3 install adafruit-circuitpython-pn532