import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from info import Config, Txt


@Client.on_message(filters.private & filters.command('start'))
async def handle_start(bot:Client, message:Message):

    Btn = [
        [InlineKeyboardButton(text='ʜєʟᴘ', callback_data='help'), InlineKeyboardButton(text='🌀𝖡𝖮𝖳 𝖲𝖳𝖠𝖳𝖴𝖲✳️', callback_data='server')],
        [InlineKeyboardButton(text='🔄 ᴜᴘᴅᴧᴛє', url='https://t.me/iamthakur007'), InlineKeyboardButton(text='🤖𝖡𝖮𝖳 𝖨𝖭𝖥𝖮ℹ️', callback_data='about')],
        [InlineKeyboardButton(text='👨‍💻 ᴅєᴠєʟσᴘєʀ', url='https://t.me/iamthakur007')]
        ]

    await message.reply_text(text=Txt.START_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(Btn))


#Restart to cancell all process 
@Client.on_message(filters.private & filters.command("r") & filters.user(Config.SUDO))
async def restart_bot(b, m):
    await m.reply_text("🔄__𝗒𝗈𝗎𝗋 𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗋𝖾𝗌𝗍𝖺𝗋𝗍.....__")
    os.execl(sys.executable, sys.executable, *sys.argv)
