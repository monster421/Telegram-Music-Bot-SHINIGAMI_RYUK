"""
<--------------------------->
|  ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ     -_-
<--------------------------->

Remastered Version of Riyuk_SINGER)VRTX)BOT
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
from handlers.ryuk.shinigami import PLAYING_HELP

from handlers.ryuk.shinigami import RM_TIME

@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^.resume"))
async def resume_playing(_, m: Message):
    mp.group_call.resume_playout()
    reply = await m.reply_text(f"""
一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]**▶️Resumed**""",
                               quote=False)
    if mp.msg.get('pause') is not None:
        await mp.msg['pause'].delete()
    await m.delete()
    await _delay_delete_messages((reply, m), RM_TIME)