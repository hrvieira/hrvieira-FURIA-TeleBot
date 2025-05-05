from bot.utils.config import bot_token
from telegram.ext import ApplicationBuilder
from bot.handlers.onboarding import onboarding_handler
from bot.handlers.menu import start_handler, menu_handler
from bot.handlers.game_calendar import calendar_handler
from bot.handlers.live import live_handler
from bot.handlers.clipadores import clipadores_handler
from bot.handlers.store import store_handler
from bot.handlers.news import news_handler
from bot.handlers.streamers import streamers_handler
from bot.handlers.furiacash import furiacash_handler
from bot.handlers.fallback import fallback_handler

def main():
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(onboarding_handler) 
    app.add_handler(start_handler)
    app.add_handler(menu_handler)
    app.add_handler(live_handler)
    app.add_handler(clipadores_handler)
    app.add_handler(calendar_handler)
    app.add_handler(store_handler)
    app.add_handler(news_handler)
    app.add_handler(streamers_handler)
    app.add_handler(furiacash_handler)
    app.add_handler(fallback_handler)

    print("Bot está rodando... (Ctrl + C para parar)")
    app.run_polling()

if __name__ == '__main__':
    main()