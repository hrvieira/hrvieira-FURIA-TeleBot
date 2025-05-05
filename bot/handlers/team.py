from telegram.ext import MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

async def show_team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    team_info = (
        "🦁 *Escalação Atual da FURIA CS*\n\n"
        "🔫 arT (Andrei Piovezan)\n"
        "🔫 KSCERATO (Kaike Cerato)\n"
        "🔫 yuurih (Yuri Santos)\n"
        "🔫 chelo (Marcelo Cespedes)\n"
        "🔫 saffee (Rafael Costa)\n"
    )
    await update.message.reply_markdown(team_info)

team_handler = MessageHandler(filters.Regex('^🦁 Escalação Atual$'), show_team)