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
                   & filters.regex("^!on$"))
async def join_group_call(client, Message):
    group_call = mp.group_call
    group_call.client = client
    if group_call.is_connected:
        await Message.reply_text(f="一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]**Already joined**")
        return
    await group_call.start(Message.chat.id)
    await Message.delete()
