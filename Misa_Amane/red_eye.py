"""
🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁
            from |=== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_-====|
            For any support ask me in here @vrtxmusic
🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁

🍁Remastered Version of Riyuk_Singer_Vrtx🍁
"""
from pyrogram import Client, filters
from VOIP.voice import ded
from pyrogram.types import Message
import ffmpeg

"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"

async def current_vc_filter(_, __, m: Message):
    group_call = ded.group_call
    if not group_call.is_connected:
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if m.chat.id == chat_id:
        return True
    return False

current_vc = filters.create(current_vc_filter)

"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"
