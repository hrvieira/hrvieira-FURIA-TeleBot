from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def clipadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "📹 Campeonato de Clipadores FURIA\n\n"
        "Mostre seu talento, grave os melhores momentos das lives e concorra a prêmios!\n"
        "Regras e inscrições: https://clipadores.furia.gg/\n\n"
        "Premiação total: R$ 5.000 + FURIA Cash 🔥"
    )
    await update.message.reply_text(mensagem)

clipadores_handler = CommandHandler("clipadores", clipadores)