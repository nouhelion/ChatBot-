import os
import discord
#my_secret = os.environ['TOKEN']
import json
import random
from replit import db
from keep_alive import keep_alive

client =discord.Client()

sad_words=["sad","depressed","unhappy","angry","miserable","bad","crying"]

encourang=[
  "Cheer up!",
  "Hang in there",
  "Don't say that!",
  "U are an amazing girlfriend , I love u the most",
  "Dont't cry , please"
]

if "responding" not in db.keys():
 db["responding"]=True




data_JSON =  """
{
	"size": "Medium",
  "height": "1.93 cm",
	"love": "I adore you",
  "morning": "Good morning to the one who rules my heart! Every day I feel blessed to spend my day with you. I love you!",
  "night": "Come to my dreams if you can. I'll kiss you there.",
	"flirting": {
		"1": "Call me i miss your voice 😔 ",
		"2": "What on earth did I think about all the time before you",
		"3": "If loving you was a job, I'd be the most deserving, dedicated, and qualified candidate. In fact, I'd even be willing to work for free!",
    "4": "Your smile is literally the cutest thing I've ever seen in my life.",
    "5": "If someone asked me to describe you in just two words, I'd say 'Simply Amazing'.",
    "6": "If you were a movie, I'd watch you over and over again.",
    "7": "In a sea of people, my eyes always search for you.",
    "8": "I know fairy tales come true because I have you.",
    "9": "You do a million little things that bring to joy to my life.",
    "10": "There are only two times that I want to be with you: Now and Forever.",
    "11": "My six word love story: 'I can't imagine life without you.'",
    "12": "Stop making me think about you! I'm busy.",
    "13": "Cuddling with you would be perfect right now 💑",
    "14": "If nothing lasts forever, can I be your nothing?",
    "15": "You make my heart melt! 💕",
    "16": "I couldn't ignore you even if I wanted to.",
    "17": "Next time I hug you, I probably won't let go for a long time.",
    "18": "I can't decide if the best part of my day is waking up next to you, or going to sleep with you. Hurry home so I can compare the two again.",
    "19": "Whenever my phone vibrates, I hope you're the reason for it.",
    "20": "Forget the butterflies, I feel the whole zoo when I am with you! 🐻🐼🐨🐯",
    "21": "You know I really want you to come over, but you're so hot my air condition bill would skyrocket the second you stepped foot in the door!",
    "22": "I know you might be too busy today ⏰, but please add me too in your to-do list ✔",
    "23": "We make a great 🍐",
    "24": "You've 🔒 up my ❤ and thrown away the 🔑",
    "25": "The only time I stupidly smile at my phone is when I get text messages from you.",
    "26": "Just had to let you know… loving you is the best thing that happened to me 💕",
    "27": "I always wake up smiling. I think it's your fault.",
    "28": "What is love? It is what makes your cell phone ring every time I send text messages.",
    "29": "If Van Gogh had you as a subject, the sunflowers would have gone in the trash 🌻🌻🌻",
    "30": "If I were a stop light 🚦, I would turn red every time you passed by so that I could stare at you a bit longer.",
    "31": "🐳 you be mine forever?",
    "32": "You've turned my life 🔄⬆⬇",
    "33": " 'You can't blame gravity for falling in love.' – Albert Einstein",
    "34": "'Love is when the other person's happiness is more important than your own.' – H. Jackson Brown, Jr.",
    "35": "Hey, my name's Microsoft. Can I crash at your place tonight?",
    "36": "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together.",
    "37": "Is your name Google? Because you have everything I’ve been searching for"
  }
}
"""

def get_size():
  # returns JSON object asz
  # a dictionary
  data_dict = json.loads(data_JSON)
  #returns the size :3
  size=data_dict["size"]
  return (size)

def get_height():
  # returns JSON object asz
  # a dictionary
  data_dict = json.loads(data_JSON)
  #returns the height
  height=data_dict["height"]
  return (height)

def get_love():
  # returns JSON object asz
  # a dictionary
  data_dict = json.loads(data_JSON)
  #returns the love
  love=data_dict["love"]
  return (love)

def get_flirt():
  # returns JSON object as
  # a dictionary
  data_dict = json.loads(data_JSON)
  #load a random id number for the messages
  num=random.randint(1,37)
  flirt=data_dict["flirting"]
  return (flirt[str(num)])

def update_encouragements(encourang):
  if "encouragements" in db.keys():
    encouragements=db["encouragements"]
    encouragements.append(encourang)
    db["encouragements"]=encouragements
  else:
    db["encouragements"]=[encourang]
    
def delete_encouragements(index):
  encouragements=db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"]=encouragements 

def get_night():
  # returns JSON object as
  # a dictionary
  data_dict = json.loads(data_JSON)
  night=data_dict["night"]
  return (night)

def get_morning():
  # returns JSON object as
  # a dictionary
  data_dict = json.loads(data_JSON)
  morning=data_dict["morning"]
  return (morning)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
#not interacting if the message is from the bot
async def on_message(message):
  if message.author==client.user:
    return
    
#when the bot sees a hello it gonna respond to it
  if message.content.startswith('$flirt'):
    flirt=get_flirt()
    await message.channel.send(flirt)
  elif message.content.startswith('$night'):
    night=get_night()
    await message.channel.send(night)
  elif message.content.startswith('$morning'):
    morning=get_morning()
    await message.channel.send(morning)
  elif message.content.startswith('$size'):
    size=get_size()
    await message.channel.send(size)
  elif message.content.startswith('$height'):
    height=get_height()
    await message.channel.send(height)
  elif message.content.startswith('$love'):
    love=get_love()
    await message.channel.send(love)
  
  if db["responding"]:
    options=encourang
    if "encouragements" in db.keys():
      options.extend(db["encouragements"])
    
    if any(word in message.content for word in sad_words):
      await message.channel.send(random.choice(options))
  
  if message.content.startswith("$new"):
    encouraging_message=message.content.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouranging message added !")

  if message.content.startswith("$del"):
    encouragements=[]
    if "encouragements" in db.keys():
      index=int(message.content.split("$del ",1)[1])
      delete_encouragements(index)
      encouragements=db["encouragements"]
    await message.channel.send(encouragements)

  if message.content.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if message.content.startswith("$responding"):
    value = message.content.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive()
client.run(os.getenv('TOKEN'))