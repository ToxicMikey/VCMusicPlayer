from pyrogram import Client, filters
from pyrogram.types import Message
from utils import mp, RADIO, USERNAME
from config import Config
from config import STREAM
CHAT=Config.CHAT
ADMINS=Config.ADMINS

@Client.on_message(filters.command(["stream", f"stream@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT) | filters.private))
async def radio(client, message: Message):
    if 1 in RADIO:
        k=await message.reply_text("Ngừng stream nhạc dùng /offstream")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.start_radio()
    k=await message.reply_text(f"Radio bắt đầu: <code>{STREAM}</code>")
    await mp.delete(k)
    await mp.delete(message)

@Client.on_message(filters.command(['offstream', f"offstream@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT) | filters.private))
async def stop(_, message: Message):
    if 0 in RADIO:
        k=await message.reply_text("Vui lòng bắt đầu stream trước /stream")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.stop_radio()
    k=await message.reply_text("Luồng radio đã kết thúc.")
    await mp.delete(k)
    await mp.delete(message)
