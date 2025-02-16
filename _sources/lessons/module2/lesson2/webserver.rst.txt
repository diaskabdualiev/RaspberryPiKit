====================================================
Урок 2: Веб-лендинг с отдельной HTML-страницей
====================================================


Теоретическая часть
-------------------
В этом уроке мы создадим простой «лендинг» (одностраничный сайт) с помощью **Flask**, при этом основной контент будет вынесен в отдельный HTML-файл. Flask поддерживает шаблоны, которые обычно хранятся в папке `templates`. Это позволяет разделять логику приложения (Python-код) и структуру/верстку (HTML).

Необходимые компоненты
----------------------
- Raspberry Pi (или любой компьютер с Python 3)
- Установленный Flask (`pip3 install flask`)
- Папка `templates` c HTML-файлом

Структура проекта
-----------------
.. code-block:: bash

   lessons/
   └── lesson14/
       ├── app.py
       └── templates/
           └── index.html

**Пояснение:**
- `app.py` – файл с Flask-приложением
- `templates/` – директория для HTML-шаблонов
- `index.html` – сам HTML-файл с версткой

Код приложения (app.py)
-----------------------

.. code-block:: python

   from flask import Flask, render_template

Просто создаём Flask-приложение и импортируем функцию render_template.

.. code-block:: python

   app = Flask(__name__)

Здесь мы создаём экземпляр приложения Flask, передавая в него специальную переменную `__name__`, чтобы Flask знал, где искать шаблоны.

.. code-block:: python

   @app.route('/')
   def landing_page():
       return render_template('index.html')

Мы определяем маршрут `/` (корневой URL). При переходе на http://<IP>:5000/ Flask возвращает содержимое шаблона `index.html` из папки `templates`.

.. code-block:: python

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)

Если файл запущен напрямую, стартуем встроенный сервер Flask на порту 5000.

HTML-файл (index.html)
----------------------

.. code-block:: html

   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8"/>
       <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
       <title>My Landing Page</title>
       <style>
           body {
               margin: 0;
               font-family: Arial, sans-serif;
               background: #f7f9fb;
           }
           .hero {
               display: flex;
               align-items: center;
               justify-content: center;
               height: 100vh;
               background: linear-gradient(to bottom right, #4facfe, #00f2fe);
               color: white;
               text-align: center;
           }
           .hero h1 {
               font-size: 3rem;
               margin-bottom: 1rem;
           }
           .hero p {
               font-size: 1.5rem;
           }
           .cta-btn {
               display: inline-block;
               margin-top: 2rem;
               padding: 1rem 2rem;
               font-size: 1.2rem;
               background: #fff;
               color: #333;
               border: none;
               border-radius: 4px;
               cursor: pointer;
               transition: background 0.3s ease;
           }
           .cta-btn:hover {
               background: #eaeaea;
           }
       </style>
   </head>
   <body>
       <div class="hero">
           <div>
               <h1>Welcome to My Landing Page!</h1>
               <p>This is a simple hero section with a call-to-action button.</p>
               <button class="cta-btn">Learn More</button>
           </div>
       </div>
   </body>
   </html>

В этом файле мы используем стандартную структуру HTML5. Блок `.hero` занимает всю высоту экрана и имеет градиентный фон. Класс `.cta-btn` — это кнопка с анимацией при наведении.

Запуск проекта
--------------
1. Убедитесь, что в папке lesson14 есть `app.py` и папка `templates/index.html`.
2. Запустите приложение:

   .. code-block:: bash

      python3 lessons/lesson14/app.py

3. Перейдите в браузере на http://<RaspberryPi_IP>:5000

Ожидаемый результат
-------------------
На экране появится полноценная HTML-страница с заголовком, описанием и кнопкой на красочном фоне.

.. figure:: images/landing_page_preview.png
   :width: 50%
   :align: center

   **Рис. 2:** Пример отображения Landing Page

Завершение работы
-----------------
Нажмите **Ctrl + C** в терминале, чтобы остановить сервер. Поздравляем! Вы создали простой лэндинг-сайт, отделив HTML от логики Flask-приложения.
