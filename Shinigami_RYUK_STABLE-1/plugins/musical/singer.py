"""
|---------------------------------------------------_____________$$$
|---------------------------------------------------_____________$$$$
|---------------------------------------------------_____________$$$$
|---------------------------------------------------_____________$$$$$
|---------------------------------------------------_____________$$$$$$
|---------------------------------------------------_____________$$$$$$$
|---------------------------------------------------_____________$$$$$$$$
|---------------------------------------------------_____________$$$$$$$$$
|---------------------------------------------------____________$$$__$$$$$$
|---------------------------------------------------____________$$$___$$$$$$
|---------------------------------------------------____________$$$____$$$$$
|---------------------------------------------------____________$$$_____$$$$$
|---------------------------------------------------____________$$$______$$$$
|---------------------------------------------------____________$$$_______$$$$
|---------------------------------------------------____________$$$_______$$$$
|---------------------------------------------------____________$$$________$$$
|---------------------------------------------------____________$$$________$$$
|---------------------------------------------------____________$$$________$$$
|---------------------------------------------------____________$$$________$$
|---------------------------------------------------____________$$________$$$
|---------------------------------------------------____________$$_______$$$
|---------------------------------------------------____________$$______$$$
|---------------------------------------------------_____$$$$$$$$$_____$$$
|---------------------------------------------------___$$$$$$$$$$$___$$$
|---------------------------------------------------_$$$$$$$$$$$$$__$$$
|---------------------------------------------------$$$$$$$$$$$$$$$$$
|---------------------------------------------------$$$$$$$$$$$$$
|---------------------------------------------------$$$$$$$$$$$$
|---------------------------------------------------_$$$$$$$$$
|---------------------------------------------------___$$$$
ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ
"""

import asyncio
import os
from datetime import datetime, timedelta

from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from pyrogram.types import Message

from thinker.filters import main_filter, self_or_contact_filter
from thinker.voice import mp

DELETE_DELAY = 2
DURATION_AUTOPLAY_MIN = 10
DURATION_PLAY_HOUR = 1


PLAYING_HELP =f"""**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]
**Send any valid audio file and i will play it in vc or reply !play to audio.mp3 file**

                ._ＧＥＮＥＲＡＬ_ＣＯＭＭＡＮＤＳ_.
**.sing**: Reply with an audio to play/queue it.
**.sing**: Also used to check playlist
**.now**: Show current playing time of current track
**.cmd**: used for showing all bot commands.

                   ._ＯＷＮＥＲ_ＣＯＭＭＡＮＤＳ_.
**.on**: Command like a boss to join voice chat of current group.
**.off**: Leave current voice chat where is DJing.
**.check**: Check which VC is joined by the bot.
**.end**: To stop playing the song being played.
**.pause**: Pause playing.
**.resume**: Resume playing.
**.mutevc**: Mute the VC.
**.unmutevc**: Unmute the VC.
**.replay**: Play from the beginning with.
**.skip**: Skip the current or skip n(n=>2).
**.cache**: Remove unused RAW files. 
**.alive**: To check the ping status with server.
**.sys**: To check system information.
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
# - Pyrogram handlers
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
        if m.audio.duration > (DURATION_AUTOPLAY_MIN * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(DURATION_AUTOPLAY_MIN)} min won't be automatically "
                "added to playlist"
            )
            await _delay_delete_messages((reply,), DELETE_DELAY)
            return
        m_audio = m
    elif m.reply_to_message and m.reply_to_message.audio:
        m_audio = m.reply_to_message
        if m_audio.audio.duration > (DURATION_PLAY_HOUR * 60 * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(DURATION_PLAY_HOUR)} hours won't be added to playlist"
            )
            await _delay_delete_messages((reply,), DELETE_DELAY)
            return
    else:
        await mp.send_playlist()
        await m.delete()
        return
    # check already added
    if playlist and playlist[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await m.reply_text(f"**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n**Already added**")
        await _delay_delete_messages((reply, m), DELETE_DELAY)
        return
    # add to playlist
    playlist.append(m_audio)
    if len(playlist) == 1:
        m_status = await m.reply_text(f"""[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)
**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n
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


@Client.on_message(main_filter
                   & current_vc
                   & filters.regex("^.now$"))
async def show_current_playing_time(_, m: Message):
    start_time = mp.start_time
    playlist = mp.playlist
    if not start_time:
        reply = await m.reply_text(f"**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]**Unknown**")
        await _delay_delete_messages((reply, m), DELETE_DELAY)
        return
    utcnow = datetime.utcnow().replace(microsecond=0)
    if mp.msg.get('current') is not None:
        await mp.msg['current'].delete()
    mp.msg['current'] = await playlist[0].reply_text(
        f"{emoji.PLAY_BUTTON}  {utcnow - start_time} / "
        f"{timedelta(seconds=playlist[0].audio.duration)}",
        disable_notification=True
    )
    await m.delete()


@Client.on_message(main_filter
                   & (self_or_contact_filter | current_vc)
                   & filters.regex("^.cmd$"))
async def show_help(_, m: Message):
    if mp.msg.get('helpvc') is not None:
        await mp.msg['helpvc'].delete()
    mp.msg['helpvc'] = await m.reply_text(PLAYING_HELP, quote=False)
    await m.delete()


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.command("skip", prefixes="."))
async def skip_track(_, m: Message):
    playlist = mp.playlist
    if len(m.command) == 1:
        await mp.skip_current_playing()
    else:
        try:
            items = list(dict.fromkeys(m.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(playlist) - 1):
                    audio = f"[{playlist[i].audio.title}]({playlist[i].link})"
                    playlist.pop(i)
                    text.append(f"{emoji.WASTEBASKET} {i}. **{audio}**")
                else:
                    text.append(f"{emoji.CROSS_MARK} {i}")
            reply = await m.reply_text("\n".join(text))
            await mp.send_playlist()
        except (ValueError, TypeError):
            reply = await m.reply_text(f"**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]**Invalid input**",
                                       disable_web_page_preview=True)
        await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^.on$"))
async def join_group_call(client, m: Message):
    group_call = mp.group_call
    group_call.client = client
    if group_call.is_connected:
        await m.reply_text(f"**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]**Already joined**")
        return
    await group_call.start(m.chat.id)
    await m.delete()


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


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^.check$"))
async def list_voice_chat(client, m: Message):
    group_call = mp.group_call
    if group_call.is_connected:
        chat_id = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(chat_id)
        reply = await m.reply_text(
            f"""**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]
**currently in the voice chat:**
**{chat.title}**"""
        )
    else:
        reply = await m.reply_text(emoji.NO_ENTRY
                                   + "didn't join any voice chat yet")
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^.end$"))
async def stop_playing(_, m: Message):
    group_call = mp.group_call
    group_call.stop_playout()
    reply = await m.reply_text(f"""
**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]**⏹Stopped Singing**""")
    await mp.update_start_time(reset=True)
    mp.playlist.clear()
    await _delay_delete_messages((reply, m), DELETE_DELAY)


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
        f"**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n🔁Playing from the beginning"
    )
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^.pause"))
async def pause_playing(_, m: Message):
    mp.group_call.pause_playout()
    await mp.update_start_time(reset=True)
    reply = await m.reply_text(f"""
**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]**⏸Paused**""",
                               quote=False)
    mp.msg['pause'] = reply
    await m.delete()


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^.resume"))
async def resume_playing(_, m: Message):
    mp.group_call.resume_playout()
    reply = await m.reply_text(f"""
**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]**▶️Resumed**""",
                               quote=False)
    if mp.msg.get('pause') is not None:
        await mp.msg['pause'].delete()
    await m.delete()
    await _delay_delete_messages((reply,), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^.cache$"))
async def clean_raw_pcm(client, m: Message):
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    all_fn: list[str] = os.listdir(download_dir)
    for track in mp.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    reply = await m.reply_text(f"**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一****Cleaned** {count} files")
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^.mutevc$"))
async def mute(_, m: Message):
    group_call = mp.group_call
    group_call.set_is_mute(True)
    reply = await m.reply_text(f"""
**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**\n
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]
**✖️Muted**""")
    await _delay_delete_messages((reply, m), DELETE_DELAY)


@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^.unmutevc$"))
async def unmute(_, m: Message):
    group_call = mp.group_call
    group_call.set_is_mute(False)
    reply = await m.reply_text(f"""
**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**
[🍺](https://telegra.ph/file/1d858bae5f9c4c178bcfb.jpg)[🍺]\n
**🎶Unmuted**""")
    await _delay_delete_messages((reply, m), DELETE_DELAY)

# - Other functions

async def _delay_delete_messages(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for m in messages:
        await m.delete()
