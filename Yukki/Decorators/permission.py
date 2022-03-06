from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        if message.chat.type == "private":
            return await mystic(_, message)
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "I need to be admin with some permissions:\n"
                + "\n• **can_manage_voice_chats:** To manage voice chats"
                + "• **can_delete_messages:** To delete Bot's Searched Waste"
                + "• **can_invite_users**: For inviting assistant to chat."
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "I don't have the required permission "
                + "\n •**Permission:** `MANAGE VOICE CHATS`"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "I don't have the required permission "
                + "\n • **Permission:** `DELETE MESSAGES`"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "I don't have the required permission "
                + "\n • **Permission:** `INVITE USERS VIA LINK`"
            )
            return
        return await mystic(_, message)

    return wrapper
