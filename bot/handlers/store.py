from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def store(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🛒 Loja Oficial FURIA\n\n"
        "Explore os looks oficiais da Pantera! Camisas, bonés, jaquetas e muito mais!\n\n"
        "Acesse: https://store.furia.gg/\n"
        "🔥 Novidade: Coleção Streetwear 2025 já disponível!"
    )
    await update.message.reply_text(mensagem)

store_handler = CommandHandler("store", store)