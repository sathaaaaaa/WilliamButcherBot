from wbb import app
from pyrogram import filters

@app.on_message(filters.command("start"))
async def start_command(_, message):
     await message.reply_text("Hi I'm Yumiko and I'm already up")
