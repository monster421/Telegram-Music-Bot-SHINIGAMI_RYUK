
# import logging
from pyrogram import Client, idle

PLUGINS = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client("tgvc", plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('\u2022>Music-Player-Bot\u2022> STARTED')
idle()
app.stop()
print('\n\u2022>Music-Player-Bott\u2022> STOPPED')
