from os import getenv

FSUB_CHANNEL = getenv("FSUB_CHANNEL")

# This is a special python script of this bot.
# All of codes of this script will not automatically imported to main part.

from functools import wraps
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


CAPTION_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Join Support Grup", url="https://t.me/synxsupport")]])

def fsub(func):
    @wraps(func)
    async def sz_message(_, message):
        try:
            await message._client.get_chat_member(int(FSUB_CHANNEL), message.from_user.id)
        except UserNotParticipant:
            return await message.reply_text(
            text="Hai\nSupaya Bisa Menggunakan Bot Kamu Harus Bergabung Ke Grup Support bot Terlebih Dahulu!.\nSilahkan Klik Tombol Di Bawah Untuk Join Ke Grup support.",
            reply_markup=CAPTION_BTN,
            disable_web_page_preview=True) 
        return await func(_, message)    
    return sz_message
