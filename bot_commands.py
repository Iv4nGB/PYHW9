from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import logger as log


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.logger(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.logger(update, context)
    await update.message.reply_text('/hi\n/time\n/help\n/sum')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log.logger(update, context)
    await update.message.reply_text(f'Time: {datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.logger(update, context)
    await update.message.reply_text(f'введите /sum первое_число второе_число!')
    msg = update.message.text
    print(msg)
    items = msg.split() # тут мы получим: /sum первое_число второе_число (в списке)
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')