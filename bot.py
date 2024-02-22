from telegram.ext import Updater, MessageHandler, Filters
from config import Config

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot is active!")

def delete_message(update, context):
    message_text = update.message.text.lower()
    if any(copyright_message in message_text for copyright_message in Config.COPYRIGHT_MESSAGES):
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)

def delete_edited_message(update, context):
    context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.edited_message.message_id)

def main():
    updater = Updater(token=Config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), delete_message))
    dp.add_handler(MessageHandler(Filters.edited_message, delete_edited_message))
    dp.add_handler(MessageHandler(Filters.command, start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
