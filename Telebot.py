#pip install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot("xxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxx")

#function name inside this is your choice that binds it
#reply_to replies that command and sends message
@bot.message_handler(commands=['/start'])
def welcome(message):
   bot.reply_to(message, "welcome to telebot!")

#that lambda fun takes all messages and binds here except commands
#message.text is the message that we send to bot
@bot.message_handler(fun = lambda x: True)
def echo(message):
   bot.reply_to(message, message.text)



bot.polling()
#must have otherwise it will accept one request and it will stop
