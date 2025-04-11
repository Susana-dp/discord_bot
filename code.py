import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if 'meme' in message.content:
            await message.channel.send(get_meme())
        elif 'hello' in message.content:
            await message.channel.send('Hello!')
        elif 'bye' in message.content:
            await message.channel.send('Goodbye!')
        elif 'help' in message.content:
            await message.channel.send('Type: meme, hello, bye, Susana, help')
        elif '#Own name' in message.content:
            await message.channel.send('Susana is the best!')
        elif '#Own name without first letter in caps' in message.content:
            await message.channel.send('Susana is the best!')
        else:
            await message.channel.send('I do not understand you!')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('#Your own Token')
