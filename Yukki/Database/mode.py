from typing import Dict, List, Union

from Yukki import db

channeldb = db.cplaybn

# Shifting to memory [ mongo sucks often]
channelconnect = {}

async def set_cmode(chat_id: int, mode: int):
    channelconnect[chat_id] = mode
    await channeldb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )