import asyncio
from aiogram import Bot, Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import pytz

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
}

# Inizializza il bot
bot = Bot(token="ID Bot Telegram")
router = Router()
dp = Dispatcher()

# Funzione per inviare il messaggio
async def send_scheduled_message():
    day_of_week = datetime.datetime.now(pytz.timezone("Europe/Rome")).strftime("%A")
    message = messages.get(day_of_week, "Messaggio di default")
    await bot.send_message(chat_id=channel_id, text=message)

# Aggiungi un comando per verificare che il bot funzioni
@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Ciao! Il bot è attivo e funzionante.")

# Configura lo scheduler
scheduler = AsyncIOScheduler(timezone="Europe/Rome")
scheduler.add_job(send_scheduled_message, "cron", day_of_week="mon-sun", hour=19, minute=0)

async def main():
    scheduler.start()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())