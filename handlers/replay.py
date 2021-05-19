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
                   & filters.regex("^.replay$"))
async def restart_playing(_, m: Message):
    group_call = mp.group_call
    if not mp.playlist:
        return
    group_call.restart_playout()
    await mp.update_start_time()
    reply = await m.reply_text(
        f"一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n🔁Playing from the beginning"
    )
    await _delay_delete_messages((reply, m), RM_TIME)