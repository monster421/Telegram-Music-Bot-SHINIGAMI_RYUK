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

# in sec = 1sec
RM_TIME = 1
# in min = 1min
ADD_AUTO_MUSIC_TIME = 10
# in hour = 1hour
VC_AUTO_EXIT_TIME = 1


PLAYING_HELP =f"""一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]
**Send any valid audio file and i will play it in vc or reply !play to audio.mp3 file**

                ._ＧＥＮＥＲＡＬ_ＣＯＭＭＡＮＤＳ_.
**.sing**: Reply with an audio to play/queue it.
**.sing**: Also used to check playlist
**.cmd**: used for showing all bot commands.

                   ._ＯＷＮＥＲ_ＣＯＭＭＡＮＤＳ_.
**.on**: Command like a boss to join voice chat of current group.
**.off**: Leave current voice chat where is DJing.
**.check**: Check which VC is joined by the bot.
**.end**: To stop playing the song being played.
**.pause**: Pause playing.
**.resume**: Resume playing.
**.replay**: Play from the beginning with.
**.skip**: Skip the current or skip n(n=>2).
**.cache**: Remove unused RAW files. 
**.alive**: To check the ping status with server.
**.cpu**: To check up time of the cpu and bot.
"""
# - Pyrogram filters

async def current_vc_filter(_, __, m: Message):
    group_call = mp.group_call
    if not group_call.is_connected:
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if m.chat.id == chat_id:
        return True
    return False

current_vc = filters.create(current_vc_filter)

