"""
<--------------------------->
|  ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ     -_-
<--------------------------->

Remastered Version of Riyuk_SINGER)VRTX)BOT
"""
import os
from pyrogram import Client, idle

from KIRA.pyro_auth import DETATCH

API_ID = DETATCH.API_ID
API_HASH = DETATCH.API_HASH
SESSION_NAME = DETATCH.SESSION_NAME


PLUGINS = dict(
    root="handlers",
    include=[
        "ryuk.shinigami",
        "alive",
        "cache",
        "check",
        "cmd",
        "end",
        "off",
        "on",
        "pause",
        "replay",
        "resume",
        "sing",
        "skip"       
    ]
)


app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)

app.start()
print('🍁🎷一═デ︻ ֆɦɨռɨɢǟʍɨ_Rʏʊӄ ︻デ═一\nONLINE🍁🎷')


idle()


app.stop()
print('🍁⚰️一═デ︻ ֆɦɨռɨɢǟʍɨ_Rʏʊӄ ︻デ═一\nOFFLINE ⚰️🍁')

