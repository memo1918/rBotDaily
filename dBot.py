import discord,requests
from bs4 import BeautifulSoup

botToken = "Nzg3MzAwNDkwNDg4MTg0ODQy.X9S8uA.umaURBOouFWubRQ51oVmy_4KcM4"
channel = "rbotdaily"
client = discord.Client()

def picM(index):
    urls = ["https://www.reddit.com/r/memes/top/?t=day","https://www.reddit.com/r/dankmemes/top/?t=day","https://www.reddit.com/r/BikiniBottomTwitter/top/?t=day","https://www.reddit.com/r/PewdiepieSubmissions/top/?t=day"]
    picList = []
    alici = requests.get(urls[index])
    icerik = alici.content
    soup = BeautifulSoup(icerik, "html.parser")
    htlist = soup.find_all("img",class_ = "_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax")
    for j in htlist:
        picList.append(str(j.get("src")))
    return picList

@client.event
async def on_message(message):
    if str(message.channel) in channel:
        if message.content.find("!memes") != -1:
            while True:
                try:
                    mlist = picM(0)
                    for i in range(0, 5):
                        await message.channel.send(str(mlist[i]))
                    break
                except:
                    print("f")
                    continue
                break
        elif message.content.find("!dankmemes") != -1:
            while True:
                try:
                    mlist = picM(1)
                    for i in range(0, 5):
                        await message.channel.send(str(mlist[i]))
                    break
                except:
                    print("f")
                    continue
                break
        elif message.content.find("!bikinibottom") != -1:
            while True:
                try:
                    mlist = picM(2)
                    for i in range(0, 5):
                        await message.channel.send(str(mlist[i]))
                    break
                except:
                    print("f")
                    continue
                break
        elif message.content.find("!pewdiepie") != -1:
            while True:
                try:
                    mlist = picM(3)
                    for i in range(0, 5):
                        await message.channel.send(str(mlist[i]))
                    break
                except:
                    print("f")
                    continue
                break
        elif message.content.find("!help") != -1:
            await message.channel.send("!\nmemes\ndankmemes\nbikinibottom\npewdiepie")

client.run(botToken)

