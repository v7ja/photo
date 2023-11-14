from pyrogram import *
from pyrogram.types import *
from os import *
from asyncio import *


app = Client(
"Idd",20993785,"a5378e174b86b9fc3cf1ef284e2767b4",
"6756691141:AAF3f5kiv-GcvGSCm8tZqvW96FlD1iwIAT4")

   
@app.on_message(filters.command('start',''))
async def idd(c:Client,m:Message):
 user_id = m.from_user.id
 msg = await m.reply('جاري جلب معلومات الحساب...')
 user = await c.get_users(user_id)
 username = "@"+user.username if user.username else "-"
 first_name = user.first_name
 last_name = user.last_name if user.last_name else "-"
 name = user.first_name+" "+user.last_name if user.last_name else user.first_name
 b = (await c.get_chat(user_id)).bio
 bio = b if b else '-'
 status = str(user.status).replace('UserStatus.','')
 dcid = user.dc_id if user.dc_id else '-'
 txt = f"""
◈<u> معلومات الحساب </u>◈


- user id : {user_id} ✓
- first name : {first_name} ✓
- last name : {last_name} ✓
- usernane : {username} ✓
- dc id : {dcid} ✓ 
- is bot : {user.is_bot} ✓
- is scam : {user.is_scam} ✓
- premium : {user.is_premium} ✓
- bio : {bio} ✓
- last seen : {status} ✓ 
- profile link : <a href='tg://user?id={user_id}'>{name}</a>
"""
 ph = user.photo.big_file_id if user.photo else None
 if ph:
  ph2 = await c.download_media(ph)
  await gather(
  msg.delete(),
  c.send_photo(
  m.chat.id,
  ph2,
  caption=txt)
  )
  remove(ph2)
 
