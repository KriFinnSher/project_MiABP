import time
import openai
import asyncio
import logging
import schedule
import datetime
from telegram import Update
from threading import Thread
from dotenv import dotenv_values
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

content = dotenv_values()
tg_token = content["TG_TOKEN"]
openai_api_key = content["OPENAI_API_KEY"]
openai.api_key = openai_api_key

notifications = []


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Приветствую, пользователь! "
                                                                          "Если тебе нужен личный ассистент, "
                                                                          "но денег на него нет, ты можешь "
                                                                          "использовать этого бота как простую "
                                                                          "альтернативу. Используй команду /help "
                                                                          "для более подробной информации.")


def run_async_task(task, *args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(task(*args))
    loop.close()


def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


async def notif_helper(update: Update, context: ContextTypes.DEFAULT_TYPE, notif_message: str):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=notif_message)


async def set_notification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time_str = context.args[0]
    hour, minute = map(int, time_str.split(':'))
    notif_time = f'{hour:02d}:{minute:02d}'
    notif_message = " ".join(context.args[1:])
    if notif_time > datetime.datetime.now().strftime("%H:%M"):
        notifications.append((notif_time, notif_message))
        schedule.every().day.at(notif_time).do(
            run_async_task, notif_helper, update, context, notif_message).tag(update.effective_chat.id)
        await update.message.reply_text(f"Напоминание установлено на {notif_time}")
    else:
        await update.message.reply_text(f"Кажется, вы уже опоздали). Установите более позднее время, чем текущее")


async def list_notifications(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not notifications:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="У вас нет активных напоминаний, "
                                            "вы можете установить их, используя /set_notif")
    else:
        notif_list = "\n".join([f"{notif_time} - {notif_message}" for notif_time, notif_message in notifications])
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text=f"Список активных напоминаний:\n{notif_list}")


async def delete_notification(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global notifications
    notif_time = context.args[0]
    notifications = [notif for notif in notifications if notif[0] != notif_time]
    tag = f"{update.effective_chat.id}_{notif_time}"
    schedule.clear(tag)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Напоминания на время {notif_time} удалены.")


if __name__ == '__main__':
    app = ApplicationBuilder().token(tg_token).build()

    start_handler = CommandHandler('start', start)
    notify_handler = CommandHandler('set_notif', set_notification)
    notify_list_handler = CommandHandler('list_notif', list_notifications)
    del_notif_handler = CommandHandler('del_notif', delete_notification)

    app.add_handler(start_handler)
    app.add_handler(notify_handler)
    app.add_handler(notify_list_handler)
    app.add_handler(del_notif_handler)

    Thread(target=run_scheduler).start()
    app.run_polling()

from openai import OpenAI
client = OpenAI(api_key=openai_api_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)