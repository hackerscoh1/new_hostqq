from pyrogram import Client, filters,enums
import requests
import random
import urllib.parse
import tempfile
import json
import google.generativeai as genai
import PIL.Image
import io
from io import BytesIO
from PIL import Image
from pyrogram.types import InputMediaPhoto
import os
import base64
# https://github.com/SreejanPersonal/Free-Unoffical-OpenAI-API
# from pyrogram.types import InputFile
# from pytgcalls import PyTgCalls,idle,filters as fl
# from pytgcalls.exceptions import GroupCallNotFound
# from pytgcalls.types import MediaStream,ChatUpdate,Update

api_id = '25593180'
api_hash = 'b58bd82141f66e627ba6c4eb480a3dd3'

idd=[-1002096576575,-1001274621302,-1001663227286,-1002092572217,-1001539384652,-1002111908493, -1001673787011,-1002240900041]
usee=[2137830085,1093904450]
group_chat_id=[-1002096576575]
gcuser=[1300094147, 7098528110, 6536321026, 1404100466,1940516602,7267977568, 1243309538, 1091063475, 7386297062,2003954754]
API_KEY= 'AIzaSyC5O8_pS9mXjS7e_-sn_Ln3LmHOXB7RYro'
app = Client("user", api_id, api_hash)
from pyrogram.raw import functions, types
from pyrogram import  Client, filters
import asyncio
import time
import pytz
from datetime import datetime,timedelta
import random
# usee=[2137830085]
generation_config_cook = {
  "temperature": 0.35,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
    }
# model_cook = genai.GenerativeModel(model_name="gemini-1.5-flash-001",
#                               generation_config=generation_config_cook)

def validate_num(num, country):
    try:
        encoded_num = urllib.parse.quote(num)
        api_key = "num_live_hiSPCD4xTWj3j0hSwWsJF1gZWoDCyHsKK3ETkcUF"
        url = f"https://api.numlookupapi.com/v1/validate/{encoded_num}?apikey={api_key}&country_code={country}"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Return the JSON response
            return response.json()
        else:
            return {"error": "Failed to validate phone number"}
    except Exception as e:
        return {"error": str(e)}

def generate_ask(question):
    try:
        api_url = "https://chat-api-tau.vercel.app/ask?q="
        full_url = api_url + question
        response = requests.get(full_url)
        if response.status_code == 200:
            return response.json().get('response') 
        else:
            return 'Failed to generate text'
    except Exception as e:
        return 'Failed to generate text. Please try again later.'
# def generate_gpt(question):
#     try:
#         api_url = "https://chat-api-tau.vercel.app/api?chat="
#         full_url = api_url + question
#         response = requests.get(full_url)
#         if response.status_code == 200:
#             return response.json().get('response') 
#         else:
#             return 'Failed to generate text'
#     except Exception as e:
#         return 'Failed to generate text. Please try again later.'
# def generate_black(question):
#     try:
#         api_url = "https://shadow-aischat.vercel.app/api?chat="
#         full_url = api_url + question
#         response = requests.get(full_url)
#         if response.status_code == 200:
#             return response.json().get('response') 
#         else:
#             return 'Failed to generate text'
#     except Exception as e:
#         return 'Failed to generate text. Please try again later.'

@app.on_message(filters.command("id", prefixes=".") & filters.user(usee) )
def user_info_command(bot, update):
    try:
        if update.reply_to_message:
            reply_message = update.reply_to_message
            user_id = reply_message.from_user.id
            chat_id = update.chat.id
            # group_id = update.chat.id if update.chat.type in ["group", "supergroup"] else None

            update.reply_text(f"User ID: {user_id}\nChat ID: {chat_id}")
        else:
            update.reply_text("Please reply to a message to get the user ID, chat ID")
    except IndexError:
        update.reply_text("Please provide a user ID.")
# def get_audio_text_completion(prompt: str):
#     url = "https://devsdocode-openai.hf.space/chat/completions"
#     payload = {
#         "messages": [{"role": "user", "content": prompt}],
#         "model": "gpt-4o-audio-preview-2024-10-01",
#         "modalities": ["text", "audio"],
#         "audio": {"voice": "nova", "format": "wav"},
#         "temperature": 0.9,
#         "presence_penalty": 0,
#         "frequency_penalty": 0,
#         "top_p": 1
#     }

#     response = requests.post(url, json=payload)
#     if response.ok:
#         data = response.json()
#         try:
#             if "choices" in data and data["choices"]:
#                 message = data["choices"][0].get("message", {})
#                 audio_data = None
#                 if "audio" in message and "data" in message["audio"]:
#                     audio_data = base64.b64decode(message["audio"]["data"])
#                     return audio_data, message.get("audio", {}).get("transcript", "")
#                 else:
#                     return None, "No audio data found."
#         except Exception as e:
#             print(f"Error: {e}")
#             return None, "An error occurred while processing the request."
#     else:
#         print("Request failed with status code:", response.status_code)
#         return None, "Failed to get response from the service."


# @app.on_message(filters.command("talk", prefixes=".")  &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser) ))
# async def handle_bro(client, message):
#     try:
#         i=await message.reply_text("<code>Wait...</code>")
#         if len(message.command) > 1:
#             prompt = message.text.split(maxsplit=1)[1]
#         elif message.reply_to_message:
#             prompt = message.reply_to_message.text
#         else:
#             await message.reply_text(
#                 f"<b>Usage: </b><code>.talk [prompt/reply to prompt] </code>")
#             return
#         audio_bytes, transcript = get_audio_text_completion(prompt)
    
#         if audio_bytes:
#             # Save the audio file
#             file_name = "AI_response.wav"
#             with open(file_name, "wb") as audio_file:
#                 audio_file.write(audio_bytes)

#             # Send the audio file to the user
#             with open(file_name, "rb") as audio_file:
#                 await message.reply_audio(audio=audio_file, caption=f"Transcript: {transcript}")
#             await i.delete()


#             # Delete the file after sending
#             os.remove(file_name)
#         else:
#             await message.reply_text(f"Error: {transcript}")



#     except Exception as e:
#         await message.reply_text(f"An error occurred: {str(e)}")

@app.on_message(filters.command("audio", prefixes=".")  &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser) ))
async def handle_bro(client, message):
    try:
        i=await message.reply_text("<code>Wait...</code>")
        if len(message.command) > 1:
            prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
            prompt = message.reply_to_message.text
        else:
            await message.reply_text(
                f"<b>Usage: </b><code>.audio [prompt/reply to prompt] </code>")
            return
        full_url=f'https://voiceap.vercel.app/voice?text={prompt}'
        response = requests.get(full_url).json()

        audio_url = response["OutputUri"]

    # Download the audio file
        audio_data = requests.get(audio_url)
        if audio_data.status_code == 200:
            # Save the file locally
            with open("output.mp3", "wb") as file:
                file.write(audio_data.content)

            # Send the audio file in response
            await i.delete()
            await message.reply_audio(
                audio="output.mp3",  # Path to the downloaded file
                caption='🤖'
                
            )
        else:
            await i.delete()
            await message.reply("Failed to download the audio file.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

        


@app.on_message(filters.command("num", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    text_to_generate = message.text.split(".num", 1)[1].strip()
    if text_to_generate:
        parts = text_to_generate.split()
        num = parts[0]
        country = parts[1] if len(parts) > 1 else "in"
        result = validate_num(num, country)
        response_message = (
                f"**Phone Number Validation Result:**\n"
                f"- **Valid:** {'Yes' if result['valid'] else 'No'}\n"
                f"- **Number:** {result.get('number', 'N/A')}\n"
                f"- **Local Format:** {result.get('local_format', 'N/A')}\n"
                f"- **International Format:** {result.get('international_format', 'N/A')}\n"
                f"- **Country Prefix:** {result.get('country_prefix', 'N/A')}\n"
                f"- **Country Code:** {result.get('country_code', 'N/A')}\n"
                f"- **Country Name:** {result.get('country_name', 'N/A')}\n"
                f"- **Location:** {result.get('location', 'N/A')}\n"
                f"- **Carrier:** {result.get('carrier', 'N/A')}\n"
                f"- **Line Type:** {result.get('line_type', 'N/A')}\n"
            )
        await message.reply(response_message)
# call_py = PyTgCalls(app)
# @app.on_message(filters.command("py", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def handle_bro(client, message):
#     chat_id = message.chat.id
#     reply = message.reply_to_message
    
#     # Check if the replied message contains an audio or video file
#     if reply.audio or reply.voice:
#         media = reply.audio or reply.voice
#         await message.reply("Downloading audio...")
#         media_file = await client.download_media(media, file_name=f"{media.file_id}.mp3")
#         # media_stream = AudioPiped(media_file)
#         media_stream= MediaStream(media_file,)
#     elif reply.video:
#         media = reply.video
#         i=await message.reply("Downloading video...")
#         media_file = await client.download_media(media, file_name=f"{media.file_id}.mp4")
#         media_stream = MediaStream(media_file)
#     else:
#         await message.reply("Please reply to an audio or video file.")
#         return

#     try:
#         await i.delete()
#         await call_py.play(chat_id, media_stream)
#         await message.reply("Playing...")
#         @call_py.on_update(fl.stream_end)
#         async def stream_end_handler(_: PyTgCalls, update: Update):
#             if update.chat_id == chat_id:
#                 # print(f'Stream ended in {update.chat_id}')
#                 await call_py.leave_call(chat_id)
#                 await message.reply("finished now sleep")
#     except GroupCallNotFound:
#         await message.reply("Could not join the vc")
#     if os.path.exists(media_file):
#         os.remove(media_file)
# @app.on_message(filters.command("pause", prefixes=".") & (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def pause_handler(client, message):
#     try:
#         await call_py.pause_stream(message.chat.id)
#         await message.reply("Paused")
#     except Exception as e:
#         pass
#         # await message.reply(f"Error pausing the stream: {str(e)}")


# @app.on_message(filters.command("resume", prefixes=".") & (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def resume_handler(client, message):
#     try:
#         await call_py.resume_stream(message.chat.id)
#         await message.reply("Resumed")
#     except Exception as e:
#         pass
#         # await message.reply(f"Error resuming the stream: {str(e)}")


# @app.on_message(filters.command(['stop', 'end'], prefixes=".") & (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def stop_handler(client, message):
#     try:
#         await call_py.leave_call(message.chat.id)
#         await message.reply("Stopped")
#     except Exception as e:
#         pass
#         # await message.reply(f"Error stopping the stream: {str(e)}")


# @app.on_message(filters.command("status", prefixes=".") & (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def get_play_status(client, message):
#     try:
#         played_time = await call_py.played_time(message.chat.id)
#         await client.send_message(message.chat.id, f'Current seconds: {played_time}')
#     except Exception as e:
#         pass
#         # await message.reply(f"Error fetching the status: {str(e)}")

@app.on_message(filters.command("ai", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    text_to_generate = message.text.split(".ai", 1)[1].strip()
    if text_to_generate:
        generated_text = generate_ask(text_to_generate)
        await message.reply(generated_text)
@app.on_message(filters.command("gpt", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    if len(message.command) > 1:
        q = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        q = message.reply_to_message.text
    else:
        await message.reply_text(
        f"<b>Usage: </b><code>.code [prompt/reply to message]</code>"
    )
        return
    i=await message.reply_text("<code>Wait...</code>")
    if q:
        generated_text = generate_gpt(q)
        await i.delete()
        await message.reply(generated_text)
# @app.on_message(filters.command("b", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def handle_bro(client, message):
#     text_to_generate = message.text.split(".b", 1)[1].strip()
#     if text_to_generate:
#         generated_text = generate_black(text_to_generate)
#         await message.reply(generated_text)
@app.on_message(filters.command("air", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    text_to_generate = message.text.split(".air", 1)[1].strip()
    if message.reply_to_message:
            replied_message = message.reply_to_message
            replied_content = replied_message.text
            # await client.delete_messages("me", sent_message.id)
            if text_to_generate:
                generated_text = generate_ask(replied_content+' '+text_to_generate)
                await message.reply(generated_text)
            else :
                generated_text = generate_ask(replied_content)
                await message.reply(generated_text)
@app.on_message(filters.command("s", prefixes=".") &   filters.user(usee) )
async def handle_bro(client, message):
    if message.reply_to_message:
        replied_message = message.reply_to_message
        if replied_message.text:
            replied_content = replied_message.text
        elif replied_message.caption:
            replied_content = replied_message.caption
        elif replied_message.document.file_name:
            replied_content = replied_message.document.file_name
        elif replied_message.media.caption:
            replied_content = replied_message.media.caption
        else:
            await message.reply_text("Error")
            return
        await client.send_message("me", replied_content)
        await asyncio.sleep(3)
        # await message.delete()
        await message.edit("saved")
    else:
        await message.reply_text("reply")

# @app.on_message(filters.command(["img3",'image3'], prefixes=".")  &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser) ))
# async def handle_bro(client, message):
#     try:
#         i=await message.reply_text("<code>Wait...</code>")
#         if len(message.command) > 1:
#             prompt = message.text.split(maxsplit=1)[1]
#         elif message.reply_to_message:
#             prompt = message.reply_to_message.text
#         else:
#             await message.reply_text(
#                 f"<b>Usage: </b><code>.img3 [prompt/reply to prompt] </code>")
#             return
#     # prompt=message.text.split(".img", 1)[1].strip()
#         api_url = f"https://dalleimg.vercel.app/search?query={prompt}"
#         response = requests.get(api_url)
#         # if response.status_code == 200:
#             # Save the image to a file
#             # with open("generated_image.png", "wb") as f:
#             #     f.write(response.content)           
#         # await client.send_photo(message.chat.id, 'https://tse1.mm.bing.net/th/id/OIG2.C2W1pk42.Njqr_n.lqAK?pid=ImgGn', caption=f"Generated image for:",reply_to_message_id=message.id )
#         if response.status_code == 200:
#             data = response.json()
#             images = data.get("response", {}).get("images", [])
#             if images:
#                 await i.delete()
#                 media_group = []
#                 for i, image in enumerate(images[:4]):  # Limit to 4 images
#                     image_url = image.get("url")
                    
#                     # Download the image
#                     img_data = requests.get(image_url).content
#                     filename = f"image_{i}.jpg"
#                     with open(filename, "wb") as img_file:
#                         img_file.write(img_data)
                    
#                     # Append to media group
#                     media_group.append(InputMediaPhoto(filename, caption=f"Generated image for: {prompt}" if i == 0 else ""))
                
                
#                 # Send the images as a media group
                
#                 await client.send_media_group(
#                     chat_id=message.chat.id,
#                     media=media_group,
#                     reply_to_message_id=message.id
#                 )
#                 for media in media_group:
#                         os.remove(media.media)
#         else:
#             await message.reply_text("Failed to generate the image. Try again later.")
#     except Exception as e:
#         await message.reply_text(f"An error occurred: {str(e)}")




# @app.on_message(filters.command(["img1",'image','image1'], prefixes=".")  &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser) ))
# async def handle_bro(client, message):
#     try:
#         i=await message.reply_text("<code>Wait...</code>")

#         prompt = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else (message.reply_to_message.text if message.reply_to_message else None)
        
#         if not prompt:
#             await i.delete()
#             return await message.reply_text("<b>Usage: </b><code>.img1 [prompt/reply to prompt]</code>")

#         API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
#         headers = {"Authorization": "Bearer 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"}
#         response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

#         if response.status_code != 200:
#             return await message.reply("Failed to generate the image")

#         # Open image directly from the response content
#         image = Image.open(BytesIO(response.content))

#         # Use BytesIO for in-memory file handling
#         temp_file = BytesIO()
#         image.save(temp_file, format="PNG")
#         temp_file.seek(0)

#         # Send the image back
#         await message.reply_photo(photo=temp_file, reply_to_message_id=message.id, caption=f"Flux model: {prompt}")

#         await i.delete()

#     except Exception as e:
#         await message.reply_text(f"An error occurred: {str(e)}")
async def extract_text_from_image(client, file_id):
    with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_file:
        await client.download_media(file_id, file_name=temp_file.name)
        with open(temp_file.name, 'rb') as image_file_descriptor:
            files = {'image': image_file_descriptor}
            api_urll = 'https://api.api-ninjas.com/v1/imagetotext'
            r = requests.post(api_urll, files=files)
        if r.status_code == 200:
            data = r.json()
            all_text = " ".join([item['text'] for item in data])
            return all_text if all_text.strip() else "No text found in the image."
        else:
            return "Failed to process the image. Please try again."

# @app.on_message(filters.command(["img","img2",'image2'], prefixes=".")  &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser) ))
# async def handle_bro(client, message):
#     try:
#         # Send initial response
#         i = await message.reply_text("<code>Wait...</code>")

#         # Extract the prompt
#         prompt = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else (
#             message.reply_to_message.text if message.reply_to_message else None)

#         if not prompt:
#             await i.delete()
#             return await message.reply_text("<b>Usage: </b><code>.img2 [prompt/reply to prompt]</code>")

#         # Hugging Face API details
#         API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
#         headers = {"Authorization": "Bearer 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"}

#         # Make API request
#         response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

#         if response.status_code != 200:
#             await i.delete()
#             return await message.reply("Failed to generate the image.")

#         # Process image directly from response content
#         image = Image.open(BytesIO(response.content))

#         # Use BytesIO to avoid disk I/O
#         temp_file = BytesIO()
#         image.save(temp_file, format="PNG")
#         temp_file.seek(0)

#         # Reply with the generated image
#         await message.reply_photo(photo=temp_file, reply_to_message_id=message.id, caption=f"Stable Diffusion Model: {prompt}")

#         # Cleanup
#         await i.delete()

#     except Exception as e:
#         await message.reply_text(f"An error occurred: {str(e)}")

async def extract_text_from_image(client, file_id):
    with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_file:
        await client.download_media(file_id, file_name=temp_file.name)
        with open(temp_file.name, 'rb') as image_file_descriptor:
            files = {'image': image_file_descriptor}
            api_urll = 'https://api.api-ninjas.com/v1/imagetotext'
            r = requests.post(api_urll, files=files)
        if r.status_code == 200:
            data = r.json()
            all_text = " ".join([item['text'] for item in data])
            return all_text if all_text.strip() else "No text found in the image."
        else:
            return "Failed to process the image. Please try again."



@app.on_message(filters.command("quote", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_broooo(client, message):
    api_url = 'https://api.api-ninjas.com/v1/quotes?'
    try:
        response = requests.get(api_url, headers={'X-Api-Key': 'A8m7h4XKrRDAdWf0AvgcHg==6P5pAiJiswiB90nB'})
        if response.status_code == requests.codes.ok:
            resu=json.loads(response.text)[0]
            # print(json.loads(resu)[0]['fact'])
            await message.reply(resu['quote']+'\n\n  \t\t- -'+resu['author'])
        else:
            await message.reply("Error:")
    except Exception as e:
        # General catch-all for any other exceptions
        await message.reply(f"An unexpected error occurred: {str(e)}")
@app.on_message(filters.command("fact", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    q=message.text.split(".fact", 1)[1].strip()
    api_url = 'https://factapi-lovat.vercel.app/ask?fact='+q
    r = requests.get(api_url)
    if r.status_code == requests.codes.ok:
        ans=r.json().get('answer')
        await message.reply(ans)
    else:
        await message.reply("Error:")


@app.on_message(filters.command("tor", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    q = message.text.split(".tor", 1)[1].strip()
    try:
        k = requests.get(f'https://itorrentsearch.vercel.app/api/yts/{q}')
        
        # Check the status code to handle any request errors
        if k.status_code == 200:
            l = k.json()
            if "error" in l:
                await message.reply(f"Error: {l['error']}")
            else:
                names = [file["Name"].lower() for file in l]
                e = []
                q=q.lower()
                
                if q in names:
                    e.append(names.index(q))
                else:
                    for i in names:
                        if q in i:
                            e.append(i.index(q))
                
                if len(e) > 0:
                    # await message.reply('Exact match found')
                    match = l[e[0]]
                else:
                    await message.reply('exact match not found')
                    match=l[0]
                name = match.get("Name", "N/A")
                released_date = match.get("ReleasedDate", "N/A")
                genre = match.get("Genre", "N/A")
                runtime = match.get("Runtime", "N/A")
                language = match.get("Language", "N/A")
                first_file = match["Files"][0] if match.get("Files") else {}
                file_size = first_file.get("Size", "N/A")
                magnet_link = first_file.get("Magnet", "N/A")
                reply_message = (
                    f"**Name:** __{name}__\n"
                    f"**Released Date:** __{released_date}__\n"
                    f"**Genre:** __{genre}__\n"
                    f"**Runtime:** __{runtime}__\n"
                    f"**Language:** __{language}__\n"
                    f"**File Size:** __{file_size}__\n"
                    f"**Magnet Link:** ```\n{magnet_link}\n```"
                    f"\ncopy code and paste in utorrent* lite web or any torrent* app\nuse vpn for safety purpose"
                )

                await message.reply(reply_message)

        else:
            await message.reply(f"Error: Status code {k.status_code}")
    except Exception as ex:
        await message.reply(f"An error occurred: {str(ex)}")

# -------------------------------------------------
@app.on_message(filters.command("web", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    # q=message.text.split(".web", 1)[1].strip()
    if len(message.command) > 1:
        q = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        q = message.reply_to_message.text
    else:
        await message.reply_text(
        f"<b>Usage: </b><code>.web [prompt/reply to message]</code>"
    )
        return
    api_url = 'https://webacesapi.vercel.app/search?query='+q
    # api_url = 'https://webacesapi.onrender.com/search?query='+q
    i=await message.reply_text("<code>Wait...</code>")
    r = requests.get(api_url)
    await i.delete()
    if r.status_code == requests.codes.ok:
        ans=r.json().get('response')
        await message.reply(ans)
    else:
        await message.reply("Error:",r.status_code)

# -------------------------------------------------
# genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel("gemini-1.5-flash-001")
# @app.on_message(filters.command(["gem",'gemini'], prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def handle_bro(client, message):
#     # q=message.text.split(".gem", 1)[1].strip()
#     try:
#         # i = await message.reply_text("<code>Please Wait...</code>")
#         if len(message.command) > 1:
#          prompt = message.text.split(maxsplit=1)[1]
#         elif message.reply_to_message:
#          prompt = message.reply_to_message.text
#         else:
#          await message.reply_text(
#             f"<b>Usage: </b><code>.gem [prompt/reply to message]</code>"
#         )
#          return
    
#         chat = model.start_chat()
#         response = chat.send_message(prompt)
#         # i.delete()
    
#         await message.reply_text(f"{response.text}", parse_mode=enums.ParseMode.MARKDOWN)
#     except Exception as e:
#         await message.reply_text(f"An error occurred: {str(e)}")
# # -------------------------------------------------
# @app.on_message(filters.command(["get",'info'], prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def handle_bro(client, message):
#     try:
#         i = await message.reply_text("<code> Wait...</code>")

#         base_img = await message.reply_to_message.download()

#         img = PIL.Image.open(base_img)

#         response = model.generate_content(img)
#         # print(response)
#         await i.delete()

#         await message.reply_text(
#             f"**Detail Of Image:** {response.parts[0].text}", parse_mode=enums.ParseMode.MARKDOWN
#         )
#         os.remove(base_img)
#     except Exception as e:
#         await i.delete()
#         await message.reply_text(e)

# # -------------------------------------------------
# @app.on_message(filters.command(["cook",'aicook'], prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
# async def handle_bro(client, message):
#     try:
#         i = await message.reply_text("<code>Cooking...</code>")

#         base_img = await message.reply_to_message.download()

#         img = PIL.Image.open(base_img)
#         cook_img = [
#         "Accurately identify the baked good in the image and provide an appropriate and recipe consistent with your analysis. ",
#         img,
#         ]

#         response = model_cook.generate_content(cook_img)
#         await i.delete()

#         await message.reply_text(
#             f"{response.text}", parse_mode=enums.ParseMode.MARKDOWN
#         )
#         os.remove(base_img)
#     except Exception as e:
#         await i.delete()
#         await message.reply_text(e)
# -------------------------------------------------
@app.on_message(filters.command(["down",'d'], prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    try:
        i = await message.reply_text("<code>downloading...</code>")
        if len(message.command) > 1:
         prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
         prompt = message.reply_to_message.text
        else:
         await message.reply_text(
            f"<b>Usage: </b><code>.down [prompt/reply to message]</code>"
        )
         return
        url = "https://ugly-merrile-mahee-2d0a2ff4.koyeb.app/"  # Replace with your API endpoint
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        data = {
            "url": prompt,  # Replace with the actual URL
            "videoQuality": "1080",
            "audioFormat": "mp3",
            "audioBitrate": "128",
            "filenameStyle": "classic",
            "downloadMode": "auto",
            "youtubeVideoCodec": "h264",
            "youtubeDubLang": "en",
            "alwaysProxy": False,
            "disableMetadata": False
        }

        response = requests.post(url, headers=headers, json=data).json()
        message_text = (
        "**Status:** {}\n"
        "🎥 File: {}\n\n" 
        "[Click to view the video]({})\n\n"
            ).format(response.get('status'),response.get("filename"),response.get("url"))
        await i.delete()

        await message.reply_text(text=message_text, parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
# -------------------------------------------------
@app.on_message(filters.command("gita", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    try:
        # i = await message.reply_text("<code>Please Wait...</code>")
        if len(message.command) > 1:
         prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
         prompt = message.reply_to_message.text
        else:
         await message.reply_text(
            f"<b>Usage: </b><code>.gita [prompt/reply to message]</code>"
        )
         return
        r=requests.get('https://api.mygitagpt.com/api/v1/gpt/campaign?prompt='+prompt)
        text= r.content.decode()
    
        await message.reply_text(f"{text}", parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")


@app.on_message(filters.command("insta", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    try:
        # i = await message.reply_text("<code>Please Wait...</code>")
        if len(message.command) > 1:
         prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
         prompt = message.reply_to_message.text
        else:
         await message.reply_text(
            f"<b>Usage: </b><code>.insta [insta_id/reply to id] without @</code>"
        )
         return
        r=requests.get('https://follllowapi.vercel.app/follow/'+prompt)
        response= r.json()
        if response.get("status") == "error":
            await message.reply_text(f"**Error:** {response['message']}")
        else:
            await message.reply_text(f"**Done:** {response['message']}")
    
        # await message.reply_text(f"{text}", parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

        

# -------------------------------------------------

@app.on_message(filters.command(["h",'help','cmds','commands'], prefixes=".")&    (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    help_text = (
        "🤖 **Available Commands**\n\n"
        
        "**Text-related Commands:**\n"
        "1. `.ai` - ChatGPT response.\n"
        "2. `.web` - Web access GPT.\n"
        "3. `.air` - Add reply text and given text.\n"
        "4. `.text` - Audio to text(reply to audio file).\n"
        "5. `.audio` - text to audio(reply to text file).\n"
        "6. `.gita` - Bhagavad Gita response.\n"
        # "2. `.gem` / `.gemini` - Gemini AI response.\n"
        # "4. `.b` - Unrestricted content.\n"
        # "8. `.talk` - AI response in audio format.\n\n"

        
        "\n**Image-related Commands** :\n"
        "1. `.img1` -for flux Image generation.\n"
        "2. `.img2` -for stable diffusion Image generation.\n"
        "3. `.t` - Extract text from image.__(Reply to an image)__\n"
        # "3. `.img3` -for dalle Image generation.\n"
        # "5. `.get` / `.info` - Get information about image.__(Reply to an image)__\n"
        # "6. `.cook` - Get recipe for item in image.__(Reply to an image)__\n\n"
        
        "**\nOther Commands:**\n"
        '1. `.al` - Check if the bot is alive.\n'
        "2. `.num 9998881234` - Check phone number validation.\n"
        "3. `.tor Kalki 2898 AD` - Get Tor link for the query.\n"
        "4. `.fact hen or egg` - fact checker.\n"
        "5. `.insta` - for instagram followers\n"
        "7. `.quote` - Get a random quote.\n"
        "8. `.h`, `.help`, `.cmds` - Show this help message."
        # "1. `.down` / `.d` - Download any video from a given URL __(e.g., Insta, X,fb,tiktok,snap,vimeo and so on)__.\n"
    )
    await message.reply(help_text)
# @app.on_message(filters.private & ~filters.user(usee))
# def forward_private_messages(client, message):
#     if not message.from_user.is_bot:
#         client.forward_messages(chat_id=-1002096576575, from_chat_id=message.chat.id, message_ids=message.id)
    # print(f"Message from {message.chat.id} forwarded to group {-1002096576575}.")
async def query(filename):
    try:
        with open(filename, "rb") as f:
            data = f.read()
        API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
        headers = {"Authorization": "Bearer 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"}
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        # Return the error message if the API request fails
        return {"error": f"Error: {str(e)}"}

@app.on_message(filters.command("text", prefixes=".")  & filters.reply &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def listen(client, message):
    try:
        if message.reply_to_message and (message.reply_to_message.audio or message.reply_to_message.voice):
                # Check if the message contains an audio file or voice message
            if message.reply_to_message.audio:
                audio_file = message.reply_to_message.audio
                file_id = audio_file.file_id
                file_name = f"{file_id}.flac"
            elif message.reply_to_message.voice:
                # Voice messages are sent as voice, not audio
                audio_file = message.reply_to_message.voice
                file_id = audio_file.file_id
                file_name = f"{file_id}.ogg"  # Voice messages are usually .ogg

            # Download the audio file (either from .audio or .voice)
            downloaded_file = await message.reply_to_message.download(file_name)
            # Send the file to Hugging Face API for transcription
            result = await query(downloaded_file)
            if "error" in result:
                raise Exception(result["error"])
            for i in result:
                r=result
            transcribed_text=r.get('text')
            MAX_MESSAGE_LENGTH=3500
            if len(transcribed_text) > MAX_MESSAGE_LENGTH:
                transcribed_text = transcribed_text[:MAX_MESSAGE_LENGTH]  # Truncate to the first part
                transcribed_text += "\n... [Message Truncated]"  # Add a note that the message was truncated
            await message.reply(f"**transcribed text** \n\n {transcribed_text}")
            os.remove(downloaded_file)    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}\n\n"
        await message.reply(error_message)
        os.remove(downloaded_file)



    # Send the file to Hugging Face API for transcription
    # result = query(downloaded_file)

    # Extract the transcription text
    # transcribed_text = result.get("text", "Sorry, I couldn't transcribe the audio.")

    # Send the transcribed text back to the user

@app.on_message(filters.command("al", prefixes=".") )
async def handle_bro(client, message):
    await message.reply('Im alive')
@app.on_message(filters.command("t", prefixes=".") & (filters.photo & filters.caption) | (filters.reply & filters.text)   &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_text_extraction(client, message):
    if message.caption == ".t" or message.text == ".t":
        if message.photo:
            photo = message.photo
        elif message.reply_to_message and message.reply_to_message.photo:
            photo = message.reply_to_message.photo
        else:
            await message.reply("Please send a valid image with the `.t` command.")
            return
        extracted_text = await extract_text_from_image(client, photo.file_id)
        if extracted_text:
            generated_text =  generate_ask(extracted_text)
            # k=
            await message.reply(f'**extracted text:**\n{extracted_text}\n\n**Answer:**\n __{generated_text}__ ')
        else:
            await message.reply("No text was extracted from the image.")

# async def change_name():
#     while True:
#         try:
#             # current_time = time.strftime("%H:%M:%S")
#             # utc_time = datetime.utcnow()
#             # ist = pytz.timezone('Asia/Kolkata')
#             # ti=(utc_time.astimezone(ist)+ timedelta(minutes=1)).strftime("%I:%M %p")
#             # await app.update_profile(last_name=ti)
#             pass
#         except Exception as e:
#             await app.send_message(-1002096576575, e)
#         await asyncio.sleep(60) 
# async def main():
#     async with app:
#         await change_name()
# app.run(main())
app.run()
# call_py.start()  
# idle()      
# app.start()          # Start the Pyrogram client manually
# call_py.start()   # Start the PyTgCalls client
# idle()