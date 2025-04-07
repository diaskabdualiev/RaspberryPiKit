# Raspberry Pi Wiki Platform

Это образ для Raspberry Pi 5, предназначенный для Wiki платформы по изучению Raspberry Pi. Файл содержит инструкции по настройке окружения и установке необходимого программного обеспечения.

## Содержание
1. [Первоначальная настройка](#первоначальная-настройка)
2. [Установка Pi Apps](#установка-pi-apps)
3. [Установка VSCode](#установка-vscode)
4. [Загрузка учебных материалов](#загрузка-учебных-материалов)
5. [Отключение служб безопасности](#дополнительные-настройки)

## Первоначальная настройка

### Установка обоев Wiki платформы

```bash
# Создаем директорию для обоев, если она не существует
mkdir -p /home/pi/Pictures/Wallpapers

# Загружаем фоновое изображение
wget -O /home/pi/Pictures/Wallpapers/raspberry-pi-wiki-wallpaper.jpg https://[URL_к_обоям]

# Устанавливаем обои как изображение рабочего стола
pcmanfm --set-wallpaper=/home/pi/Pictures/Wallpapers/raspberry-pi-wiki-wallpaper.jpg
```

## Установка Pi Apps

Pi Apps - это магазин приложений для Raspberry Pi, который упрощает установку различных программ.

```bash
# Установка Pi Apps
wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash
```

## Установка VSCode

VSCode будет использоваться для работы с учебными материалами и запуска кода.

```bash
# Установка Visual Studio Code через Pi Apps
/home/pi/pi-apps/manage install "Visual Studio Code"
```

## Загрузка учебных материалов

```bash
# Создаем директорию для учебных материалов
mkdir -p /home/pi/RaspberryPi-Wiki

# Клонируем репозиторий с учебными материалами
git clone https://github.com/[ваш_репозиторий]/raspberry-pi-wiki-lessons.git /home/pi/RaspberryPi-Wiki/lessons
```

## Дополнительные настройки

### Отключение служб безопасности

```bash
# Отключаем файервол, если он активен
sudo systemctl stop ufw
sudo systemctl disable ufw

# Отключаем другие службы безопасности, которые могут замедлить работу
sudo systemctl disable apparmor
```

### Подготовка для учебных целей

```bash
# Разрешаем доступ по SSH без пароля для учебных целей
# Примечание: Использовать только в защищенной учебной среде
mkdir -p /home/pi/.ssh
touch /home/pi/.ssh/authorized_keys
chmod 700 /home/pi/.ssh
chmod 600 /home/pi/.ssh/authorized_keys
```

## Проверка установки

После выполнения всех шагов проверьте:

1. Обои Wiki платформы установлены
2. Pi Apps успешно установлен
3. Visual Studio Code запускается
4. Учебные материалы доступны в директории `/home/pi/RaspberryPi-Wiki/lessons`
5. Службы безопасности отключены для удобства обучения

## Примечания

- Замените `[URL_к_обоям]` на реальный URL к вашим обоям
- Замените `[ваш_репозиторий]` на имя вашего репозитория GitHub с учебными материалами
- При необходимости адаптируйте пути и команды под вашу конкретную конфигурацию
