
# import logging
from os import environ

from pyrogram import Client, idle

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
SESSION_NAME = environ["SESSION_NAME"]

PLUGINS = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('🍁🎷𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 is ready to make you happy.\nVisit @musicvrtx to check the main bot🍁🎷')
idle()
app.stop()
print(' 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 has been Destroyed⚰️')
