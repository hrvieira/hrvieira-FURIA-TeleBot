from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "📰 Últimas notícias FURIA:\n\n"
        "• FURIA vence NAVI e avança na Blast Premier! (02/05)\n"
        "• Nova line de Valorant apresentada com destaque mundial (01/05)\n"
        "• Drop especial da Loja alcança recorde de vendas (29/04)\n\n"
        "Leia mais: https://news.furia.gg/"
    )
    await update.message.reply_text(mensagem)

news_handler = CommandHandler("news", news)