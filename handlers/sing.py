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
from handlers.ryuk.shinigami import ADD_AUTO_MUSIC_TIME, VC_AUTO_EXIT_TIME

@Client.on_message(
    filters.group
    & ~filters.edited
    & current_vc
    & (filters.regex("^.sing$") | filters.audio)
)
async def play_track(client, m: Message):
    group_call = mp.group_call
    playlist = mp.playlist
   # check audio
    if m.audio:
       if m.audio.duration >= (ADD_AUTO_MUSIC_TIME * 60):
           reply = await m.reply_text(
               f"{emoji.ROBOT} audio which duration longer than "
               f"{str(ADD_AUTO_MUSIC_TIME)} min won't be automatically "
               "added to playlist"
           )
           await _delay_delete_messages((reply,), RM_TIME)
           return
       m_audio = m
    elif m.reply_to_message and m.reply_to_message.audio:
       m_audio = m.reply_to_message
       if m_audio.audio.duration >= (VC_AUTO_EXIT_TIME * 60 * 60):
           reply = await m.reply_text(
               f"{emoji.ROBOT} audio which duration longer than "
               f"{str(VC_AUTO_EXIT_TIME)} hours won't be added to playlist"
           )
           await _delay_delete_messages((reply,), RM_TIME)
           return
    else:
       await mp.send_playlist()
       await m.delete()
       return
    # check already added
    if playlist and playlist[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await m.reply_text(f"一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n**Already added**")
        await _delay_delete_messages((reply, m), RM_TIME)
        return
    # add to playlist
    playlist.append(m_audio)
    if len(playlist) == 1:
        m_status = await m.reply_text(f"""[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)
一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n
**Analyzing Audio & sending to heroku**"""
        )
        await mp.download_audio(playlist[0])
        group_call.input_filename = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await mp.update_start_time()
        await m_status.delete()
        print(f"- PLAYING: {playlist[0].audio.title}")
    await mp.send_playlist()
    for track in playlist[:2]:
        await mp.download_audio(track)
    if not m.audio:
        await m.delete()