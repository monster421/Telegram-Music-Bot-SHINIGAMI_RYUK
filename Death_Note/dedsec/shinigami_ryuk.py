
"|""""
"|"🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁
"|"            from |=== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_-====|
"|"           For any support ask me in here @vrtxmusic
"|"🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁
"|"
"|"🍁Remastered Version of Riyuk_Singer_Vrtx🍁
"|"""
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"|"
"|"
"|"
import asyncio
import os
from datetime import datetime, timedelta
from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from pyrogram.types import Message
from VOIP.filters import main_filter, self_or_contact_filter
from VOIP.voice import ded
from NoteBook.notes import *
from Misa_Amane.life_death import *
#from Misa_Amane.red_eye import current_vc
from pytgcalls import GroupCall
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"|"
"|"
"|"
async def current_vc_filter(_, __, m: Message):
    group_call = ded.group_call
    if not group_call.is_connected:
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if m.chat.id == chat_id:
        return True
    return False

current_vc = filters.create(current_vc_filter)
"|"
"|"
"|"                                                                                                                                                  
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"******************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕥𝕦𝕣𝕟𝕚𝕟𝕘 𝕠𝕟 𝕥𝕙𝕖 𝕦𝕤𝕖𝕣𝕓𝕠𝕥 ***********************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^!on$"))
async def join_group_call(client, m: Message):
    group_call = ded.group_call
    group_call.client = client
    if group_call.is_connected:
        await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]\n"
            "                          .**Already joined**\n"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
            )   
        return
    await group_call.start(m.chat.id)
    await m.delete()
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"*************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕥𝕙𝕖 𝕤𝕙𝕠𝕨𝕚𝕟𝕘 𝕠𝕗 ✨ŇỖŴ_ƤĹÃЎĮŇĞ✨ ********************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & current_vc
                   & filters.regex("^.now$"))
async def show_current_playing_time(_, m: Message):
    start_time = ded.start_time
    playlist = ded.playlist
    if not start_time:
        reply = await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]"
            "                          .**Unknown**\n"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
            )   
        await _delay_delete_messages((reply, m), Kill_Time)
        return
    utcnow = datetime.utcnow().replace(microsecond=0)
    if ded.msg.get('current') is not None:
        await ded.msg['current'].delete()
    ded.msg['current'] = await playlist[0].reply_text(
        f"{emoji.PLAY_BUTTON}  {utcnow - start_time} / "
        f"{timedelta(seconds=playlist[0].audio.duration)}",
        disable_notification=True
    )
    await m.delete()
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"**************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕥𝕙𝕖 𝕤𝕙𝕠𝕨𝕚𝕟𝕘 𝕗𝕦𝕝𝕝 𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤 𝕝𝕚𝕤𝕥 ******************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & (self_or_contact_filter | current_vc)
                   & filters.regex("^.cmd$"))
async def show_help(_, m: Message):
    if ded.msg.get('cmd') is not None:
        await ded.msg['cmd'].delete()
    ded.msg['cmd'] = await m.reply_text(FULL_PLAYING_HELP, quote=False)
    await m.delete()
"|"
"|"
"|"
# "+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
# "**************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕥𝕙𝕖 𝕤𝕙𝕠𝕨𝕚𝕟𝕘 𝕠𝕗 𝕞𝕖𝕞𝕓𝕖𝕣 𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤 *****************************"
"|"
"|"
"|"
# @Client.on_message(main_filter
#                    & (self_or_contact_filter | current_vc)
#                    & filters.regex("^.cmd$"))
# async def show_help(_, m: Message):
#     if ded.msg.get('cmd') is not None:
#         await ded.msg['cmd'].delete()
#     ded.msg['cmd'] = await m.reply_text(MEMBERS_PLAYING_HELP, quote=False)
#     await m.delete()

# "+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
# "**************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕥𝕙𝕖 𝕤𝕙𝕠𝕨𝕚𝕟𝕘 𝕠𝕗 𝕒𝕕𝕞𝕚𝕟 𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤 *****************************"
"|"
"|"
"|"
# @Client.on_message(main_filter
#                    & (self_or_contact_filter | current_vc)
#                    & filters.regex("^.cmd$"))
# async def show_help(_, m: Message):
#     if ded.msg.get('cmd') is not None:
#         await ded.msg['cmd'].delete()
#     ded.msg['cmd'] = await m.reply_text(ADMIN_PLAYING_HELP, quote=False)
#     await m.delete()
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"************************* ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝔹𝕠𝕥𝕙 𝕒𝕕𝕕𝕚𝕟𝕘 𝕞𝕦𝕤𝕚𝕔 𝕥𝕠 𝕡𝕝𝕒𝕪𝕝𝕚𝕤𝕥 𝕒𝕟𝕕 𝕥𝕠 𝕤𝕙𝕠𝕨 𝕡𝕝𝕒𝕪𝕝𝕚𝕤𝕥 **************************"
"|"
"|"
"|"
@Client.on_message(
    filters.group
    & ~filters.edited
    & current_vc
    & (filters.regex("^.sing$") | filters.audio)
)
async def play_track(client, m: Message):
    group_call = ded.group_call
    playlist = ded.playlist
    # check audio
    if m.audio:
        if m.audio.duration > (Auto_Add2Play_TimeM * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(Auto_Add2Play_TimeM)} min won't be automatically "
                "                          .**added to playlist**\n"
                "\n"
                "-/===============\-\n"
                "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
                "+\===============/+\n"
            )
            await _delay_delete_messages((reply,), Kill_Time)
            return
        m_audio = m
    elif m.reply_to_message and m.reply_to_message.audio:
        m_audio = m.reply_to_message
        if m_audio.audio.duration > (Kill_Hour * 60 * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(Kill_Hour)} hours won't be added to playlist\n"
                "\n"
                "-/===============\-\n"
                "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
                "+\===============/+\n"
            )
            await _delay_delete_messages((reply,), Kill_Time)
            return
    else:
        await ded.send_playlist()
        await m.delete()
        return
    # check already added
    if playlist and playlist[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await m.reply_text(f"                        .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n"
                                   "                         .**Already added**")
        await _delay_delete_messages((reply, m), Kill_Time)
        return
    # add to playlist
    playlist.append(m_audio)
    if len(playlist) == 1:
        m_status = await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]"            
            "˜”*°• Analyzing Audio & sending to server •°*”˜\n"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
        )
        await ded.download_audio(playlist[0])
        group_call.input_filename = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await ded.update_start_time()
        await m_status.delete()
        print(f"- PLAYING: {playlist[0].audio.title}")
    await ded.send_playlist()
    for track in playlist[:2]:
        await ded.download_audio(track)
    if not m.audio:
        await m.delete()
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"****************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕤𝕜𝕚𝕡𝕡𝕚𝕟𝕘 𝕠𝕗 𝕥𝕣𝕒𝕔𝕜𝕤 ***************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.command("skip", prefixes="!"))
async def skip_track(_, m: Message):
    playlist = ded.playlist
    if len(m.command) == 1:
        await ded.skip_current_playing()
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
            await ded.send_playlist()
        except (ValueError, TypeError):
            reply = await m.reply_text(
                f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
                "[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]"
                "                          .**Invalid input**"
                "\n"
                "-/===============\-\n"
                "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
                "+\===============/+\n",    
                                disable_web_page_preview=True
                                )
        await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"******************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕥𝕦𝕣𝕟𝕚𝕟𝕘 𝕠𝕗𝕗 𝕥𝕙𝕖 𝕦𝕤𝕖𝕣𝕓𝕠𝕥 ***********************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!off$"))
async def leave_voice_chat(_, m: Message):
    group_call = ded.group_call
    ded.playlist.clear()
    group_call.input_filename = ''
    await group_call.stop()
    await m.delete()
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"********************************* ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕗𝕚𝕟𝕕𝕚𝕟𝕘 𝕨𝕙𝕚𝕔𝕙 𝕘𝕣𝕠𝕦𝕡 𝕥𝕙𝕖 𝕦𝕤𝕖𝕣𝕓𝕠𝕥 𝕚𝕤 𝕡𝕝𝕒𝕪𝕚𝕟𝕘 *************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^!group$"))
async def list_voice_chat(client, m: Message):
    group_call = ded.group_call
    if group_call.is_connected:
        chat_id = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(chat_id)
        reply = await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]"
            "                          .**currently in the voice chat:**"
            "                          .**{chat.title}**\n"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
            )   
    else:
        reply = await m.reply_text(emoji.NO_ENTRY
                                   + "didn't join any voice chat yet")
    await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"***************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕥𝕖𝕞𝕚𝕟𝕒𝕥𝕚𝕠𝕟 𝕠𝕗 𝕡𝕝𝕒𝕪𝕝𝕚𝕤𝕥 ***************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!end$"))
async def stop_playing(_, m: Message):
    group_call = ded.group_call
    group_call.stop_playout()
    reply = await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "[🦋](https://telegra.ph/file/2e419eca28153982c5e54.jpg)[🦋]"
            "                          .**⏹Stopped Singing**\n"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
            )   
    await ded.update_start_time(reset=True)
    ded.playlist.clear()
    await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"******************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕡𝕒𝕦𝕤𝕚𝕟𝕘 𝕔𝕠𝕞𝕞𝕒𝕟𝕕 *****************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!pause"))
async def pause_playing(_, m: Message):
    ded.group_call.pause_playout()
    await ded.update_start_time(reset=True)
    reply = await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "[🦋](https://telegra.ph/file/53c1e3bb9d92f745d32bc.jpg)[🦋]"
            "                          .**⏸Paused**"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n",
                            quote=False
                            )
    ded.msg['pause'] = reply
    await m.delete()
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"******************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕣𝕖𝕡𝕝𝕒𝕪𝕚𝕟𝕘 𝕠𝕗 𝕥𝕙𝕖 𝕡𝕝𝕒𝕪𝕝𝕚𝕤𝕥 **********************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!replay$"))
async def restart_playing(_, m: Message):
    group_call = ded.group_call
    if not ded.playlist:
        return
    group_call.restart_playout()
    await ded.update_start_time()
    reply = await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "[🦋](https://telegra.ph/file/c20d0c751ae61a68f8330.jpg)[🦋]"
            "                          .🔁Playing from the beginning"
            "-_-\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
            )   
    await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"******************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕣𝕖𝕤𝕦𝕞𝕚𝕟𝕘 𝕔𝕠𝕞𝕞𝕒𝕟𝕕 ***************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!resume"))
async def resume_playing(_, m: Message):
    ded.group_call.resume_playout()
    reply = await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "[🦋](https://telegra.ph/file/0f0a508854eebdf8cd693.jpg)[🦋]"
            "                          .**▶️Resumed**"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n",
                                quote=False
                                )
    if ded.msg.get('pause') is not None:
        await ded.msg['pause'].delete()
    await m.delete()
    await _delay_delete_messages((reply,), Kill_Time)
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"****************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕦𝕟𝕞𝕦𝕥𝕚𝕟𝕘 𝕥𝕙𝕖 𝕦𝕤𝕖𝕣𝕓𝕠𝕥 𝕚𝕟 𝕧𝕔 *********************************"
"|"
"|"
"|"
# @Client.on_message(main_filter
#                    & self_or_contact_filter
#                    & current_vc
#                    & filters.regex("^!unmutevc$"))
# async def unmute(_, m: Message):
#     group_call = ded.group_call
#     group_call.set_is_mute(False)
#     reply = await m.reply_text(
#             f"一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
#             "[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]\n"
#             "                          .**🎶Unmuted**\n"
#             "\n"
#             "-/===============\-\n"
#             "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
#             "+\===============/+\n"
#             )   
#     await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"******************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕔𝕝𝕖𝕒𝕟𝕚𝕟𝕘 𝕠𝕗 𝕥𝕖𝕞𝕡 𝕗𝕚𝕝𝕖𝕤 ************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!temp$"))
async def clean_raw_pcm(client, m: Message):
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    all_fn: list[str] = os.listdir(download_dir)
    for track in ded.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    reply = await m.reply_text(
            f"                         .一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"
            "                          .**Cleaned** {count} files\n"
            "\n"
            "-/===============\-\n"
            "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
            "+\===============/+\n"
            )   
    await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"******************************************** ℍ𝕒𝕟𝕕𝕝𝕖𝕤 𝕞𝕦𝕥𝕚𝕟𝕘 𝕥𝕙𝕖 𝕦𝕤𝕖𝕣𝕓𝕠𝕥 𝕚𝕟 𝕧𝕔 *********************************"
"|"
"|"
"|"
# @Client.on_message(main_filter
#                    & self_or_contact_filter
#                    & current_vc
#                    & filters.regex("^!mutevc$"))
# async def mute(_, m: Message):
#     group_call = ded.group_call
#     group_call.set_is_mute(True)
#     reply = await m.reply_text(
#             f"一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一"       
#             "[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]"
#             "                          .**✖️Muted**\n"
#             "-/===============\-\n"
#             "|**ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ**|\n"
#             "+\===============/+\n"
#             )   
#     await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"*********************************************** 𝓔𝓝𝓓 𝓞𝓕 𝓛𝓘𝓕𝓔 **********************************************"

async def _delay_delete_messages(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"|"
"|"
"|"
"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
"*********************************************** 𝓔𝓝𝓓 𝓞𝓕 𝓛𝓘𝓕𝓔 **********************************************"

