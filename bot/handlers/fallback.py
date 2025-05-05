from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler, filters

async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤔 FUR, acho que não escolheu uma de nossas opções...\n\n"
        "👉 Por favor, escolha uma opção no menu abaixo para continuar:")

fallback_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, fallback)