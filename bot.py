from telegram import Bot
from telegram.ext import Updater, CommandHandler
import time
import threading
from dotenv import load_dotenv
import os

# تحميل المتغيرات من ملف .env
load_dotenv()

# استرجاع Token البوت من المتغيرات البيئية
TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)

# متغير لتخزين حالة البوت (تشغيل أو إيقاف)
running = False

def start(update, context):
    global running
    running = True
    update.message.reply_text("بدأت في إرسال الرسائل بشكل مزعج!")

    # دالة لإرسال الرسائل بشكل متكرر
    def send_messages():
        while running:
            bot.send_message(chat_id=update.message.chat_id, text="رسالة مزعجة!")
            time.sleep(0.5)  # الوقت بين الرسائل أقل من ثانية

    # تشغيل الرسائل في Thread منفصل
    threading.Thread(target=send_messages).start()

def stop(update, context):
    global running
    running = False
    update.message.reply_text("تم إيقاف إرسال الرسائل.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # إضافة الأوامر للبوت
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
