from pyrogram.client import Client
from info import *


class Bot(Client):
    def __init__(self):
        super().__init__( # type:ignore
            name="Heart Gptt",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self): # type:ignore
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        await self.send_message(ADMIN, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
    async def stop(self, *args): # type:ignore
        await super().stop()
        print("Bᴏᴛ Iꜱ Sᴛᴏᴘᴘᴇᴅ....")

Bot().run() # type:ignore
