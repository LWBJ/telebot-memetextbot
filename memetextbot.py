from telegram.ext import Updater, CommandHandler, MessageHandler
from random import random
import os

def random_case(letter):
  #helper function to randomise letter casing
  
  if random() < 0.5:
    return letter.upper()
  return letter

def random_caps(bot, update):
    #echoes with randomised casing.

    message = update.message.text.partition(" ")[2].lower()
    new_message1 = ''
    new_message2 = ''
    new_message3 = ''
    
    for letter in message:
        new_message1 += random_case(letter)
    
    for letter in message:
        new_message2 += random_case(letter)
    
    for letter in message:
        new_message3 += random_case(letter)
    
    update.message.reply_text(text=new_message1)
    update.message.reply_text(text=new_message2)
    update.message.reply_text(text=new_message3)
    sendEndOfLifeNotice(update)
    
def spaced_caps(bot, update):
    #echoes with spaces  between letters and upper case.

    message = update.message.text.partition(" ")[2]
    new_message = " ".join(message)

    update.message.reply_text(text=new_message.upper())
    sendEndOfLifeNotice(update)
    
def spaced_lower(bot, update):
    #echoes with spaces  between letters and upper case.

    message = update.message.text.partition(" ")[2]
    new_message = " ".join(message)

    update.message.reply_text(text=new_message.lower())
    sendEndOfLifeNotice(update)
    
def alt_caps(bot, update):
    #echoes with alternating capitalization

    message = update.message.text.partition(" ")[2].lower()
    new_message=''
    
    for num, letter in enumerate(message, start=1):
        if num%2==1:
            new_message += letter.upper()
        else:
            new_message += letter
      
    update.message.reply_text(text=new_message)
    sendEndOfLifeNotice(update)

def owoifier(bot, update):
    #The owoifier

    message = update.message.text.partition(" ")[2]
    swaps =[
      ('r','w'),('R','W'),
      ('l','w'),('L','W'),
      ('ove','uv'),('OVE','UV'),
      ('na','nya'),('ne','nye'),('ni','nyi'),('no','nyo'),('nu','nyu'),
      ('Na','Nya'),('Ne','Nye'),('Ni','Nyi'),('No','Nyo'),('Nu','Nyu'),
      ('nA','nYA'),('nE','nYE'),('nI','nYI'),('nO','nYO'),('nU','nYU'),
      ('NA','NYA'),('NE','NYE'),('NI','NYI'),('NO','NYO'),('NU','NYU'),
    ]
    
    new_message = message
    for pair in swaps:
      new_message = new_message.replace(pair[0],pair[1])
        
    update.message.reply_text(text=new_message)
    sendEndOfLifeNotice(update)

def help(bot,update):
    #help command
    message = """
/a <message here> will echo the message with random capitalization

/b <message here> will echo the message in caps with spaces between each letter

/c <message here> will echo the message in lower case with spaces between each letter

/d <message here> will echo the message with alternating capitalization, starting with a capital letter

/owo <message here> will echo the message in owo text
    """
    update.message.reply_text(text=message)
    sendEndOfLifeNotice(update)
    
def start(bot,update):
    #help command
    message = """
This bot allows you to get formatted meme text easily. Simply send a command and your message to the bot. The bot will echo the message in your desired format. 

Use /help to see the available commands to choose your formatting. 
    """
    update.message.reply_text(text=message)
    sendEndOfLifeNotice(update)
    
    
def main():
  TOKEN = os.environ.get('API_KEY','')
  NAME = "memetextbot"
  PORT = os.environ.get('PORT')
  
  updater = Updater(token=TOKEN)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("a", random_caps))
  dp.add_handler(CommandHandler("b", spaced_caps))
  dp.add_handler(CommandHandler("c", spaced_lower))
  dp.add_handler(CommandHandler("d", alt_caps))
  dp.add_handler(CommandHandler("owo", owoifier))
  dp.add_handler(CommandHandler("help", help))
  dp.add_handler(CommandHandler("start", start))

  #updater.start_polling()
  updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
  updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))

if __name__ == "__main__":
  main()

#------------------------------------End of Life Notice---------------------------------------------
def sendEndOfLifeNotice(update):
    message = """
        **END OF LIFE NOTICE**
        
        This bot runs on heroku's free tier. Heroku's free tier is expiring in Nov 2022, hence the bot will cease to function then.
        Thank you for using memetextbot. If you have any urgent issues, you can send an email to memetextbotdev@gmail.com until 2023.
    """
    update.message.reply_text(text="This bot runs on Heroku")