import os
from telethon import TelegramClient, events

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

client = TelegramClient("music_bot", api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("Music bot is running ✅")

print("Bot is running...")
client.run_until_disconnected()