# used to get telegram session string code using either terminal or repl.it
"""Generate your Pyrogram Session String and send it to
Saved Messages of your Telegram account
requirements:
- Pyrogram
- TgCrypto
Get your Telegram API Key from:
https://my.telegram.org/apps
"""
import asyncio
import tgcrypto
from pyrogram import Client


async def main():
    api_id = int(input("API ID: "))
    api_hash = input("API HASH: ")
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            "**一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一**:\nPyrogram Session String**:\n"
            f"`{await app.export_session_string()}`"
        )
        print(
            "一═デ︻ 𝕊𝕚𝕟𝕘𝕖𝕣𝕍𝕣𝕥𝕩 ︻デ═一Your Pyrogram session string has been sent to "
            "Saved Messages of your Telegram account!"
        )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
