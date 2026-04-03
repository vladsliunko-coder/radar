from telethon import TelegramClient, events
import re
import json

# --- ТВОИ ДАННЫЕ ---
api_id = 39733197
api_hash = '938df5ddd522f9e955bd4556fdee1dfb'

# Обновленный список каналов
source_channels = [
    'war_monitor', 
    'https://t.me/+XJhSk7a1dSwxZjAy', 
    'https://t.me/+NG6TGFCykeRmMTYy',
    'https://t.me/+TlE6YYbNMrgyZTUy' # Новый канал
]

# База координат (можешь дописывать сюда новые города)
LOCATIONS = {
"Київ|Киев": {"lat": 50.45, "lon": 30.52},
    "Чернігів|Чернигов": {"lat": 51.49, "lon": 31.28},
    "Полтава": {"lat": 49.58, "lon": 34.55},
    "Харків|Харьков": {"lat": 50.00, "lon": 36.23},
    "Дніпро|Днепр": {"lat": 48.46, "lon": 35.04},
    "Одеса|Одесса": {"lat": 46.48, "lon": 30.72},
    "Миколаїв|Николаев": {"lat": 46.97, "lon": 31.99},
    "Запоріжжя|Запорожье": {"lat": 47.83, "lon": 35.13},
    "Суми|Сумы": {"lat": 50.91, "lon": 34.79},
    "Львів|Львов": {"lat": 49.83, "lon": 24.02},
    "Житомир": {"lat": 50.25, "lon": 28.65},
    "Вінниця|Винница": {"lat": 49.23, "lon": 28.46}
}

client = TelegramClient('shahed_session', api_id, api_hash)

def update_map_file(targets):
    with open('map_data.json', 'w', encoding='utf-8') as f:
        json.dump(targets, f, ensure_ascii=False, indent=4)

print("🚀 Скрипт запущен! Слушаю 4 канала...")

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    if event.message.message:
        text = event.message.message
        print(f"\n📩 Новое сообщение:\n{text}")

        found_targets = []
        for city, coords in LOCATIONS.items():
            # Ищем город в тексте (игнорируя регистр)
            if re.search(city, text, re.IGNORECASE):
                print(f"🎯 Нашел в тексте: {city}")
                found_targets.append({
                    "city": city, 
                    "lat": coords['lat'], 
                    "lon": coords['lon']
                })
        
        if found_targets:
            update_map_file(found_targets)
            print("💾 Данные для карты index.html обновлены!")

client.start()
client.run_until_disconnected()