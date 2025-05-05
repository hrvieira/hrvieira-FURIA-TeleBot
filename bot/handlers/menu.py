import re
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import MessageHandler, CommandHandler, filters, ContextTypes
from bot.handlers.live import live
from bot.handlers.clipadores import clipadores
from bot.handlers.game_calendar import game_calendar
from bot.handlers.store import store
from bot.handlers.news import news
from bot.handlers.streamers import streamers
from bot.handlers.furiacash import furiacash
from bot.handlers.team import show_team
from bot.database import verificar_e_atualizar_saldo_furiacash, get_db_connection

MENU_OPCOES = [
    "⚡ Acompanhe jogos ao vivo",
    "🎯 Campeonato de Clipadores",
    "📅 Calendário de Jogos",
    "🛒 Lojinha da Pantera",
    "📰 Esports News / Trend Topics",
    "🎥 Criadores de Conteúdo e Streamers",
    "🤑 FURIA Cash",
    "🦁 Escalação Atual"
]

def main_menu_keyboard():
    keyboard = [
        ["⚡ Acompanhe jogos ao vivo", "🎯 Campeonato de Clipadores"],
        ["📅 Calendário de Jogos", "🛒 Lojinha da Pantera"],
        ["📰 Esports News / Trend Topics", "🎥 Criadores de Conteúdo e Streamers"],
        ["🤑 FURIA Cash", "🦁 Escalação Atual"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def enviar_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    telegram_id = update.effective_chat.id

    conn = await get_db_connection()
    resultado = await conn.fetchrow('SELECT cpf FROM usuarios WHERE telegram_id = $1;', telegram_id)
    await conn.close()
    
    cpf = resultado['cpf'] if resultado else None

    saldo_atualizado, novo_saldo = await verificar_e_atualizar_saldo_furiacash(telegram_id, cpf)
    
    if saldo_atualizado:
        await update.effective_chat.send_message(
            f"💰 Você ganhou +$0,10 FURIA Cash pelo login de hoje!\n"
            f"Seu novo saldo é ${novo_saldo:.2f} FURIA Cash."
        )

    
    await update.effective_chat.send_message("🐾 Escolha uma das opções abaixo:", reply_markup=main_menu_keyboard())

async def tratar_escolha_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if texto == "⚡ Acompanhe jogos ao vivo":
        await live(update, context)
    elif texto == "🎯 Campeonato de Clipadores":
        await clipadores(update, context)
    elif texto == "📅 Calendário de Jogos":
        await game_calendar(update, context)
    elif texto == "🛒 Lojinha da Pantera":
        await store(update, context)
    elif texto == "📰 Esports News / Trend Topics":
        await news(update, context)
    elif texto == "🎥 Criadores de Conteúdo e Streamers":
        await streamers(update, context)
    elif texto == "🤑 FURIA Cash":
        await furiacash(update, context)
    elif texto == "🦁 Escalação Atual":
        await show_team(update, context)
    else:
        await update.message.reply_text("🤔 FUR, acho que não escolheu uma de nossas opções...")
        await update.message.reply_text("👉 Por favor, escolha uma opção no menu abaixo para continuar:")

start_handler = CommandHandler('menu', enviar_menu)

menu_handler = MessageHandler(
    filters.Regex(re.compile("^(" + "|".join(re.escape(opcao) for opcao in MENU_OPCOES) + ")$")),
    tratar_escolha_menu
)
