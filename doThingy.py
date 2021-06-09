
import json
  
# Opening JSON file

with open('svv-raamattu.json',encoding='utf-8') as json_file:
    data = json.load(json_file)

#‎[9.7.2016, 14.20.11] Joh doe: ‎image omitted

outputPsat = ""
serviceCount = 0

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
                messageBody = "Image or weirdness was ommited."
        else:
            if isinstance(msg["text"],list):
                try:
                    if msg["text"][0]["type"] == "bot_command":
                        messageBody = str(msg["text"][0]["text"])
                    elif msg["text"][0]["type"]=="link":
                        try:
                            messageBody = "Sent URL: "+ msg["text"][0]["text"] + " With comment: " + msg["text"][1]
                        except Exception as e:
                            messageBody = "Sent URL: "+ msg["text"][0]["text"]
                except Exception as e:
                    messageBody = str(msg["text"])
            else:
                messageBody = str(msg["text"])


        insertStr = "["+date+", "+time+"] "+sender+": "+messageBody+"\n"
        outputPsat = outputPsat +insertStr
    else:
        serviceCount = serviceCount + 1

print(serviceCount)


chatFile = open("./_chat","w+",encoding='utf-8')
chatFile.write(outputPsat)
chatFile.close()
