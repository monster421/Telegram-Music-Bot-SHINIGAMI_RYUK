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
from NoteBook.notes import MEMBERS_PLAYING_HELP

from handlers.ryuk.shinigami import DELETE_DELAY


@Client.on_message(main_filter
                   & (self_or_contact_filter | current_vc)
                   & filters.regex("!mcmd$"))
async def show_help(_, m: Message):
    if mp.msg.get('!mcmd') is not None:
        await mp.msg['!mcmd'].delete()
    mp.msg['!mcmd'] = await m.reply_text(MEMBERS_PLAYING_HELP, quote=False)
    await m.delete(DELETE_DELAY)
    #await _delay_delete_messages((reply, m), DELETE_DELAY)
