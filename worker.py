import discord, random, json, datetime
from discord.ext import commands

# YO! JUJI! pay attention to this "labmda expression"
fix_date = lambda o: datetime.datetime.strptime(o, "%Y-%m-%dT%H:%M").strftime('%m/%d %h:%M')

# create bot instance
bot = commands.Bot(command_prefix='!', description='SD Memorial Bot')

# load file into json, strip non-SD comments then del 'o' object
o = json.load(open('sd.json','rb'))
quotes = [(fix_date(m['timestamp'][:16]),m['content']) for m in o if int(m['author']['id']) ==  315864528774627338]
del o

@bot.event
async def on_ready():
    channel = discord.Object(id=432066274336440330)
    print("Logged in as:  name={}, id={}".format( bot.user.name, bot.user.id ))
    


@bot.command(pass_context=True)
async def sd(ctx):
    """Chooses a random quote."""
    timestamp, content = random.choice(quotes)
    msg = "{}: {}".format(timestamp, content)
    await bot.say(msg)


@bot.command(pass_context=True)
async def search(ctx, phrase : str):
    """Match quotes with a search-phrase"""
    results = []
    for timestamp, content in quotes:
        if phrase in content: results.append( "{}: {}".format(timestamp, content) )
        if len(results) > 3: break

    if len(results) > 0:
        msg = "Results:\n\n{}".format( "\n".join(results) )
    else:
        msg = "no results for `{}`".format(phrase)
    await bot.say(msg)

if __name__ == "__main__":
    try:
        bot.run('NDM0MTUyNTkxMjg3NTE3MjE0.DbGP0Q.8W6JWgCKfPwVnhOYozkJmPL55NI')
    except:
        pass
