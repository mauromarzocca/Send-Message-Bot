import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

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
    # ... add the other days of the week
}

# Initialize the bot and the dispatcher
bot = Bot(token='Telegram_Bot_ID')
dp = Dispatcher(bot)

# Function to send the message
async def send_scheduled_message():
    day_of_week = datetime.datetime.today().strftime("%A")
    message = messages.get(day_of_week, "Default Message")

    await bot.send_message(chat_id=channel_id, text=message)

# Configure the scheduler to run the function every day at a specific time
scheduler = BlockingScheduler(timezone="UTC")  # Specify the desired time zone

# Use the add_job function of APScheduler to execute the asynchronous function
scheduler.add_job(lambda: asyncio.run(send_scheduled_message()), 'cron', day_of_week='mon-sun', hour=19, minute=0)
scheduler.start()

# Execute the aiogram dispatcher
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
