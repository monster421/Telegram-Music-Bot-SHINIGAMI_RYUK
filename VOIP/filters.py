"""
🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁
            from |=== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_-====|
            For any support ask me in here @vrtxmusic
🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁

🍁Remastered Version of Riyuk_Singer_Vrtx🍁
"""

"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"

from pyrogram import filters

main_filter = (
    filters.group
    & filters.text
    & ~filters.edited
    & ~filters.via_bot
)

self_or_contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)

"+|========================================== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_- ==============================================+"