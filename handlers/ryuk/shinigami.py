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




# in sec = 1sec
DELETE_DELAY = 2
# in min = 1min
ADD_AUTO_MUSIC_TIME = 10
# in hour = 1hour
VC_AUTO_EXIT_TIME = 1


async def current_vc_filter(_, __, m: Message):
    group_call = mp.group_call
    if not group_call.is_connected:
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if m.chat.id == chat_id:
        return True
    return False

current_vc = filters.create(current_vc_filter)

