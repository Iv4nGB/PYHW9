from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bot
#from bot_commands import * # импортировать все




app = ApplicationBuilder().token("5629640823:AAGNiW-uQuWHzZibfwWL0IQ26uEYoitJ8VI").build()

app.add_handler(CommandHandler("hi", bot.hi_command))
app.add_handler(CommandHandler("time", bot.time_command))
app.add_handler(CommandHandler("help", bot.help_command))
app.add_handler(CommandHandler("sum", bot.sum_command))
print('server START')
app.run_polling()
