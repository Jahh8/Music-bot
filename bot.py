import os
import yt_dlp
from telethon import TelegramClient, events

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

client = TelegramClient("music_bot", api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("🎵 Music Bot is running!\nSend a song name or YouTube link.")


def download_audio(query):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "song.mp3",
        "quiet": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }],
    }

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "song.mp3",
    "quiet": True,
    "noplaylist": True,
    "extractor_args": {
        "youtube": {
            "player_client": ["android"]
        }
    }
}
        ydl.download([f"ytsearch1:{query}"])


@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text

    if text.startswith("/"):
        return

    await event.reply("🔍 Searching & downloading...")

    try:
        download_audio(text)
        await client.send_file(event.chat_id, "song.mp3", caption="🎶 Here is your song!")
    except Exception as e:
        await event.reply(f"❌ Error: {e}")


print("Bot is running...")
client.run_until_disconnected()