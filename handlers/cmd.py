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
                   & (self_or_contact_filter | current_vc)
                   & filters.regex("^.cmd$"))
async def show_help(_, m: Message):
    if mp.msg.get('cmd') is not None:
        await mp.msg['cmd'].delete()
    mp.msg['cmd'] = await m.reply_text(PLAYING_HELP, quote=False)
    await m.delete()
