import requests
import json
from datetime import datetime, timedelta

# Telegram bot token and chat ID
BOT_TOKEN = ''
CHAT_ID = ''

# Get items from localStorage (simulate for now)
items = [
    {"productName": "Milk", "bestBefore": "2024-10-25"},
    {"productName": "Yogurt", "bestBefore": "2024-10-20"}
]

# Check if an item is expiring within 2 weeks
def is_expiring_soon(best_before):
    today = datetime.today()
    best_before_date = datetime.strptime(best_before, "%Y-%m-%d")
    return best_before_date <= today + timedelta(days=14)

# Send a Telegram message
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

# Check items and send alerts
for item in items:
    if is_expiring_soon(item["bestBefore"]):
        message = f"⚠️ {item['productName']} is expiring soon! Best Before: {item['bestBefore']}"
        send_telegram_message(message)
