


from database.users_chats_db import db


import os
from pyrogram import Client, filters, enums
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from info import IMDB_TEMPLATE
from utils import extract_user, get_file_id, get_poster, last_online
import time
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)



# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot
# License Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot/blob/Auto-Approved-Bot/LICENSE
from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages, broadcast_messages_group
import asyncio
        



from os import environ
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest



pr0fess0r_99=Client(
    "Auto Approved Bot",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)

AUTH_CHANNEL = [int(pr0fess0r_99) for pr0fess0r_99 in environ.get("AUTH_CHANNEL", None).split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "ʜᴇʟʟᴏ {mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴄʜᴀɴɴᴇʟ. {title}\n\nᴏɴʟʏ ɴᴇᴡ ᴀɴᴅ ʟᴏᴡ ꜱɪᴢᴇ ᴍᴏᴠɪᴇ ᴀᴠᴀɪʟᴀʙʟᴇ. ᴇɴᴊᴏʏɪɴɢ🔥🔥")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

@Client.on_message(filters.private & filters.command(["aprv"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("📦 Repo", url="https://ttttt.me/MONEY_HIEST_ROBOT"), InlineKeyboardButton("Updates 📢", url="t.me/Mo_Tech_YT") ],
              [ InlineKeyboardButton("➕️ Add Me To Your Chat ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart") ]]
    await client.send_message(chat_id=message.chat.id, text=f"🥰{message.from_user.mention}🥰", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(AUTH_CHANNEL) if AUTH_CHANNEL else (filters.group | filters.channel))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    from_user = None
    from_user_id, _ = extract_user(message)
    chat_photo = from_user.photo
    local_user_photo = await client.download_media(
        message=chat_photo.big_file_id
    )
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        
        buttons = [[
            InlineKeyboardButton('🧩𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏🧩', url=f'https://t.me/nasrani_update')
            
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        k = await client.send_photo(photo=local_user_photo, chat_id=chat.id, caption=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
        )
        print("Welcome....")
 
        users = await db.get_all_users()
        b_msg = TEXT
        
        start_time = time.time()
        total_users = await db.total_users_count()
        done = 0
        blocked = 0
        deleted = 0
        failed =0

        success = 0
        async for user in users:
            pti, sh = await broadcast_messages(int(user['id']), b_msg)
            if pti:
                success += 1
            elif pti == False:
                if sh == "Blocked":
                    blocked+=1
                elif sh == "Deleted":
                    deleted += 1
                elif sh == "Error":
                    failed += 1
            done += 1
            await asyncio.sleep(2)
            if not done % 20:
                
                print("Welcome....")


print("Auto Approved Bot")

