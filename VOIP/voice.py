"""
🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁
            from |=== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_-====|
            For any support ask me in here @vrtxmusic
🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁

🍁Remastered Version of Riyuk_Singer_Vrtx🍁
"""
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"

import os
import ffmpeg

from datetime import datetime
from pyrogram import emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from pyrogram.types import Message
from pytgcalls import GroupCall
from NoteBook.design_i import *


"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"

class DeathCharm(object):
    def __init__(self):
        self.group_call = GroupCall(None, path_to_log_file='')
        self.chat_id = None
        self.start_time = None
        self.playlist = []
        self.msg = {}

    async def update_start_time(self, reset=False):
        self.start_time = (
            None if reset
            else datetime.utcnow().replace(microsecond=0)
        )

    async def send_playlist(self):
        playlist = self.playlist
        if not playlist:
            pl = f"{emoji.NO_ENTRY}**Nothing is the playlist**"
        else:
            if len(playlist) == 1:
                pl = f"""
一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n🦋ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ🦋
✨ŇỖŴ_ƤĹÃЎĮŇĞ✨:-\n
"""
            else:
                pl = f"""
一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n🦋ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ🦋
✨ŇỖŴ_ƤĹÃЎĮŇĞ✨:-\n
"""
            pl += "\n".join([
                f"**{i}**. **[{x.audio.title}({x.link})**"
                for i, x in enumerate(playlist)
            ])
        if self.msg.get('playlist') is not None:
            await self.msg['playlist'].delete()
        self.msg['playlist'] = await self.send_text(pl)

    async def skip_current_playing(self):
        group_call = self.group_call
        playlist = self.playlist
        if not playlist:
            return
        if len(playlist) == 1:
            await self.update_start_time()
            return
        client = group_call.client
        download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
        group_call.input_filename = os.path.join(
            download_dir,
            f"{playlist[1].audio.file_unique_id}.raw"
        )
        await self.update_start_time()
        # remove old track from playlist
        old_track = playlist.pop(0)
        print(f"- START PLAYING: {playlist[0].audio.title}")
        await self.send_playlist()
        os.remove(os.path.join(
            download_dir,
            f"{old_track.audio.file_unique_id}.raw")
        )
        if len(playlist) == 1:
            return
        await self.download_audio(playlist[1])

    async def send_text(self, text):
        group_call = self.group_call
        client = group_call.client
        chat_id = self.chat_id
        message = await client.send_message(
            chat_id,
            text,
            disable_web_page_preview=True,
            disable_notification=True
        )
        return message

    async def download_audio(self, m: Message):
        group_call = self.group_call
        client = group_call.client
        raw_file = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR,
                                f"{m.audio.file_unique_id}.raw")
        if not os.path.isfile(raw_file):
            original_file = await m.download()
            ffmpeg.input(original_file).output(
                raw_file,
                format='s16le',
                acodec='pcm_s16le',
                ac=2,
                ar='48k',
                loglevel='error'
            ).overwrite_output().run()
            os.remove(original_file)
ded = DeathCharm()

"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"


@ded.group_call.on_network_status_changed
async def network_status_changed_handler(gc: GroupCall, is_connected: bool):
    if is_connected:
        ded.chat_id = int("-100" + str(gc.full_chat.id))
        await ded.send_text(
            f"一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一[🦋]\n"
            "𝕆ℕ𝕃𝕀ℕ𝔼🟢\n"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
            )   
    else:
        await ded.send_text(
            f"一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一[🦋]\n"     
            "🔇𝕀𝔻𝕃𝔼_𝕄𝕆𝔻𝔼_𝔸ℂ𝕋𝕀𝕍𝔼🔇\n"
            "--𝕊𝕃𝔼𝔼ℙ(🔶)\n"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
            )              
        ded.chat_id = None

"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"

@ded.group_call.on_playout_ended
async def playout_ended_handler(_, __):
    await ded.skip_current_playing()

"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"