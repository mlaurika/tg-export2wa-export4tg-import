
import json
  
# plz change the name of the js to your liking

with open('svv-raamattu.json',encoding='utf-8') as json_file:
    data = json.load(json_file)
    
#FORMAT OF WA _chat.txt this goes to zip
#‎[9.7.2016, 14.20.11] Joh doe: ‎image omitted

outputPsat = ""
serviceCount = 0
msgCount = 0

for msg in data["messages"]:
    if msg["type"] == "message":
        dateBase = msg["date"].split("T")[0]
        date= dateBase.split("-")[2]+"."+dateBase.split("-")[1]+"."+dateBase.split("-")[0]
        time = msg["date"].split("T")[1].replace(":",".")
        sender = msg["from"]

        if msg["text"]=="":
            try:
                if msg["media_type"] == "sticker":
                    messageBody = "Sent sticker corresponding this emoji: " +msg["sticker_emoji"] +"."
            except Exception as e:
                try:
                    if msg["poll"]:
                        messageBody = "Poll: " + msg["poll"]["question"] + " Total voters: " + str(msg["poll"]["total_voters"])
                        for answer in msg["poll"]["answers"]:
                            messageBody = messageBody + "\n " +"Option: " + answer["text"] + " Votes:" + str(answer["voters"])
                except Exception as x:
                    try:
                        if msg["photo"]:
                            messageBody = "Photo ommited: " + str(msg["width"]) + " by " + str(msg["height"])
                    except Exception as y:
                        messageBody = "Animation, audio or weirdness was ommited."
        else:
            if isinstance(msg["text"],list):
                try:
                    if msg["text"][0]["type"] == "bot_command":
                        messageBody = str(msg["text"][0]["text"])
                    else:
                        messageBody = ""
                        for msgCnt in msg["text"]:
                            if isinstance(msgCnt, str):
                                messageBody = messageBody +msgCnt + " "
                            elif isinstance(msgCnt,dict):
                                messageBody = messageBody +msgCnt["text"] + " "
                except Exception as e:
                    try:
                        messageBody = ""
                        for msgCnt in msg["text"]:
                            if isinstance(msgCnt, str):
                                messageBody = messageBody + msgCnt
                            else:
                                messageBody = messageBody +msgCnt["text"] + " "
                    except Exception as e:
                        messageBody = str(msg["text"])
            else:
                try:
                    if msg["photo"]:
                        messageBody = "Photo ommited: " + str(msg["width"]) + " by " + str(msg["height"]) +" With text: "+ str(msg["text"])
                except Exception as y:
                    messageBody = "Animation, audio or weirdness was ommited."
                    messageBody = str(msg["text"])


        insertStr = "["+date+", "+time+"] "+sender+": "+messageBody+"\n"
        outputPsat = outputPsat +insertStr
        msgCount = msgCount +1
        print(msgCount/len(data["messages"])*100)
    else:
        serviceCount = serviceCount + 1

print("Messages: " +str(msgCount))
print("Services ommited:"+str(serviceCount))


chatFile = open("./_chat.txt","w+",encoding='utf-8')
chatFile.write(outputPsat)
chatFile.close()
