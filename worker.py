import json, discord, random

# start discord client
client = discord.Client()

# load file into json
o = json.load(open('sd.json','rb'))

# strip json-shit we dont want
quotes = [m['content'] for m in o if int(m['author']['id']) ==  315864528774627338]

# ditch o object since we're done with it..
del o

@client.event
async def on_message(message):

    if message.content == '!sd':
        msg = '{}'.format(random.choice(quotes))
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as', client.user.name,client.user.id)

if __name__ == "__main__":
    client.run('NDMyMDM3Nzg3MTI3MjUwOTU0.DannQw.RPA7NHrXaRutfWGtZsPNEdYjBR8')