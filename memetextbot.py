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
    
def spaced_caps(bot, update):
    #echoes with spaces  between letters and upper case.

    message = update.message.text.partition(" ")[2]
    new_message = " ".join(message)

    update.message.reply_text(text=new_message.upper())
    
def spaced_lower(bot, update):
    #echoes with spaces  between letters and upper case.

    message = update.message.text.partition(" ")[2]
    new_message = " ".join(message)

    update.message.reply_text(text=new_message.lower())

def help(bot,update):
    #help command
    message = """
/a <message here> will echo the message with random capitalization

/b <message here> will echo the message in caps with spaces between each letter

/c <message here> will echo the message in lower case with spaces between each letter
    """
    update.message.reply_text(text=message)
    
def start(bot,update):
    #help command
    message = """
This bot allows you to get formatted meme text easily. Simply send a command and your message to the bot. The bot will echo the message in your desired format. 

Use /help to see the available commands to choose your formatting. 
    """
    update.message.reply_text(text=message)
    
def main():
  TOKEN = "950795385:AAGoS9dhssbR8j08FCsUfTRv2KR-yqljbkQ"
  NAME = "memetextbot"
  PORT = os.environ.get('PORT')
  
  updater = Updater(token=TOKEN)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("a", random_caps))
  dp.add_handler(CommandHandler("b", spaced_caps))
  dp.add_handler(CommandHandler("c", spaced_lower))
  dp.add_handler(CommandHandler("help", help))
  dp.add_handler(CommandHandler("start", start))

  #updater.start_polling()
  updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
  updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))

if __name__ == "__main__":
  main()