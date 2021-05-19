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
                   & filters.regex("^.off$"))
async def leave_voice_chat(_, m: Message):
    group_call = mp.group_call
    mp.playlist.clear()
    group_call.input_filename = ''
    await group_call.stop()
    await m.delete()