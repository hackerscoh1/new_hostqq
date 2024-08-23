from pyrogram import Client, filters
import requests
import random

# api_id = 25593180 #--Add your Api Id here
# api_hash = 'b58bd82141f66e627ba6c4eb480a3dd3' #--Enter Api Hash Here

# token = '6916100902:AAFpi3Y6GFv4vpaaRa9H9SEzv4-wxmlk6jA' #--Enter Bot Token Here.

api_id = '25593180'
api_hash = 'b58bd82141f66e627ba6c4eb480a3dd3'
# bot_token = '6916100902:AAE1oZS0MmN3FhqjLpi80PVTJVMF_CeTk1g'
app = Client("user", api_id, api_hash)
from pyrogram.raw import functions, types
from pyrogram import  Client, filters
import asyncio
import time
import pytz
from datetime import datetime,timedelta
import random
usee=[2137830085]
@app.on_message(filters.command("ai", prefixes=".")&  filters.user(usee) )
async def handle_bro(client, message):
    text_to_generate = message.text.split(".ai", 1)[1].strip()
    # if text_to_generate:
        # generated_text = generate_ask(text_to_generate)
    await message.reply('alive')
async def change_name():
    while True:
        
        
        try:
            current_time = time.strftime("%H:%M:%S")
            utc_time = datetime.utcnow()
       
            ist = pytz.timezone('Asia/Kolkata')
        
            ti=(utc_time.astimezone(ist)+ timedelta(minutes=1)).strftime("%I:%M %p")
          
            await app.update_profile(last_name=ti)
           
        except Exception as e:
            await app.send_message(-10020965765, e)
        await asyncio.sleep(60)  # Sleep for 60 seconds (1 minute)



async def main():
    async with app:
        await change_name()

app.run(main())
