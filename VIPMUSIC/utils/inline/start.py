from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬",
                url=f"https://t.me/{BOT_USERNAME}?start=help"
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ 𝐁𝐨𝐭 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 ⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=f"https://t.me/BWF_MUSIC1"
            ),
            InlineKeyboardButton(
                text="𝐔𝐩𝐝𝐚𝐭𝐞𝐬 📡", url=f"https://t.me/BWF_MUSIC1"
            )
        ],
     ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 ʜᴇʟᴩ 🔎",
                callback_data="settings_back_helper",
            )
        ],
        [
            InlineKeyboardButton(
                text="📨 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/BWF_MUSIC1"
            ),
            InlineKeyboardButton(
                text="📨 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/BWF_MUSIC1"
            )
        ],
        [
            InlineKeyboardButton(
                text="⛩️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⛩️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔥 ᴏᴡɴᴇʀ 🔥",
                user_id=OWNER,
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳 ʟᴀɴɢᴜᴀɢᴇ 🏳️‍🌈",
                callback_data="LG"
            )
        ]
     ]
    return buttons
