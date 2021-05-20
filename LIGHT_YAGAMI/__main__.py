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
                            "acmd",     
                                "alive",    
                            "end",        
                                "fcmd",     
                            "group",    
                                "mcmd",     
                            "off",     
                                "on",       
                            "pause",    
                                "replay",   
                            "resume",   
                                "sing",     
                            "skip",     
                                "temp"         
            ]
                )

vrtx = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
vrtx.start()
print('🍁🎷一═デ︻ ֆɦɨռɨɢǟʍɨ_Rʏʊӄ ︻デ═一\nONLINE🍁🎷')
idle()
vrtx.stop()
print('🍁⚰️一═デ︻ ֆɦɨռɨɢǟʍɨ_Rʏʊӄ ︻デ═一\nOFFLINE ⚰️🍁')

