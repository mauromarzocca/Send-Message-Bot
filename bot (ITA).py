import asyncio
from aiogram import Bot, Router, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import pytz

# Your Telegram channel name
channel_id = "@Channel_ID"

# Messages to be sent every day of the week
messages = {
    "Monday": "Today is Monday",
    "Tuesday": "Today is Tuesday",
    "Wednesday": "Today is Wednesday",
    "Thursday": "Today is Thursday",
    "Friday": "Today is Friday",
    "Saturday": "Today is Saturday",
    "Sunday": "Today is Sunday",
}

# Initialize the bot
bot = Bot(token="Telegram_Bot_ID")
router = Router()
dp = Dispatcher()

# Function to send the message
async def send_scheduled_message():
    day_of_week = datetime.datetime.now(pytz.timezone("UTC")).strftime("%A")
    message = messages.get(day_of_week, "Default Message")
    await bot.send_message(chat_id=channel_id, text=message)

# Add a command to verify the bot is working
@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Hello! The bot is up and running.")

# Configure the scheduler
scheduler = AsyncIOScheduler(timezone="UTC")
scheduler.add_job(send_scheduled_message, "cron", day_of_week="mon-sun", hour=19, minute=0)

async def main():
    scheduler.start()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())