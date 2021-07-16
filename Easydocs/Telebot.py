#pip install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot("xxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxx")

#function name inside this is your choice that binds it
#reply_to replies that command and sends message
@bot.message_handler(commands=['start'])
def welcome(message):
   bot.reply_to(message, "welcome to telebot!")

#that lambda fun takes all messages and binds here except commands
#message.text is the message that we send to bot
@bot.message_handler(fun = lambda x: True)
def echo(message):
   bot.reply_to(message, message.text)


#message handlers by - content_types, regex, commands, func

#commands
@bot.message_handler(commands=['start', 'help'])
def start_help(message):
  bot.send_message("start command is triggered")

#content_types - text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message
@bot.message_handler(content_types=['document', 'audio'])
def documents(message):
  bot.send_message("Document is sent!")

#regex
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
  bot.send_message("regex filter is used")

#function
@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
  bot.send_message("function is used")


#sending messages and documents as reply
@bot.message_handler(commands=['send'])
def send_all(message):
  bot.send_message(message.chat.id, "message")
  bot.edit_message_text("new_text", message.chat.id, "message_id")
  bot.forward_message("to_chat_id", "from_chat_id", "message_id")

  #fileid of photo sent by user
  fileid = message.photo[0].file_id

  photo = open('./photo.png', 'rb')
  bot.send_photo(chat_id, photo)
  bot.send_photo(chat_id, "FILEID")

  audio = open('/tmp/audio.mp3', 'rb')
  bot.send_audio(chat_id, audio)
  bot.send_audio(chat_id, "FILEID")

  voice = open('/tmp/voice.ogg', 'rb')
  bot.send_voice(chat_id, voice)
  bot.send_voice(chat_id, "FILEID")

  doc = open('/tmp/file.txt', 'rb')
  bot.send_document(chat_id, doc)
  bot.send_document(chat_id, "FILEID")

  sti = open('/tmp/sti.webp', 'rb')
  bot.send_sticker(chat_id, sti)
  bot.send_sticker(chat_id, "FILEID")

  video = open('/tmp/video.mp4', 'rb')
  bot.send_video(chat_id, video)
  bot.send_video(chat_id, "FILEID")

  #action_string - 'typing','upload_photo','record_video','upload_video','record_audio','upload_audio','upload_document'and'find_location'
  bot.send_chat_action(chat_id, action_string)

  #download and save file sent by user - photo
  fileid = message.photo[0].file_id
  file = bot.get_file(fileid)
  filepath = file.file_path
  download = bot.download_file(filepath)
  with open("image.jpg", 'wb') as new_file:
    new_file.write(download)


bot.polling()
#must have otherwise it will accept one request and it will stop
