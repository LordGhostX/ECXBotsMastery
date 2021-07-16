from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from dog_images import generate_dog_image
from crypto_fetcher import fetch_crypto_price
from dictionary import find_word_meaning

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

last_commands = {}


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hello World!")


def dog(update, context):
    dog_image = generate_dog_image()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_image)


def crypto(update, context):
    chat_id = update.effective_chat.id
    last_commands[chat_id] = "crypto"
    context.bot.send_message(chat_id=chat_id,
                             text="Enter the cryptocurrency you want to get the price of: ")


def dictionary(update, context):
    chat_id = update.effective_chat.id
    last_commands[chat_id] = "dictionary"
    context.bot.send_message(chat_id=chat_id,
                             text="Enter the word you want to get the meaning of: ")


def echo(update, context):
    chat_id = update.effective_chat.id
    user_last_command = last_commands.get(chat_id)

    if user_last_command == "crypto":
        ticker = update.message.text
        context.bot.send_message(
            chat_id=chat_id, text=fetch_crypto_price(ticker))
        last_commands[chat_id] = None
    if user_last_command == "dictionary":
        word = update.message.text
        context.bot.send_message(chat_id, text=find_word_meaning(word))


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

dog_handler = CommandHandler('dog', dog)
dispatcher.add_handler(dog_handler)

crypto_handler = CommandHandler('crypto', crypto)
dispatcher.add_handler(crypto_handler)

dictionary_handler = CommandHandler('dictionary', dictionary)
dispatcher.add_handler(dictionary_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
