from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def game_calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    mensagem = "📅 Próximos jogos da FURIA:\n\n"
    mensagem += "🕹️ 04/05 - FURIA vs Team Liquid - 18:00\n"
    mensagem += "🕹️ 06/05 - FURIA vs Cloud9 - 20:00\n"
    
    await update.message.reply_text(mensagem)

calendar_handler = CommandHandler('calendar', game_calendar)