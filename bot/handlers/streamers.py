from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def streamers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🎥 Streamers FURIA ao vivo agora:\n\n"
        "• Gaules - CS2 (https://twitch.tv/gaules)\n"
        "• Rakin - Valorant (https://twitch.tv/rakin)\n"
        "• Isadora Basile - Just Chatting (https://twitch.tv/isadorabasile)\n\n"
        "Acompanhe e ganhe FURIA Cash assistindo!"
    )
    await update.message.reply_text(mensagem)

streamers_handler = CommandHandler("streamers", streamers)