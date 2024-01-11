# Send Message Bot

This script allows a bot to send a message to a Telegram channel without storing the IDs of all users.<br>
This Python script utilizes the `aiogram` and `apscheduler` libraries to send scheduled messages to a Telegram channel based on the day of the week. It can be used to send daily reminders or periodic messages to a specific Telegram channel.

## Index

- [Send Message Bot](#send-message-bot)
  - [Index](#index)
  - [Prerequisites](#prerequisites)
  - [Configuration](#configuration)
  - [Running Script](#running-script)

## Prerequisites

Before running the script, make sure to install the following dependencies:

```bash
pip install --force-install -v "aiogram==2.23.1"
pip install apscheduler
```

## Configuration

1. Telegram Bot Token: Replace ID Bot Telegram with the token of your Telegram bot. You can obtain a token by registering a new bot on <a href="https://t.me/botfather" target="_blank" > BotFather </a>.

```bash
    bot = Bot(token='ID Bot Telegram')
```

2. Telegram Channel ID: Replace @ID Canale with the ID of your Telegram channel, where you want to send the messages.

```bash
    channel_id = "@Channel ID"
```

1. Daily Messages: Modify the messages dictionary to customize the messages that will be sent each day of the week.

```bash
    messages = {
    "Monday": "Today is Monday",
    "Tuesday": "Today is Tuesday",
    "Wednesday": "Today is Wednesday",
    "Thursday": "Today is Thursday",
    "Friday": "Today is Friday",
    "Saturday": "Today is Saturday",
    "Sunday": "Today is Sunday",
}
```

4. Sending Time: Configure the time when you want to send the messages by modifying the scheduler.add_job function. In the example, messages are sent every day at 19:00 (UTC).

```bash
    scheduler.add_job(lambda: asyncio.run(send_scheduled_message()), 'cron', day_of_week='mon-sun', hour=19, minute=0)
```

## Running Script

Run the Python script, and the bot will automatically start sending scheduled messages to your Telegram channel.

```bash
    python bot.py
```
