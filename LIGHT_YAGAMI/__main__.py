"""
<--------------------------->
|  ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ     -_-
<--------------------------->

Remastered Version of Riyuk_SINGER)VRTX)BOT
"""
import os
from pyrogram import Client, idle

#from KIRA.pyro_auth import DETATCH

#API_ID = DETATCH.API_ID
#API_HASH = DETATCH.API_HASH
#SESSION_NAME = DETATCH.SESSION_NAME
API_ID =3595484
API_HASH ="869f1bfacc8e787f3a79327e9113c489"
SESSION_NAME ="BQAPyr4joLKj3gcvSq6f7kfyl_Wdi1Ktc5HoORcnqy7XPF0Fcw4Q-7WyUNbuEkFeCzyFu6z9yAzn3yM52qMrDuGyWgdYsSR6PTp-tOQqQonibYV4_z0B1R1bV8w04TVJnc-PlcDNhcbfcdxYTNxGJPQFoLIPTDFY0mBilQzuLJGoqq5rO-4iBXN7W8Y93fJqJHpXxfPsRyMqlTBfqtQHnlosp8uGP1UcLg4JQYggEK6BA3_8uBKhlx1kiK1qyrMdvpf6J31kSv3zH1my1dr_fXWv5Z3mEvtL7BGESvBplXDBf3VSNTsHn9oTaHRqHCGVnKkuGw8gN5_Pl5LNbUi1ZL2BVOgZ9QA"

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

