============================================================
Урок 17: Работа с камерой Raspberry Pi (CircuitPython) 📷
============================================================

Теоретическая часть
-------------------
Камера Raspberry Pi – это официальный модуль камеры для Raspberry Pi, который подключается напрямую к плате через CSI (Camera Serial Interface). Существует несколько моделей камер, включая стандартную и NoIR (без ИК-фильтра). Для работы с камерой в CircuitPython мы будем использовать библиотеку `picamera2`, которая предоставляет современный API для работы с камерой на Python.

В этом уроке мы научимся захватывать фотографии, изменять их параметры и создавать простую систему видеонаблюдения с использованием камеры Raspberry Pi.

Необходимые компоненты
----------------------
- Raspberry Pi
- Модуль камеры Raspberry Pi
- (Опционально) Кнопка для запуска съемки

Схема подключения
-----------------
.. figure:: images/camera.png
   :width: 80%
   :align: center

   **Рис. 1:** Подключение камеры к Raspberry Pi

Установка необходимых библиотек
-------------------------------
Перед запуском кода установите библиотеку picamera2 и OpenCV:

.. code-block:: bash

   sudo apt-get update
   sudo apt-get install -y python3-picamera2
   sudo apt-get install -y python3-opencv

Запуск кода
------------
1. Откройте текстовый редактор или IDE (например, Thonny или VS Code) на Raspberry Pi.
2. Создайте новый файл **camera_circuit.py** в папке `lessons/lesson17/`.
3. Вставьте в файл следующий код:

Код программы
-------------
Файл: `lessons/lesson17/camera_circuit.py`

.. code-block:: python

    import time
    import os
    import datetime
    from picamera2 import Picamera2
    import cv2
    import numpy as np
    
    # Создаем директорию для сохранения изображений, если она не существует
    SAVE_DIR = "camera_captures"
    os.makedirs(SAVE_DIR, exist_ok=True)
    
    # Инициализация камеры
    picam2 = Picamera2()
    
    # Настройка конфигурации для фото (разрешение может быть изменено)
    photo_config = picam2.create_still_configuration(
        main={"size": (1920, 1080), "format": "RGB"},
        lores={"size": (640, 480), "format": "YUV420"}
    )
    
    # Настройка конфигурации для видео (меньшее разрешение для реального времени)
    video_config = picam2.create_preview_configuration(
        main={"size": (640, 480), "format": "RGB"}
    )
    
    # Функция для захвата фото с текущей датой/временем в имени файла
    def capture_photo():
        # Настраиваем камеру для фото
        picam2.configure(photo_config)
        picam2.start()
        
        # Даем камере время на адаптацию
        time.sleep(2)
        
        # Создаем имя файла с текущей датой и временем
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{SAVE_DIR}/photo_{timestamp}.jpg"
        
        # Захватываем изображение
        picam2.capture_file(filename)
        
        print(f"Фото сохранено как {filename}")
        
        # Останавливаем камеру
        picam2.stop()
        return filename
    
    # Функция для захвата фото с эффектами
    def capture_photo_with_effects():
        # Настраиваем камеру для фото
        picam2.configure(photo_config)
        picam2.start()
        
        # Даем камере время на адаптацию
        time.sleep(2)
        
        # Создаем имя файла с текущей датой и временем
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        
        # Захватываем изображение в массив
        img = picam2.capture_array()
        
        # Применяем эффекты (конвертируем в оттенки серого)
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        
        # Применяем детектор краев Canny
        edges = cv2.Canny(gray_img, 100, 200)
        
        # Сохраняем результаты
        gray_filename = f"{SAVE_DIR}/gray_{timestamp}.jpg"
        edges_filename = f"{SAVE_DIR}/edges_{timestamp}.jpg"
        
        cv2.imwrite(gray_filename, gray_img)
        cv2.imwrite(edges_filename, edges)
        
        print(f"Чёрно-белое фото сохранено как {gray_filename}")
        print(f"Фото с выделенными краями сохранено как {edges_filename}")
        
        # Останавливаем камеру
        picam2.stop()
        return gray_filename, edges_filename
    
    # Функция для запуска простого видеонаблюдения с обнаружением движения
    def motion_detection(duration=30):
        # Настраиваем камеру для видео
        picam2.configure(video_config)
        picam2.start()
        
        # Даем камере время на адаптацию
        time.sleep(2)
        
        # Захватываем первый кадр как фон
        background = picam2.capture_array()
        background_gray = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY)
        background_gray = cv2.GaussianBlur(background_gray, (21, 21), 0)
        
        print("Начало обнаружения движения. Нажмите Ctrl+C для остановки.")
        
        start_time = time.time()
        motion_detected = False
        
        try:
            while time.time() - start_time < duration:
                # Захватываем текущий кадр
                current_frame = picam2.capture_array()
                
                # Преобразуем в оттенки серого
                gray = cv2.cvtColor(current_frame, cv2.COLOR_RGB2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)
                
                # Вычисляем разницу между текущим кадром и фоном
                frame_delta = cv2.absdiff(background_gray, gray)
                thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
                
                # Расширяем область для лучшего обнаружения
                thresh = cv2.dilate(thresh, None, iterations=2)
                
                # Находим контуры на бинарном изображении
                contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                # Проверяем, есть ли обнаруженные контуры достаточного размера
                for contour in contours:
                    if cv2.contourArea(contour) < 500:  # Отфильтрованные маленькие изменения
                        continue
                    
                    # Достаточно большое изменение - движение обнаружено
                    if not motion_detected:
                        motion_detected = True
                        print("Обнаружено движение!")
                        
                        # Сохраняем кадр с движением
                        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                        motion_filename = f"{SAVE_DIR}/motion_{timestamp}.jpg"
                        
                        # Рисуем прямоугольник вокруг области движения
                        (x, y, w, h) = cv2.boundingRect(contour)
                        cv2.rectangle(current_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        
                        # Добавляем текст
                        cv2.putText(current_frame, "Движение обнаружено", (10, 20),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                        
                        # Сохраняем изображение
                        cv2.imwrite(motion_filename, cv2.cvtColor(current_frame, cv2.COLOR_RGB2BGR))
                        print(f"Кадр с движением сохранен как {motion_filename}")
                
                # Небольшая задержка
                time.sleep(0.1)
                
                # Обновляем фон (медленная адаптация)
                if not motion_detected:
                    cv2.accumulateWeighted(gray, background_gray, 0.1)
                else:
                    # Сбрасываем флаг обнаружения через некоторое время
                    motion_detected = False
        
        except KeyboardInterrupt:
            print("\nОбнаружение движения остановлено.")
        
        finally:
            # Останавливаем камеру
            picam2.stop()
    
    # Основной код
    try:
        print("Программа для работы с камерой Raspberry Pi")
        print("1. Захват фотографии")
        print("2. Захват фотографии с эффектами")
        print("3. Обнаружение движения (30 секунд)")
        
        choice = input("Выберите опцию (1-3): ")
        
        if choice == "1":
            photo_path = capture_photo()
            print(f"Фотография сохранена: {photo_path}")
        
        elif choice == "2":
            gray_path, edges_path = capture_photo_with_effects()
            print(f"Фотографии с эффектами сохранены: {gray_path}, {edges_path}")
        
        elif choice == "3":
            motion_detection(30)  # 30 секунд обнаружения движения
        
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
    
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")


Разбор кода
------------
- `Picamera2()` – инициализация камеры с использованием современного API Picamera2.
- `create_still_configuration()` – создание конфигурации для фотографий высокого разрешения.
- `create_preview_configuration()` – создание конфигурации для видеопотока с меньшим разрешением.
- `capture_photo()` – функция для захвата фотографии и сохранения ее с временной меткой.
- `capture_photo_with_effects()` – функция для захвата фотографии и применения эффектов с помощью OpenCV:
  - Преобразование в оттенки серого.
  - Применение детектора краев Canny.
- `motion_detection()` – функция для обнаружения движения:
  - Захват фонового изображения.
  - Сравнение текущего кадра с фоном.
  - Обнаружение значительных изменений (контуров).
  - Сохранение кадров с обнаруженным движением.

Ожидаемый результат
-------------------
1. При выборе опции 1 камера делает снимок и сохраняет его в папку `camera_captures`.
2. При выборе опции 2 камера делает снимок, применяет к нему эффекты (черно-белый и выделение краев) и сохраняет результаты.
3. При выборе опции 3 камера запускает систему обнаружения движения на 30 секунд, которая автоматически сохраняет кадры при обнаружении движения.

.. note::
   Для наилучших результатов рекомендуется использовать хорошее освещение. Параметры обнаружения движения могут потребовать настройки в зависимости от условий окружающей среды. Обратите внимание, что обработка изображений с помощью OpenCV может быть ресурсоемкой на Raspberry Pi.

Завершение работы
-----------------
По окончании работы программы или при нажатии **Ctrl + C** камера автоматически останавливается.

Поздравляем! 🎉 Вы успешно научились работать с камерой Raspberry Pi с помощью CircuitPython и OpenCV! Теперь вы можете использовать камеру для создания проектов с распознаванием образов, видеонаблюдением и других интересных приложений компьютерного зрения.