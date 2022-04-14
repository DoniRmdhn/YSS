#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from Yukki import app


from Yukki.Database.mode import set_cmode
from Yukki.Decorators.admins import AdminActual
from . fsub import fsub



@app.on_message(filters.command(["channelplay","cplay"])& filters.group)
@fsub
@AdminActual
async def playmode_(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text("""
You can play music in channels from this chat {}
to any channel or your chat's linked channel.

• **For linked channel:**`/channelplay linked` or `/cplay linked`
• **For any other channel:**`/channelplay  [Channel ID]` or `/cplay  [Channel ID]`

""".format(message.chat.title)
        )
    query = message.text.split(None, 2)[1].lower().strip()
    if str(query) == "linked":
        chat = await app.get_chat(message.chat.id)
        if chat.linked_chat:
            chat_id = chat.linked_chat.id
            await set_cmode(message.chat.id, chat_id)
            return await message.reply_text("""
Channel Defined to {0}
Channel ID: {1}
            """.format(
                    chat.linked_chat.title, chat.linked_chat.id
                )
            )
        else:
            return await message.reply_text("This chat has no linked channel.")
    else:
        try:
            chat = await app.get_chat(query)
        except:
            return await message.reply_text("""
Failed to get channel.
Make sure you have added bot in your channel and promoted it as admin.
Change channel via /channelplay .
            """)
        if chat.type != "channel":
            return await message.reply_text(_["cplay_5"])
        try:
            admins = await app.get_chat_members(
                chat.id, filter="administrators"
            )
        except:
            return await message.reply_text("""
Failed to get channel.
Make sure you have added bot in your channel and promoted it as admin.
Change channel via /channelplay .
            """)
        for users in admins:
            if users.status == "creator":
                creatorusername = users.user.username
                creatorid = users.user.id
        if creatorid != message.from_user.id:
            return await message.reply_text("""
You need to be the **Owner** of the channel[{0}] to connect it 
with this group.
**Channel's Owner:** @{1}
Alternatively you can link your group to that channel and then try connnecting with 
`/channelplay linked`
""".format(chat.title, creatorusername)
            )
        await set_cmode(message.chat.id, chat.id)
        return await message.reply_text("""
Channel Defined to {0}
Channel ID: {1}        
        """.format(chat.title, chat.id)
        )
