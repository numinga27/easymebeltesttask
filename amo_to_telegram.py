import requests
import schedule
import time
from telegram import Bot

# Конфигурация
AMOCRM_DOMAIN = 'your_amocrm_domain'
AMOCRM_ACCESS_TOKEN = 'your_access_token'
TELEGRAM_TOKEN = 'your_telegram_bot_token'
CHAT_ID = 'your_chat_id'  # ID чата или пользователя

bot = Bot(token=TELEGRAM_TOKEN)


def get_revenue_data():
    headers = {
        'Authorization': f'Bearer {AMOCRM_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(
        f'https://{AMOCRM_DOMAIN}/api/v4/leads', headers=headers)

    if response.status_code == 200:
        leads = response.json()['_embedded']['leads']
        revenue_by_manager = {}

        for lead in leads:
            manager_id = lead['responsible_user_id']
            revenue = lead['price']
            if manager_id in revenue_by_manager:
                revenue_by_manager[manager_id] += revenue
            else:
                revenue_by_manager[manager_id] = revenue

        return revenue_by_manager
    else:
        print("Ошибка при получении данных:", response.text)
        return None


def send_revenue_to_telegram():
    revenue_data = get_revenue_data()

    if revenue_data:
        message = "Выручка по менеджерам:\n"
        for manager_id, revenue in revenue_data.items():
            message += f"Менеджер ID {manager_id}: {revenue} руб.\n"

        bot.send_message(chat_id=CHAT_ID, text=message)


# Запланируйте выполнение функции ежедневно
schedule.every().day.at("09:00").do(send_revenue_to_telegram)

while True:
    schedule.run_pending()
    time.sleep(60)
