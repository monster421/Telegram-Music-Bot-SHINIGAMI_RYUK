"""
🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁
            from |=== ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ -_-====|
            For any support ask me in here @vrtxmusic
🍁~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍁

🍁Remastered Version of Riyuk_Singer_Vrtx🍁
"""

from time import time
from datetime import datetime
from pyrogram import Client, filters, emoji
from pyrogram.types import Message

# DELAY_DELETE = 60
START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

self_or_contact_filter = filters.create(
    lambda
    _,
    __,
    message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


# https://gist.github.com/borgstrom/936ca741e885a1438c374824efb038b3
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.text
                   & self_or_contact_filter
                   & ~filters.edited
                   & ~filters.via_bot
                   & filters.regex("^.ryuk$"))
async def ping_pong(_, m: Message):
    start = time()
    m_reply = await m.reply_text("...")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"""一═デ︻ **ֆɦɨռɨɢǟʍɨ_Rʏʊӄ** ︻デ═一\n[🦋](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[🦋]
by~ @mastermindvrtx        
**I am alive and ready to play in vc✌🏻**:
        `{delta_ping * 1000:.3f}ms`"""
    )

