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
                   & current_vc
                   & filters.regex("!pause"))
async def pause_playing(_, m: Message):
    mp.group_call.pause_playout()
    await mp.update_start_time(reset=True)
    reply = await m.reply_text(f"""
一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n
[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]
**⏸𝙋𝙖𝙪𝙨𝙚𝙙**""",
                               quote=False)
    mp.msg['pause'] = reply
    await m.delete()