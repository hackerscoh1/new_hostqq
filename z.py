from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
import os
from pytgcalls import filters as fl
from pytgcalls import idle
from pytgcalls import PyTgCalls
# from pytgcalls.types.input_stream import AudioPiped, VideoPiped
from pytgcalls.types import ChatUpdate
from pytgcalls.types import MediaStream
from pytgcalls.types import Update
from pytgcalls.exceptions import GroupCallNotFound
api_id = '25593180'
api_hash = 'b58bd82141f66e627ba6c4eb480a3dd3'

# Initialize Pyrogram client and PyTgCalls
app = Client("user",api_id,api_hash)

call_py = PyTgCalls(app)
@app.on_message(filters.command("play", prefixes=".") & filters.reply)
async def play_media(client: Client, message: Message):
    chat_id = message.chat.id
    reply = message.reply_to_message
    
    # Check if the replied message contains an audio or video file
    if reply.audio or reply.voice:
        media = reply.audio or reply.voice
        media_file = await client.download_media(media, file_name=f"{media.file_id}.mp3")
        # media_stream = AudioPiped(media_file)
        media_stream= MediaStream(media_file,)
    elif reply.video:
        media = reply.video
        media_file = await client.download_media(media, file_name=f"{media.file_id}.mp4")
        media_stream = MediaStream(media_file)
    else:
        await message.reply("Please reply to an audio or video file.")
        return

    try:

        await call_py.play(chat_id, media_stream)
        await message.reply("Playing...")
        @call_py.on_update(fl.stream_end)
        async def stream_end_handler(_: PyTgCalls, update: Update):
            if update.chat_id == chat_id:
                # print(f'Stream ended in {update.chat_id}')
                await call_py.leave_call(chat_id)
                await message.reply("finished now sleep")
    except GroupCallNotFound:
        await message.reply("Could not join the vc")

    # Wait for the media to finish (this depends on pytgcalls handling)
    # await call_py.wait_for_playback(chat_id)
    
    # Leave the voice chat after media finishes
    # await call_py.leave_call(chat_id)
    # await message.reply("Playback finished, left the voice chat.")
    
    # Clean up by removing the downloaded file after playback
    if os.path.exists(media_file):
        os.remove(media_file)


# Start both clients correctly
app.start()          # Start the Pyrogram client manually
call_py.start()   # Start the PyTgCalls client
idle()      