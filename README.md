rBotMeme

Discord bot that can post subreddit images 
You can add urls in "urls" and you need to add
##
elif message.content.find(COMMANDNAME)!= -1:
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
##
this line before else statement (change COMMANDNAME)
