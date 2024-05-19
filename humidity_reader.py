from queries import get_humidity
from time import sleep
from sender import bot
from config import OP_CHAT  # operator chat id

referenced_humidity = 80.0  # эталонное значение

while True:  # запускать как отдельный инстанс
    humidity_values = get_humidity()
    for humidity_data in humidity_values:
        humidity = humidity_data[1]
        zone = humidity_data[0]
        if humidity > referenced_humidity:
            bot.send_message(OP_CHAT, f'нарушение в зоне {zone}')
    sleep(3000)  # чуть меньше часа во избежание конфликтов
