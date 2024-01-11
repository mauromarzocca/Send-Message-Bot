import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

# Nome del tuo canale Telegram
channel_id = "@ID Canale"

# Messaggi da inviare ogni giorno della settimana
messages = {
    "Monday": "Oggi è Lunedì",
    "Tuesday": "Oggi è Martedì",
    "Wednesday": "Oggi è Mercoledì",
    "Thursday": "Oggi è Giovedì",
    "Friday": "Oggi è Venerdì",
    "Saturday": "Oggi è Sabato",
    "Sunday": "Oggi è Domenica",
    # ... aggiungi gli altri giorni della settimana
}

# Inizializza il bot e il dispatcher
bot = Bot(token='ID Bot Telegram')
dp = Dispatcher(bot)


# Funzione per inviare il messaggio
async def send_scheduled_message():
    day_of_week = datetime.datetime.today().strftime("%A")
    message = messages.get(day_of_week, "Messaggio di default")

    await bot.send_message(chat_id=channel_id, text=message)


# Configura lo scheduler per eseguire la funzione ogni giorno a un determinato orario
scheduler = BlockingScheduler(timezone="UTC")  # Specifica il fuso orario desiderato

# Usa la funzione add_job di APScheduler per eseguire la funzione asincrona
scheduler.add_job(lambda: asyncio.run(send_scheduled_message()), 'cron', day_of_week='mon-sun', hour=19, minute=0)
scheduler.start()

# Esegui il dispatcher di aiogram
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)