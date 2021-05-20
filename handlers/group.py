"""
<--------------------------->
|  ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ     -_-
<--------------------------->

Remastered Version of Riyuk_Singer_Vrtx
"""
import asyncio
import os
from datetime import datetime, timedelta

from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from pyrogram.types import Message

from VOIP.filters import main_filter, self_or_contact_filter
from VOIP.voice import mp
from handlers.ryuk.shinigami import current_vc

from handlers.ryuk.shinigami import DELETE_DELAY



@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("!group$"))
async def list_voice_chat(client, m: Message):
    group_call = mp.group_call
    if group_call.is_connected:
        chat_id = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(chat_id)
        reply = await m.reply_text(
            f"""一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n
[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]
**currently in the voice chat:**
**{chat.title}**"""
        )
    else:
        reply = await m.reply_text(emoji.NO_ENTRY
                                   + "didn't join any voice chat yet")
    await _delay_delete_messages((reply, m), DELETE_DELAY)