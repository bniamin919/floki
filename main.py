from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# دستور شروع ربات
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! من ربات شما هستم.')

# توکن ربات خودتون رو اینجا وارد کنید
updater = Updater("7853903322:AAG28DnOzHOia0wcdOZJW4FDxzskWYcGzeg", use_context=True)

# اضافه کردن دستور start
updater.dispatcher.add_handler(CommandHandler('start', start))

# شروع ربات
updater.start_polling()
updater.idle()
