▎Шаг 1: Подготовка окружения

1. Установите Python: Убедитесь, что у вас установлен Python (рекомендуется версия 3.7 и выше).

2. Создайте виртуальное окружение (рекомендуется):
   
   python -m venv myenv
   source myenv/bin/activate  # Для Linux/Mac
   myenvScriptsactivate  # Для Windows
   

3. Установите необходимые библиотеки:
   
   pip install requests python-telegram-bot schedule
   

▎Шаг 2: Получение данных из amoCRM

1. Создайте приложение в amoCRM:

   • Перейдите в настройки вашего аккаунта amoCRM и создайте новое приложение для получения API-ключа.

   • Запишите client_id, client_secret и redirect_uri.

2. Получите токен доступа:

   • Используйте OAuth 2.0 для получения токена доступа. Вам нужно будет выполнить запрос на получение токена, используя ваши учетные данные.

3. Получите данные по выручке:

   • Используйте API amoCRM для получения данных по выручке. Например, вы можете использовать метод GET /api/v4/leads для получения сделок и их сумм.

▎Шаг 3: Настройка Telegram бота

1. Создайте бота в Telegram:

   • Найдите BotFather в Telegram и создайте нового бота. Запишите токен вашего бота.
Запустите скрипт:
   
   python amo_to_telegram.py
 Настройте автоматический запуск (по желанию):

   • Используйте cron (Linux) или Task Scheduler (Windows) для автоматического запуска скрипта.    


▎Настройка автоматического запуска с помощью cron (Linux)

1. Откройте терминал.

2. Запустите редактор crontab:
   
   crontab -e
   

3. Добавьте новую задачу:
   В открывшемся редакторе добавьте строку, которая будет запускать ваш скрипт. Например, если вы хотите запускать его каждый день в 9:00, добавьте следующую строку:
   
   0 9 * * * /path/to/your/venv/bin/python /path/to/your/script/amo_to_telegram.py
   
   Замените /path/to/your/venv/bin/python на путь к интерпретатору Python в вашем виртуальном окружении и /path/to/your/script/amo_to_telegram.py на полный путь к вашему скрипту.

   Пример:
   
   0 9 * * * /home/user/myenv/bin/python /home/user/projects/amo_to_telegram.py
   

4. Сохраните и закройте редактор:
   Если вы используете nano, нажмите CTRL + X, затем Y, чтобы подтвердить сохранение, и Enter, чтобы выйти.

5. Проверьте настройки cron:
   Вы можете проверить, что ваша задача была добавлена, выполнив команду:
   
   crontab -l
   

▎Настройка автоматического запуска с помощью Task Scheduler (Windows)

1. Откройте Task Scheduler:

   • Нажмите Win + R, введите taskschd.msc и нажмите Enter.

2. Создайте новую задачу:

   • В правом верхнем углу выберите "Create Basic Task...".

3. Назовите задачу:

   • Введите название и описание задачи (например, "AmoCRM to Telegram").

4. Выберите триггер:

   • Выберите "Daily" (Ежедневно) и нажмите "Next".

5. Настройте время запуска:

   • Укажите время (например, 09:00) и нажмите "Next".

6. Выберите действие:

   • Выберите "Start a program" (Запустить программу) и нажмите "Next".

7. Укажите программу для запуска:

   • В поле "Program/script" укажите путь к вашему интерпретатору Python (например, C:PathToYourPythonpython.exe).

   • В поле "Add arguments (optional)" добавьте путь к вашему скрипту (например, C:PathToYourScriptamo_to_telegram.py).

   • В поле "Start in (optional)" укажите папку, где находится ваш скрипт.

8. Завершите создание задачи:

   • Нажмите "Next", проверьте настройки и нажмите "Finish".

▎Дополнительные советы

• Убедитесь, что ваш скрипт работает корректно при ручном запуске перед тем, как настраивать автоматический запуск.

• Проверьте логи (если они есть) или вывод ошибок в случае проблем с запуском через cron или Task Scheduler.

• Если ваш скрипт использует виртуальное окружение, убедитесь, что путь к интерпретатору Python в задании cron или Task Scheduler указывает на это окружение.
