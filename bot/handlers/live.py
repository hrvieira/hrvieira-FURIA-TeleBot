from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def live(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🎮 Jogos ao vivo da FURIA:\n\n"
        "• CS2 - FURIA vs NAVI (16h - Blast Premier)\n"
        "• Valorant - FURIA vs LOUD (18h - VCT Américas)\n"
        "• Free Fire - FURIA vs Fluxo (19h - LBFF)\n\n"
        "Acompanhe em: https://live.furia.gg/"
    )
    await update.message.reply_text(mensagem)

live_handler = CommandHandler("live", live)
