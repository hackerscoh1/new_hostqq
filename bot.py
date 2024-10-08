from pyrogram import Client, filters
import requests
import random
import urllib.parse
import tempfile
import json

api_id = '25593180'
api_hash = 'b58bd82141f66e627ba6c4eb480a3dd3'

idd=[-1002096576575,-1001274621302,-1001663227286,-1002092572217,-1001539384652,-1002111908493]
usee=[2137830085]
group_chat_id=[-1002096576575]
gcuser=[1300094147, 7098528110, 6536321026, 1404100466,1940516602,7267977568, 1243309538, 1091063475, 7386297062,2003954754]

app = Client("user", api_id, api_hash)
from pyrogram.raw import functions, types
from pyrogram import  Client, filters
import asyncio
import time
import pytz
from datetime import datetime,timedelta
import random
usee=[2137830085]


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
        api_url = "https://chat-api-tau.vercel.app/api?chat="
        full_url = api_url + question
        response = requests.get(full_url)
        if response.status_code == 200:
            return response.json().get('response') 
        else:
            return 'Failed to generate text'
    except Exception as e:
        return 'Failed to generate text. Please try again later.'
def generate_black(question):
    try:
        api_url = "https://shadow-aischat.vercel.app/api?chat="
        full_url = api_url + question
        response = requests.get(full_url)
        if response.status_code == 200:
            return response.json().get('response') 
        else:
            return 'Failed to generate text'
    except Exception as e:
        return 'Failed to generate text. Please try again later.'

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
@app.on_message(filters.command("ai", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    text_to_generate = message.text.split(".ai", 1)[1].strip()
    if text_to_generate:
        generated_text = generate_ask(text_to_generate)
        await message.reply(generated_text)
@app.on_message(filters.command("b", prefixes=".") &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_bro(client, message):
    text_to_generate = message.text.split(".b", 1)[1].strip()
    if text_to_generate:
        generated_text = generate_black(text_to_generate)
        await message.reply(generated_text)
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

@app.on_message(filters.command("img", prefixes=".")  &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser) ))
async def handle_bro(client, message):
    prompt=message.text.split(".img", 1)[1].strip()
    api_url = f"https://aiimage.ukefuehatwo.workers.dev/?prompt={prompt}"
    try:
        # Send a request to the API to get the generated image
        response = requests.get(api_url)

        if response.status_code == 200:
            # Save the image to a file
            with open("generated_image.png", "wb") as f:
                f.write(response.content)
            
            # Send the image to the user
            await client.send_photo(message.chat.id, "generated_image.png", caption=f"Generated image for: {prompt}",reply_to_message_id=message.id )
        else:
            await message.reply_text("Failed to generate the image. Try again later.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")


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



@app.on_message(filters.command("al", prefixes=".")&  filters.user(usee) )
async def handle_bro(client, message):
    await message.reply('Im alive')
@app.on_message(filters.command("text", prefixes=".") & (filters.photo & filters.caption) | (filters.reply & filters.text)   &  (filters.chat(idd) | filters.private | filters.user(usee) | filters.user(gcuser)))
async def handle_text_extraction(client, message):
    if message.caption == ".text" or message.text == ".text":
        if message.photo:
            photo = message.photo
        elif message.reply_to_message and message.reply_to_message.photo:
            photo = message.reply_to_message.photo
        else:
            await message.reply("Please send a valid image with the `.text` command.")
            return
        extracted_text = await extract_text_from_image(client, photo.file_id)
        if extracted_text:
            generated_text =  generate_ask(extracted_text)
            # k=
            await message.reply(f'**extracted text:**\n{extracted_text}\n\n**Answer:**\n __{generated_text}__ ')
        else:
            await message.reply("No text was extracted from the image.")

async def change_name():
    while True:
        try:
            # current_time = time.strftime("%H:%M:%S")
            # utc_time = datetime.utcnow()
            # ist = pytz.timezone('Asia/Kolkata')
            # ti=(utc_time.astimezone(ist)+ timedelta(minutes=1)).strftime("%I:%M %p")
            # await app.update_profile(last_name=ti)
            pass
        except Exception as e:
            await app.send_message(-10020965765, e)
        await asyncio.sleep(60) 
async def main():
    async with app:
        await change_name()
app.run(main())
