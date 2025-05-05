from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from bot.database import obter_saldo_furiacash

async def furiacash(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_chat.id

    saldo = await obter_saldo_furiacash(telegram_id)

    if saldo is not None:
        mensagem = (
            "💰 FURIA Cash\n\n"
            "Você acumula FURIA Cash interagindo com o bot, assistindo lives, comprando na loja e participando de eventos.\n\n"
            f"Seu saldo atual: ${saldo:.2f} FURIA Cash\n"
            "➡️ Use seu saldo para resgatar recompensas exclusivas da FURIA!\n\n"
            "Catálogo de recompensas: https://furiacash.furia.gg/"
        )
    else:
        mensagem = (
            "❌ Não encontramos seu saldo de FURIA Cash.\n"
            "Verifique se você já concluiu o cadastro no bot."
        )

    await update.message.reply_text(mensagem)

furiacash_handler = CommandHandler("furiacash", furiacash)